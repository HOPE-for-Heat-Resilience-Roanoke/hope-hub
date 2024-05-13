function initAutocomplete() {
  const southwest = { lat: 37.2336297, lng: -80.136922 };
  const northeast = { lat: 37.3587137, lng: -79.942215 };
  const defaultBounds = new google.maps.LatLngBounds(southwest, northeast);

  autocomplete = new google.maps.places.Autocomplete(
      (document.getElementById('autocomplete')), {
        types: ['geocode'],
        bounds: defaultBounds,
        strictBounds: true,
      }
  );

  service = new google.maps.Geocoder();
  // service = new google.maps.places.PlacesService();


  // When the user selects an address from the dropdown, populate the address
  // fields in the form.
  autocomplete.addListener('place_changed', function () {
    fillInAddress(autocomplete.getPlace());
  });
}

function fillInAddress(place) {
   // place = autocomplete.getPlace();
  console.log(place);
  console.log(place.geometry.location.lat());
  console.log(place.geometry.location.lng());

  document.getElementById('id_latitude').value = place.geometry.location.lat();
  document.getElementById('id_longitude').value = place.geometry.location.lng();
}

// document.addEventListener("DOMContentLoaded", () => {
//   document.getElementById('id_latitude').disabled = "true";
//   document.getElementById('id_longitude').disabled = "true";
// });
