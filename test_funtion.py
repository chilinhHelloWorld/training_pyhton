# def swap (x ,y ):
#     x, y = y , x
#     print (x ,y)
#     return x,y

# a = 5
# b = 7
# swap(a,b)
# x , y = swap(a,b)
# print (x,y)

# def test_swap():
#     x , y = swap(5,8)
#     assert x == 8
#     assert y == 5
# def test_swap1():
#     x , y = swap(5,8)
#     assert x == 5
#     assert y == 8
# class TestClass:
#     def test_one(self):
#         x = "this"
#         assert "i" in x

#     def test_two(self):
#         x = "hello"
#         assert hasattr(x, "h")
import python_ex
import pytest

@pytest.mark.number
def test_add():
        assert python_ex.add(7,3) == 10
        assert python_ex.add(7) == 9
        assert python_ex.add(5) == 7

@pytest.mark.number
def test_product():
        assert python_ex.product(5,5) == 25
        assert python_ex.product(5) == 10
        assert python_ex.product(5) == 10

@pytest.mark.strings
def test_add_strings():
    result = python_ex.add('Hello', ' World')
    assert result =='Hello World'
    assert type(result) is str
    assert 'Hello' in result

@pytest.mark.strings
def test_product_strings():
    assert python_ex.product(' Hello', 3) == ' Hello Hello Hello'
    result = python_ex.product('Hello ')
    assert result == 'Hello Hello '
    assert type(result) == str
    assert 'Hello' in result

@pytest.mark.parametrize('value1, value2, result',
                         [(7,3,10),
                          (15.5,25.5,41),
                          ('Hello ','Hello ','Hello Hello ')
                         ]
                         )
def test_add_product(value1, value2, result):
    assert python_ex.add_product(value1, value2) == result