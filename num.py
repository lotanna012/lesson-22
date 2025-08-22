numbers1=[1,2,3]
numbers2=[4,5,6]
def add (x,y):
    return x+y
result=map(add,numbers1, numbers2)
print("addition of two lists")
print(list(result))
nums=[1,2,3,4,5]
def sq(n):
    return n*n
square=map(sq,nums)
print("square of numbers in a list")
print(list(square))

    