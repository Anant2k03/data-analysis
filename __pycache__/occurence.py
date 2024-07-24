file = open("india.txt",'w')

file.write("India is a vast, diverse, and peaceful country in South Asia.\n")
file = open('india.txt', 'r')
count = 0

content = file.read()

content = content.upper()

words = content.split()

for word in words:
    if word == "INDIA":
        count += 1

print(f'The word "INDIA" occurs {count} times in the file.')

file.close()
