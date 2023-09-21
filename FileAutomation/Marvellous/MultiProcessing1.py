
import multiprocessing
import os

def Task1 () :
    print("Executiong the First Task ")
    print("Pid is for Task 1 : " , os.getpid())

def Task2 () :
    print("Executiong the Second Task ")
    print("Pid is for Task 2  : " , os.getpid())

def main():
    print("Number of Cores are : " , multiprocessing.cpu_count())
    print("Pid is : " , os.getpid())
    Task1()
    Task2()


if __name__ == "__main__":
    main()