string = input('Enter the string whose presence in the text you want to check: ')
text = input('Enter the text: ')

if string in text:
    print("Yes")
else:
    print("No")