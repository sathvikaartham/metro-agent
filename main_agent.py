from agent import metro_agent, booking
from fare_agent import fare_agent, fare_memory
from train_agent import train_agent, train_memory

def main_agent(message):
    text = message.lower().strip()

    if booking["step"] != "start":
        return metro_agent(message)
    
    if fare_memory["step"] != "start":
        return fare_agent(message)
   
    if train_memory["step"] != "start":
        return train_agent(message)

    if text == "book ticket":
        return metro_agent(message)
  
    fare_keywords = [
        "fare",
        "fare details",
        "price",
        "cost",
        "ticket price",
        "how much"
    ]
    if any(keyword in text for keyword in fare_keywords):
        return fare_agent(message)

    train_keywords = [
        "train",
        "train details",
        "next train",
        "timing",
        "timings",
        "schedule",
        "arrival"
    ]

    if any(keyword in text for keyword in train_keywords):
        return train_agent(message)

    
    reply = """
👋 Welcome to Hyderabad Metro Assistant

Your smart assistant for Hyderabad Metro services.

Please choose one of the services below to get started.

🎟 Book Ticket

💰 Fare Details

🚇 Train Details

Example Queries

• Book Ticket

• Fare from Miyapur to Ameerpet

• Fare from MGBS to Raidurg

• Next train at JBS

• Train timing for Dilsukhnagar
"""
    return reply, None