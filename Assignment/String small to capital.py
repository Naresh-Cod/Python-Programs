# Get a string from the user convert first and last letter of the word as capital

def str_upper(string:str):
    start = 0
    end = len(string)-1
    return ''.join(string[start].upper() + string[end].upper())
pri = str_upper(input("Enter a string: "))
print(pri)