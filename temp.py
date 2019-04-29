# Temp conversion 

print('Temperature Conversion Tool.')

try:
    convert_type = int(input("Enter 1 for Celsius to Fareheit. Enter 2 for Farenheit to Celsius: "))
    if convert_type == 1:
        temp = int(input('Enter the temp in celsius to convert: '))
        converted = temp * 9/5 + 32
        print(f'{temp} celsius is {converted} degrees farenheit.\n')
    
    if convert_type == 2:
        temp = int(input('Enter the temp in farenheit to convert: '))
        converted = (temp - 32) * 5/9
        converted = int(round(converted, 0))
        print(f'{temp} degrees farenheit is {converted} degree celsius.')
    
    if convert_type > 2 or convert_type < 1:
        print("You must enter 1 or 2.")
        
except ValueError:
    val = int
    print("You must enter 1 or 2.")
    

