import json
import geojson
import csv
import copy
import random

from osgeo import ogr

#Obrir i carregar poligons de barris en una llista ordenada per codi barri-1
with open('barris.geojson', 'r') as f:
    data = json.load(f)

poligonsbarris = {}
for feature in data['features']:
        geom = feature['geometry']
        geom = json.dumps(geom)
        
        poligonsbarris[int(feature["properties"]["BARRI"])] = ogr.CreateGeometryFromJson(geom)




duracions = [0,1,2]
dictduracions = {0:"Fins a 6 mesos", 1:"De 6 a 12 mesos", 2:"Més de 12 mesos"}
inv_dictduracions = {"Fins a 6 mesos":0, "De 6 a 12 mesos":1, "Més de 12 mesos":2}
aturats_barri = {}


#Read geoJson header
with open('points_duracioatur.geojson', 'r') as nf:
    newdata = json.load(nf)

with open('2020_Durada_atur.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0

	#S'ha de guardar coordenades, mes i duracio.
	feature_barri_base ={"type": "Feature", "properties" :{}, "geometry" : {"type": "MultiPoint", "coordinates": []} }
	feature_barris = {}
	line_count = 0
	for row in csv_reader:
		if (line_count != 0 and inv_dictduracions[row[6]] == 2):

			num_barri = int(row[4])
			num_mes = int(row[1])
			print("Barri-",num_barri ,"  Mes-" , num_mes)

			if num_barri != 99 and num_barri != "Codi_Barri": #Codi de barri diferent de no consta
				
				polygon = poligonsbarris[num_barri]
				print
				env = polygon.GetEnvelope()
				xmin, ymin, xmax, ymax = env[0],env[2],env[1],env[3]
				num_aturats = int(row[7])
				print("Row 7: ", num_aturats)

				if num_mes == 1:
					aturats_barri[num_barri] = num_aturats
					feature_barris[num_barri] = copy.deepcopy(feature_barri_base)
					feature_barris[num_barri]["properties"]["Barri"] = num_barri
					
					counter = 0
					for i in range(num_aturats):
					    while counter < num_aturats:
					        point = ogr.Geometry(ogr.wkbPoint)
					        point.AddPoint(random.uniform(xmin, xmax),
					                       random.uniform(ymin, ymax))
					        if point.Within(polygon):
					            feature_barris[num_barri]["geometry"]["coordinates"].append([point.GetX(),point.GetY()])
					            counter += 1
					feat = copy.deepcopy(feature_barris[num_barri])
					
					coordenades = feature_barris[num_barri]["geometry"]["coordinates"]
					
				else:
	
					feat = copy.deepcopy(feature_barris[num_barri])
					coordenades = feature_barris[num_barri]["geometry"]["coordinates"]
					#Si el num nou d'aturats es més baix seleccionar una part dels aturats màxims

					if num_aturats < aturats_barri[num_barri]:
						coordenades = coordenades[0:num_aturats]

					else:
						num_points = num_aturats - aturats_barri[num_barri]
						aturats_barri[num_barri] = num_aturats

						counter = 0
						for i in range(num_points):
						    while counter < num_points:
						        point = ogr.Geometry(ogr.wkbPoint)
						        point.AddPoint(random.uniform(xmin, xmax),
						                       random.uniform(ymin, ymax))
						        if point.Within(polygon):
						            coordenades.append([point.GetX(),point.GetY()])
						            counter += 1

						feature_barris[num_barri]["geometry"]["coordinates"] = coordenades            	

				feat["geometry"]["coordinates"] = coordenades
				feat["properties"]["Mes"] = num_mes
				print(len(coordenades))
				print("Punts afegits: ", len(feat["geometry"]["coordinates"]))
				
				newdata['features'].append(copy.deepcopy(feat))

		line_count += 1

#Write result to a new file
with open('points_duracioatur2.geojson', 'w') as n2f:
    json.dump(newdata, n2f)

