function updateOrders() {
    if (window.token) {
        fetch("http://localhost:8000/view_orders?format=json", {
            method: 'GET',
            headers :{
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': `Token ${window.token}`
            }
        }).then(response => response.json())
            .then(data => {
            console.log(data);
            let noOrders = document.getElementById("no-orders");
            let table = document.getElementById("orders-table");

            // clear table as it will be rebuilt
            table.innerHTML = "";

            // if no orders inform user
            // checking for 1 because object always contains admin flag
            if (data.length == 1) {
                noOrders.classList.remove("d-none");
                table.classList.add("d-none");
            }
            else {  
                noOrders.classList.add("d-none");
                table.classList.remove("d-none");
    
                // create table headings
                let newRow = document.createElement("tr");
                table.appendChild(newRow);
    
                let headings = ["#", "Address", "Date", "Contact Number"];

                // if user is admin display extra info
                if (data[0]['is_admin']) {
                    headings.push("User");
                    document.getElementById("nav-orders-link-text").innerHTML = "All Orders";
                }
                else {
                    document.getElementById("nav-orders-link-text").innerHTML = "Your Orders";
                }

                let orderKeys = Object.keys(data[1]);
    
                headings.forEach(heading => {
                let newCol = document.createElement("th");
                newRow.appendChild(newCol);
                newCol.innerHTML = heading;
                })
    
                // add orders to table
                data.slice(1).forEach(element => {
                    let newRow = document.createElement("tr");
                    table.appendChild(newRow);

                    // add each column to the new row
                    orderKeys.forEach(key => {
                        let column = document.createElement("td");
                        column.innerHTML = element[key];
                        newRow.appendChild(column);
                    })
                })
            }
        })
    }
}