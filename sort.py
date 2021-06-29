my_Str = input(
    "Enter all the hackathons name you have attended and give some space between each: ")

words = [word.lower() for word in my_Str.split()]

words.sort()

print("The sorted hackathons are:")
for word in words:
    print(word)
