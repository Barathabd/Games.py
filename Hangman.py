print(guess)
choice=(input("Enter the letter:").lower())

for letter in guess:
    if choice==guess:
        print("right")
        
    else:
        print("wrong")
for i in guess:
    if i==choice:
        print(i)
print(len(guess))