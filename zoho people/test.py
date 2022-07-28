x=5

def same():
    print(x)
    def same1():
        print(x)

    same1()

same()