mapboxgl.accessToken = 'pk.eyJ1Ijoiam9hbm1hbGxlciIsImEiOiJja2doYWt6MnAwMXZ6MnRxa3AycXJwNWtxIn0.l6RbufRk2cbYgd0rhiYwJQ';

var map = new mapboxgl.Map({
  container: 'map', // container id
  style: 'your-style-url' // replace this with your style URL
});

map.on('load', function() {
  // the rest of the code will go in here
});