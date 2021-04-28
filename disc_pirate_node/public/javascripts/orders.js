function getOrders() {
    if (window.token) {
        fetch("http://localhost:8000/view_orders?format=json", {
            method: "GET",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': `Token ${window.token}`
            }
        }).then(response => response.json()).then(data => console.log(data));
    }
}