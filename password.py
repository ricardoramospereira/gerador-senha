import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
           'T', 'U', 'V', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('---------------Bem vindo ao gerador de senhas!-----------------')
num_letters = int(input('Quantas letras você gostaria de ter na senha?\n'))
num_numbers = int(input('Quantos números na senha?\n'))
num_symbols = int(input('Quantos símbolos na senha?\n'))


senha = []

for let in range(1, num_letters + 1):
    senha.append(random.choice(letters))

for num in range(1, num_numbers + 1):
    senha.append(random.choice(numbers))

for sym in range(1, num_symbols + 1):
    senha.append(random.choice(symbols))

random.shuffle(senha)  # embaralhar a lista

passw = ''

for password in senha:
    passw += password
print(passw)

'''
modo sequencial.

senha = ''

for let in range(1, num_letters + 1):
    rand = random.choice(letters)
    senha += rand


for num in range(1, num_numbers + 1):
    rand = random.choice(numbers)
    senha += rand


for sym in range(1, num_symbols + 1):
    rand = random.choice(symbols)
    senha += rand
print(senha)
'''
