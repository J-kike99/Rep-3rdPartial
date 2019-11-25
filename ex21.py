def add(a , b):
    print(f"ADDING {a} + {b}")
    return a + b    
          
def subtract(a , b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a , b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b 
          
def divide (a , b):
    print(f"DIVIDING {a} / {b}")
    return a / b
          
print("Let's do math with justifications!")

          
age= add(30,5)
height= subtract(71,4)
weight= multiply (5 , 5)
iq= divide(100000 , 5)
          
print(f" Age: {age} , height: {height} , weight: {weight} , iq: {iq}")
          
          
print("Here is a puzzle.")
          
what = add(age , subtract(height , multiply(weight , divide(iq ,2)))) 
          
print("That becomes:" , what , "Can you do it by hand?")          
          
