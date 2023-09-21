
import multiprocessing , os


#  Creating Processes

def Task1 (value) :
    print("Execution the First Task ")
    for i in range(value):
        print("Task1 : " , i)


def Task2 (value) :
    print("Execution the Second Task ")
    for i in range(value):
        print("Task2 : " , i)


def main():
    No1 = 500 ;
    No2 = 800 ;
    print("Number of Cores are : " , multiprocessing.cpu_count())
    print("Pid is : " , os.getpid())
    p1 = multiprocessing.Process(target=Task1 , args=(No1,))
    p2 = multiprocessing.Process(target=Task2 , args=(No2,))

    # Parent Id , Process Id , name of process 
    # p1 is object which contains -> 


    p2.start()
    p1.start()


    print(p1);   
    print(p2);  

    p1.join()
    p2.join()

    # if We dont call join method then our main process will execute while main code asynchronously
    # 
    #  

    print("Inside Last")

if __name__ == "__main__":
    main()