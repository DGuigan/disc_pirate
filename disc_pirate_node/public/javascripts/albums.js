function addToBasket(albumId) {
  if (window.token){
    fetch(`http://localhost:8000/add_to_basket/${albumId}?format=json`, {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': `Token ${window.token}`
        }
      }
    ).then(response => response.json()).then(data => console.log(data));
  }
  else {
    alert("Log in to proceed");
  }
}

function showBasket() {
  if (window.token) {
    fetch("http://localhost:8000/view_basket?format=json", {
      method: 'GET',
      headers :{
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': `Token ${window.token}`
      }
    }).then(response => response.json())
      .then(data => {
        let table = document.getElementById("basket-table");

        // create table headings
        let newRow = document.createElement("tr");
        table.appendChild(newRow);

        let headings = ["Album", "Artist", "Quantity"];

        headings.forEach(heading => {
          let newCol = document.createElement("th");
          newRow.appendChild(newCol);
          newCol.innerHTML = heading;
        })

        // add basket items to table
        data.forEach(element => {
          let newRow = document.createElement("tr");
          table.appendChild(newRow);

          let name = document.createElement("td");
          let artist = document.createElement("td");
          let quantity = document.createElement("td");
          
          name.innerHTML = element['albumName'];
          artist.innerHTML = element['artist'];
          quantity.innerHTML = element['quantity'];

          newRow.appendChild(name);
          newRow.appendChild(artist);
          newRow.appendChild(quantity);
        })
      })

    let album_button = document.getElementById("basket-button");
    album_button.onclick = hideBasket;
    album_button.innerHTML = "Hide Basket";
    console.log("Albums loaded");
    }
    else {
      alert("Sign in");
    }
}

function hideBasket() {

  // create blank table
  let table = document.getElementById("basket-table");
  table.innerHTML = "";
  

  // reverse button function
  let album_button = document.getElementById("basket-button");
    album_button.onclick = showBasket;
    album_button.innerHTML = "Show Basket";
    console.log("Basket hidden");
}