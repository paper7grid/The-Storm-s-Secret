# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character. 

define n = Character("Narrator")
define e = Character("Ethan Sterling", color="#01011d")
define s = Character("Mr. Sterling", color="#000000")
define l = Character("Lila", color="#510129")
define v = Character("Victor", color="#250101")
define d = Character("Detective alex (you)", color="#474701")
image SC_Hall = "SceneH1.png"
image fscene = "SCHill.png"
image study = "SCstudy.png"
image black = Solid("#000")
image ethan = "ethan.png"
image lila = "lila.png"
image victor = "victor.png"
#hello 
# The game starts here.

label start:

    scene fscene

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    # These display lines of dialogue.

    n "On the top of the hill in his huge house."
    n "lived Mr. Sterling, a wealthy businessman."

    n "Welcome to Sterling's mansion."

    scene SC_Hall

    s "welcome my old friend Alex! please have a seat."

    show ethan with moveinleft
    show mrsterling
    s "This is Ethan Sterling, my nephew."

    show lila with moveinleft
    s "And this is my fiance, Lila."
    
    show victor at right
    s "And this is my business partner, Victor."

    s "We were just discussing about our future business plans when my enphew and fiance stopped by and because of the rain they will be spending the noght here"

    return

label second_scene:
    scene black with fade
    n "And just as you were about to settle down for the night, after a delicious dinner..."
    
    n "A sudden shrill scream echoed through the mansion, in the dead silence."
    n "you hurried out of your room to find the source of the scream."

    show lila at with moveinleft
    n "It was Laila, standing outside the study room, trembling with fear."

    d "You asked her what happened."
    l "I - I- think... come here... quick...look"
    n "She pointed towards the study room and as you enter the room, you are met with a horrifying sight."

    scene study
    n "Mr. Sterling was lying on his desk, motionless, with a bloody knife in sight and an open letter in front of him."

    l "Oh my god! HELP call the police! oh lord, he is dead! suicide??"

label third_scene: 
    scene black with dissolve
    n "After a few moments of chaos in the study room, you all gather in the living room."

    scene SC_Hall
    show detective
    d "I think we should all stay together for now."
    d "If there is a killer in the house, we should be careful."


    show victor
    v "I agree with Detective Alex. We should be cautious."
    v "but I think if this is a suicide, I think it's a bit sad."

    n "as Lila sobs"

    l "I can't believe he is gone, oh what a poor soul."

    n "The night passed in silence, with everyone staying close together, trying to make sense of the tragedy."

    n "As the detective in the scene you get to work on solving the mystery of Mr. Sterling's death."

    d "So who was there at that time?"

    e "I was just passing by to get some water."

    l "I was in my room, when I heard a loud noise" 

    d "so you heard a loud noise while sleeping... hmm.."
    d "And what time was it when you, Ethan, were passing by?"

    e "probably somewhere around 10:30 at night"
