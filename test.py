f = open("sherlock.txt")

words = []

for line in f:
    line = line.rstrip()
    words.extend(line.split())
    print words