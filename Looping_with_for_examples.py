#!/usr/bin/python3
dogs = ["dalmation", "husky", "australian shepard"]
# index     0          1              2


#print(type(dogs))
#print(dogs[1])
#print(type(dogs[1]))


# Goal - Print the sentence "I like _______s" (fill in blank with dog type)
#sentence0 = f"I like animals such as {dogs[0]}"
#print(sentence0)
#sentence1 = f"I like animals such as {dogs[1]}"
#print(sentence1)
#sentence2 = f"I like animals such as {dogs[2]}"
#print(sentence2)

# Do this for all the dogs in the list using a for loop
for item in dogs:
    sentence = f"I like animals such as {item}"
    print(sentence)
