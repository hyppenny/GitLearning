window.onload = function initMap() {
    var canvas = document.getElementById("map");
    var options = {
        center: new google.maps.LatLng(53.343507, -6.253920),
        zoom: 16
    };
    var map = new google.maps.Map(canvas, options);
}

document.write('<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAN-k2Z0JpTVPPzGkt61YImxgxTf4PUzk0&language=en"></script>')
