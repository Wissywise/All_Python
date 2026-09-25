#Input temperature in celcius
celcius = float(input("Please enter the temperature in celcius: "))

#convert celcius to fahrenheit
fahrenheit = (celcius * 9/5) + 32
print("The temperature in fahrenheit is:", fahrenheit)

#Input temperature in fahrenheit
fahrenheit = float(input("Please enter the temperature in fahrenheit: "))

#convert fahrenheit to celcius
celcius = (fahrenheit - 32) * 5/9
print(f"The temperature in Celsius is: {celcius: .2f}")
