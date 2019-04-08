import re
import csv
f = open('prohibition.txt', 'r')

directory = open("prohibition.txt", "r")
booze = open("booze.csv", "w")

patternDistill = re.compile('(.*)(D|d)istill(.*)')
patternBrew = re.compile('(.*)(B|b)rew(.*)')
pattern1 = re.compile('([a-z]+.*?)([0-9]+.*)', re.IGNORECASE)


#results = regex.findall(directory)

with open('prohibition.csv', mode='w') as project_file:
	project_writer = csv.writer(project_file, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
	
	for line in open("prohibition.txt"):
		#if re.search('(.*)(D|d)istill(.*)', line):
			r1 = patternDistill.search(line)
			if r1 != None:
				newline = line.replace('44', '')
				splitLine = pattern1.split(newline)
				project_writer.writerow(splitLine)
			r2 = patternBrew.search(line)
			if r2 != None:
				newline = line.replace('44', '')
				splitLine = pattern1.split(newline)
				splitLine = pattern1.split(newline)
				project_writer.writerow(splitLine)




#([A|a-z]+.*?)([0-9]+.*)

#newline = line.replace('44', '')
 #booze.write(newline)
    	# 	newline = line.replace('44', '')
    	# 	booze.write(newline)
    	# if re.search('(.*)(B|b)rew(.*)', line):
    	# 	newline = line.replace('44', '')
    	# 	booze.write(newline)



#REMOVE THE 44s

	#newline = line.replace('44', '')
				#booze.write(newline)
