def sumation(*kwargs):
    addition = 0;
    for i in kwargs:
        addition += i
    return addition

def sumation1(*kwargs):
    addition = 0;
    for i in kwargs:
        addition += i
    return addition

if __name__ == '__main__':
    print (sumation(1, 2))
    print (sumation(1, 2, 5))