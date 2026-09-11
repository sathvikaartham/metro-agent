import random
import re

stations = [

    # red
    "Miyapur",
    "JNTU College",
    "KPHB Colony",
    "Kukatpally",
    "Balanagar",
    "Moosapet",
    "Bharat Nagar",
    "Erragadda",
    "ESI Hospital",
    "SR Nagar",
    "Ameerpet",
    "Punjagutta",
    "Irrum Manzil",
    "Khairatabad",
    "Lakdikapul",
    "Assembly",
    "Nampally",
    "Gandhi Bhavan",
    "Osmania Medical College",
    "MG Bus Station",
    "Malakpet",
    "New Market",
    "Musarambagh",
    "Dilsukhnagar",
    "Chaitanyapuri",
    "Victoria Memorial",
    "LB Nagar",

    # blue
    "Nagole",
    "Uppal",
    "Stadium",
    "NGRI",
    "Habsiguda",
    "Tarnaka",
    "Mettuguda",
    "Secunderabad East",
    "Parade Ground",
    "Paradise",
    "Rasoolpura",
    "Prakash Nagar",
    "Begumpet",
    "Madhura Nagar",
    "Yusufguda",
    "Jubilee Hills Road No. 5",
    "Jubilee Hills Check Post",
    "Peddamma Gudi",
    "Madhapur",
    "Durgam Cheruvu",
    "HITEC City",
    "Raidurg",

    # Green
    "JBS Parade Ground",
    "Secunderabad West",
    "Gandhi Hospital",
    "Musheerabad",
    "RTC Cross Roads",
    "Chikkadpally",
    "Narayanguda",
    "Sultan Bazaar"
]
fare_table = {
    1: 10,
    2: 15,
    3: 20,
    4: 25,
    5: 30,
    6: 35,
    7: 40,
    8: 45,
    9: 50,
    10: 55,
    11: 60
}
booking = {
    "step": "start",
    "source": "",
    "destination": "",
    "passengers": "",
    "date": "",
    "fare": "",
    "booking_id": ""
}
aliases = {
    # red
   "miyapur": "Miyapur",
    "jntu":"JNTU College",
    "jntu college":"JNTU College",
    "kphb":"KPHB Colony",
    "kphb colony":"KPHB Colony",
    "kukatpally": "Kukatpally",
    "balanagar": "Balanagar",
    "moosapet": "Moosapet",
    "bharat nagar": "Bharat Nagar",
    "bharatnagar": "Bharat Nagar",
    "erragadda": "Erragadda",
    "esi": "ESI Hospital",
    "esi hospital": "ESI Hospital",
    "sr nagar": "SR Nagar",
    "srnagar": "SR Nagar",
    "ameerpet": "Ameerpet",
    "punjagutta": "Punjagutta",
    "irrum manzil": "Irrum Manzil",
    "irrummanzil": "Irrum Manzil",
    "khairatabad": "Khairatabad",
    "lakdikapul": "Lakdikapul",
    "lakdi ka pul": "Lakdikapul",
    "assembly": "Assembly",
    "nampally": "Nampally",
    "gandhi bhavan": "Gandhi Bhavan",
    "gandhibhavan": "Gandhi Bhavan",
    "osmania": "Osmania Medical College",
    "osmania medical college": "Osmania Medical College",
    "mgbs": "MG Bus Station",
    "mg bus station": "MG Bus Station",
    "malakpet": "Malakpet",
    "new market": "New Market",
    "newmarket": "New Market",
    "musarambagh": "Musarambagh",
    "dilsukhnagar": "Dilsukhnagar",
    "dilshuknagar": "Dilsukhnagar",
    "dilsukh nagar": "Dilsukhnagar",
    "chaitanyapuri": "Chaitanyapuri",
    "victoria memorial": "Victoria Memorial",
    "victoriamemorial": "Victoria Memorial",
    "lb nagar": "LB Nagar",
    "lbnagar": "LB Nagar",
    #blue
    "nagole": "Nagole",
    "uppal": "Uppal",
    "stadium": "Stadium",
    "ngri": "NGRI",
    "habsiguda": "Habsiguda",
    "tarnaka": "Tarnaka",
    "mettuguda": "Mettuguda",
    "secunderabad east": "Secunderabad East",
    "secunderabad": "Secunderabad East",
    "secbad": "Secunderabad East",
    "parade ground": "Parade Ground",
    "parade grounds": "Parade Ground",
    "paradise": "Paradise",
    "rasoolpura": "Rasoolpura",
    "prakash nagar": "Prakash Nagar",
    "prakashnagar": "Prakash Nagar",
    "begumpet": "Begumpet",
    "madhura nagar": "Madhura Nagar",
    "madhuranagar": "Madhura Nagar",
    "yusufguda": "Yusufguda",
    "jubilee hills road no 5": "Jubilee Hills Road No. 5",
    "jubilee hills road no. 5": "Jubilee Hills Road No. 5",
    "road no 5": "Jubilee Hills Road No. 5",
    "jubilee hills check post": "Jubilee Hills Check Post",
    "jhcp": "Jubilee Hills Check Post",
    "peddamma gudi": "Peddamma Gudi",
    "madhapur": "Madhapur",
    "durgam cheruvu": "Durgam Cheruvu",
    "durgam": "Durgam Cheruvu",
    "hitech": "HITEC City",
    "hi-tech": "HITEC City",
    "hi-tech city": "HITEC City",
    "hitech city": "HITEC City",
    "raidurg": "Raidurg",
    # green
    "jbs": "JBS Parade Ground",
    "jbs parade ground": "JBS Parade Ground",
    "secunderabad west": "Secunderabad West",
    "gandhi hospital": "Gandhi Hospital",
    "musheerabad": "Musheerabad",
    "rtc cross roads": "RTC Cross Roads",
    "rtc crossroads": "RTC Cross Roads",
    "rtc x roads": "RTC Cross Roads",
    "chikkadpally": "Chikkadpally",
    "narayanguda": "Narayanguda",
    "sultan bazaar": "Sultan Bazaar"
}

def find_station(user_input):

    user_input = user_input.strip().lower()

    if user_input in aliases:
        return aliases[user_input]

    for station in stations:
        if station.lower() == user_input:
            return station

    for station in stations:
        if user_input in station.lower():
            return station

    return None

def calculate_fare(source, destination, passengers):

    source = find_station(source)
    destination = find_station(destination)

    if source is None or destination is None:
        return 0

    source_index = stations.index(source)
    destination_index = stations.index(destination)

    distance = abs(destination_index - source_index)

    if distance == 0:
        fare = 10
    elif distance in fare_table:
        fare = fare_table[distance]
    else:
        fare = 60

    return fare * int(passengers)

def generate_booking_id():
    return "MET" + str(random.randint(10000,99999))

def generate_transaction_id():
    return "TXN" + str(random.randint(100000,999999))
def reset_booking():
    booking["step"]="start"
    booking["source"]=""
    booking["destination"]=""
    booking["passengers"]=""
    booking["date"]=""
    booking["fare"]=""
    booking["booking_id"]=""

def metro_agent(message):

    message = message.strip()

    if booking["step"] == "start":

        if message.lower() == "book ticket":
            booking["step"] = "source"
            return "🚉 Which station are you travelling from?", None

        return """
👋 Welcome to Hyderabad Metro Assistant 🚇

I can help you with:

🎟 Book Ticket
Example: Book Ticket

💰 Fare Details
Example: Fare from Miyapur to Ameerpet

🚇 Train Details
Example: Next train at Ameerpet

Please type your request.
""", None

    elif booking["step"] == "source":

        station = find_station(message)

        if station is None:
            return "❌ Please enter a valid Hyderabad Metro station.", None

        booking["source"] = station
        booking["step"] = "destination"

        panel = {
            "type": "booking",
            "stage": "from",
            "data": {
                "from": booking["source"]
            }
        }

        return "📍 Enter Destination Station.", panel

    elif booking["step"] == "destination":

        station = find_station(message)

        if station is None:
            return "❌ Please enter a valid Hyderabad Metro station.", None

        if station == booking["source"]:
            return "❌ Source and Destination cannot be the same.", None

        booking["destination"] = station
        booking["step"] = "passengers"

        panel = {
            "type": "booking",
            "stage": "to",
            "data": {
                "from": booking["source"],
                "to": booking["destination"]
            }
        }

        return "👥 Enter Number of Passengers.", panel

    elif booking["step"] == "passengers":

        if not message.isdigit():
            return "❌ Please enter a valid number.", None

        if int(message) <= 0:
            return "❌ Passenger count should be at least 1.", None

        booking["passengers"] = message
        booking["step"] = "date"

        panel = {
            "type": "booking",
            "stage": "passengers",
            "data": {
                "from": booking["source"],
                "to": booking["destination"],
                "passengers": booking["passengers"]
            }
        }

        return "📅 Enter Travel Date (DD-MM-YYYY).", panel

    elif booking["step"] == "date":

        if not re.match(r"\d{2}-\d{2}-\d{4}$", message):
            return "❌ Enter date in DD-MM-YYYY format.", None

        booking["date"] = message

        fare = calculate_fare(
            booking["source"],
            booking["destination"],
            booking["passengers"]
        )

        booking["fare"] = fare
        booking["booking_id"] = generate_booking_id()

        booking["step"] = "payment"

        reply = f"""
✅ BOOKING SUMMARY

🚉 Source : {booking['source']}
📍 Destination : {booking['destination']}
👥 Passengers : {booking['passengers']}
📅 Travel Date : {booking['date']}

💰 Total Fare : ₹{fare}

🎟 Booking ID : {booking['booking_id']}

------------------------------------

💳 Type PAY to complete your booking.
"""

        panel = {
            "type": "booking",
            "stage": "confirm",
            "data": {
                "from": booking["source"],
                "to": booking["destination"],
                "passengers": booking["passengers"],
                "date": booking["date"],
                "fare": booking["fare"]
            }
        }

        return reply, panel
    elif booking["step"] == "payment":

        if message.lower() == "pay":

            data = {
                "from": booking["source"],
                "to": booking["destination"],
                "passengers": booking["passengers"],
                "date": booking["date"],
                "fare": booking["fare"],
                "booking_id": booking["booking_id"],
                "transaction": generate_transaction_id(),
                "status": "Confirmed"
            }

            reset_booking()

            reply = f"""
✅ PAYMENT SUCCESSFUL!

🎉 Metro Ticket Booked Successfully.

🎟 Booking ID : {data['booking_id']}

Thank you for choosing Hyderabad Metro.

🚇 Have a Safe Journey!
"""

            panel = {
                "type": "booking",
                "stage": "done",
                "data": data
            }

            return reply, panel

        return "💳 Please type PAY to complete your booking.", None

    return "❌ Something went wrong. Please start again by typing 'Book Ticket'.", None