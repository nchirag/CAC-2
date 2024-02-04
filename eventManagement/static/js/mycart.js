const product = [
    {
        id: 0,
        image: '/static/images/ticket-01.jpg',
        title: 'Rhythmic Oasis',
        price: 1699,
    },
    {
        id: 1,
        image: '/static/images/ticket-02.jpg',
        title: 'Neon Groove Arena',
        price: 2799,
    },
    {
        id: 2,
        image: '/static/images/ticket-03.jpg',
        title: 'Haven Courtyard',
        price: 1899,
    },
    {
        id: 3,
        image: '/static/images/event-02.jpg',
        title: 'WonderLand Music & Art Festival',
        price: 1599,
    },
    {
        id: 4,
        image: '/static/images/ticket-05.jpg',
        title: 'Big Water Splashing Festival',
        price: 1500,
    },
    {
        id: 5,
        image: '/static/images/ticket-06.jpg',
        title: 'Tiger Dance Hip Hop Festival',
        price: 1799,
    },
];

const categories = product;

let i = 0;
document.getElementById('root').innerHTML = categories.map((item) => {
    var { image, title, price } = item;
    return (
        `<div class='box'>
            <div class='img-box'>
                <img class='images' src=${image}></img>
            </div>
            <div class='bottom'>
                <p>${title}</p>
                <h2>$ ${price}.00</h2>` +
                "<button onclick='addtocart(" + (i++) + ")'>Add to cart</button>" +
                `</div>
        </div>`
    );
}).join('');

var cart = [];

function addtocart(a) {
    cart.push({ ...categories[a], id: cart.length + 1 });
    displaycart();
}

function delElement(a) {
    cart.splice(a, 1);
    displaycart();
}

function displaycart() {
    document.getElementById("count").innerHTML = cart.length;
    if (cart.length === 0) {
        document.getElementById('cartItem').innerHTML = "Your cart is empty";
        document.getElementById("totalMain").innerHTML = "$ 0.00";
        document.getElementById("totalSummary").innerHTML = "$ 0.00";
    } else {
        const cartItemsHTML = cart.map((item) => {
            const { image, title, price, id } = item;
            return (
                `<div class='cart-item'>
                    <div class='row-img'>
                        <img class='rowimg' src=${image}>
                    </div>
                    <p style='font-size:12px;'>${title}</p>
                    <h2 style='font-size: 15px;'>$ ${price}.00</h2>
                    <i class='fa-solid fa-trash' onclick='delElement(${cart.indexOf(item)})'></i>
                </div>`
            );
        }).join('');

        // Update Cart Items
        document.getElementById("cartItem").innerHTML = cartItemsHTML;

        // Update Order Summary
        const total = cart.reduce((acc, item) => acc + item.price, 0).toFixed(2);
        document.getElementById("quantity").innerHTML = cart.length;
        document.getElementById("totalMain").innerHTML = `$ ${total}`;
        document.getElementById("totalSummary").innerHTML = `$ ${total}`;
    }
}

function generatePDF() {
    let total = cart.reduce((acc, item) => acc + item.price, 0); // Calculate total amount

    const htmlContent = `
    <div class="pdf-content">
        <h2>Order Summary</h2>
        ${cart.map((item) => {
            const { image, title, price } = item;
            return `
            <div class='cart-item'>
                <div class='row-img'>
                    <img class='rowimg' src=${image}>
                </div>
                <p style='font-size:12px;'>${title}</p>
                <h2 style='font-size: 15px;'>$ ${price}.00</h2>
            </div>`;
        }).join('')}
        <div class='summary-item'>
            <p>Total Tickets:</p>
            <p>${cart.length}</p>
        </div>
        <div class='summary-item'>
            <p>Total Amount:</p>
            <p>$ ${total.toFixed(2)}</p>
        </div>
    </div>`;

    const element = document.createElement('div');
    element.innerHTML = htmlContent;

    html2pdf(element, {
        margin: 10,
        filename: 'event_tickets.pdf',
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: { scale: 2 },
        jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' },
    });
}

function checkout() {
    generatePDF();
    // Additional checkout logic if needed
}
