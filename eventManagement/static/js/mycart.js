const product = [
    {
        id: 0,
        image: '/static/images/ticket-01.jpg',
        title: 'Rhytmic Oasis',
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
const categories = [...new Set(product.map((item)=>
    {return item}))]
    let i=0;
document.getElementById('root').innerHTML = categories.map((item)=>
{
    var {image, title, price} = item;
    return(
        `<div class='box'>
            <div class='img-box'>
                <img class='images' src=${image}></img>
            </div>
        <div class='bottom'>
        <p>${title}</p>
        <h2>$ ${price}.00</h2>`+
        "<button onclick='addtocart("+(i++)+")'>Add to cart</button>"+
        `</div>
        </div>`
    )
}).join('')

var cart =[];

function addtocart(a){
    cart.push({...categories[a]});
    displaycart();
}
function delElement(a){
    cart.splice(a, 1);
    displaycart();
}

function displaycart(){
    let j = 0, total=0;
    document.getElementById("count").innerHTML=cart.length;
    if(cart.length==0){
        document.getElementById('cartItem').innerHTML = "Your cart is empty";
        document.getElementById("total").innerHTML = "$ "+0+".00";
    }
    else{
        document.getElementById("cartItem").innerHTML = cart.map((items)=>
        {
            var {image, title, price} = items;
            total=total+price;
            document.getElementById("total").innerHTML = "$ "+total+".00";
            return(
                `<div class='cart-item'>
                <div class='row-img'>
                    <img class='rowimg' src=${image}>
                </div>
                <p style='font-size:12px;'>${title}</p>
                <h2 style='font-size: 15px;'>$ ${price}.00</h2>`+
                "<i class='fa-solid fa-trash' onclick='delElement("+ (j++) +")'></i></div>"
            );
        }).join('');
    }

    
}