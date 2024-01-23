secret_number = 4
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
  guess = int(input("Guess: "))
guess_count += 1
if guess == secret_number:
        print("you are awesome!")
     break
else:
  Print("You failed")

#This is a guessing game if the answer is wrong the else code will ne executed#