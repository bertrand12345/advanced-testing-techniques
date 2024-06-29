def addthis(x,y):
    import pdb;pdb.set_trace()
    print(f"this is x: {x} and the x-type {type(x)}")
    print(f"this is y: {y} and the y-type is  {type(y)}")

    try:
        result = x+y
    except TypeError:
        print(f"The wrong type passed")
        result = int(x)+int(y)


    print(f"this is result: {result}")
    return result

print(addthis("one",2))
