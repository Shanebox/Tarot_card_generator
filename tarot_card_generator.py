import random

def main():
    print_disclaimer()
    spread = ask_what_spread()
    cards = generate_cards(spread)
    unique_numbers = check_for_duplicates(cards)

    print_cards(unique_numbers)


# This asks the user what spread they want and only accepts 3, 5, 7, 13.
def ask_what_spread():
    while True:
        try:
            spread = int(input("What spread 3, 5, 7, 13? "))
            if spread == 3 or spread == 5 or spread == 7 or spread == 13:
                return spread
            else:
                print("\nERROR Code 44: Input was not 3, 5, 13\n")
        except ValueError:
            print("\nERROR Code 55: Input was a letter\n")


# This generates the cards.
def generate_cards(spread):
    numbers = []

# This picks a random number between 0 - 77 then adds it to numbers.
    for _ in range(spread):
        numbers.append(random.randrange(0, 77))

    return numbers


# This checks for duplicates
def check_for_duplicates(cards):
    unique_numbers = []
    numbers = set()
    duplicates = set()

    # This removes the duplicates.
    for x in cards:
        if x in numbers:
            duplicates.add(x)
        else:
            numbers.add(x)

    # This fixes the number of the cards when duplicates were removed.
    while len(numbers) < len(cards):
        numbers.add(random.randrange(0, 77))

    # This converts set(numbers) to a list named: unique_numbers
    for x in numbers:
        unique_numbers.append(x)

    random.shuffle(unique_numbers)
    return unique_numbers

# This makes the card reversed or not
def is_reversed():
    chances_of_reversed = random.randrange(0, 50)

    if chances_of_reversed >= 25:
        return "Yes"
    else:
        return "No"


# This prints the cards.
def print_cards(cards):
    tarot_cards = ["The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor"
             , "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit", "Wheel of Fortune"
             , "Justice", "The Hanged Man", "Death", "Temperance", "The Devil", "The Tower", "The Star"
             , "The Moon", "The Sun", "Judgement", "The World"
             
                                            # Minor Arcana Cards 
             # These are the Wands:
             , "Ace of Wands", "2 of Wands", "3 of Wands", "4 of Wands", "5 of Wands", "6 of Wands"
             , "7 of Wands", "8 of Wands", "9 of Wands", "10 of Wands", "Page of Wands", "Knight of Wands"
             , "Queen of Wands", "King of Wands"
             
             # These are the Swords:
             , "Ace of Swords", "2 of Swords", "3 of Swords", "4 of Swords", "5 of Swords"
             , "6 of Swords", "7 of Swords", "8 of Swords", "9 of Swords", "10 of Swords", "Page of Swords"
             , "Knight of Swords", "Queen of Swords", "King of Swords"
             
             # These are the Cups:
             , "Ace of Cups", "2 of Cups", "3 of Cups", "4 of Cups", "5 of Cups", "6 of Cups", "7 of Cups"
             , "8 of Cups", "9 of Cups", "Page of Cups", "10 of Cups", "Knight of Cups", "Queen of Cups"
             , "King of Cups"
             
             # These are the Pentacles:
             , "Ace of Pentacles", "2 of Pentacles", "3 of Pentacles", "4 of Pentacles", "5 of Pentacles"
             , "6 of Pentacles", "7 of Pentacles", "8 of Pentacles", "9 of Pentacles", "10 of Pentacles"
             , "Page of Pentacles", "Knight of Pentacles", "Queen of Pentacles", "King of Pentacles"
             ]
    
    length = len(cards)
    i = 0
    for _ in range(length):
        print(f"Card {i + 1}: {tarot_cards[cards[i]]}\nReversed: {is_reversed()}\n")
        i = i + 1
    

# This prints the version number and a disclaimer.
def print_disclaimer():
    print("Version: 1.0\nThis does not replace a tarot card reader.\n")


main()