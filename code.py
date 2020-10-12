def addition(a, b):
    return eval("%s + %s" % (a, b))

def minus(a, b):
    return a-b

if __name__ == "__main__":

    func_input = {"a":"1", "b":"2"}
    result1 = addition(func_input['a'], func_input['b'])

    print("The addition result is %d." % result1)

    a = int(input("a: "))
    b = int(input("b: "))
    result2 = minus(a,b)

    print("The minus result is %d." % result2)