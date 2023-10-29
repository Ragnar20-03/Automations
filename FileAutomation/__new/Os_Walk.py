from sys import * ; 
import os 



def main():
    print (argv[1])
    path = argv[1]
    flag = os.path.isabs(argv[1])
    if flag == False:
        argv[1] = os.path.abspath(argv[1])
    exists = os.path.isdir(argv[1])

    for dirName , subdirs , fileList in os.walk(path):
       print("Current folder is : " , dirName , "-------------------------")
       print("Cuurent SubDir is : " , subdirs , "-------------------------")
       for file in fileList:
            print("file : " , file)


if __name__=="__main__":
    main()