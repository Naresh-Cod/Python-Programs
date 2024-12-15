def vowel(ch):
    if chr(ch).lower() in 'aeiou':
        print("Vowel")
    else:
        print("Consonant")

# Driver code
if __name__ == '__main__':
    vowel(ord('a'))