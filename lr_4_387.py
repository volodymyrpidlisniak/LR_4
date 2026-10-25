string = input('Enter your string: ')

encoded = []
i = 0
while i < len(string):
    count = 1
    while i + 1 < len(string) and string[i] == string[i + 1]:
        count += 1
        i += 1
    encoded.append(string[i] + str(count))
    i += 1

print(''.join(encoded))