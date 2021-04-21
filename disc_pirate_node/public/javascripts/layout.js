function toggleAlbums() {
    let album_div = document.getElementById("all-albums");
    
    if (album_div.classList.contains("d-none")) {
        album_div.classList.remove("d-none");
        console.log("albums displayed");

    }
    else {
        album_div.classList.add("d-none")
        console.log("albums hidden");
    }
}