import json
import csv

with open('2020_Durada_atur.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0

	#S'ha de guardar coordenades, mes i duracio.

	for row in csv_reader:

		if line_count == 0:
			pass
		elif line_count < xx: #Inicialitzar variables
			pesaturdict[int(row[4])] = [float(row[7])]
			poblaciodict[int(row[4])] = int(row[6])
			# row[2] mes
			# row[4] codi Barri
			# row[6] població
			# row[7] pes atur
		else :
			pesaturdict[int(row[4])].append(float(row[7]))
			
		line_count += 1



duracions = [0,1,2]
dictduracions = {0:' < de 6 mesos', 1:' de 6 a 12 mesos', 2:' > 12 mesos'}

c = []
for d in duracions:
c.append 


#Read geoJson header
with open('points_duracioatur.geojson', 'r') as f:
    data = json.load

#Loop over GeoJSON features and add the new points
for d in duracions:

	feature = {}
	feature['type'] = 'Feature'
	feature['geometry'] = {'type' : 'MultiPoint','coordinates' : c[d]}
	feature['properties'] = {'MES': m, 'DURACIO' : d}
	data['features'].append(feature)


#Write result to a new file
with open('points_duracioaturnew.geojson', 'w') as f:
    json.dump(data, f)

