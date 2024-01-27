let qtyselected = 0;
const ticketPrice = 1899;
const maxQuantity = 10;

function addcount() {
    if (qtyselected < maxQuantity) {
        qtyselected += 1;
        updateTotalPrice();
    }
}

function subcount() {
    if (qtyselected > 0) {
        qtyselected -= 1;
        updateTotalPrice();
    }
}

function updateTotalPrice() {
    qtyselected = Math.max(0, qtyselected); // Ensure quantity doesn't go below 0
    const totalPrice = qtyselected * ticketPrice;
    document.getElementById('totalAmount').innerText = totalPrice.toFixed(2);
}

function purchaseTickets() {
    // Add your logic for handling the purchase of tickets
    if (qtyselected > 0) {
        alert("You have purchased ${qtyselected} ticket(s) for a total of Rs ${qtyselected * ticketPrice}.");
    } else {
        alert("Please select at least one ticket.");
    }
}