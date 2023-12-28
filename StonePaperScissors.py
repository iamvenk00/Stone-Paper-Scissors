player=0
computer=0
list=["stone","paper","scissors"]
list2=["Arre Gajab!","Oho Mast!","Jiyo Beta!","10 mL Daaru, Khela Tu Faaru!"]
list3=["Chal Nikal!","Namaste Beta!","Oops!","Tumse Naa Ho Paayega!"]
i=1
import random
while (i<=6):
    i=i+1
    p=input("\nYour turn: ")
    p=p.lower()
    c=random.choice(list)
    print("Computer chose",c)
    if c=="stone":
        if p=="stone":
            print("\nPlayer: ",player)
            print("Computer: ",computer)
        elif p=="paper":
            print("\n",random.choice(list2))
            player=player+1
            print("\nPlayer: ", player)
            print("Computer: ", computer)
        elif p=="scissors":
            print("\n",random.choice(list3))
            computer=computer+1
            print("\nPlayer: ", player)
            print("Computer: ", computer)
    elif c=="paper":
        if p=="stone":
            print("\n",random.choice(list3))
            computer=computer+1
            print("\nPlayer: ",player)
            print("Computer: ",computer)
        elif p=="paper":
            print("\nPlayer: ", player)
            print("Computer: ", computer)
        elif p=="scissors":
            print("\n",random.choice(list2))
            player=player+1
            print("\nPlayer: ", player)
            print("Computer: ", computer)
    elif c=="scissors":
        if p=="stone":
            print("\n",random.choice(list2))
            player=player+1
            print("\nPlayer: ", player)
            print("Computer: ", computer)
        elif p=="paper":
            print("\n",random.choice(list3))
            computer=computer+1
            print("\nPlayer: ", player)
            print("Computer: ", computer)
        elif p=="scissors":
            print("\nPlayer: ", player)
            print("Computer: ", computer)
if(player>computer):
    print("\nCongrats! Jeet Gaya Saala!\n")
elif player<computer:
    print("\nTumse Sahi Me Kuchh Naa Ho Paayega...Loser!\n")
else:
    print("\nTied! Kya Bolu Ab.\n")
print("\n** Final Scores **\n")
print("      Your score: ", player)
print("Computer's score: ", computer)