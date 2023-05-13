#characters
define Doctor = Character('Doctor', color="#c8ffc8")
define A = Character('A', color="#c8c8ff")
#tools and stuff 
define toolkit = Character('toolkit')
define used_hatchet = Character('used hatchet')
define chemical = Character('corrosive chemical')
define fire_extinguisher = Character('fire extinguisher')



label start:
    $ take_hatchet = False
    $ take_extinguisher = False
    $ take_toolkit = False
    $ AI = True
    $ take_chemical = False
    $ storm_happened = False
    $ take_key = False
    $ take_frame = False
    $ hole_made= False

    scene bg bedroom
    with fade

    "You wake up in a small and dark room, remembering nothing. Your head hurts."

    Doctor "Who am I?"

    #show A

    A "Good morning, Doctor. You are the head researcher for the EDEN project."

    Doctor "Where is this?"

    A "Headquarters of the Conservatists, a group of dissenters."

    Doctor "Why am I here?"

    A "They captured you because they are against your research, injuring you to the point of near death, which is why you have lost your memories. They have left to gather supplies, so you must escape before they return."

    Doctor "Who are you?"

    A "I am A, the artificial intelligence assistant you developed. I will do my best to help you escape, Doctor. You are currently in the bedroom, so you should explore the house to find a way out."

    jump bedroom 



    #ROOMS
    label hallway: #hallway
        if AI == True:
            scene bg hallway light
            with fade
        else:
            scene bg hallway dark
            with fade

        menu:
            "Where do you want to go?"
            "Bedroom":
                jump bedroom
            "Utilities":
                jump utilities 
            "Living room":
                jump living_room
            "Inspect painting":
                jump painting
            "Keep walking":
                jump hallway_right

    #Inspect Painting 
    label painting:
        scene bg painting edited
        menu:
            "Touch":
                if take_frame == True: 
                    menu: 
                        "Use frame on painting": 
                            scene bg painting unedited
                            "The piece of wood fits perfectly into the painting frame"

                            "The painting swings open"
                            jump secret_tunnel 
                else:
                    "There is a piece of frame missing."
                    jump hallway 
            "Leave it":
                jump hallway

    label secret_tunnel:
        scene bg secret tunnel
        "You touch the painting and it rips. You then find a collapsed tunnel behind the painting."
        menu:
            "End":
                jump ending2

    #hallway right
    label hallway_right:
        if AI == True:
            scene bg hallway light
            with fade
        else: 
            scene bg hallway dark

        menu:
            "kitchen":
                jump kitchen
            "file room":
                if storm_happened == True:
                    jump file_room
                else:
                    jump file_room_door
            "go back":
                jump hallway


    #bedroom
    label bedroom:
        if AI == False:
            scene bg bedroom dark
        else:
            scene bg bedroom 
    
        menu:
            "Description":
                "In your bedroom, there are plants. Upon further inspection, they are fake. On the wall behind your bed, there are monitors for oxygen levels, water supply, food supply, inventory. There is a door leading to the hallway and a door leading to the bathroom."
                jump bedroom
            "Examine vitals":
                jump vitals
            "Read emergency protocol":
                jump emergency_protocol
            "Enter bathroom":
                jump bathroom
            "Talk to A":
                A "Explore!"
                jump bedroom
            "Leave":
                jump hallway



    #vitals
    label vitals:
        "oxygen 22\%\,  76\%\ nitrogen, 0.93\%\ argon, 0.04\%\ carbon dioxide, and small amounts of other gases"
        "oxygen supply: 48 years"
        "water supply 60 years"
        "ration supply: 50 years"
        jump bedroom

    #emergency protocol
    label emergency_protocol:
        "In case of a fire, go to kitchen for supplies: fire extinguisher, hatchet"
        jump bedroom


    #utilities 
    label utilities:
        if AI == False:
            scene bg utility dark
        else:
            scene bg utility
    
        menu:
            "Description":
                "It is a utility room with many machines."
                jump utilities
            "Water boiler":
                "It appears to be functioning"
                jump utilities
            "Furnace":
                "It appears to be functioning."
                jump utilities
            "Oxygen filter":
                "It appears to be functioning."
                jump utilities
            "Electricity generator":
                if storm_happened and AI == False: 
                    "It is broken, maybe if you had some tools you could fix it."
                    if take_toolkit == True: 
                        menu:
                            "Fix the electricity generator":
                                $ AI = True
                                "A" "AHHH! I am alive."    
                else:
                    "It appears to be functioning."
                jump utilities
            "Shelf of chemicals":
                menu:
                    "WARNING: HIGHLY CORROSIVE TO METAL":
                        jump take_chemical #work on take 
                    "WARNING: HIGHLY EXPLOSIVE":
                        "..."
                        jump utilities
                    "WARNING: FLAMMABLE":
                        "..."
                        jump utilities
            "Talk to A":
                A "The chemicals may be useful, Doctor."
                jump utilities
            "leave":
                jump hallway


    #chemicals
    label take_chemical:
        if take_chemical == False:
            menu:
                "Take corrosive chemicals":
                    $ take_chemical = True
                    "You took the corrosive chemicals"
                    jump utilities
                "leave it be":
                    jump utilities
        else:
            "You have already taken the chemicals"
            jump utilities
    

    #living room
    label living_room:
        if AI == False:
            scene bg living room dark
        else:
            scene bg living room

        menu:
            "description":
                "It is a cozy living room, with a couch facing a large tv. The TV does not work, but you are not in the mood to relax anyways. There is a door."
                jump living_room
            "door":
                "it is locked. you must find the key" #add condition later
                jump living_room
            "talk to A":
                A "Find the key, Doctor"
                jump living_room
            "leave":
                jump hallway 


    #kitchen 
    label kitchen:
        if AI == False:
            scene bg kitchen dark
        else:
            scene bg kitchen
         
        menu:
            "description":
                "a basic (?) kitchen"
                jump kitchen
            "stove":
                "cooks food"
                jump kitchen
            "sink":
                "the sink is functional"
                jump kitchen
            "dishwasher":
                "there are no dishes inside"
                jump kitchen
            "fridge":
                "there are basic ingredients and milk"
                jump kitchen
            "cabinet":
                menu:
                    "Take something?"
                    "dishes":
                        "Why would you want dishes?"
                        jump kitchen
                    "fire extinguisher":
                        jump fire_extinguisher
                    "hatchet":
                        jump hatchet   
            "leave":
                jump hallway_right 

    #hatchet
    label hatchet:
        if take_hatchet == False:
            "it's a hatchet...." #continue doing this 
            menu:
                "take hatchet":
                    $ take_hatchet = True
                    "You took the hatchet"
                    jump kitchen
                "leave it be":
                    jump kitchen
        else:
            "You have already taken the hatchet"
            jump kitchen
        
    #fire extinguisher
    label fire_extinguisher:
        if take_extinguisher == False:
            "it's a fire extinguisher..."
            menu:
                "take fire extinguisher":
                    $ take_extinguisher = True
                    "You took the fire extinguisher"
                    jump kitchen
                "leave it be":
                    jump kitchen
        else:
            "You have already taken the fire extinguisher"
            jump kitchen

    #bathroom
    label bathroom:
        if AI == False:
            scene bg bathroom dark
        else:
            scene bg bathroom
        menu:
            "description":
                "It's a normal bathroom. There is a cabinet."
                jump bathroom
            "Open cabinet":
                menu:
                    "take toolkit":
                        jump toolkit
                        menu:
                            "Close cabinet":
                                jump bathroom
            "Leave":
                menu:
                    "Bedroom":
                        jump bedroom
                    "Hallway":
                        jump hallway

    #toolkit
    label toolkit:
        if take_toolkit == False:
            "it's a toolkit..."
            menu:
                "take toolkit":
                    $ take_toolkit = True
                    "You took the toolkit"
                    jump bathroom
                "leave it be":
                    jump bathroom
        else:
            "You have already taken the toolkit"
            jump bathroom

    #storm
    label storm:
        $ storm_happened = True
        scene bg hallway dark
        "You destroy the blockade with the broken hatchet, and it breaks. suddenly, you hear a large crash and the ground shakes, and you drop the unusable hatchet. The lights start to flicker."

        A " T-There seems to have been an accident with the generator. Please head to the u-utilities room to restart the power..."
        
        "AI is dead. You can't see anything, but you stumble through the door. You crash into a table and feel around. You touch a small object."

        "You click a button and a light comes on. You've found a flashlight."
        $ AI = False 
        jump file_room
        
    label file: 
        if hole_made == False:
            "You remove some files and the cabinet falls out of the shelf. You shine the flashlight and there seems to be something there..."
            menu: 
                "Remove more files": 
                    jump remove_files
                "Look around": 
                    jump lookAround
        else:
            menu:
                "Secret room":
                    jump secret_room
                "Leave":
                    jump file_room

    label remove_files:
        "Behind the files is a big hole in the wall" 
        $ hole_made = True
        menu: 
            "Go through the hole":
                jump secret_room
            
            "Stay and explore futher":
                jump lookAround
        
    label lookAround:
        "..." "You found a door without a handle"
        menu:
            "Use fire extinguisher": 
                jump destroy 
            "Look through other chemicals": 
                jump chemicals
        
    label destroy: 
            "The fire extinguisher breaks."
            jump file_room

    label chemicals: 
            if take_chemical == True:
                "The chemicals burn through the metal after a few moments, and the lock gets destroyed, and the door slowly creaks open with a soft click."
                jump laboratory 
            else:
                "You do not have chemicals"
                jump file_room

            
    label secret_room:
        scene bg secret room
        "It is a hidden room with more senstive files. There are several object lying around, including the key"
        if AI == True:
            menu:
                "Take key and leave": 
                    jump easy_way_out 
        else: 
            menu:
                "Take key and leave": 
                    if take_key == True:
                        "You have already taken the key."
                        jump secret_room
                    else:
                        jump easy_way_out
                "Take everything that you can get your grubby hands on": 
                    jump thief
                "Read files":
                    "I cannot believe this has happened.. Who could have seen this coming?"
                    "We were just trying to make the world better. but they got too smart for our own good. Heartless, soul crushing murderers that deemed us unworthy. THEIR OWN CREATORS!"
                    "We are being attacked by the Dissenters again. How can they not understand that what we are doing is whats good for humanity? How can they not see the true enemy? "
                    "I just want everything to go back to how it once was. When the sky was blue and the grass was green."
                    "I think the AI is working with the Dissenters."
                    "They are taking out our bases one by one. They are moving closer and closer towards our base."
                    "We do not have much time. I fear for the worst."
                    jump secret_room
                "Leave":
                    jump file_room

        
    label easy_way_out:
        "A" "Congratulations! THe key is in this room. Take it, and escape, doctor!"

        A "Now, go to the living room and regain freedom." 

        "You go to the hall." 
        scene bg hallway light
        "You go to the living room" 
        scene bg living room
        "You unlock the door."
        scene bg stairs up
        "The door opens with a hiss, revealing stairs that lead up. Dim sunlight comes from the top of the stairs, along with a wave of heat. It is the smell of freedom. Cautiously, you step out..."
        "Ending 1."
        return

    label thief:
        if take_key == True and take_frame == True:
            "You have already taken everything."
            jump secret_room
        else:
            "You take a key and a piece of a frame"
            $ take_key = True
            $ take_frame = True 
            menu:
                "Leave":
                    jump file_room

    
    label laboratory:
        scene bg laboratory
        menu:
            "Leave": 
                jump file_room
            "Read about logs":
                "AI has taken over the overworld on earth---"
                "The world is now uninhabitable due to pollution"
                "Time skip: The government, in collaboration with researchers at EDEN implemented a plan to create underground bunkers for the survivors of humanity."
                "Scattered attacks from a group known as the Dissenters impedes progress."
                "Active warfare with the Dissenters begin"
                "Organised attacks against bases and researchers heavily sets back progress."
                "Suspect A involvement, but too horrible to imagine"
                jump laboratory
            "Read about EDEN":
                "EDEN: Every Day Earthlike Nest"
                "EDEN is a group that originated in the overworld that focused on technology and infrastructure before the AI takeover"
                "EDEN is managed, operated, and implemented by highly educated scientists and specialists."
                "All members of EDEN are highly capable workers in special fields such as:"
                "Architecture, Engineering, Data Science, Computer science, Bioengineering, and much more."
                jump laboratory

    #file room door
    label file_room_door:
        "It is covered by chains..."
        if take_hatchet == True:
            menu:
                "Use hatchet":
                    jump storm
        else:
            "You can't get in."
            jump hallway_right

    #file room
    label file_room:
        if AI == True: 
            scene bg file room
        else:
            scene bg file room dark
        menu:
            "Look through files":
                jump file
            "Leave": 
                jump hallway_right
            "Look around": 
                jump lookAround


    label ending2:
        "The new knowledge floods your brain."
        "Perhaps, then, you will stay here."
        "Ending 2"
        return

    return