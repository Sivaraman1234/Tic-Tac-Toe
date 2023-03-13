pannel=["--","--","--",
      "--","--","--",
       "--","--","--" ]

gamerunning=True
winner=None
player="x"

def displaypannel():
    print(pannel[0] + "|" + pannel[1] + "|" +pannel[2] + "       0 | 1 | 2")
    print("---------------")
    print(pannel[3] + "|" + pannel[4] + "|" +pannel[5] + "       3 | 4 | 5")
    print("---------------")
    print(pannel[6] + "|" + pannel[7] + "|" +pannel[8] + "       6 | 7 | 8")

def entry(player):
    inp=int(input("enter the number from 0-8: "))
    if pannel[inp]=="--":
        pannel[inp]="x"
    else:
        print("already exit")
        entry(player)

def check_horizontel():
    global gamerunning
    global winner
    if pannel[0]==pannel[1]==pannel[2]!="--":
        winner=pannel[0]
        gamerunning=False
        return True
    elif pannel[3]==pannel[4]==pannel[5]!="--":
        winner=pannel[3]
        gamerunning=False
        return True
    elif pannel[6]==pannel[7]==pannel[8]!="--":
        winner=pannel[6]
        gamerunning=False
        return True

def check_vertical():
    global gamerunning
    if pannel[0]==pannel[3]==pannel[6]!="--":
        winner=pannel[0]
        gamerunning=False
        return True
    elif pannel[1]==pannel[4]==pannel[7]!="--":
        winner=pannel[1]
        gamerunning=False
        return True
    elif pannel[2]==pannel[5]==pannel[8]!="--":
        winner=pannel[2]
        gamerunning=False
        return True

def check_diagnol():
    global gamerunning
    if pannel[0]==pannel[4]==pannel[8]!="--":
        winner=pannel[0]
        gamerunning=False
        return True
    elif pannel[6]==pannel[4]==pannel[2]!="--":
        winner=pannel[6]
        gamerunning=False
        return True

def check_win():
    if check_horizontel() or check_vertical() or check_diagnol:
        print(f"the winner is {winner}")
        gamerunning=False
    else:
        print("the game is Tie")

def switch_player():
    global player
    if player == "x":
        player = "o"
    
    
    
while gamerunning:
    displaypannel()
    entry(player)
    check_win()
    switch_player()
