d = 1


def test_function():
    d = 10

    def inner_function():
        d = 'local'
        print("Я в области видимости функции test_function")

    inner_function()


test_function()
