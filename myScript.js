mapboxgl.accessToken = 'pk.eyJ1IjoiamF1bWVwIiwiYSI6ImNrZ2wwY3dqdjAwd3cycmw4dHNwdnAzbHIifQ.rthttt-mtWvDX8f0R1O49w';

var map = new mapboxgl.Map({
  container: 'map', // container id
  style: 'mapbox://styles/jaumep/ckgl0etv12e9j19mpedc5gt2l', // replace this with your style URL
  center: [2.16, 41.38], // centre [lon,lat]
  zoom : 12


});

map.on('load', function() {
  // the rest of the code will go in here
});