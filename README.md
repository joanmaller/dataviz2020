![alt text](https://github.com/joanmaller/dataviz2020/blob/master/AturMapBcn.png?raw=true)
# Atur Map Bcn
Una manera creativa de visualitzar les durades d'atur a través del color i el temps

## Descripció 

Visualització del mapa de Barcelona amb un conjunt de punts on cada un d’ells representa una persona en atur. D’aquesta manera s’obté un núvol de punts que reflecteix la densitat d’aturats en cada barri.  El color, la tercera dimensió, mostra les diferents durades d’atur: fins a 6 mesos, de 6 a 12 i més de 12 mesos. A part de filtrar per la durada de l’atur, també es disposa d’una barra del temps que permet fer un escombrat temporal en cada un dels mesos del 2020. A partir de la visualització, cadascú pot fer el seu anàlisi, nosaltres objectivament intentem fer el següent: Es pot observar l’augment d’aturats de curta durada als primers mesos de l’any, de febrer a abril, com a conseqüència de la crisi de la COVID-19. Tant com la transició de durada d'aturats,  d'un color verd-vermell al Gener, canvia a un vermell-blau al Setembre. Una part de la població segueix aturada i aquesta és una emergència social que hem d'abordar com a societat. Venen temps difícils i entre tots hem d'ajudar a gestionar la crisi, visibilitzar el problema és només una part de la solució. 

Visualització: https://aturmapbcn.000webhostapp.com/


## Usage web

Per utilitzar-ho en local:
Baixar el projecte i visualitzar l'index.html al navegador. 
Fitxer necessaris: styles.css, myScript.js, points_duracioatur0.geojson, points_duracioatur1.geojson i point_duracioatur2.geojson.


## Usage addjsonpoints.py
Per executar l'script d'addjsonpoints.py cal instal·lar les llibreries GDAL i el mòdul osgeo per python
```bash
pip3 install osgeo

```

## Misc
També hi han les dades barris_pesatur.geojson, que son els barris de barcelona situats com a tiles al geojson amb una densitat agafada de les Dades del pes d'atur de 16 a 64 anys, per a graficar com a choropleth.

## Contributing
Ens ha semblat necessari penjar tots els documents de la web, scripts de Python i fitxer geoJson creats en un repositori públic per fer-ho accessible a tothom, que ho vulgui consultar, modificar i replicar. Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. 



