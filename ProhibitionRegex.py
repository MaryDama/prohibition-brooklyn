import re
import csv
import requests, json

f = open('prohibition.txt', 'r')

directory = open("prohibition.txt", "r")
booze = open("prohibition.csv", "w")

patternDistill = re.compile('(.*)(D|d)istill(.*)')
patternBrew = re.compile('(.*)(B|b)rewer(.*)')
patternBrew2 = re.compile('(.*)(B|b)rewing(.*)')
#this regex splits the text before and after numerals -- creates name/address split
pattern1 = re.compile('([a-z]+.*?)([0-9]+.*)', re.IGNORECASE)
pattern2 = re.compile('[^A-Za-z0-9]+', re.IGNORECASE)

#results = regex.findall(directory)

with open('prohibition.csv', 'w', newline='') as project_file:
	project_writer = csv.writer(project_file) #delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
		
	for line in open("prohibition.txt"):
		#search for all instances of the word "distill"
			r1 = patternDistill.search(line)
			if r1 != None:
				#remove weird 44s and stray letters
				newline = line.replace('44', '')
				newline = newline.replace('av', 'ave')
				newline = newline.replace(' h ', '')
				newline = newline.replace(' k ', '')
				newline = newline.replace(' b ', '')
				newline = newline.replace(' , ', '')
				#split the lines into cells using the regex pattern defined above
				splitLine = pattern1.split(newline)
				del splitLine[0]
				#line.split()
				project_writer.writerow(splitLine) 

			#search directory for all instances of word "brew"	
			r2 = patternBrew.search(line)
			if r2 != None:
				newline = line.replace('44', '')
				newline = newline.replace('av', 'ave')
				newline = newline.replace(' h ', '')
				newline = newline.replace(' k ', '')
				newline = newline.replace(' b ', '')
				#newline = newline.replace("B'wick", "Bushwick")
				newline = newline.replace(' , ', '')
				#split the lines into cells using the regex pattern defined above
				splitLine = pattern1.split(newline)
				del splitLine[0]
				#write the split up lines to the csv file
				project_writer.writerow(splitLine)

			r3 = patternBrew2.search(line)
			if r3 != None:
				newline = line.replace('44', '')
				newline = newline.replace('av', 'ave')
				newline = newline.replace(' h ', ' residence')
				newline = newline.replace(' k ', '')
				newline = newline.replace(' b ', '')
				newline = newline.replace(' , ', '')
				#split the lines into cells using the regex pattern defined above
				splitLine = pattern1.split(newline)
				del splitLine[0]
				#write the split up lines to the csv file
				project_writer.writerow(splitLine)




#abbreviated places and streets B'wick
#addresses with no number
#Google geocoder to convert to lat and long
