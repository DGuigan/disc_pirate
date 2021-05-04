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
    ).then(response => response.json()).then(data => {
      console.log(data);
      updateBasket();
    });
  }
  else {
    alert("Log in to proceed");
  }
}

function updateBasket() {
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
        let checkoutForm = document.getElementById("checkout-form-container");
        let emptyBasket = document.getElementById("empty-basket");
        let table = document.getElementById("basket-table");
        let totalPrice = 0;

        // clear table as it will be rebuilt
        table.innerHTML = "";

        // if basket empty inform user
        if (data.length == 0) {
          emptyBasket.classList.remove("d-none");
          checkoutForm.classList.add("d-none");
          table.classList.add("d-none");
        }
        else {
          checkoutForm.classList.remove("d-none");
          table.classList.remove("d-none");
          emptyBasket.classList.add("d-none");

          // create table headings
          let newRow = document.createElement("tr");
          table.appendChild(newRow);

          let headings = ["Album", "Artist", "Quantity", "Single Price"];
          let basketKeys = Object.keys(data[0]);

          // create table headings
          headings.forEach(heading => {
            let newCol = document.createElement("th");
            newRow.appendChild(newCol);
            newCol.innerHTML = heading;
          })

          // add basket items to table
          data.forEach(element => {
            let newRow = document.createElement("tr");
            table.appendChild(newRow);

            // add each column to the new row
            basketKeys.forEach(key => {
              let column = document.createElement("td");
              column.innerHTML = element[key];
              newRow.appendChild(column);
            })
            totalPrice += parseFloat(element['price']) * element['quantity'];
          })
          document.getElementById("checkout-button").innerHTML = `Checkout (${totalPrice.toFixed(2)})`;
        }
      })
    }
    else {
      alert("Sign in");
    }
}

function getAlbums() {
  fetch("http://localhost:8000/api/albums/?format=json")
    .then(response => response.json())
    .then(data => {
      console.log(data);
      let album_div = document.getElementById("all-albums");

      // add album cards
      data.forEach(element => {
        let card_col = document.createElement("div");
        card_col.classList.add("mt-2", "mb-2", "col-xs-12", "col-sm-6", "col-md-4", "col-lg-4", "col-xl-3");

        let card = document.createElement("div");
        card.classList.add("card", "h-100");

        let card_art = document.createElement("img");
        card_art.classList.add("card-img-top");
        card_art.src = element['albumArt'];

        let card_body = document.createElement("div");
        card_body.classList.add("card-body");

        let card_title = document.createElement("h3");
        card_title.classList.add("card-title");
        card_title.innerHTML = element['albumName'];
        
        let artist = document.createElement("p");
        artist.classList.add("card-text");
        artist.innerHTML = `<b>Artist</b>: ${element['artist']}`;

        let price = document.createElement("p");
        price.classList.add("card-text");
        price.innerHTML = `<b>Price</b>: ${element['price']}`;

        let desc = document.createElement("p");
        desc.classList.add("card-text", "font-italic");
        desc.innerHTML = element['description'];

        let card_button = document.createElement("button");
        card_button.type = "button";
        card_button.classList.add("btn", "mt-100");
        card_button.innerHTML = "Add to basket";

        let card_footer = document.createElement("div");
        card_footer.classList.add("card-footer");
        
        card_button.addEventListener("click", function() {
            addToBasket(element['id']);
        });

        album_div.appendChild(card_col);
        card_col.appendChild(card);
        card.appendChild(card_art);
        card.appendChild(card_body);
        card_body.appendChild(card_title);
        card_body.appendChild(artist);
        card_body.appendChild(price);
        card_body.appendChild(desc);
        card.appendChild(card_footer);
        card_footer.appendChild(card_button);
      })
    })
  }

  getAlbums();