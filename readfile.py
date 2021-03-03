#Open files
import csv

with open("leads.txt") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count=0

    for line in csv_reader:
        print("Nombre: %s %s\nCompany: %s\n" % (line[0], line[1], line[2]))
    
    
    
