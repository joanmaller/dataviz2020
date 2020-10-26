# World Data Viz 2020

Participació al concurs de World Data Viz Challenge 2020. 
Veient el repositori de datasets de OpenData, vam decidir que seria interessant com l'atur havia evolucionat a Barcelona en els últims mesos, per això seria interessant creuar les dades de l'atur per barris amb les geogràfiques dels propis barris de Barcelona. Així aconseguint un núvol de densitats d'aturats.
Al veure que també hi havia informació sobre la durada de l'atur, vam pensar en el color, una altra manera de visualitzar dades.

Una visualització en l'espai 2d de barcelona, en que també tenim el control del temps i de les capes de color per veure l'evolució de l'atur i fer l'anàlisi nosaltres a partir de la propia viz.

Visualització: https://aturmapbcn.000webhostapp.com/

Ens ha semblat necessari penjar també tots els documents de la web, scripts de Python i fitxer geoJson creats en un repositori públic per fer-ho accessible a tothom, que ho vulgui consultar, modificar i replicar. 

## Usage web

Per utilitzar-ho en local:
Baixar el projecte i visualitzar l'index.html al navegador. 
Fitxer necessaris: styles.css, myScript.js, points_duracioatur0.geojson, points_duracioatur1.geojson i point_duracioatur2.geojson.


## Usage addjsonpoints.py
Per executar l'script d'addjsonpoints.py cal instal·lar les llibreries GDAL i el mòdul osgeo per python
'''bash
pip3 install osgeo

'''
## Misc
També hi han les dades barris_pesatur.geojson, que son els barris de barcelona situats com a tiles al geojson amb una densitat agafada de les Dades del pes d'atur de 16 a 64 anys, per a graficar com a choropleth.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


