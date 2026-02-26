def add_numbers(a,b):
    print(a+b)
add_numbers(8,12)
def add_numbers(a,b):
    return a+b
result=add_numbers(15,25)
print(result)
def calculate(a,b,c):
    return (a+b)*c
result=calculate(3,5,2)
print(result)
def get_triangle_area(base,height):
    return base*height/2
print(get_triangle_area(8,3))
def get_sum(x,y,z):
    return x+y+z
print(get_sum(1,2,3))
def get_larger_number(a,b):
    if a>=b:
        return a
    else:
        return b
print(get_larger_number(1,2))
def is_even(number):
    if number%2==0:
        return True
    else:
        return False
print(is_even(3))
def repeat_string(text,times):
    return text*times
print(repeat_string("Hello",4))