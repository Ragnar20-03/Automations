from sys import *

    
def Addition (No1 , No2 ): return No1 + No2 

def main():
    print("------------------------------------------ Automation Script ----------------------------")
    
    if (len(argv) == 2):    
        if(argv[1] == '-h' or argv[1] == '-H'):  #Flag for Displaying help
            print("This script is used to perform addition of two numbers ")
            exit()

        elif (argv[1] == "-u" or argv[1] == '-U'):  #Flag for Displaying Usage of script
            print("Usage : Name_Of_Script Fiyrst_Argument Second_Argument ")
            print("Example : Demo.py 11  10")
            exit()
        else:
            print("There is No such Flag ")

    if (len(argv) != 3) :
        print("Invalid Nuber of arguments")
        exit()
    else :
        print("Addition is : " , Addition(int(argv[1]) , int (argv[2])))


if __name__ =="__main__":
    main()


# pyhton3 Script1.py 11 10