import requests
import csv
import json

#PURPOSE: api function used for getting address and other data
def getGeoIP(ip):
	url = "http://freegeoip.net/json/" + ip
	try:
		response = requests.get(url)
	except:
		print "error"
	return response.json()


#PURPOSE: method for finding the index of the x occurence of particular
#value in the list
###
#i.e find the 5th 4 in the list
###
#This method is written because the WebGL Globe does not
#support more than 3 data sets of (long lat intensity), from
#the same long and lat. The globe will fail to appear.
#The error shown is attached in the repo, hopefully there is a fix!
def indexForTheXOccurenceOfValue(x, value, theList):
	count = 0
	index = -1
	while count < x:
		index += 1
		if theList[index] == value:
			count+=1
	return index

#reading the data source file
file_name = "finalServiceData15_days_smaller_than_1000_fewer_data.csv"
csvFile = open(file_name,"rU")
rows = csv.reader(csvFile)

#three categories declaration
longitude_latitude_front_end = []
longitude_latitude_infrastructure = []
longitude_latitude_core = []

# loop through rows and reorganize
# some csv may require a change to:
# for src_ip, service, normalized_count, _ in rows
for src_ip, service, normalized_count in rows:
	try:
		print src_ip
		jsonIP = getGeoIP(src_ip)
		temp_longitude = jsonIP['longitude']
		print "got longitude"
		temp_latitude = jsonIP['latitude']
		print "got latitude"
		temp_magnitude = normalized_count

		#Three categories (commented region did not generate the json file: ignoring all lon lan after 3rd count)
		if (service == 'imedidata' or service == 'production' or service == 'balance'
		or service == 'janus' or service == 'validationportal'):
			print longitude_latitude_front_end

			# testIndexForThirdLatitude = indexForTheXOccurenceOfValue(3,temp_latitude,longitude_latitude_front_end)
			# testIndexForThirdLongitude = testIndexForThirdLatitude+1
			# totalIndexCount = len(longitude_latitude_front_end) - 1
			# if testIndexForThirdLatitude != totalIndexCount and longitude_latitude_front_end[testIndexForThirdLongitude] == temp_longitude:
			# 	continue
			# else:

			longitude_latitude_front_end = longitude_latitude_front_end +  [temp_latitude,temp_longitude, temp_magnitude]

		if (service == 'mauth' or service == 'kraken' or service == 'Dalton'
		or service == 'heureka' or service == 'archon' or service == 'eureka'
		or service == 'checkmate' or service == 'connectome' or service == 'hercules'):

			# testIndexForThirdLatitude = indexForTheXOccurenceOfValue(3,temp_latitude,longitude_latitude_infrastructure)
			# testIndexForThirdLongitude = testIndexForThirdLatitude+1
			# totalIndexCount = len(longitude_latitude_infrastructure) - 1
			# if testIndexForThirdLatitude != totalIndexCount and longitude_latitude_infrastructure[testIndexForThirdLongitude] == temp_longitude:
			# 	continue
			# else:

			longitude_latitude_infrastructure = longitude_latitude_infrastructure +  [temp_latitude,temp_longitude, temp_magnitude]

		if (service == 'Subjects' or service == 'apollo' or service == 'mccadmin'
		or service == 'athena' or service == 'activities' or service == 'maudit'
		or service == 'plinth' or service == 'kotengu'):

			# testIndexForThirdLatitude = indexForTheXOccurenceOfValue(3,temp_latitude,longitude_latitude_core)
			# testIndexForThirdLongitude = testIndexForThirdLatitude+1
			# totalIndexCount = len(longitude_latitude_core) - 1
			# if testIndexForThirdLatitude != totalIndexCount and longitude_latitude_core[testIndexForThirdLongitude] == temp_longitude:
			# 	continue
			# else:

			longitude_latitude_core = longitude_latitude_core +  [temp_latitude,temp_longitude, temp_magnitude]

	except:
		print "unable to get coordinates for " + src_ip

print "done!!!!!"

#format the output to fit globe.js
output = [["Front End", longitude_latitude_front_end],
["Infrastructure", longitude_latitude_infrastructure],
["Core", longitude_latitude_core]]

# Generate the JSON file
json_file = open("globe/trial_smaller_than_1000_new.json","w")
json.dump(output, json_file)
