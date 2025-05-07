#Find vowels and non vowel using lambda

is_vowel=lambda char:char.lower() in 'aeiou'
def seperate_vowels_consonents(s):
    vowels=list(filter(is_vowel,s))
    consonents=list(filter(lambda char:char.isalpha() and not is_vowel(char),s))
    return vowels,consonents

string=input("Enter a string:")
vowels,consonents=seperate_vowels_consonents(string)
print(f"Vowels:{vowels}")
print(f"Consonents:{consonents}")