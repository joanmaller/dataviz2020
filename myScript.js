/* ---- AturBcnMap ---- */

mapboxgl.accessToken = 'pk.eyJ1IjoiamF1bWVwIiwiYSI6ImNrZ2wwY3dqdjAwd3cycmw4dHNwdnAzbHIifQ.rthttt-mtWvDX8f0R1O49w';

var map = new mapboxgl.Map({
  container: 'map', // container element id
  style: 'mapbox://styles/jaumep/ckgl0etv12e9j19mpedc5gt2l',
  center: [2.155, 41.393], // initial map center in [lon, lat]
  zoom: 12
});

map.on('load', function() {
    
    document.getElementById('content').style.display = 'none';
    
    var coll = document.getElementsByClassName("collapsible");
    coll[0].addEventListener('click', function(e) {
        this.classList.toggle('active');
        var cont = document.getElementById('content')
        cont.style.display = (cont.style.display === 'block') ? 'none' : 'block';
        

      });
    
  map.addLayer({
    id: 'points_duracioatur0',
    type: 'circle',
    filter: ['==', ['number', ['get', 'Mes']], 1],
    source: {
      type: 'geojson',
      data: './points_duracioatur0.geojson' // replace this with the url of your own geojson
    },
    paint: {
      'circle-radius': 3,
      'circle-color': '#00FF00',
      'circle-opacity': 0.25
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
      'circle-radius': 3,
      'circle-color': '#FF0000',
      'circle-opacity': 0.25
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
      'circle-radius': 3,
      'circle-color': '#0000FF',
      'circle-opacity': 0.15
    }
  });
  
  mesos = ['Gener', 'Febrer', 'Març', 'Abril', 'Maig', 'Juny', 'Juliol', 'Agost', 'Setembre', 'Octubre', 'Novembre', 'Desembre']

  //Time Slide Bar
    document.getElementById('slider').addEventListener('input', function(e) {
		var month = parseInt(e.target.value);

	  	map.setFilter('points_duracioatur0', ['==', ['number', ['get', 'Mes']], month]);
	  	map.setFilter('points_duracioatur1', ['==', ['number', ['get', 'Mes']], month]);
	  	map.setFilter('points_duracioatur2', ['==', ['number', ['get', 'Mes']], month]);

	  	// update text in the UI
	  	document.getElementById('active-month').innerText = mesos[month-1];
	});
	
    
   
	document.getElementById('filter0').addEventListener('change', function(e) {
	    map.setLayoutProperty('points_duracioatur0','visibility', e.target.checked ? 'visible' : 'none');
	});
	
	document.getElementById('filter1').addEventListener('change', function(e) {
	    map.setLayoutProperty('points_duracioatur1','visibility', e.target.checked ? 'visible' : 'none');
	});
	
	document.getElementById('filter2').addEventListener('change', function(e) {
	    map.setLayoutProperty('points_duracioatur2','visibility', e.target.checked ? 'visible' : 'none');
	});
	
	

    
});

