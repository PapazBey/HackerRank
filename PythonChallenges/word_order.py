#You are given  words. Some words may repeat. For each word, output its number of occurrences. 
#The output order should correspond with the input order of appearance of the word

num = int(input())

dict = {}
arr = []
x = 0

while x < num:
    k = input()
    arr.append(k) 
    x = x + 1

total = 0

for words in arr:
    for kelime in arr:
        if words == kelime:
            total = total + 1
    dict[words] = total
    total = 0

# print(dict)
print(len(dict))

akm = []
for key, value in dict.items():
    akm.append(value)

print(akm)


