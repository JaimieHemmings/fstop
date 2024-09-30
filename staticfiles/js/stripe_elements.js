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
    color: '#000',
    fontFamily: '"Open Sans", sans-serif',
    fontSmoothing: 'antialiased',
    fontSize: '16px',
    '::placeholder': {
      color: '#aab7c4'
    }
  },
  invalid: {
    color: '#dc3545',
    iconColor: '#dc3545'
  }
};

var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle validation errors on the card element
card.addEventListener('change', function(event) {
  var errorDiv = document.getElementById('card-errors');
  if (event.error) {
    var html = `
      ${svgError}
      <span>${event.error.message}</span>
    `;
    $(errorDiv).html(html);
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

  var csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
  var postData = {
    'csrfmiddlewaretoken': csrfToken,
    'client_secret': clientSecret,
  };

  var url = '/checkout/cache_checkout_data/';

  $.post(url, postData).done(function() {
    stripe.confirmCardPayment(clientSecret, {
      payment_method: {
        card: card,
        billing_details: {
          name: $.trim(form.full_name.value),
          email: $.trim(form.email.value),
          phone: $.trim(form.phone_number.value),
          address: {
            line1: $.trim(form.address.value),
            city: $.trim(form.city.value),
            postal_code: $.trim(form.postcode.value),
            country: $.trim(form.country.value)
          }
        }
      },
      shipping: {
        name: $.trim(form.full_name.value),
        phone: $.trim(form.phone_number.value),
        address: {
          line1: $.trim(form.address.value),
          city: $.trim(form.city.value),
          postal_code: $.trim(form.postcode.value),
          country: $.trim(form.country.value)
        }
      }
    }).then(function(result) {
      if (result.error) {
        // Show an error
        var errorDiv = document.getElementById('card-errors');
        var html = `
          ${svgError}
          <span>${result.error.message}</span>
          `
          errorDiv.innerHTML = html;
          card.update({ 'disabled': false});
          document.getElementById('submit-button').disabled = false;
      } else {
        // The payment has been processed!
        if (result.paymentIntent.status === 'succeeded') {
          form.submit();
        }
      }
    });
  }).fail(function() {
    // just reload the page, the error will be in django messages
    location.reload();
  });
});