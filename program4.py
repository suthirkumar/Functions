# Check if a word is palindrome or not

def is_palindrome(string):
    reversed_string=string[::-1]
    if string.lower()==reversed_string.lower():
        return True
    else:
        return False
    
word =input("Enter the word:")
if is_palindrome(word):
    print(word,"is a palindrome")
else:
    print(word,"is not a palindrome")