class Test:

    def __init__(self, foo):
        self.__foo = foo

    def bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    # AttributeError: 'Test' object has no attribute '__bar'
    test.bar()
    # AttributeError: 'Test' object has no attribute '__foo'
    #print(test.__foo)


if __name__ == "__main__":
    main()