secret_word="secret word"
guess = input("Guess the secret word: ")
guess_count = 0
guess_limit = 5
out_of_guesses = False
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
     guess = input("Wrong! Guess again: ")
     guess_count += 1
    else:
       out_of_guesses = True
if out_of_guesses:
    print("Out of guesses, you lose!")
else:
    print("Congratulations! You guessed the secret word.")
    print("It took you", guess_count, "guesses.")