<!--var map = L.map('map').setView([{{ cords.lat }}, {{ cords.lng }}], 15);-->



var map = L.map('map');

var MAX_MAKERS = 100;
var markers = [];

var ZOOM_REFRESH = 3;
var zoom_counter = 0;

function markerIn(){

}

function addMarker(marker) {

  if (markers.length>MAX_MAKERS)
  {

    markerRemove = markers[0];
    markers = markers.slice(1,101);



    map.removeLayer(markerRemove);
  };

  map.addLayer(marker);
  markers.push(marker);


};

function removeMarker(marker) {

}

var icons = [];
var lngDefault = 51.507351;
var latDefault = -0.127758;
var zoomDefault = 16;
var icon = L.icon({iconUrl: '/static/frontend/img/markers/marker0.png'});
icons[0] = L.icon({iconUrl: '/static/frontend/img/markers/marker0.png'});
icons[1] = L.icon({iconUrl: '/static/frontend/img/markers/marker1.png'});
icons[2] = L.icon({iconUrl: '/static/frontend/img/markers/marker2.png'});
icons[3] = L.icon({iconUrl: '/static/frontend/img/markers/marker3.png'});
icons[4] = L.icon({iconUrl: '/static/frontend/img/markers/marker4.png'});
icons[5] = L.icon({iconUrl: '/static/frontend/img/markers/marker5.png'});
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a>\
  contributors'
}).addTo(map);

map.setView(new L.LatLng(51.3, 10.1),zoomDefault);

if ("geolocation" in navigator) {
  navigator.geolocation.getCurrentPosition(function(position) {
    map.setView(new L.LatLng(position.coords.latitude,
      position.coords.longitude),zoomDefault);
    var marker = L.marker([position.coords.latitude,
      position.coords.longitude]).addTo(map);
  //   $.ajax({
  //     url: "/vegapi/closest?long="+position.coords.longitude + "&lat=" +
  //      position.coords.latitude,
  //     dataType: "json",
  //     context: document.body
  //   }).done(function(data) {
  //
  //     <!--alert(data);-->
  //     $.each(data['places'],function(datad)
  //     {
  //       <!--console.log(datad);-->
  //       <!--console.log(data['places'][datad]['long']);-->
  //       <!--console.log(data['places'][datad]['lat']);-->
  //       var lng = data['places'][datad]['long'];
  //       var lat = data['places'][datad]['lat'];
  //       var level = data['places'][datad]['level'];
  //       var marker = L.marker([lat, lng], {icon: icons[level]});
  //       addMarker(marker);
  //
  //     }
  //   )
  // });

},function(datae){
  map.setView(new L.LatLng(lngDefault, latDefault),zoomDefault);
  var marker = L.marker([lngDefault, latDefault]).addTo(map);
//   $.ajax({
//     url: "/vegapi/closest?long="+latDefault+"&lat="+lngDefault,
//     dataType: "json",
//     context: document.body
//   }).done(function(data) {
//
//     <!--alert(data);-->
//     $.each(data['places'],function(datad)
//     {
//       <!--console.log(datad);-->
//       <!--console.log(data['places'][datad]['long']);-->
//       <!--console.log(data['places'][datad]['lat']);-->
//       var lng = data['places'][datad]['long'];
//       var lat = data['places'][datad]['lat'];
//       var level = data['places'][datad]['level'];
//       var marker = L.marker([lat, lng], {icon: icons[level]});
//       addMarker(marker);
//
//     }
//   )
// });
}
);
} else {
}


function refresh(e)
{
  console.log(map.getBounds());
  bounds = map.getBounds();
  console.log(bounds["_southWest"]);
  console.log(bounds["_northEast"]);

  bl = bounds["_southWest"];
  tr = bounds["_northEast"];
//
//   $.ajax({
//     url: "/vegapi/box?long1=" + bl['lng'] + "&lat1=" + bl['lat'] + "&" +
//     "long2=" + tr['lng'] + "&lat2=" + tr['lat'],
//     dataType: "json",
//     context: document.body
//   }).done(function(data) {
//
//     <!--alert(data);-->
//     $.each(data['places'],function(datad)
//     {
//       <!--console.log(datad);-->
//       <!--console.log(data['places'][datad]['long']);-->
//       <!--console.log(data['places'][datad]['lat']);-->
//       var lng = data['places'][datad]['long'];
//       var lat = data['places'][datad]['lat'];
//       var level = data['places'][datad]['level'];
//       var marker = L.marker([lat, lng], {icon: icons[level]});
//       addMarker(marker);
//     }
//   )
//
// });
}


map.on('zoomend', function(e) {
  // alert("yes");
  zoom_counter += 1;
  if (zoom_counter>ZOOM_REFRESH){
    refresh(e);
    zoom_counter = 0;
  }
});
map.on('dragend', function(e) {
  zoom_counter += 1;
  if (zoom_counter>ZOOM_REFRESH){
    refresh(e);
    zoom_counter = 0;
  }
});
