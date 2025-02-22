def max2(x,y):
    """нахождение максимальнгого числа из двух """
    if x>y:
        return x
    return y

print(max2(4,6))            #6

def max3(x,y,z):
    return max2(x,max2(y,z))

print(max3(4,5,8))          #8
print(max3(0.2,0.8,0.5))     #0.8
print(max3("a","abc","abd"))  #abd
print(max3("abd","qwerty","asv")) #qwerty


print("----------------------------")

def hello():
    print("Hello world")

hello()             #Hello world
f=hello
f()                 #Hello world

print("----------------------------")


def hello_separated(name="World",separated = "_"):
    print("Hello", name, sep=separated)

hello_separated(separated="***", name="John")  #Hello***John

hello_separated(separated="***")  #Hello***World
