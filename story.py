var = input("Please enter your name: ")
print("Hello " + str(var))
 
choose= input ("You have been selected by the king to rescue the princess. Do you choose your sword or your bow and arrow?")
print("you have choosen " + str(choose))
index = 0
if(str(choose)[index] ==4):
    print("You have choosen rightous weapon for close up battles, so you have no defense for far away attacks. ")
    c=input ("You began your mission, but you came apon a fork in the road. Do you choose to go left or right?  ")
    if(c=="left"):     
        print("You have found a person.")
        d=input("Do you want to ask for directions?")
        if (d=="yes"):
            print("The stranger gave you a map anyway and decided to join you on your quest. The stranger's name is Roman.")
            e=input("The both of you perfected you attacks so you can be synced so your attacks are stronger. Roman begins to spot the castle that the princess was held up in. Do you decide to go in recklessly or use stealth?")
            if(e=="go in recklessly"):
                f=input("Roman and you go through the entire castle destroying anyone in sight. You both head up to the princess's cabin. You decide to let Roman proctect the princess until you got out the kingdom bcause he's a better proctor. As soon as you exit the castle, you see a foe aiming a bow and arrow at Roman. What do you do, either move Roman out the way or call Roman's name?")
                if (f=="move Roman"):
                    print ("In your attempt to move Roman, You got in the way of the arrow. It pierced you through the chest. The last thing you told Roman to do was to save the princess. Roman slaughtered the sniper and told the king your tale. The king made Roman a trustworthy worker in his kingdom amd they also sprea your story across the land as if it was legend. GAME OVER")
                else:
                    print("You witnessed Roman die, enraged you catch the arrow that the sniper aimed at you and carved a hole through the archer's skull. You return to the kingdom saddened, the king praised you for returning his daughter. Your actions became a children's story years later, therefore you became a very famous individual. GAME OVER")
            else:
                print("Roman wore squeaky shoes and you both got caught. GAME OVER")
        else:
            g=input("You see the Dungon at which the princess is staying. Do you want to go in reckless or use stealth?")
            if (g=="go in reckless"):
                h=input(" You single handedly massacured 20 foes, but as you make your way to the princess; you spot another warrior ready to save her. What do you do? Do you either attack the other warrior or go back to the king empty handed. ")
                if (h=="attack other warrior"):
                    print ("you successfuly engaged the opponent. The warrior thrust his sword in a death blow but you evade it and countered which made the warrior fumble and flee. You return to the king with the princess. He appreciates your dedication. You live a licious lifestyle because you earned the fame and foutune. GAME OVER")
                else:
                    print ("The king is ashamed of you and banishes you from the kingdom for not even trying. Years later you are sucessful in another kingdom but as a labour because they don't trust you as a warrior. GAME OVER")
            else:
                print("You easily pass through the foes unorganized sturcture, and swoop the princess out her enslavement. You return to the king and the King is very pleased and made you name known throught the kingdom. GAME OVER") 
    else:
        print("You have enountered a foe")
        i=input("Do you want to fight or flee? ")
        if (i=="fight"):
            j=input("The foe is not armed. Do you want to attack with your hands or sword? ")
            if(j=="hands"):
                k=input("You try to attack but the foe was an expert in hand-to-hand combat. The foe put you in a sleeper hold, which made you knock out. when you awoke al of your items are missing including your weapon. You wander for shelter because you woke up in the middle of the night, You stumble upon a ble house dou you want to enter it?")
                if (k=="yes"):
                    l=input("The house has a table ser for someone. Do you take the food thats out or look for someone?")
                    if (l=="take it"):
                        m=input("As soon as you turn around someone is starring at you. What do you do, kill them, run, or apoligize")
                        if (m=="kill them"):
                            n=input("You try to attack them with a fork but they easily evade the attack and put you in a submission lock. What do you do apoigize or fight back?")
                            if (n=="apoligize"):
                                print("The person claims to understand and lets you eat and stay for the night. They also teach you how to fight. When you wake up, you are chained up and the house owner holds a knife up to your neck yelling at you because you tried to attack them before apolgizing, so he decides to end your life. GAME OVER  ")
                            else:
                                print("They break your arm and slits your throat so you experience a slow and painful death. GAME OVER")
                        elif (m=="run"):
                            o=input("You successfully arn with a plate full of food, but you also lost the chance to have shelter. You end up sleeping on the ground. A wolf ends up waking you, what do you do, get up and run or stay still")
                            if (o=="get up and run"):
                                print("The wolf chased you and ate you. You Have Died. GAME OVER")
                            else:
                                print("The wolf at the scraps for the plate and left for a moment, it later came back with it's pack and ate you. You Have Died. GAME OVER")
                        else:
                            q=input("they understand, they give you food and teach you how to fight. When you wake up you are able to save the princess, so you continue with your journey. You come across the stronghold at which the princess is held. Do you wish to get the princess the easy way or the hard way? ")
                            if (q=="easy way"):
                                print("you easiy sneak through the security and obtain the princess and return her to her kingdom. You become a legend years later. GAME OVER")
                            else:
                                print("You walk straight into the stronghold destroying anyone and anything in the way of your main mission. You become nearly an expert at fighting because it seems like second nature. The princess is amazed at your style and when you return to the king with her, she requests to marry you. Do you accept this request?")
                                if("yes"):
                                    print("You are happily wed and retire as a warrior but you remain a signficant leader in the kingdom. GAME OVER")
                                else:
                                    print("You gladly decline the offer, because you enjoy being a rightous warrior for the king. You also gained fame and fourtune. GAME OVER")
                                        
                    else:
                        print("You found the person and they said they would help you, but they poision you. You Have Died. GAME OVER")
            else:
                print("You used the sowrd to cut off the foe's arms and then you piereced the sword through his neck")
                r=input("You continue the mission and spot the castle. You approach the dome, but you notice that there is no guards from keeping the princess from running. Do you investigate the area or get the princess")
                if (r=="investigate the area"):
                    print("gladly you did not find anythig alarming, so you resced the princess and returned to th King. He honored you and the kingdom celebrated once the princes arrived again. GAME OVER")
                else:
                    print("Your novice got to the best of you, but luckly they was nothing to worry about. You save the princess and return back to the kingdom reaizing that the Princess was harmed somehow. Then you realize that she must've killed all those me. Upon asking her she repies 'I got tired of waiting'. When you reached the kingdom there was a huge celebration for the arrivial of the princess. GAME OVER")
                
        else:
            print("The foe tried to chase you but you out ran them, so you pursue your journey again.")
                
elif(str(choose)[index] != 4):
    print("You have choosen a stealthy weapon, for far away battles, so you have no defense for close up attacks. ")
    path= input ("You began your mission, but you came apon a fork in the road. Do you choose to go left or right?  ") 

    if(path =="left"):
        a=input("You have found a person. Do you want to ask for directions?")
        if (a=="yes"):
            print("The stranger gave you a map anyway and decided to join you on your quest. The stranger's name is Roman.")
            s=input("The both of you perfected you attacks so you can be synced so your attacks are stronger. Roman begins to spot the castle that the princess was held up in. Do you decide to go in recklessly or use stealth?")
            if(s=="go in recklessly"):
                t=input("Roman and you go through the entire castle destroying anyone in sight. You both head up to the princess's cabin. You decide to let Roman proctect the princess until you got out the kingdom bcause he's a better proctor. As soon as you exit the castle, you see a foe aiming a bow and arrow at Roman. What do you do, either move Roman out the way or call Roman's name?")
                if (t=="move Roman"):
                    print ("In your attempt to move Roman, You got in the way of the arrow. It pierced you through the chest. The last thing you told Roman to do was to save the princess. Roman slaughtered the sniper and told the king your tale. The king made Roman a trustworthy worker in his kingdom amd they also sprea your story across the land as if it was legend. GAME OVER")
                else:
                    print("You witnessed Roman die, enraged you catch the arrow that the sniper aimed at you and carved a hole through the archer's skull. You return to the kingdom saddened, the king praised you for returning his daughter. Your actions became a children's story years later, therefore you became a very famous individual. GAME OVER")
            else:
                print("Roman slipped on the unmaintained victims in the Dungon, this cause you to fall because he bumped into you mid-fall. You both end up on the floor surrounded by all of the guardians. The guardians immediatley stab you and Roman with their spears and left your bodies with the other victims. You Have Died. GAME OVER.")
        else :
            u=input("You see the Dungon at which the princess is staying. Do you want to go in reckless or use stealth?")
            if (u=="go in reckless"):
                v=input(" You single handedly massacured 20 foes, but as you make your way to the princess; you spot another warrior ready to save her. What do you do? Do you either attack the other warrior or go back to the king empty handed. ")
                if (v=="attack other warrior"):
                    print ("you successfuly engaged the opponent. The warrior thrust his sword in a death blow but you evade it and countered which made the warrior fumble and flee. You return to the king with the princess. He appreciates your dedication. You live a licious lifestyle because you earned the fame and foutune. GAME OVER")
                else:
                    print ("The king is ashamed of you and banishes you from the kingdom for not even trying. Years later you are sucessful in another kingdom but as a labour because they don't trust you as a warrior. GAME OVER")
            else:
                print("You easily pass through the foes unorganized sturcture, and swoop the princess out her enslavement. You return to the king and the King is very pleased and made you name known throught the kingdom. GAME OVER") 
    elif(path =="right"):
        b=input("You have enountered a foe, Do you want to fight or flee? ")
        if (b=="fight"):
            w=input("The foe is not armed. Do you want to attack with your hands or sword? ")
            if(w=="hands"):
                x=input("You try to attack but the foe was an expert in hand-to-hand combat. The foe put you in a sleeper hold, which made you knock out. when you awoke al of your items are missing including your weapon. You wander for shelter because you woke up in the middle of the night, You stumble upon a ble house dou you want to enter it?")
                if (x=="yes"):
                    y=input("The house has a table ser for someone. Do you take the food thats out or look for someone?")
                    if (y=="take it"):
                        z=input("As soon as you turn around someone is starring at you. What do you do, kill them, run, or apoligize")
                        if (z=="kill them"):
                            xz=input("You try to attack them with a fork but they easily evade the attack and put you in a submission lock. What do you do apoigize or fight back?")
                            if (xz=="apoligize"):
                                print("The person claims to understand and lets you eat and stay for the night. They also teach you how to fight. When you wake up, you are chained up and the house owner holds a knife up to your neck yelling at you because you tried to attack them before apolgizing, so he decides to end your life. GAME OVER  ")
                            else:
                                print("They break your arm and slits your throat so you experience a slow and painful death. GAME OVER")
                        elif (z=="run"):
                            xyz=input("You successfully arn with a plate full of food, but you also lost the chance to have shelter. You end up sleeping on the ground. A wolf ends up waking you, what do you do, get up and run or stay still")
                            if (xyz=="get up and run"):
                                print("The wolf chased you and ate you. You Have Died. GAME OVER")
                            else:
                                print("The wolf at the scraps for the plate and left for a moment, it later came back with it's pack and ate you. You Have Died. GAME OVER")
                        else:
                            ab=input("they understand, they give you food and teach you how to fight. When you wake up you are able to save the princess, so you continue with your journey. You come across the stronghold at which the princess is held. Do you wish to get the princess the easy way or the hard way? ")
                            if (ab=="easy way"):
                                print("you easiy sneak through the security and obtain the princess and return her to her kingdom. You become a legend years later. GAME OVER")
                            else:
                                cd=input("You walk straight into the stronghold destroying anyone and anything in the way of your main mission. You become nearly an expert at fighting because it seems like second nature. The princess is amazed at your style and when you return to the king with her, she requests to marry you. Do you accept this request?")
                                if(cd=="yes"):
                                    print("You are happily wed and retire as a warrior but you remain a signficant leader in the kingdom. GAME OVER")
                                else:
                                    print("You gladly decline the offer, because you enjoy being a rightous warrior for the king. You also gained fame and fourtune. GAME OVER")
                                        
                                
            else:
                print("You used the sowrd to cut off the foe's arms and then you piereced the sword through his neck")
                wx=input("You continue the mission and spot the castle. You approach the dome, but you notice that there is no guards from keeping the princess from running. Do you investigate the area or get the princess")
                if (wx=="investigate the area"):
                    print("gladly you did not find anythig alarming, so you resced the princess and returned to th King. He honored you and the kingdom celebrated once the princes arrived again. GAME OVER")
                else:
                    print("Your novice got to the best of you, but luckly they was nothing to worry about. You save the princess and return back to the kingdom reaizing that the Princess was harmed somehow. Then you realize that she must've killed all those me. Upon asking her she repies 'I got tired of waiting'. When you reached the kingdom there was a huge celebration for the arrivial of the princess. GAME OVER")
                
        else:
            print("The foe caught you and killed you. GAME OVER")
                


