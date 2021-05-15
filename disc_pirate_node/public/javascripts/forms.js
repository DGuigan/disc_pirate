let login_dropdown = document.getElementById("nav-login-link");
// event listener for login
let loginform = document.getElementById("login-form");

loginform.addEventListener("submit", (event)=>{
  event.preventDefault();
  let user = document.getElementById("login-form-username").value;
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
    // store user token in window
    if (data.hasOwnProperty('token')) {
      window.token = data['token'];

      // update tables for first time
      updateBasket();
      updateOrders();

      // adjust layout of navbar for logged in user
      let basket = document.getElementById("nav-basket-link");
      let orders = document.getElementById("nav-orders-link");
      basket.classList.remove("d-none");
      orders.classList.remove("d-none");
      login_dropdown.classList.add("d-none");
    }
    else {
      alert("Invalid login details");
    }
  })
}, true);

// event listener for signup
let signupform = document.getElementById("signup-form");

signupform.addEventListener("submit", (event)=>{
  event.preventDefault();
  let user = document.getElementById("signup-form-username").value;
  let pass1 = document.getElementById("form-password-1").value;
  let pass2 = document.getElementById("form-password-2").value;

  if (pass1.localeCompare(pass2) == 0) {
    fetch("http://localhost:8000/node_signup/?format=json/", {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify( {username: user, password1: pass1, password2: pass2} )
    }).then(response => response.json()).then(data => {
      console.log(data);
      // store user token in window
      if (data.hasOwnProperty('token')) {
        window.token = data['token'];

        // update tables for first time
        updateBasket();
        updateOrders();

        // adjust layout of navbar for logged in user
        let basket = document.getElementById("nav-basket-link");
        let orders = document.getElementById("nav-orders-link");
        basket.classList.remove("d-none");
        orders.classList.remove("d-none");
        login_dropdown.classList.add("d-none");
      }
      else {
        alert("Invalid signup details");
      }
    })
  }
  else {
    alert("Passwords do not match");
  }
}, true);

// event listener for checkout form
let checkoutButton = document.getElementById("checkout-button");
checkoutButton.addEventListener("click", (event) => {
  event.preventDefault();
  let addr = document.getElementById("checkout-form-address").value;
  let contact = document.getElementById("checkout-form-contact").value;

  if (window.token && addr && contact) {
    fetch("http://localhost:8000/order_form/?format=json", {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': `Token ${window.token}`
      },
      body: JSON.stringify( {address: addr, contactNumber: contact} )
    }).then(response => response.json()).then(data => {
      console.log(data);

      // update tables as they will have changed
      updateBasket();
      updateOrders();

      // reset form values
      document.getElementById("checkout-form-address").value = null;
      document.getElementById("checkout-form-contact").value = null;
    })
  }
  else if (!window.token){
    alert("SIGN IN!");
  }
  else {
    alert("Order form must be filled in.");
  }
}, true);
