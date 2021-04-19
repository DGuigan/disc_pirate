function showAlbums() {
    fetch("http://localhost:8000/api/albums/?format=json")
      .then(response => response.json())
      .then(data => {
        console.log(data);
        let table = document.getElementById("album-table");
        data.forEach(element => {
          let newRow = document.createElement("tr");
          table.appendChild(newRow);

          let buttonTd = document.createElement("td");
          let button = document.createElement("button");
          let name = document.createElement("td");
          let artist = document.createElement("td");
          let genre = document.createElement("td");
          let artTd = document.createElement("td");
          let art = document.createElement("img");
          
          button.innerHTML = "Add to basket";
          button.addEventListener('click', function() {
            addToBasket(element['id']);
          });
          name.innerHTML = element['albumName'];
          artist.innerHTML = element['artist'];
          genre.innerHTML = element['genre'];
          art.src = element['albumArt'];

          newRow.appendChild(buttonTd);
          buttonTd.appendChild(button);

          newRow.appendChild(name);
          newRow.appendChild(artist);
          newRow.appendChild(genre);
          newRow.appendChild(artTd);
          artTd.appendChild(art);
        })
      })
    
    // reverse button function
    let album_button = document.getElementById("album-button");
    album_button.onclick = hideAlbums;
    album_button.innerHTML = "Hide Albums";
    console.log("Albums loaded");
}

function hideAlbums() {

  // create blank table
  let table = document.getElementById("album-table");
  table.innerHTML = "";
  let newRow = document.createElement("tr");
  table.appendChild(newRow);

  let headings = ["", "Album", "Artist", "Genre", "Cover"];

  headings.forEach(heading => {
    let newCol = document.createElement("th");
    newRow.appendChild(newCol);
    newCol.innerHTML = heading;
  })

  // reverse button function
  let album_button = document.getElementById("album-button");
    album_button.onclick = showAlbums;
    album_button.innerHTML = "Show Albums";
    console.log("Albums hidden");
}

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
  let newRow = document.createElement("tr");
  table.appendChild(newRow);

  let headings = ["Album", "Artist", "Quantity"];

  headings.forEach(heading => {
    let newCol = document.createElement("th");
    newRow.appendChild(newCol);
    newCol.innerHTML = heading;
  })

  // reverse button function
  let album_button = document.getElementById("basket-button");
    album_button.onclick = showBasket;
    album_button.innerHTML = "Show Basket";
    console.log("Basket hidden");
}