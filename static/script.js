const chat = document.getElementById("chat-box");
const input = document.getElementById("user-input");
const panelPlaceholder = document.getElementById("panel-placeholder");
const panelContent = document.getElementById("panel-content");

function addMessage(message, sender) {

    const div = document.createElement("div");

    div.className = sender === "user"
        ? "user-message"
        : "bot-message";

    div.innerHTML = message.replace(/\n/g, "<br>");

    chat.appendChild(div);

    chat.scrollTop = chat.scrollHeight;
}

function renderPanel(panel) {

    if (!panel) return; 

    panelContent.style.display = "block";

    let html = "";

    if (panel.type === "fare") {
        const d = panel.data;
        html = `
            <div class="result-card">
                <div class="card-header">💰 Fare Details</div>
                <div class="card-body">
                    <div class="detail-row">
                        <span class="detail-label">Source</span>
                        <span class="detail-value">${d.source}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">Destination</span>
                        <span class="detail-value">${d.destination}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">Passengers</span>
                        <span class="detail-value">${d.passengers}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">Total Fare</span>
                        <span class="detail-value highlight">₹${d.fare}</span>
                    </div>
                </div>
            </div>
        `;
        panelContent.innerHTML = html;
    }

    else if (panel.type === "train") {
        const d = panel.data;
        html = `
            <div class="result-card">
                <div class="card-header">🚇 Train Details</div>
                <div class="card-body">
                    <div class="detail-row">
                        <span class="detail-label">Station</span>
                        <span class="detail-value">${d.station}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">Next Train</span>
                        <span class="detail-value highlight">${d.next_train}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">Frequency</span>
                        <span class="detail-value">${d.frequency}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">Operating Hours</span>
                        <span class="detail-value">${d.hours}</span>
                    </div>
                </div>
            </div>
        `;
        panelContent.innerHTML = html;
    }

    else if (panel.type === "booking") {
        renderBookingPanel(panel);
    }
}

function renderBookingPanel(panel) {

    const stages = ["from", "to", "passengers", "date", "confirm", "done"];
    const currentIndex = stages.indexOf(panel.stage);
    const d = panel.data || {};

    // Progress bar
    let progressHtml = `<div class="result-card"><div class="booking-progress">`;
    stages.forEach((s, i) => {
        progressHtml += `<div class="progress-step ${i <= currentIndex ? "done" : ""}"></div>`;
    });
    progressHtml += `</div>`;

    // Card body depends on stage
    let bodyHtml = `<div class="card-header">🎟 Booking In Progress</div><div class="card-body">`;

    if (d.from) {
        bodyHtml += `
            <div class="detail-row">
                <span class="detail-label">From</span>
                <span class="detail-value">${d.from}</span>
            </div>`;
    }
    if (d.to) {
        bodyHtml += `
            <div class="detail-row">
                <span class="detail-label">To</span>
                <span class="detail-value">${d.to}</span>
            </div>`;
    }
    if (d.passengers) {
        bodyHtml += `
            <div class="detail-row">
                <span class="detail-label">Passengers</span>
                <span class="detail-value">${d.passengers}</span>
            </div>`;
    }
    if (d.date) {
        bodyHtml += `
            <div class="detail-row">
                <span class="detail-label">Travel Date</span>
                <span class="detail-value">${d.date}</span>
            </div>`;
    }
    if (d.fare) {
        bodyHtml += `
            <div class="detail-row">
                <span class="detail-label">Estimated Fare</span>
                <span class="detail-value highlight">₹${d.fare}</span>
            </div>`;
    }

    bodyHtml += `</div>`;

    let finalHtml = progressHtml + bodyHtml + `</div>`;

    if (panel.stage === "done") {
        finalHtml += `
            <div class="result-card">
                <div class="card-header green">✅ Booking Confirmation</div>
                <div class="card-body">
                    <div class="detail-row">
                        <span class="detail-label">Booking ID</span>
                        <span class="detail-value highlight">${d.booking_id}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">From</span>
                        <span class="detail-value">${d.from}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">To</span>
                        <span class="detail-value">${d.to}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">Passengers</span>
                        <span class="detail-value">${d.passengers}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">Travel Date</span>
                        <span class="detail-value">${d.date}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">Fare</span>
                        <span class="detail-value">₹${d.fare}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">Transaction ID</span>
                        <span class="detail-value">${d.transaction}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">Status</span>
                        <span class="status-badge">${d.status}</span>
                    </div>

                    <div class="success-banner">
                        <span class="icon">🎉</span>
                        <span>Payment Successful! Have a safe and happy journey!</span>
                    </div>
                </div>
            </div>
        `;
    }

    panelContent.innerHTML = finalHtml;
}

async function sendMessage() {

    const message = input.value.trim();

    if (message === "") return;

    addMessage(message, "user");

    input.value = "";

    try {

        const response = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });

        const data = await response.json();

        addMessage(data.reply, "bot");

        renderPanel(data.panel);

    } catch (error) {

        addMessage(
            "❌ Unable to connect to the server. Please try again.",
            "bot"
        );

        console.error(error);
    }
}

function selectService(service) {
    input.value = service;
    sendMessage();
}

document.getElementById("send-btn")
    .addEventListener("click", sendMessage);
input.addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});