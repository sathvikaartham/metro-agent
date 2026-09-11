from agent import find_station
from datetime import datetime, timedelta

train_timings = {
    # RED LINE
    "Miyapur": "06:00 AM",
    "JNTU College": "06:02 AM",
    "KPHB Colony": "06:04 AM",
    "Kukatpally": "06:06 AM",
    "Balanagar": "06:08 AM",
    "Moosapet": "06:10 AM",
    "Bharat Nagar": "06:12 AM",
    "Erragadda": "06:14 AM",
    "ESI Hospital": "06:16 AM",
    "SR Nagar": "06:18 AM",
    "Ameerpet": "06:20 AM",
    "Punjagutta": "06:22 AM",
    "Irrum Manzil": "06:24 AM",
    "Khairatabad": "06:26 AM",
    "Lakdikapul": "06:28 AM",
    "Assembly": "06:30 AM",
    "Nampally": "06:32 AM",
    "Gandhi Bhavan": "06:34 AM",
    "Osmania Medical College": "06:36 AM",
    "MG Bus Station": "06:38 AM",
    "Malakpet": "06:40 AM",
    "New Market": "06:42 AM",
    "Musarambagh": "06:44 AM",
    "Dilsukhnagar": "06:46 AM",
    "Chaitanyapuri": "06:48 AM",
    "Victoria Memorial": "06:50 AM",
    "LB Nagar": "06:52 AM",

    # BLUE LINE
    "Nagole": "06:00 AM",
    "Uppal": "06:02 AM",
    "Stadium": "06:04 AM",
    "NGRI": "06:06 AM",
    "Habsiguda": "06:08 AM",
    "Tarnaka": "06:10 AM",
    "Mettuguda": "06:12 AM",
    "Secunderabad East": "06:14 AM",
    "Parade Ground": "06:16 AM",
    "Paradise": "06:18 AM",
    "Rasoolpura": "06:20 AM",
    "Prakash Nagar": "06:22 AM",
    "Begumpet": "06:24 AM",
    "Madhura Nagar": "06:26 AM",
    "Yusufguda": "06:28 AM",
    "Jubilee Hills Road No. 5": "06:30 AM",
    "Jubilee Hills Check Post": "06:32 AM",
    "Peddamma Gudi": "06:34 AM",
    "Madhapur": "06:36 AM",
    "Durgam Cheruvu": "06:38 AM",
    "HITEC City": "06:40 AM",
    "Raidurg": "06:42 AM",

    # GREEN LINE
    "JBS Parade Ground": "06:00 AM",
    "Secunderabad West": "06:02 AM",
    "Gandhi Hospital": "06:04 AM",
    "Musheerabad": "06:06 AM",
    "RTC Cross Roads": "06:08 AM",
    "Chikkadpally": "06:10 AM",
    "Narayanguda": "06:12 AM",
    "Sultan Bazaar": "06:14 AM"
}


def get_live_train_time(first_train):
    """
    Returns the next train time based on current time.
    Metro Frequency: Every 5 minutes
    Metro Timings: 06:00 AM – 11:00 PM
    """

    now = datetime.now()

    first = datetime.strptime(first_train, "%I:%M %p")
    first = first.replace(
        year=now.year,
        month=now.month,
        day=now.day
    )

    closing = first.replace(hour=23, minute=0)

    # Before service starts
    if now < first:
        return first.strftime("%I:%M %p")

    # After service ends
    if now >= closing:
        return "Metro Service Closed"

    elapsed_minutes = int((now - first).total_seconds() // 60)

    next_minutes = ((elapsed_minutes // 5) + 1) * 5

    next_train = first + timedelta(minutes=next_minutes)

    if next_train > closing:
        return "Metro Service Closed"

    return next_train.strftime("%I:%M %p")


train_memory = {
    "step": "start"
}


def reset_train():
    train_memory["step"] = "start"


def train_agent(message):
    text = message.strip()

    if train_memory["step"] == "start":

        lower = text.lower()

        if lower == "train details":
            train_memory["step"] = "station"
            return "🚉 Please enter the Station Name.", None

        remove_words = [
            "next",
            "train",
            "timing",
            "timings",
            "schedule",
            "at",
            "for",
            "of",
            "the"
        ]

        cleaned = lower

        for word in remove_words:
            cleaned = cleaned.replace(word, "")

        station = find_station(cleaned.strip())

        if station is None:
            return (
                "❌ Please mention a valid Hyderabad Metro station.\n\n"
                "Examples:\n"
                "• Next train at Ameerpet\n"
                "• Train timing for Miyapur\n"
                "• Next train at JBS\n"
                "• Next train at MGBS"
            ), None

        timing = get_live_train_time(train_timings.get(station, "06:00 AM"))

        reply = f"""
🚇 TRAIN DETAILS

📍 Station : {station}
🕒 Next Train : {timing}
⏱ Frequency : Every 5 Minutes
🕕 Metro Timings : 06:00 AM – 11:00 PM

✅ Have a Safe Journey!
"""

        panel = {
            "type": "train",
            "data": {
                "station": station,
                "next_train": timing,
                "frequency": "Every 5 Minutes",
                "hours": "06:00 AM – 11:00 PM"
            }
        }

        return reply, panel

    elif train_memory["step"] == "station":

        station = find_station(text)

        if station is None:
            return "❌ Please enter a valid Hyderabad Metro station.", None

        timing = get_live_train_time(train_timings.get(station, "06:00 AM"))

        reset_train()

        reply = f"""
🚇 TRAIN DETAILS

📍 Station : {station}
🕒 Next Train : {timing}
⏱ Frequency : Every 5 Minutes
🕕 Metro Timings : 06:00 AM – 11:00 PM

✅ Have a Safe Journey!
"""

        panel = {
            "type": "train",
            "data": {
                "station": station,
                "next_train": timing,
                "frequency": "Every 5 Minutes",
                "hours": "06:00 AM – 11:00 PM"
            }
        }

        return reply, panel

    return "❌ Something went wrong.", None