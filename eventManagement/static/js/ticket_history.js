// ticket_history.js

const ticketHistory = [
    { id: 1, eventName: 'Concert at Venue A', date: 'January 1, 2023', quantity: 2, totalAmount: 1699 },
    // Add more ticket history items as needed
];

document.addEventListener('DOMContentLoaded', displayHistory);

function displayHistory() {
    const historyContainer = document.getElementById('ticketHistory');

    if (ticketHistory.length === 0) {
        historyContainer.innerHTML = '<p>No tickets have been purchased yet.</p>';
    } else {
        const historyItemsHTML = ticketHistory.map((item) => {
            const { eventName, date, quantity, totalAmount } = item;
            return `
            <div class="history-item">
                <div class="event-info">
                    <p><strong>Event Name:</strong> ${eventName}</p>
                    <p><strong>Date:</strong> ${date}</p>
                    <p><strong>Quantity:</strong> ${quantity}</p>
                    <p><strong>Total Amount:</strong> $${totalAmount.toFixed(2)}</p>
                </div>
            </div>`;
        }).join('');

        historyContainer.innerHTML = historyItemsHTML;
    }
}
