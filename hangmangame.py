import random

def hangman():
    words = ['python', 'computer', 'science', 'hangman', 'keyboard']
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
        else:
            attempts -= 1
            print(f"Wrong! You have {attempts} attempts left.")

        display_word = [letter if letter in guessed_letters else "_" for letter in word]
        print(" ".join(display_word))

        if "_" not in display_word:
            print("Congratulations! You guessed the word:", word)
            break
    else:
        print("Sorry, you lost! The word was:", word)

hangman()


        

