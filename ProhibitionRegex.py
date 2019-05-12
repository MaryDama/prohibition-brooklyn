import re
import csv


#define regex patterns to locate words "brew", "brewing", "distill", and "distilling"
patternDistill = re.compile('(.*)(D|d)istill(.*)')
patternBrew = re.compile('(.*)(B|b)rewer(.*)')
patternBrew2 = re.compile('(.*)(B|b)rewing(.*)')

#this regex splits the text before and after numerals -- creates name/address split in CSV
pattern1 = re.compile('([a-z]+.*?)([0-9]+.*)', re.IGNORECASE)


print('Working...')
#This is where you name a csv file for your data to go into
with open('prohibition1869.csv', 'w', newline='', encoding='utf-8') as project_file:
	project_writer = csv.writer(project_file) 		
	#name of text file (city directory) goes in parentheses here
	for line in open("1869.txt"):
			#search text for all instances of the word "distill" etc.
			r1 = patternDistill.search(line)
			if r1 != None:
				#remove 44's and other stray letters - result of OCR misreading 
				newline = line.replace('44', '')
				newline = newline.replace('av', 'ave')
				#h is abbreviation for "home" in city directories - we replaced this with the word "Residence" to make it
				#more obvious on the map that the point is the residence of a brewer/distiller, rather than a business or 
				#commercial space
				newline = newline.replace(' h ', ' (Residence)') 
				newline = newline.replace(' k ', '')
				#b is abbreviation for "boarder" or "boarding" in city directories - we replaced this with the word "Residence" to make it
				#more obvious on the map that the point is the residence of a brewer/distiller, rather than a business or 
				#commercial space
				newline = newline.replace(' b ', ' (Residence)')
				newline = newline.replace(' , ', '')
				#split the lines into cells using the regex pattern defined above
				splitLine = pattern1.split(newline)
				del splitLine[0]
				#writes the split lines to CSV file
				project_writer.writerow(splitLine)
 
			#reapeat steps above, but search for word "brew" and "brewing"	
			r2 = patternBrew.search(line)
			if r2 != None:
				newline = line.replace('44', '')
				newline = newline.replace('av', 'ave')
				newline = newline.replace(' h ', ' (Residence)')
				newline = newline.replace(' k ', '')
				newline = newline.replace(' b ', ' (Residence)')
				newline = newline.replace(' , ', '')	
				splitLine = pattern1.split(newline)
				del splitLine[0]
				project_writer.writerow(splitLine)

			r3 = patternBrew2.search(line)
			if r3 != None:
				newline = line.replace('44', '')
				newline = newline.replace('av', 'ave')
				newline = newline.replace(' h ', ' (Residence)')
				newline = newline.replace(' k ', '')
				newline = newline.replace(' b ', ' (Residence)')
				newline = newline.replace(' , ', '')
				splitLine = pattern1.split(newline)
				del splitLine[0]
				project_writer.writerow(splitLine)

#Can repeat this as many times as necessary for multiple city directories

with open('prohibition1903.csv', 'w', newline='', encoding='utf-8') as project_file:
	project_writer = csv.writer(project_file) 
		
	for line in open("1903.txt"):
		
			r1 = patternDistill.search(line)
			if r1 != None:
				newline = line.replace('44', '')
				newline = newline.replace('av', 'ave')
				newline = newline.replace(' h ', ' (Residence)')
				newline = newline.replace(' k ', '')
				newline = newline.replace(' b ', ' (Residence)')
				newline = newline.replace(' , ', '')
				splitLine = pattern1.split(newline)
				del splitLine[0]
				project_writer.writerow(splitLine)
 
			r2 = patternBrew.search(line)
			if r2 != None:
				newline = line.replace('44', '')
				newline = newline.replace('av', 'ave')
				newline = newline.replace(' h ', ' (Residence)')
				newline = newline.replace(' k ', '')
				newline = newline.replace(' b ', ' (Residence)')
				newline = newline.replace(' , ', '')	
				splitLine = pattern1.split(newline)
				del splitLine[0]
				project_writer.writerow(splitLine)

			r3 = patternBrew2.search(line)
			if r3 != None:
				newline = line.replace('44', '')
				newline = newline.replace('av', 'ave')
				newline = newline.replace(' h ', ' (Residence)')
				newline = newline.replace(' k ', '')
				newline = newline.replace(' b ', ' (Residence)')
				newline = newline.replace(' , ', '')
				splitLine = pattern1.split(newline)
				del splitLine[0]
				project_writer.writerow(splitLine)

with open('prohibition1912.csv', 'w', newline='', encoding='utf-8') as project_file:
	project_writer = csv.writer(project_file) 
		
	for line in open("1912.txt"):
		
			r1 = patternDistill.search(line)
			if r1 != None:
				newline = line.replace('44', '')
				newline = newline.replace('av', 'ave')
				newline = newline.replace(' h ', ' (Residence)')
				newline = newline.replace(' k ', '')
				newline = newline.replace(' b ', ' (Residence)')
				newline = newline.replace(' , ', '')
				splitLine = pattern1.split(newline)
				del splitLine[0]
				project_writer.writerow(splitLine)
 
			r2 = patternBrew.search(line)
			if r2 != None:
				newline = line.replace('44', '')
				newline = newline.replace('av', 'ave')
				newline = newline.replace(' h ', ' (Residence)')
				newline = newline.replace(' k ', '')
				newline = newline.replace(' b ', ' (Residence)')
				newline = newline.replace(' , ', '')	
				splitLine = pattern1.split(newline)
				del splitLine[0]
				project_writer.writerow(splitLine)

			r3 = patternBrew2.search(line)
			if r3 != None:
				newline = line.replace('44', '')
				newline = newline.replace('av', 'ave')
				newline = newline.replace(' h ', ' (Residence)')
				newline = newline.replace(' k ', '')
				newline = newline.replace(' b ', ' (Residence)')
				newline = newline.replace(' , ', '')
				splitLine = pattern1.split(newline)
				del splitLine[0]
				project_writer.writerow(splitLine)

print('Finished')


