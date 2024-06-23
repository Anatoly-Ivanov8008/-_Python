def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


test_function()
# inner_function() - SyntaxError: invalid syntax, нельзя вызвать, так как не в той области видимости