

def do_something(a, b, c, *args, **kwargs):
    # print("funkcijos")
    # print(a, b, c)
    # print(args, (type(args)))
    # for arg in args:
    #     print(arg)
    #
    #     print(kwargs, type(kwargs))
    if "word" in kwargs:
        print("word exists")
    print("viskas")


def another_function(a, **kwargs):
    print(a)
    print(kwargs)


do_something(a=1, b=2, z=3, y=8, word=9, c=99)

another_function(9, bull=10)