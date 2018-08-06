# This is a comment
test = "3"
print("first: test is", test)

class HelloWorld:
    """I print hello world"""
    def __init__(self):
        ## Create a reference to global variable test, ie the outermost scope
        ## middle scopes are not checked
        test = 4
        print("second, test is", test)

        def innerscope():
            ## Create a reference to an outer socpe's "test"; outer scopes tested in order
            nonlocal test 
            test = "5"
            print("fourth, test is", test)

        print("third, test is", test)
        innerscope()
        print("fifth, test is", test)

hello = HelloWorld()
print("sixth, test is", test)
