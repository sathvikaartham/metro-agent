# 🚇 Metro Agent

An AI-powered Metro Assistant that helps users get useful information about metro trains, routes, fares, and other metro-related queries through an interactive chat interface.

## 🌐 Live Demo

👉 [Try Metro Agent](https://metro-agent-1.onrender.com/)

## 📌 About the Project

Metro Agent is a web-based AI assistant designed to make metro travel information easier to access. Users can interact with the assistant through a simple chat interface and ask questions related to metro services.

The application uses a Flask backend and an AI agent system to process user queries and generate relevant responses.

## ✨ Features

- 🤖 AI-powered conversational metro assistant
- 🚆 Train-related information
- 💰 Fare-related information
- 🛤️ Metro and route-related queries
- 💬 Interactive chat interface
- 📊 Additional information panels for supported responses
- 🌐 Deployed and accessible online
- 📱 Simple and user-friendly interface

## 🏗️ Project Structure

```text
Metro-Agent/
│
├── app.py
├── main_agent.py
├── agent.py
├── fare_agent.py
├── train_agent.py
├── templates/
│   └── index.html
├── static/
├── requirements.txt
├── Procfile
└── README.md
```

## 🛠️ Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- AI Agents
- Gunicorn
- GitHub
- Render

## 🔄 How It Works

```text
User
  │
  ▼
Chat Interface
  │
  ▼
Flask Backend
  │
  ▼
Main Agent
  │
  ├── Train Agent
  ├── Fare Agent
  └── Other Agent Functions
  │
  ▼
Response
  │
  ▼
User
```

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Metro-Agent
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

### 5. Run the application

```bash
python3 app.py
```

Open:

```text
http://localhost:50001
```

## ☁️ Deployment

The application is deployed using Render.

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
gunicorn app:app
```

### Live Application

https://metro-agent-1.onrender.com/

## 🔐 Environment Variables

If the project uses API keys or other sensitive credentials, store them as environment variables rather than committing them to GitHub.

> ⚠️ Never commit API keys, passwords, or other secrets to the repository.

## 📋 Example Queries

Users can ask questions such as:

- What is the fare between two metro stations?
- Which trains are available?
- How can I travel between two stations?
- Give me metro-related information.

## 🎯 Project Goals

- Make metro information easier to access
- Provide a conversational interface for users
- Reduce the need to search multiple sources
- Demonstrate the use of AI agents in a real-world application
- Build a deployable AI-powered web application

## 🔮 Future Enhancements

- 📍 Real-time metro tracking
- 🚉 Station-wise information
- 🗺️ Interactive metro maps
- ⏱️ Real-time arrival information
- 🚨 Service disruption notifications
- 🎫 Ticket and booking integration
- 📱 Mobile application
- 🎙️ Voice-based interaction
- 🌍 Support for multiple cities and metro systems

## 👩‍💻 Author

**Sathvika Artham**

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

## 📄 License

This project is created for educational and project-development purposes.
