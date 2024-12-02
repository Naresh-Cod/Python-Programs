# Take from a number user have to check if whether that number is a palindrome or not

def palindrome(nums):
    store = 0
    while nums > 0:
        rev = nums % 10
        store = store * 10 + rev
        nums = nums // 10
    return store

number = int(input("Enter a number: "))
call = palindrome(number)
if call == number:
    print("The number is palindrome")
else:
    print("The number is not palindrome")

