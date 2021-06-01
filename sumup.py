#first code
num1 = 1.0
num2 = 4.0

def sumup_two_numbers(num1,num2):    
    return float(num1+num2)

print(num1+num2)
#(I added the "print" to see it in the command line)


#second code (if I have no argument or only one)
num1 = 1
num2 = 4

def sumup_numbers(num1=0,num2=0): 
    return float(num1+num2)
