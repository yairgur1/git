import sys

sys.argv = ["start.py", r"C:\Users\User\Desktop\syberC\git\sys1.txt"]

path = sys.argv[1]

with open(path, "r", encoding = "utf-8") as f:
    text = f.read()
    words = text.split()
    
counts = {}

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print("there are " + str(len(counts)) + " unique words in the text file.")
print()

flag = True

while flag:
    print("Enter the number of most common words to find, between 0 and "+ str(len(counts)) + ": ")
    findWord = int(input())
    if findWord < 0 or findWord > len(counts):
        print("Invalid number of words to find.")
    else:
        flag = False

counts1 = counts.copy()
for i in range(findWord):
    mostCommon = max(counts1, key = counts1.get)
    print(f"{mostCommon} : {counts1[mostCommon]}")
    del counts1[mostCommon]

# (: 