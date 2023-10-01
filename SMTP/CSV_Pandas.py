
import pandas
 
# reading the CSV file
file = pandas.read_csv("Demo.csv" )
print(file.Email)
 
for lines in file:
    print(lines)
# displaying the contents of the CSV file
