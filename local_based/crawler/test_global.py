
def add_change():
    global test_n
    print(test_n)
    test_n+=1
    print(test_n)

def p_n():
    global test_n
    print(test_n)

class Number():
    def __init__(self):
        global test_n

    def minus_change(self):
        global test_n
        test_n-=1
        print(test_n)

if __name__=='__main__':
    global test_n
    test_n=3
    add_change()
    p_n()
    number=Number()
    number.minus_change()
    p_n()