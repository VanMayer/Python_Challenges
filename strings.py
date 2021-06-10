#first code
def stringupper_1(word):
    return(word.upper())

#testing code in the command line
stringupper_1('freefall')
stringupper_1('tree')

#second code (to be able to call the function with a number or a boolean value)
def stringupper(word):
    if type(word) != str:
        return('Input must be a string')
    else:
        return(word.upper())

#testing code in the command line
stringupper('freefall')
stringupper('tree')
stringupper(6)