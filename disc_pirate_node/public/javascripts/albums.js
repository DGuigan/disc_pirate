function populateTable() {
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
    console.log("Albums loaded");
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

populateTable();