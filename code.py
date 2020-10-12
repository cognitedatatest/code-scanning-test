def addition(a, b):
  return eval("%s + %s" % (a, b))


if __name__ == "__main__":

    func_input = {"a":"1", "b":"2"}
    result = addition(func_input['a'], func_input['b'])
    
    print("The result is %d." % result)