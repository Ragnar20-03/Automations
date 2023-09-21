import multiprocessing

def square(no):
    return no*no;

def main():
    Arr=[10,20,30,40,50]

    result = []

    p = multiprocessing.Pool()
    result = p.map(square  , Arr)
    p.close();
    p.join()

    print(result);



if (__name__=="__main__"):
    main()