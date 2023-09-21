import time
import multiprocessing

def fun(no):
    sum = 0 ;
    for i in range(100000):
        sum = sum+(no*no);
    return sum


def main():
    print("Demomstartion of Serial Execution using Single Core")
    
    result =[]
    
    start = time.time()
    
    p = multiprocessing.Pool()
    result = p.map(fun , range(10000))
    p.close()
    p.join()

    end = time.time()
    print("Time Required to execute App: " , end - start);

        
if __name__ == "__main__":
    main()