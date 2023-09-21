
import multiprocessing , os


#  Creating Processes

def Task1 (value) :
    print("Execution the First Task ")
    print("Pid is for Task 1 : " , os.getpid())
    print("Pid Of Parent is for Task 1 : " , os.getppid())

def Task2 (value) :
    print("Execution the Second Task ")
    print("Pid is for Task 2  : " , os.getpid())
    print("Pid Of Parent is for Task 2 : " , os.getppid())

def main():
    No = 5 ;
    print("Number of Cores are : " , multiprocessing.cpu_count())
    print("Pid is : " , os.getpid())
    p1 = multiprocessing.Process(target=Task1 , args=(No,))
    p2 = multiprocessing.Process(target=Task2 , args=(No,))

    p2.start()
    p1.start()

    print(p1);    # p1 is object which contains -> 
                  # Parent Id , Process Id , name of process 
    print(p2);  

    p1.join()
    p2.join()

    # if We dont call join method then our main process will execute while main code asynchronously
    # 
    #  

    print("Inside Last")

if __name__ == "__main__":
    main()