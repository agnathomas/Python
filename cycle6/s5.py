f = open("C:/Users/student.MCALAB/Desktop/20mca006/python1/Book3.csv", 'a')
import json
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
result = json.dumps(thisdict)
f.write(result)
f.close()
f = open("C:/Users/student.MCALAB/Desktop/20mca006/python1/Book3.csv", 'r')
print(f.read())