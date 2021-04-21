// event listener for login
let loginContainer = document.getElementById("nav-login");
let loginform = document.getElementById("login-form");

loginform.addEventListener("submit", (event)=>{
  event.preventDefault();
  let user = document.getElementById("form-username").value;
  let pass = document.getElementById("form-password").value;
  fetch("http://localhost:8000/token/", {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify( {username: user, password: pass} )
  }).then(response => response.json()).then(data => {
    console.log(data);
    window.token = data['token'];        
  })

  // replace form with greeting
  let greeting = document.createElement("h3");
  greeting.innerHTML = `Hello ${user}`;
  loginContainer.innerHTML = "";
  loginContainer.appendChild(greeting);
}, true);