/**
 * Stripe Elements
 */
var stripePublicKey = document.getElementById('id_stripe_public_key').innerText.slice(1, -1);
var clientSecret = document.getElementById('client_secret').innerText.slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

var svgError = `<span class="icon" role="alert">
<svg class="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 13V8m0 8h.01M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"/>
</svg>
</span>`;

var style = {
  base: {
    lineHeight: '1.429',
    color: '#000',
    fontFamily: 'Futura, system-ui, "Helvetica Neue"',
    fontSmoothing: 'antialiased',
    fontSize: '16px',
    '::placeholder': {
      color: '#212529'
    }
  },
  invalid: {
    color: '#f53b00',
    iconColor: '#f53b00'
  }
};

var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle validation errors on the card element
card.addEventListener('change', function(event) {
  var errorDiv = document.getElementById('card-errors');
  if (event.error) {
    var html = `<span>${svgError} ${event.error.message}</span>`;
    errorDiv.innerHTML = html;
  } else {
    errorDiv.textContent = '';
  }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {

  ev.preventDefault();
  card.update({ 'disabled': true});
  document.getElementById('submit-button').disabled = true;

  stripe.confirmCardPayment(clientSecret, {
    payment_method: {
      card: card,
    }
  }).then(function(result) {
    console.log(result);
    if (result.error) {
      var errorDiv = document.getElementById('card-errors');
      var html = `<span>${svgError} ${result.error.message}</span>`;
      errorDiv.innerHTML = html;
      card.update({ 'disabled': false});
      document.getElementById('submit-button').disabled = false;
    } else {
      if (result.paymentIntent.status === 'succeeded') {
        form.submit();
      }
    }
  });
});