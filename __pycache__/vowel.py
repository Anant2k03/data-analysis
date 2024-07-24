file = open("myfile.txt",'w')

file.write("Hello World!\nThis is a test file.\n")
file = open('myfile.txt', 'r')

vowel_count = 0
consonant_count = 0

vowels = 'AEIOUaeiou'

content = file.read()

for char in content:
    if char in vowels:
        vowel_count += 1
    elif char.isalpha():
        consonant_count += 1

print(f'The number of vowels in the file is {vowel_count}.')
print(f'The number of consonants in the file is {consonant_count}.')

file.close()
