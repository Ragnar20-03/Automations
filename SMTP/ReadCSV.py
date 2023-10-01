import csv

def main():

    # opening the CSV file 
    with open('Demo.csv', mode ='r')as file: 

      # reading the CSV file 
      csvFile = csv.reader(file )
       

      # displaying the contents of the CSV file 
      for lines in csvFile: 
            print(lines[1]) 


if __name__=="__main__":
    main()

