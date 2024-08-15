def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


#inner_function() Функция создается внутри другой функции которая не возвращает ничего
#поэтому вне функции inner_function не существует
test_function()
