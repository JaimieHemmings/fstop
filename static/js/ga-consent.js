function allConsentGranted() {
  gtag('consent', 'update', {
    'ad_user_data': 'granted',
    'ad_personalization': 'granted',
    'ad_storage': 'granted',
    'analytics_storage': 'granted'
  });
}

let dc = document.cookie;

document.addEventListener("DOMContentLoaded", function() {

  // Check if the user has already consented
  if (dc.indexOf("cookie_consent=accepted") > -1) {
    allConsentGranted();
    return;
  } else {
    document.getElementById("cookie-consent").classList.add("show");
    // If the user clicks the consent button then remove the class show from the cookie consent div
    document.getElementById("accept-cookies").addEventListener("click", function() {
      document.getElementById("cookie-consent").classList.remove("show");
      // then add a cookie to the user session to remember that the user has consented
      dc = "cookie_consent=accepted; expires=Fri, 31 Dec 9999 23:59:59 GMT";
      allConsentGranted();
    });
    return;
  }
});