# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
# define e = Character('Eileen', color="#c8ffc8")
init:
    define g1 = DynamicCharacter('aaa', color='#c8ffc8')
    define g2 = Character('BBB', color='#ff0505')
    define g3 = Character('CCC', color='#00cbff')
    define t = Character('Generic Soldier', color='#850000')
    define mc = DynamicCharacter('mc', color='#2b00ff')

# The game starts here.
label start:
    $ aaa = '???'
    $ mc = ''
    $ revealed = False

    "The foul stench of my basetment is getting to me."
    
    "Usually I'm able to ignore my own filth but something is different today."

menu:
    "Go Outside.":
        "You remember that you're alergic to going outside."
        jump important

    "Clean your room":
        "You get cry out and get your mom to clean your flith. She has a distinct look of resignation and sadness as she picks up your dirtied underwear."
        jump important
        
label important:
    
    "Alas the filth is gone. Now I can focus on important business!"

    "*important things happening*"

    "Ahh, if it wasn't for me that anime would have gone unwatched! I should get a good citizen award or something"

menu:
    "Go to sleep.":
        "You spend 2 hrs being baited by a troll before losing consciousness"
        jump acquiring_grill

    "Do more important business":
        "There is no more business to be done today. Instead you go on a date with your Dakimakura."
        jump acquiring_grill

label acquiring_grill:
    "You wake up the next day. Your face is wet with drool."

    "You don't bother cleaning it and instead it slowly evaporates and drips off your face throughout the day."

    "However today isn't any day! It's the day you're meeting your GF for the first time."

    "You head downstairs after hearing the doorbell."

    "You open the door, thank the delivery man, grab your precious package and head back into your lair."
    
    "Before you begin your l33t unboxing video you hear a strange sound."

    g1 "Let me out of here. Reeeeeeee. I know you're out there!"
    
    "This startles the bananas out of you but you slowly calm down. It must be just a prank."
    
    g1 "Come on bro. Let me out of here. Don't just leave me in here. Also I'm a real person."
    
menu:
    "Freak out":
        "You scream out and hide under your bed sheets."
        jump name

    "Show off your manly side":
        "You try to say something but you're a huge loser. You end up blacking out for a minute."
        jump name

label name:
    g1 "Jesus Christ. The type of people who would buy a dakimakura are obviously degenerates but this is worse than I had anticipated."
        
    g1 "I promise I won't bite."
    
    "You muster up all your courage and open the box."
    
    "Nothing is out of place. It's the dakimakura you ordered."
    

    $ aaa = "Idrin"
    g1 "Boo! My name is %(aaa)s. Yes I know it's probably different than whatever girl is printed on the pillow."

    g1 "Anyways, what's your name?"

    $ mc = renpy.input("What is your name?")

menu:
    "My name is %(mc)s. W-what is going on?":
        g1 "I'll explain in a moment but please go change. It was a mistake to scare you. I didn't think you'd literally shit your pants."
        jump plot

    "My name is %(mc)s. Greetings M\'\Lady":
        g1 "Fuck it. Please incinerate me."
        jump gameover
        
label gameover:
    "Your degeneracy has caused this game to end early."
    jump end
    
label plot:
    g1 "I'm a normal everyday person that was randomly trapped in this dakimakura. I randomly woke up one day and I saw nothing but blackness."
   
    g1 "I can still hear, see, and smell so I could hear factory sounds and truck sounds which helped me figure out what was going on."
    
    g1 "But with no limbs I'm kind of useless, therefore it'll be up to you to save me and help me get back in my own body."
    
label end:
