import json
import geojson
import csv
import random

from osgeo import ogr

#Obrir i carregar poligons de barris en una llista ordenada per codi barri-1
with open('barris.geojson', 'r') as f:
    data = json.load(f)

poligonsbarris = []
for feature in data['features']:
        geom = feature['geometry']
        geom = json.dumps(geom)
        # Poligon del barri 1 serà guardat a pos 0 de poligonsbarris
        poligonsbarris.append(ogr.CreateGeometryFromJson(geom)) 

"""
duracions = [0,1,2]
dictduracions = {0:"Fins a 6 mesos", 1:"De 6 a 12 mesos", 2:"Més de 12 mesos"}
inv_dictduracions = {"Fins a 6 mesos":0, "De 6 a 12 mesos":1, "Més de 12 mesos":2}

numatur_durada1 = [{}*9]

with open('2020_Durada_atur.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0

		
	#S'ha de guardar coordenades, mes i duracio.
	for row in csv_reader:
		indx_durada = inv_dictduracions[row[6]]

		if line_count == 0:
			pass
		elif int(row[4]) == 1: #Inicialitzar variables

			if indx_durada == 0:
				numatur_durada1[int(row[4])][int(row[1])] = [int(row[7])]
			elif indx_durada == 1:
				numatur_durada2[int(row[4])][int(row[1])] = [int(row[7])]
			else:
			# row[1] mes
			# row[4] codi Barri
			# row[6] durada
			# row[7] número de punts
		else :
			numaturdict[int(row[4])][int(row[1])] = [int(row[7])]
			
		line_count += 1


"""
b = 1
m = 1
polygon = poligonsbarris[b-1]
env = polygon.GetEnvelope()
xmin, ymin, xmax, ymax = env[0],env[2],env[1],env[3]

num_points = 1000

counter = 0

multipoint = ogr.Geometry(ogr.wkbMultiPoint)


for i in range(num_points):
    while counter < num_points:

        point = ogr.Geometry(ogr.wkbPoint)
        point.AddPoint(random.uniform(xmin, xmax),
                       random.uniform(ymin, ymax))

        if point.Within(polygon):

            multipoint.AddGeometry(point)

            counter += 1

feature_barri = multipoint.ExportToJson()
print("Feature Barri:")
print(feature_barri)



#Read geoJson header
with open('points_duracioatur.geojson', 'r') as nf:
    newdata = json.load(nf)

newdata['features'].append(feature_barri)
'''
#Loop over GeoJSON features and add the new points
newdata = data
feature = feature_barri
print(feature["type"])
feature['properties'] = {}
feature['properties']["Mes"] = m
feature['properties']["Codi_Barri"] = b
newdata['features'].append(feature)
'''
#Write result to a new file
with open('points_duracioaturnew.geojson', 'w') as n2f:
    json.dump(newdata, n2f)

