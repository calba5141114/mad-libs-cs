import sys
import time

# mad libs stories
stories = [
    " \n The 🍌 is {} and was made by {} they are also eaten by {} and is super super super {} so you can thank {} for the 🍌 ",
    "\n Being launched in 🚀 is {} and not super freindly to {} the only way we know this is {} told us and ate a {} 🍅 while doing so but he does not like {}"
]


def searchloop(story_mode, storieslist):
    ''' returns story from story array '''
    story = storieslist[story_mode]
    return story


def getuserinput(story):
    ''' gets user input and formats story strings '''

    try:
        adjective1 = input(" \n Tell me an adjective, and click enter: ")
        noun1 = input("\n Tell me a noun, and click enter:")
        noun2 = input(" \n Tell me another noun, and click enter: ")
        adjective2 = input(
            "\n Tell me an another adjective, and click enter: ")
    except Exception as e:
        print(" \nWe encountered an error {} and will ask for input again".format(e))
        time.sleep(2)
        getuserinput(story)

    try:
        return story.format(adjective1, noun1, noun2, adjective2, noun1)
    except Exception as e:
        print("\n We encountered and error {} and will close the program".format(e))
        sys.exit(0)


def initiateGame():
    ''' decide if we want the user to play another round '''
    continue_loop = input(
        " \n Do you wanna go for another round Yes(0) or No(1):")
    continue_loop = abs(int(continue_loop))
    if continue_loop == 0:
        game_loop(stories)
    elif continue_loop == 1:
        print(" \n No problem closing game in 3 seconds")
        time.sleep(3)
        sys.exit(0)
    else:
        print(" \n Closing game in 5 seconds")
        time.sleep(5)
        sys.exit(0)


def game_loop(stories):
    ''' game loop '''
    print("\n Madlibs The Game \n")
    print(" \n What kind of story do you want? 🍌(0) or 🚀(1) \n ")
    try:
        story_mode = input("Pick  🍌(0) or 🚀(1) (type in the number you want):")
        story_mode = abs(int(story_mode))
        if story_mode == 0 or story_mode == 1:
            story = searchloop(story_mode, stories)
        else:
            print("\n Not valid input restarting game loop")
            game_loop(stories)
        storyfmted = getuserinput(story)
        print(storyfmted)

    except Exception as e:
        print(" \n We encoutered {} ending program in 5 seconds".format(e))
        time.sleep(5)
        sys.exit(0)

    #  Starting or closing new game
    try:
        initiateGame()
    except Exception as e:
        print(" \n We encoutered {} ending program in 5 seconds".format(e))
        time.sleep(5)
        sys.exit(0)


if __name__ == "__main__":
    game_loop(stories)
