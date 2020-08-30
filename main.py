# -*- coding: utf-8 -*-
bridge = ('Bridge', "Ok solider, We have landed on the bridge of the ship. Guide yourself to the main core of this heap of rubble and gather the primary plastic cores")
readyRoom = ("Captains quarters", "Proceeding towards the quarters, I could hear faint weird noises of an animal struggling in agony. Opening the doors, I could see the animal. A rare flying specie trapped amongest plastic. Seeing the sight of the beast calls sadness to me. Deciding on whether I should set it free or not as the animal glances at me aggresivly.  ")
lift = ("Lift", "A turbolift that takes you to the lower level of the ship")
barrack = ('Barrack', "Coming from the lift, You are now in the barracks where the enemys forge their armour with filth. I'm sensing higher concentration around your area. Its close.")
Dorm = ('Dorm', "Now in the sleeping quarters, Yellow faint lights appear on the otherside over the big double steel doors. Getting close to the doors, A sign named 'Reactor core' is shown on the door. ")
reactorcore = ("Reactor Core", "Entering the heart of the beast, I find myself the decision of deciding to grab the 4 reactor plastic cores from their pods or overload the pod through the mainframe to explode ")
loadingbay = ("Loading Bay", "While walking through the massive bay, I have catched glimpse of a teleporter used to transport large cargo which could be my safer route of escape or take a I leap of faith out of the moving ship counting down its doom. ")
hatch = ("Escape through the hatch", "Escaping the hatch seems to be the best bet. Without hesitation, I jumped out of the ship.  ")
teleporter = ("Teleporter", "I quickly dashed to the teleporter and waited. Particles of green light appear beneath men as in a few moments, I open my eyes to see the ships in blazes of fire as it crashes towards the ground. Feeling relieved from my quick escape, unfortunatly, I look around to see myself surrounded with bulks of plastic facing towards me. At least I completed the mission. ")
base = ("After a full victory, we rejoice as were a step closer to winning this war.")
# Commands by the Player for their decision
free = ("Free the Bird", "Knowing that this might end badly,I used my knife to cut the tangling plastic carefully. Once set free, the beast grouls at me hesitantly and jumps through the outside window, flying off in the distance. After the circumstance, I continue to search the quarters and see the reactor beneath me through the window.")
leave = ("Leave the bird", "For my safety, I avoided the animal and continue to search for the reactor. Looking through the window, I catch glimpse of the reactor at the very bottom.")
explode = ("Explode", "I have made my decision. Blowing up the plastic cores is a best option againest the plastic. The interior starts to break down as the countdown has started for the overload to begin. Going through the same path will take to long so I need to decide quick. I could see a hatch at the far distance leading outside but see no parchutes in here. ")
take = ("Take the cores", "Taking the plastic cores might help us againest the fight with the enemys by using their own creation againest them. Grabing the cores for a few seconds, Alarms began to echo as red lights flash repeatingly. Knowing the ships doom, I decided to run back through the rooms I have been through. Reaching at the lift where the buttons seem to not work, I start to look around vigrantly for an exit. A sign I spot named 'Loading Bay' could be my ticket out of here or I could stay and find a new entrance")
stay = ("Stay in the ship", "Waiting in the ship for another route proved to fail as the ship countdowns for a few seconds... Boom. The blazes of the ship as he crashes down. The solider who took his life to save many. Not a best option though :/ ")
jump = ("Jump", "Just a few seconds before death, I jumped as the blast pushes me ever so further from the ship.")
#The decisions made in the game
safe_jump = ("Falling to my doom, I notice faintly a big figure coming towards me. Coming closer towards me, I now knew that it was the bird I had save in the captain quarters trying to resuce me. Just within reach, I hoped on his back and flew across the polluted sky towards my base")
unsafe_jump = ("Falling to my doom, I wonder if this was a good plan. Knowing my fate as I reach ever so close to the ground, I gaze upon the ship gulfed in flames, soaring down to the ground as shreded plastic leaves as trails. ")


transitions = {
  bridge: (readyRoom, lift),
  readyRoom: (free, leave),
  free: (lift,),
  leave: (lift,),
  lift: (barrack, Dorm),
  barrack: (reactorcore,),
  Dorm: (reactorcore,),
  reactorcore: (explode, take),
  explode: (hatch, stay,),
  take: (loadingbay,),
  loadingbay: (jump, teleporter),
}



location = bridge
free == safe_jump
leave == unsafe_jump

jump = safe_jump or unsafe_jump


while True:
  
  print (location[1])
  print ('Choose solider')
  print (" ")

  for (i, t) in enumerate(transitions[location]):
    print (i + 1, t[0])

  print (" ")
  choice= int(input('Select possible option by number: '))
  location = transitions[location][choice - 1]




if hatch and jump == safe_jump or unsafe_jump:
    print(safe_jump)
    print(base)
    print("The End")
else:
    print(unsafe_jump)
    print("The End")





