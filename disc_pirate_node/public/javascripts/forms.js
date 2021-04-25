// event listener for login
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
    updateBasket();       
  })

  let basket = document.getElementById("nav-basket-link");
  basket.classList.remove("d-none");
  loginform.classList.add("d-none");
}, true);

// event listener for checkout form
let checkoutButton = document.getElementById("checkout-button");
checkoutButton.addEventListener("click", (event) => {
  event.preventDefault();
  let addr = document.getElementById("checkout-form-address").value;
  let contact = document.getElementById("checkout-form-contact").value;

  if (window.token) {
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
      updateBasket();

      // form.reset() didn't work for me but this works
      document.getElementById("checkout-form-address").value = null;
      document.getElementById("checkout-form-contact").value = null;
    })
  }
  else {
    alert("SIGN IN!");
  }
}, true);
