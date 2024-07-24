file = open("story.txt",'w')

file.write = ("'Once upon a time, in a land far, far away, there lived a brave knight named Ron.\nRon rode through the snowy mountains, chasing knights and battling dragons.\nOne day, Ron stumbled upon a hidden treasure chest.\nInside the chest, he found a magical sword named Sword of Destiny.\nWith Sword of Destiny, Ron could")
file = open('story.txt', 'r')

count = 0

lines = file.readlines()

for line in lines:
    if line.startswith('t') or line.startswith('T'):
        count += 1
        print(line.strip())
print(f'The number of lines starting with "t" or "T" is {count}.')
file.close()
