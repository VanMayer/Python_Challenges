#Validate Pin
# Do I have to add something for empty strings?
def validpin(word):
    if len(word)==4 or len(word)==6 and word.isdigit():
        return True
    else:
        return False
