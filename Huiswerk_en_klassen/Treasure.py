# Je gaat een nieuw programma schrijven, genaamd Treasure.py. Dit programma is een spel waarbij de speler een aantal keuzes moet maken.
# Je mag zelf bepalen wat de keuzes zijn en wat de uitkomsten zijn van de keuzes. Het spel moet minimaal 4 verschillende keuzes bevatten.
# Het einde van het spel is een if elif else statement.
#
# Voorbeeld:
# Welkom op het eiland van de schat.
# Je bent op een kruispunt, ga je links of rechts?
# Rechts
#  Helaas heb je verkeerd gekozen en ben je in een gat gevallen. Game Over.
#
# Of:
# Welkom op het eiland van de schat.
# Je bent op een kruispunt, ga je links of rechts?
# Links
# Je komt bij een meer, ga je zwemmen of wachten?
# etc...

print("""
                  __..-----')
        ,.--._ .-'_..--...-'
       '-"'. _/_ /  ..--''""'-.
       _.--""...:._:(_ ..:"::. \\
    .-' ..::--""_(##)#)"':. \\ \\)    \\ _|_ /
   /_:-:'/  :__(##)##)    ): )   '-./'   '\\.-'
   "  / |  :' :/""\\///)  /:.'    --(       )--
     / :( :( :(   (#//)  "       .-'\\.___./'-.
    / :/|\\ :\\_:\\   \\#//\\            /  |  \\
    |:/ | ""--':\\   (#//)              '
    \\/  \\ :|  \\ :\\  (#//)
         \\:\\   '.':. \\#//\\
          ':|    "--'(#///)
                     (#///)
                     (#///)         ___/""\\     
                      \\#///\\           oo##
                      (##///)         `-6 #
                      (##///)          ,'`.
                      (##///)         // `.\\
                      (##///)        ||o   \\\\
                       \\##///\\        \\-+--//
                       (###///)       :_|_(/
                       (sjw////)__...--:: :...__
                       (#/::''':::     "" - -.._
                  __..-'''           __;: :            "-._
          __..--""                  `---/ ;                '\\._
 ___..--""                             `-'                    "-..___
   (_ ""---....___                                     __...--"" _)
     ""--...  ___""'''-----......._______......----""'     --""
                          ---.....   ___....----             
""")


# Schrijf hier je code:

print("welcome to the game TREASURE ISLAND")
print("Your mission is to find the hidden treasure")
print("You'll have to make choices that will direct your path")
print("-------------------------------------------------------")
print("You wake up on the beach. You think about the situation. Do you choose to drink seawater or press on?")
print("1: Drink seawater")
print("2: Press on")

riddle_solved = False

choice1 = input()
if choice1 == "1":
    print("You drink the seawater and die of dehydration")
    print("Game Over")
elif choice1 == "2":
    print("You press on and find a path")
    print("-------------------------------------------------------")
    print("You come across a river. Do you swim across or go around?")
    print("1: Swim across")
    print("2: Go around")
    choice2 = input()
    if choice2 == "1":
        print("You swim across, its almost nighttime. Do you build a fire or sleep?")
        print("1: Build a fire")
        print("2: Sleep")
        choice3 = input()
        if choice3 == "1":
            print("You build a fire and survive the night")
            print("come morning, you wake up and see a stranger at your camp")
        elif choice3 == "2":
            print("You sleep and die of hypothermia")
            print("Game Over")
            exit()
    elif choice2 == "2":
        print("You go around and meet a stranger on the path")
    print("1: Talk to the stranger")
    print("2: Ignore the stranger")
    choice3 = input()
    if choice3 == "1":
        print(
            "the stranger says he knows about the treasure on the island. He will guide you if you answer his riddle correctly, if not, he will kill you")
        print("I live in a world where spaces count,")
        print("Indentation is my way around.")
        print("I loop, I branch, with if and while,")
        print("My name's a snake, but that's just style.")
        print("What am I?")
        answer = input().lower()
        if answer == "python" or answer == "a python":
            print("You answer correctly and the stranger tells you to look behind the waterfall, fate will guide you")
            riddle_solved = True
        else:
            print("You answer incorrectly and the stranger kills you")
            print("Game Over")
            exit()
    if choice3 == "2":
        print("You ignore the stranger and keep walking")
        print("You find a waterfall, something is moving in the water")
        print("1: Swim across")
        print("2: Go around")
    if riddle_solved == True:
        print("You find the waterfall, something is moving in the water")
        print("1: Swim across")
        print("2: Go around")
    choice4 = input()
    if choice4 == "1":
        print("You swim across find treasure behind the waterfall")
        print("You find the treasure!")
        print("You win!")
        exit()
    elif choice4 == "2":
        print(
            "You go around, you see the stranger again, this time he's not asking. You have to solve his riddle or he will kill you")
        print("I live in a world where spaces count,")
        print("Indentation is my way around.")
        print("I loop, I branch, with if and while,")
        print("My name's a snake, but that's just style.")
        print("What am I?")
        answer = input().lower()
        if answer == "python" or answer == "a python":
            riddle_solved = True
            print("You answer correctly and the stranger tells you to look behind the waterfall")
            print("You find the waterfall, something is moving in the water")
            print("1: Swim across")
            print("2: Don't swim across")
            choice4 = input()
            if choice4 == "1":
                print("You swim across find treasure behind the waterfall")
                print("You find the treasure!")
                print("You win!")
                exit()
            elif choice4 == "2":
                print("You should have listened to the stranger")
                print("You spend your days wondering the island, never to be seen again")
                exit()
        else:
            print("You answer incorrectly and the stranger kills you")
            print("Game Over")
            exit()
