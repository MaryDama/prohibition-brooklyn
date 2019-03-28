import csv
f = open('prohibition.txt', 'r')


counter = 0

with open('prohibition.csv', mode='w') as project_file:
	project_writer = csv.writer(project_file, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
		
	for line in open("prohibition.txt"):
		if "distill" in line:
			#distilltext = line.split(',')
			#project_writer.writerow(distilltext)
			#print(counter)
			#print(line)
			project_writer.writerow(("line_ID " + str(counter)) + line)

		if 'brew' in line:
			#brewtext = line.split(',')
			#project_writer.writerow(brewtext)

			#print(counter)
			#print(line)
			project_writer.writerow(("line_ID " + str(counter)) + line)

		counter = counter + 1
	
#Mary is figuring out to edit a specific line in a text file



#message = f.read()
#print(message)
#f.close()


