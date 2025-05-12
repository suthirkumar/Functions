#Text analysis application using lambda

text=input("\nEnter a text:")
wc=lambda text:len(text.split())
cc=lambda text:len(text)
rt=lambda text:text[::-1]

print("\nText Analysis:")
print("Word Count:",wc(text))
print("Character Count:",cc(text))
print("Reversed Count:",rt(text))