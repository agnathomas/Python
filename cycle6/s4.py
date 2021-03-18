import csv
with open("C:/Users/student.MCALAB/Desktop/20mca006/python1/book1.csv", "r",) as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)