file = open('word.txt','w')

file.write = ('apple, banana, cherry, date, elderberry, fig, grape, honeydew, kiwi, lemon, mango, nectarine, orange, pear, quince, raspberry,strawberry, tangerine, watermelon,yogurt')
file = open('word.txt', 'r')

count = 0

content = file.read()

words = content.split()

for word in words:
    if word.startswith('i') or word.startswith('I'):
        count += 1
        print(word)

print(f'The number of words starting with "i" or "I" is {count}.')

file.close()
