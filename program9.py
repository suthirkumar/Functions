# Temperature converter application using lambda functions

c_to_f=lambda celsius:(celsius*9/5)+32
f_to_c=lambda fahrenheit:(fahrenheit-32)*5/9
print("\nTemperature Converter:")
print("1.Celsius to Fahrenheit")
print("2.Fahrenheit to Celsius")
choice=input("Enter your choice (1/2):")

if choice=="1":
    celsius=float(input("Enter temperature in celsius:"))
    print("Temperature in Fahrenheit:",c_to_f(celsius))
elif choice=="2":
    fahrenheit=float(input("Enter the temperature in fahrenheit:"))
    print("Temperature in celsius:",f_to_c(fahrenheit))
else:
    print("Invalid choice")