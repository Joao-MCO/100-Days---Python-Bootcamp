print('Welcome to the Tip Calculator!')

total = input('What was the total bill? $')
tip = input('How much tip would you like to give? 10, 12, or 15?')
people = input('How many people to split the bill? ')

bill = (float(total)*(100 + float(tip))/100)/int(people)

print(f'Each person should pay: ${bill: .2f}')
