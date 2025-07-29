import random

def setup_game():
    words = ["python", "hangman", "program", "code", "alpha"] # 
    secret_word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0 # 
    return secret_word, guessed_letters, incorrect_guesses

secret_word, guessed_letters, incorrect_guesses = setup_game()
# print(f"Secret word (for debugging): {secret_word}") # Uncomment for debugging
def display_word_state(word, guessed):
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

# Example:
# print(display_word_state(secret_word, guessed_letters))
def get_player_guess(guessed):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
        elif guess in guessed:
            print("You already guessed that letter. Try again.")
        else:
            return guess
def update_game_state(guess, secret_word, guessed_letters, incorrect_guesses):
    guessed_letters.append(guess)
    if guess not in secret_word:
        print("Incorrect guess!")
        incorrect_guesses += 1
    else:
        print("Good guess!")
    return incorrect_guesses
def check_win_loss(secret_word, guessed_letters, incorrect_guesses, max_incorrect_guesses=6): # 
    # Check for win
    win = True
    for letter in secret_word:
        if letter not in guessed_letters:
            win = False
            break
    if win:
        print(f"\nCongratulations! You guessed the word: {secret_word}")
        return True # Game over, player won

    # Check for loss
    if incorrect_guesses >= max_incorrect_guesses:
        print(f"\nGame Over! You ran out of guesses. The word was: {secret_word}")
        return True # Game over, player lost

    return False # Game not over yet
def draw_hangman(incorrect_guesses):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """
    ]
    # Display stages from 6 down to 0 (more parts shown as incorrect guesses increase)
    print(stages[6 - incorrect_guesses])

def play_hangman():
    secret_word, guessed_letters, incorrect_guesses = setup_game()
    max_incorrect_guesses = 6 # 

    print("Welcome to Hangman!")
    print(display_word_state(secret_word, guessed_letters))

    while True:
        draw_hangman(incorrect_guesses)
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print(display_word_state(secret_word, guessed_letters))

        guess = get_player_guess(guessed_letters)
        
        incorrect_guesses = update_game_state(guess, secret_word, guessed_letters, incorrect_guesses)
        
        if check_win_loss(secret_word, guessed_letters, incorrect_guesses, max_incorrect_guesses):
            break

# Start the game
if __name__ == "__main__":
    play_hangman()

        
