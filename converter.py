# miles to kilometers converter

miles = input('Please enter miles: ');

try:
    miles = float(miles);

    def converter(miles):
    
        kilometers = miles * 1.609344;
        print(f'{miles} miles is equal to {kilometers} kilometers')

    converter(miles)

except:
    print('That is not a number')

