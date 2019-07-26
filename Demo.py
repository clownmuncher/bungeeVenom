import time

def start_now():
    print("Two hunters approach, Ready for battle!")

def fightStart():
    print("Your opponent seems happy to fight")

def d1():
    print('''The battle has started!

             What Will You Do?''')



start_now()
time.sleep(1)
fightStart()
time.sleep(1)



d1()
time.sleep(1)
answer = input('''
                  <charge>
                    or
                  <wait>
                  ''')
time.sleep(1)
d2()
time.sleep(1)
if answer.lower().strip() == "charge":
    answer = input(''''You dash foward to attack. You miss. opponent lands a heel kick to your back. an opening!

                    Take it?

                     <take>
                       or
                     <observe>''')

else:
    time.sleep(1)
    d3()
    time.sleep(1)
    if answer.lower().strip() == "wait":
       answer = input('''Your focus sharpens. opponent hass no intention of moving. youre forced to charge. opponent lands a swift heel kick.there is a opening.

                                 Take it?

                                 <take>
                                   or
                                 <observe>''')
time.sleep(1)
d4()
time.sleep(1)
if answer.lower().strip() == "take":
        answer = input('''you aimed a kick to the opponent's face. you were blocked! the opponents punches get quicker! a punch lands! your entire body is thrown backwards.

                          <attack>
                            or
                          <defend>''')
else:
    d5()
    if answer.lower().strip() == "observe":
       answer = input('''you went on the defense. a punch hits you! you are thrown backwards.

                             <attack>
                                or
                             <defend>''')
time.sleep(1)
d6()
if answer.lower().strip() == "attack":
   answer = input('''you throw some punches. none of them land. its hard to keep up! you are thrown backwards.

                     <idea>
                       or
                     <backup>''')
else:
    d7()
   if answer.lower().strip() == "defend":
      answer = input('''you continue to dodge. its quick. too quick! a hit lands and you're thrown backwards.

                        <idea>
                          or
                        <backup>''')
time.sleep(1)
d8()
if answer.lower().strip() == "backup":
   answer = input('''you try to get some distance. opponent pulls you foward with his clown magic and pucnhes your face. a vicious punch cycle starts!

                     <y>
                      or
                     <y>''')
time.sleep(1)
if answer.lower().strip() == "y":
   print("you cough up blood and fall fowards")
   exit()

else:
    if answer.lower().strip() == "idea":
       answer = input('''you dash behind your opponent, stop and lift up a floor tile. you kick the tile, reducing it to shambles.

                         <y>
                          or
                         <n>''')
time.sleep(1)

if answer.lower().strip() == "y":
   answer = input('''opponent defends themselves from the debris. you watch from behind a piece of flying debris. you find your opening!

                     <go>
                      or
                     <wait>''')

else:
    if answer.lower().strip() == "n":
       print("you see your heart splatter onto the ground")
       exit()

if answer.lower().strip() == "go":
     answer = input("you beat the absoulute shit out of your opponent!")
     print("your opponent lies on the ground. you can tell your opponent enjoyed the beating")
     exit()

else:
    if answer.lower().strip() == "wait":
       print("your opponent lands the final blow while you were busy being a little bitch.")
       exit()
