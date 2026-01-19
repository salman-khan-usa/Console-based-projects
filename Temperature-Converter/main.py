# Basic temperature converter


# User input
def float_value(prompt):
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print(f'{value} is Invalid value. Try again like(20.6 or - 10)')


def menu():
    print("  Temperature Converter  ")
    print('1: Celcius to Farenheit')
    print('2: Celcius to kelvin')
    print('3: Farenheit to Celcius')
    print('4: Farenheit to kelvin')
    print('5: Kelvin to celcius')
    print('6: kelvin to farenheit')
    print('7: Quite')


def main():
    while True:
        menu()
        choice = input('Choose Your conversion (1-7): ')

        if choice == '1':
            c = float_value("Enter Temperature in celcius:")
            print("The temperature in Fahrenheit is:", c * 9 / 5 + 32,'F')

        elif choice == '2':
            c = float_value("Enter Temperature in celcius:")
            print("The temperature in kelvin is:" ,c + 273.15,'K')

        elif choice == '3':
            f = float_value("Enter Temperature in Farenheit:")
            print("The temperature in Celciusis is:",(f - 32) * 5 / 9,'C')

        elif choice == '4':
            f = float_value('Enter Temperature in Farenheit:')
            print("The temperature in kelvin is:",(f - 32) * 5 / 9 + 273.15,'K')

        elif choice == '5':
            k = float_value("Enter Temperature in Kelvin:")
            print("The temperature in Celcius is:",k - 273.15,'C')

        elif choice == '6':
            k = float_value('Enter Temperature in kelvin :')
            print("The temperature in Farenheit is:",(k - 273.15) * 9 / 5 + 32,'F')

        elif choice == '7':
            print('Quiting, thanks for using')
            break
        
        else:
            print("Invalid choice, please choose a number from 1-7.")




main()
