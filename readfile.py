import fileinput

#reads every line from the file you enter.

for line in fileinput.input():
    print(line)

