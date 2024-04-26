#(Conversions between Celsius and Fahrenheit)
def celsius_to_Fahrenheit(celsius):
    F = (celsius * 1.8) + 32
    return F

def fahrenheit_to_Celsius(fahrenheit):
    c = (fahrenheit - 32) * 5/9
    return c

#list of celsius
celsius_temps = [40.0 , 39.0 , 38.0 , 37.0 , 36.0 , 35.0 , 34.0 , 33.0 , 32.0 , 31.0]

#convert celsius to fahrenheit
fahrenheit_temps = []
for temp in celsius_temps :
    fahrenheit_temps.append(celsius_to_Fahrenheit(temp))

#table
print("\n Centigrade \t Fahrenheit")
for temp in range(len(fahrenheit_temps)):
    print(f"{celsius_temps[temp]}       \t{fahrenheit_temps[temp]}")

#list of Fahrenheit 
fahrenheit_temps = [120.0 , 110.0 , 100.0 , 90.0 , 80.0, 70.0, 60.0, 50.0, 40.0, 30.0]
print("---------------------")

# convert Fahrenheit to Celsius 
centigrade_temps = []
for temp in fahrenheit_temps:
    celsius_temps.append(fahrenheit_to_Celsius(temp))

#table
print("Fahrenheit \t celsius")
for temp in range(len(fahrenheit_temps)):
    print(f"{fahrenheit_temps[temp]}       \t{celsius_temps[temp]}")