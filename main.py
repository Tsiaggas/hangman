import random
import hangman_words
import hangman_art

lives = 6


print(hangman_art.stages[6])

chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"****************************<???>/{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    display = ""

    if guess in correct_letters:
        print(f"The letter {guess} is already guessed, please give another try. ")

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)

        elif letter in correct_letters:
            display += letter


        else:
            display += "_"



    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f" You choose letter {guess}, that's not in the word. You lose a life")

        if lives == 0:
            game_over = True

            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f"**********************YOU LOSE**********************")
            print(f"********The correct word is {chosen_word} ************")
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(hangman_art.stages[lives])
