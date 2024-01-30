document.addEventListener('DOMContentLoaded', function() {
    // This function will be executed when the DOM is fully loaded

    // Find the checkout button
    var checkoutButton = document.getElementById('checkoutButton');

    // Add a click event listener to the checkout button
    checkoutButton.addEventListener('click', function() {
        // Check if the user is authenticated (logged in)
        // You can customize the URL for your check-auth endpoint
        fetch('/check_auth/')  // Assuming you have an endpoint to check authentication status
            .then(response => {
                if (response.ok) {
                    // User is authenticated, proceed with checkout logic
                    alert('Checkout logic goes here!');
                } else {
                    // User is not authenticated, redirect to the sign-in page
                    window.location.href = '/signin/';  // Replace with the actual URL of your sign-in page
                }
            })
            .catch(error => console.error('Error checking authentication:', error));
    });
});
