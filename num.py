numbers1=[4,5,6]
numbers2=[7,8,9]
def add (x,y):
    return x+y
result=map(add,numbers1, numbers2)
print("addition of two lists")
print(list(result))
nums=[3,4,5]
def sq(n):
    return n*n
square=map(sq,nums)
print("square of numbers in a list")
print(list(square))

    