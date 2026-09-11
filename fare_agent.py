import re
from agent import find_station, calculate_fare
fare_memory = {
    "step": "start",
    "source": "",
    "destination": ""
}
def reset_fare():
    fare_memory["step"] = "start"
    fare_memory["source"] = ""
    fare_memory["destination"] = ""
def fare_agent(message):
    text = message.strip()
    if fare_memory["step"] == "start":
        lower = text.lower()
        if lower == "fare details" or lower == "fare":
            fare_memory["step"] = "source"
            return "🚉 Please enter the Source Station.", None
        if "from" in lower and "to" in lower:
            passengers = 1
            match = re.search(r'(\d+)', lower)
            if match:
                passengers = int(match.group(1))
            pattern = r'from\s+(.+?)\s+to\s+(.+)'
            m = re.search(pattern, lower)
            if not m:
                return (
                    "❌ Invalid format.\n\n"
                    "Example:\n"
                    "Fare from Miyapur to Ameerpet"
                ), None
            source_text = re.sub(
                r'[^a-zA-Z0-9\s.-]',
                '',
                m.group(1)
            ).strip()
            destination_text = re.sub(
                r'for\s+\d+.*',
                '',
                m.group(2)
            )
            destination_text = re.sub(
                r'[^a-zA-Z0-9\s.-]',
                '',
                destination_text
            ).strip()
            source = find_station(source_text)
            destination = find_station(destination_text)
            if source is None or destination is None:
                return (
                    "❌ Invalid source or destination station.\n\n"
                    "Example:\n"
                    "Fare from Miyapur to Ameerpet"
                ), None
            fare = calculate_fare(source, destination, passengers)
            reply = f"""
💰 FARE DETAILS
🚉 Source : {source}
📍 Destination : {destination}
👥 Passengers : {passengers}
💵 Total Fare : ₹{fare}
🚇 Thank you for choosing Hyderabad Metro.
"""
            panel = {
                "type": "fare",
                "data": {
                    "source": source,
                    "destination": destination,
                    "passengers": passengers,
                    "fare": fare
                }
            }
            return reply, panel
        return (
            "Please type:\n\n"
            "• Fare Details\n"
            "or\n"
            "• Fare from Miyapur to Ameerpet"
        ), None
    elif fare_memory["step"] == "source":
        station = find_station(text)
        if station is None:
            return "❌ Please enter a valid Hyderabad Metro Source Station.", None
        fare_memory["source"] = station
        fare_memory["step"] = "destination"
        return "📍 Please enter the Destination Station.", None
    elif fare_memory["step"] == "destination":
        station = find_station(text)
        if station is None:
            return "❌ Please enter a valid Hyderabad Metro Destination Station.", None
        if station == fare_memory["source"]:
            return "❌ Source and Destination cannot be the same.", None
        fare_memory["destination"] = station
        fare = calculate_fare(
            fare_memory["source"],
            fare_memory["destination"],
            1
        )
        reply = f"""
💰 FARE DETAILS
🚉 Source : {fare_memory['source']}
📍 Destination : {fare_memory['destination']}
👥 Passengers : 1
💵 Total Fare : ₹{fare}
🚇 Thank you for choosing Hyderabad Metro.
"""
        panel = {
            "type": "fare",
            "data": {
                "source": fare_memory["source"],
                "destination": fare_memory["destination"],
                "passengers": 1,
                "fare": fare
            }
     }
        reset_fare()
        return reply, panel
    return "Something went wrong.", None