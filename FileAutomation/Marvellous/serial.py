
def fun(no):
    sum = 0 ;
    for i in range(100000):
        sum = sum+(no*no);
    return sum


def main():
    print("Demomstartion of Serial Execution using Single Core")
    print(fun(5))

if __name__ == "__main__":
    main()