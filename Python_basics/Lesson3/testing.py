string = input("Enter a string: ")
chara_set = set()
for char in string:
    if char not in chara_set:
        chara_set.add(char)
print(chara_set)
print(len(chara_set))