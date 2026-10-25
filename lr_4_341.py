c1 = input('Enter your first symbol: ')
c2 = input('Enter your second symbol: ')

print(''.join(chr(i) for i in range(ord(c1), ord(c2) + 1)))