# Booze in Brooklyn: Visualizing pre-prohibition alcohol production  
King’s County Distillery, established in 2010, claims to be the “oldest whiskey distillery in Brooklyn” because of how lasting the effects of prohibition were on alcohol production in this borough. We’re interested in knowing which neighborhoods felt these effects most.

As our primary data source in this investigation, we used digitized Brooklyn city and business directories available on Internet Archive. By using python to read our three chosen directories (listed and linked below), parse them and write the relevant lines to CSV, then geocoding the CSV and importing it into Google My Maps, we visualized the distilleries and breweries in Brooklyn, showing where alcohol production occurred prior to Prohibition. 

Instructions for running script:
- The script available in ProhibitionRegex.py takes in the text file of a directory and outputs a CSV. The code is commented to explain this process.
- Each directory that we used (original linked below) is available in this repository as a txt file, and the code should be modified on line 19 to reflect which txt file you want to read. 
- Line 16 should then be modified to reflect what you'd like the resultant CSV to be called. 
- For reference, the CSVs that we produced with this code are also available in this repository. Please note that they have been manually cleaned to control for mistakes in the OCR of the original documents. 

More information on this project is available at https://sites.google.com/view/booze-in-brooklyn

 

RESOURCES

Kings County Distillery. Retrieved March 25, 2019, from http://kingscountydistillery.com/about/

(1869). Brooklyn City and Business Directory for the year ending May 1, 1869. New York: J. Lain and Company. https://archive.org/details/1869BPL/page/n4

(1903). Upington's General Directory of the Borough of Brooklyn, City of New York, for the year 1903. New York: Brooklyn Directory Company. https://archive.org/details/1903BPL/page/n1https://archive.org/details/1903BPL/page/n1

(1912). The Brooklyn City Directory volume LXXXVIII. New York: Brooklyn Directory Company. https://archive.org/details/brooklynnewyor1912p3broo/page/n6

Geocode by Awesome Table. Retrieved May 8, 2019, from https://gsuite.google.com/marketplace/app/geocode_by_awesome_table/904124517349

Google My Maps. Retrieved March 25, 2019, from https://www.google.com/mymaps

 

 

 

