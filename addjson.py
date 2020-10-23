import json
import csv

with open('barris.geojson', 'r') as f:
    data = json.load(f)

with open('2020_Pes_del_atur_registrat_sobre_poblacio_16_64_anys.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	pesaturdict = {}
	poblaciodict = {}
	for row in csv_reader:

		if line_count == 0:
			pass
		elif line_count < 74:
			pesaturdict[int(row[4])] = [float(row[7])]
			poblaciodict[int(row[4])] = int(row[6])
			# row[2] mes
			# row[4] codi Barri
			# row[6] població
			# row[7] pes atur
		else :
			pesaturdict[int(row[4])].append(float(row[7]))
			
		line_count += 1

	print(pesaturdict)

	print(poblaciodict)



#Loop over GeoJSON features and add the new properties
codi_barri = 1
for feat in data['features']:

	feat ['properties']["PES_ATUR"] = pesaturdict[codi_barri]
	feat ['properties']["POBLACIO"] = poblaciodict[codi_barri]
	codi_barri += 1

#Write result to a new file
with open('barris_pesatur.geojson', 'w') as f:
    json.dump(data, f)

