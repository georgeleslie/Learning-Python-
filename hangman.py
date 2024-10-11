

# The secret word that the player is trying to guess
secretword = "cbtnuggets"
lettersguessed = ""

# The number of turns before the player loses
failureCount = 6

# Loop until the player has made too many failed attempts
# Will 'break' the loop if they succeed
while failureCount > 0:

    # Get the guessed letter from the player
    guess = input("Enter a letter: ")

    if guess in secretword:
        print(f"Correct! There is one or more {guess} in the secret word.")
    else:
        failureCount -= 1
        print(f"Incorrect. There are no {guess} in the secret word. You have {failureCount} turns left.")

    # Maintain a list of all letters guessed
    lettersguessed = lettersguessed + guess
    wronglettercount = 0

    # Display the word with correctly guessed letters or blanks
    for letter in secretword:
        if letter in lettersguessed:
            print(f"{letter}", end="")
        else:
            print("_", end="")
            wronglettercount += 1

    print()  # Add a newline after the word display

    # Check if the player has guessed all the letters
    if wronglettercount == 0:
        print(f"Congratulations!!! The secret word was, {secretword}. You won!")
        break
else:
    print(f"Sorry, you ran out of turns. The secret word was {secretword}.")