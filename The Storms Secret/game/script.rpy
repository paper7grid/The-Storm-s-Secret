# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character. 

define n = Character("Narrator")
define e = Character("Ethan Sterling", color="#01011d")
define s = Character("Mr. Sterling", color="#000000")
define l = Character("Lila", color="#510129")
define v = Character("Victor", color="#250101")
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

    n "On the top of the hill in his huge house."
    n "lived Mr. Sterling, a wealthy businessman."

    n "Welcome to Sterling's mansion."

    scene dinner
    s "welcome, please have a seat."

    show ethan
    show mrsterling
    s "This is Ethan Sterling, my nephew."

    show lila
    s "And this is my fiance, Lila."
    
    show victor
    s "And this is my business partner, Victor."

    # This ends the game.

    return
