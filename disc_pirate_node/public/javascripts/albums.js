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
        let table = document.getElementById("basket-table");

        table.innerHTML = "";

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
      let album_div = document.getElementById("all-album-cards");

      // add album cards
      data.forEach(element => {
        let card_col = document.createElement("div");
        card_col.classList.add("col-3");

        let card = document.createElement("div");
        card.classList.add("card");

        let card_art = document.createElement("img");
        card_art.classList.add("card-img-top");
        card_art.src = element['albumArt'];

        let card_body = document.createElement("div");
        card_body.classList.add("card-body");

        let card_title = document.createElement("h4");
        card_title.classList.add("card-title");
        card_title.innerHTML = element['albumName'];

        let card_text = document.createElement("div");
        card_text.classList.add("card-text");
        
        let artist = document.createElement("p");
        artist.innerHTML = `Artist: ${element['artist']}`;

        let price = document.createElement("p");
        price.innerHTML = `Price: ${element['price']}`;

        let desc = document.createElement("p");
        desc.innerHTML = element['description'];

        let card_button = document.createElement("button");
        card_button.type = "button";
        card_button.classList.add("btn", "btn-primary");
        card_button.innerHTML = "Add to basket";
        
        card_button.addEventListener("click", function() {
            addToBasket(element['id']);
        });

        album_div.appendChild(card_col);
        card_col.appendChild(card);
        card.appendChild(card_art);
        card.appendChild(card_body);
        card_body.appendChild(card_title);
        card_body.appendChild(card_text);
        card_text.append(artist, price, desc);
        card_body.appendChild(card_button);
      })
    })
  }

  getAlbums();