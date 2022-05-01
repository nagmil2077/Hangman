import random
import os


def random_word():
    country = ["China", "India", "Hungary", "Norway", "England", "New Zealand", "Bulgaria", "Iceland", "Greenland", "Australia", "Chile", "Argentina", "Kenya", "Uganda", "Bosnia and Herzegovina", "Czech Republic", "United States of America", "United Kingdom", "United Arab Emirates"]
    word = list(" ".join(random.choice(country)))
    return word


def underscore_word(randomwordfromlist):
    uscr = []
    for i in randomwordfromlist:
        if i != " ":
            uscr.append("_")
        else:
            uscr += " "
    return uscr


def get_input_letter():
    everyletter = []
    inputletter = "Start"
    while len(inputletter) != 1 or inputletter.isnumeric() == True or inputletter != "quit":
        inputletter = input("Type in a letter then press enter: ")
        everyletter.append(inputletter)
        if len(inputletter) == 1 and inputletter.isnumeric() == False:
            return inputletter
        elif inputletter.lower() == "quit":
            print("Shutting down program... ")
            exit()
        else:
            print("I'm sorry, I didn't get that! Try only one letter, oh, and no numbers, please!")


def searchinputletterinword(inputletter, word_from_list):
    indexlista = []
    for index in range(len(word_from_list)):
        if inputletter.lower() == word_from_list[index].lower():
            indexlista.append(index)
    return indexlista


def merge(whereto_list, fromwhere_list, towhich_index):
    for index in towhich_index:
        whereto_list[index] = fromwhere_list[index]
    return whereto_list


def displayletterinword(letter_toprint, inputletter, setwronganswers_given, word_from_list, is_repeated_letter):
    os.system('cls')
    print("Your guess was: " + inputletter + "!")
    print("\n")
    for index in letter_toprint:
        print(index, end="")
    print("\n")

    if inputletter in word_from_list or inputletter.upper() in word_from_list:
        print("Good choice!")
    else:
        print("Wrong choice!")
        if is_repeated_letter == True:
            print("This letter was already used, please try a different one.")

    if len(setwronganswers_given) > 0:
        print("Your incorrect letters so far: " + str(setwronganswers_given)[1:-1])
        print("\n")


def printresult_game(gamelist, setwronganswers, lives, word_from_list):
        if gamelist.count("_") == 0:
            print("Congratulations! You've won the game!")
            print("\n")
        elif lives == len(setwronganswers):
            print("You lost. Bad luck! :( \nThe correct answer was: " + "".join(word_from_list))
            print("\n")


def play(lives):
    os.system('cls')
    replay = "Y"
    while replay == "Y" or replay == "y":
        os.system('cls')
        setwronganswers = set()
        origin_lives = lives
        print("Welcome!")
        print("Let's play Hangman!")
        print('\n')
        word_from_list = random_word()
        gamelist = underscore_word(word_from_list)
        print(*gamelist, sep="")
        print(end='\n')

        while gamelist.count("_") > 0 and lives > len(setwronganswers):
            print("Lives: " + str(lives - len(setwronganswers)))
            print('\n')
            inputletter = get_input_letter()
            index_lista = searchinputletterinword(inputletter, word_from_list)
            is_repeated_letter = inputletter in setwronganswers
            if len(index_lista) == 0:
                setwronganswers.add(inputletter)
            theletterprinted = merge(gamelist, word_from_list, index_lista)
            displayletterinword(theletterprinted, inputletter, setwronganswers, word_from_list, is_repeated_letter)

        printresult_game(gamelist, setwronganswers, lives, word_from_list)

        replay = input("Do you want to play again? Y/N ")
        lives = origin_lives


play(6)
