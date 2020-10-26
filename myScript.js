/* ---- AturBcnMap ---- */

mapboxgl.accessToken = 'pk.eyJ1IjoiamF1bWVwIiwiYSI6ImNrZ2wwY3dqdjAwd3cycmw4dHNwdnAzbHIifQ.rthttt-mtWvDX8f0R1O49w';

var map = new mapboxgl.Map({
  container: 'map', // container element id
  style: 'mapbox://styles/jaumep/ckgl0etv12e9j19mpedc5gt2l',
  center: [2.155, 41.393], // initial map center in [lon, lat]
  zoom: 12
});

map.on('load', function() {
  map.addLayer({
    id: 'points_duracioatur0',
    type: 'circle',
    filter: ['==', ['number', ['get', 'Mes']], 1],
    source: {
      type: 'geojson',
      data: './points_duracioatur0.geojson' // replace this with the url of your own geojson
    },
    paint: {
      'circle-radius': 2,
      'circle-color': '#00FF00',
      'circle-opacity': 0.5
    }
  });

  map.addLayer({
    id: 'points_duracioatur1',
    type: 'circle',
    filter: ['==', ['number', ['get', 'Mes']], 1],
    source: {
      type: 'geojson',
      data: './points_duracioatur1.geojson' // replace this with the url of your own geojson
    },
    paint: {
      'circle-radius': 2,
      'circle-color': '#FF0000',
      'circle-opacity': 0.5
    }
  });

  map.addLayer({
    id: 'points_duracioatur2',
    type: 'circle',
    filter: ['==', ['number', ['get', 'Mes']], 1],
    source: {
      type: 'geojson',
      data: './points_duracioatur2.geojson' // replace this with the url of your own geojson
    },
    paint: {
      'circle-radius': 2,
      'circle-color': '#0000FF',
      'circle-opacity': 0.5
    }
  });

  //Time Slide Bar
    document.getElementById('slider').addEventListener('input', function(e) {
		var month = parseInt(e.target.value);
		// update the map
	  	map.setFilter('points_duracioatur0', ['==', ['number', ['get', 'Mes']], month]);
	  	map.setFilter('points_duracioatur1', ['==', ['number', ['get', 'Mes']], month]);
	  	map.setFilter('points_duracioatur2', ['==', ['number', ['get', 'Mes']], month]);
	 	//filterHour = ['==', ['number', ['get', 'Hour']], hour];
		//map.setFilter('collisions', ['all', filterHour, filterDay]);

	  	// update text in the UI
	  	document.getElementById('active-hour').innerText = month;
	});
   
	//Filtre durada0
	//document.getElementById('filter0').addEventListener('change', function(e) {
		//var checked = e.target.checked;
		//if (checked) {
			//map.setLayoutProperty('durada0', 'visibility', 'visible');
		//} else {
			//map.setLayoutProperty('durada0', 'visibility', 'none');
		//}
	//}
	
	/*
	document.getElementById('filters').addEventListener('change', function(e) {
		var durada = e.target.value;
	  	// update the map filter
	  	if (durada === 'durada0') {
	  		map.getLayer(durada0).

	  	}
	    //	filterDay = ['!=', ['string', ['get', 'Day']], 'placeholder'];
	    if (day === 'all') {
		  // `null` would not work for combining filters
		  filterDay = ['!=', ['string', ['get', 'Day']], 'placeholder'];
		} else if (day === 'weekday') {
	    	filterDay = ['match', ['get', 'Day'], ['Sat', 'Sun'], false, true];
	  	} else if (day === 'weekend') {
	    	filterDay = ['match', ['get', 'Day'], ['Sat', 'Sun'], true, false];
	  	} else {
	    	console.log('error');
	  	}
	  	map.setFilter('collisions', ['all', filterHour, filterDay]);
	});
	*/
	
});

