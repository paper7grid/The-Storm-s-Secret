# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
why 

define e = Character("Eileen")
#hello 


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "On the top of the hill in his huge house."
    e "lived Mr. Sterling, a wealthy businessman."

    e "Welcome to Sterling's mansion."

    scene dinner
    e "welcome, please have a seat."

    show ethan
    show mr.sterling
    e "This is Ethan Sterling, my nephew."

    show lila
    e "Mr. sterling "And this is my fiance, Lila.""
    
    show victor
    e "And this is my business partner, Victor."

    # This ends the game.

    return
