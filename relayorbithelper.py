##  APENDICES AND ACKNOWLEDGEMENTS AT THE END OF THE DOCUMENT ##

import math

finished = "false"
while finished == "false":

    #body_radius = input("What's the current body's radius in meters? ")
    #current_sgp = input("What's the current body's Standard Gravitational Parameter (check the wiki)? ")
    #rly_height = input("Apoapsis and Periapsis being the same, what's the height of the Relay Network orbit in meters? ")

    phs_angle = "120°"

    print("\nDisclaimer: This program can only calculate orbits based on a 3 satellite relay network. As such, the resultingvalues can only be used for such a situation.") 

    bad_planet = "true"
    while bad_planet == "true":
        planet_name = input("\n\nAround what celestial body is the relay network being set up? ")
        if planet_name == "Moho":
            body_radius_int = 250000
            current_sgp_int = 1.6860938E11
            soi = 9646663
            atmo_h = "N/A"
            bad_planet = "false"
            
        elif planet_name == "Eve":
            body_radius_int = 700000
            current_sgp_int = 8.1717302E12
            soi = 85109365
            atmo_h = 90000
            bad_planet = "false"
            
        elif planet_name == "Gilly":
            body_radius_int = 13000
            current_sgp_int = 8289449.8
            soi = 126123.27
            atmo_h = "N/A"
            bad_planet = "false"
            
        elif planet_name == "Kerbin":
            body_radius_int = 600000
            current_sgp_int = 3.5316E12
            soi = 84159286
            atmo_h = 70000
            bad_planet = "false"
            
        elif planet_name == "Mun":
            body_radius_int = 200000
            current_sgp_int = 6.5138398E10
            soi = 2429559.1
            atmo_h = "N/A"
            bad_planet = "false"
            
        elif planet_name == "Minmus":
            body_radius_int = 60000
            current_sgp_int = 1.7658E9
            soi = 2247428.4
            atmo_h = "N/A"
            bad_planet = "false"
        
        elif planet_name == "Duna":
            body_radius_int = 320000
            current_sgp_int = 3.0136321E11
            soi = 47921949
            atmo_h = 50000
            bad_planet = "false"
        
        elif planet_name == "Ike":
            body_radius_int = 130000
            current_sgp_int = 1.8568369E10
            soi = 1049598.9
            atmo_h = "N/A"
            bad_planet = "false"
            
        elif planet_name == "Dres":
            body_radius_int = 138000
            current_sgp_int = 2.1484489E10
            soi = 32832480
            atmo_h = "N/A"
            bad_planet = "false"
            
        elif planet_name == "Jool":
            body_radius_int = 6000000
            current_sgp_int = 2.82528E14
            soi = 2455985200
            atmo_h = 200000
            bad_planet = "false"
            
        elif planet_name == "Laythe":
            body_radius_int = 500000
            current_sgp_int = 1.962E12
            soi = 3723645.8
            atmo_h = 50000
            bad_planet = "false"
        
        elif planet_name == "Vall":
            body_radius_int = 300000
            current_sgp_int = 2.074815E11
            soi = 2406401.4
            atmo_h = "N/A"
            bad_planet = "false"
            
        elif planet_name == "Tylo":
            body_radius_int = 600000
            current_sgp_int = 2.82528E12
            soi = 10856518
            atmo_h = "N/A"
            bad_planet = "false"
            
        elif planet_name == "Bop":
            body_radius_int = 65000
            current_sgp_int = 2.4868349E9
            soi = 1221060.9
            atmo_h = "N/A"
            bad_planet = "false"
            
        elif planet_name == "Pol":
            body_radius_int = 44000
            current_sgp_int = 7.2170208E8
            soi = 1042138.9
            atmo_h = "N/A"
            bad_planet = "false"
            
        elif planet_name == "Eeloo":
            body_radius_int = 210000
            current_sgp_int = 7.4410815E10
            soi = 119082940
            atmo_h = "N/A"
            bad_planet = "false"
            
        elif planet_name == "Bodies":
            print("Moho\nEve\nGilly\nKerbin\nMun\nMinmus\nDuna\nIke\nDres\nJool\nLaythe\nVall\nTylo\nBop\nPol\nEeloo")
        
        else: 
            print ("Unknown celestial body. Insert command Bodies to get a list of available options.")
            #quit()



    bad_height = "true"
    while bad_height == "true":
        rly_height = input("\n\nApoapsis and Periapsis being the same, what's the height of the Relay Network orbit in meters above ground? ")

        rly_height_int = int(rly_height)
        semimjr_axis = body_radius_int + rly_height_int

        if semimjr_axis > soi:
            print ("\n\nYour desired orbit would place your relay network outside of " + planet_name + "'s Sphere of Influence. Please, choosea new orbit of, at most, " + str(soi) + " meters")
        

        elif rly_height_int < body_radius_int:
            print ("\n\nYour desired orbit would place your relay network below the minimum orbit around " + planet_name + ", leading to signal occlusion. Please, choose a new orbit of, at least " + str(body_radius_int) + " meters")
        
        else:
            bad_height = "false"
        

    orbital_period_rly = 2 * math.pi * (math.sqrt((semimjr_axis ** 3)/current_sgp_int)) ##  calculating orbital period of the relay network
    orbital_period_rly = round (orbital_period_rly,6)

    #print ("Your orbital period is " + str(orbital_period_rly) + " seconds.")


    orbital_period_insert = orbital_period_rly * (2/3) ##  calculating the orbital period of the insertion craft, which must be 2/3 of the relay's
    orbital_period_insert = round (orbital_period_insert,6)

    #print ("Orbital Period insert is " + str(orbital_period_insert))


    a_insert = ((current_sgp_int * (orbital_period_insert ** 2))/(4 * (math.pi ** 2))) ** (1/3) ##  calculating the requivalent semi major axis of the orbital period of the inserting craft
    a_insert = round (a_insert,6)

    #print ("A_insert = " + str(a_insert))


    r_min = (2 * a_insert) - semimjr_axis ##  calculating the corresponding periapsis of that semi major axis, assuming the apoapsis will be the same as the relay network

    #print ("r_min = " + str(r_min))


    alt = r_min - body_radius_int
    alt = round(alt,2)

    #print ("alt =" + str(alt))

    if type(atmo_h) != str:

        if alt < atmo_h:
            #print("alt < \n\atmo_h\n\n")
            orbital_period_insert = orbital_period_rly * (4/3) ##balooning out the Apoapsis instead of reducing the Periapasis of the inserting craft.
            orbital_period_insert = round (orbital_period_insert,6)
        
            a_insert = ((current_sgp_int * (orbital_period_insert ** 2))/(4 * (math.pi ** 2))) ** (1/3)
            a_insert = round (a_insert,6)

            r_max = (2 * a_insert) - semimjr_axis

            alt = r_max - body_radius_int
            alt = round(alt,2)

            print("\n\nYour inserting craft's orbit should have an Apoapsis of " + str(alt) + " meters, and a Perapsis of " + str(rly_height) + " meters to ensure optimal dispersion of satellites.")

            print("\n\nThis value, of course, is idealized. Ingame, the execution is a lot more finnicky and you cannot get a perfectly circular orbit where both the Periapsis and Apoapsis of your relay network are " + str(rly_height_int) + ", so, when setting this up, the most imporant aspect will be the orbital period relation between the relay's orbit and the inserting craft's orbit. To make sure that this program can help you do just that, after establishing the inserting craft's orbit with the values for the Apoapsis and Periapsis stated above, please answer the following question:\n\n")        


            string_craft_d = input("Ingame, how many days the orbital period of the inserting craft has (nothiing equals 0)? ")
            string_craft_h = input("\nNow the hours. ")
            string_craft_m = input("\nNow the minutes. ")
            string_craft_s = input("\nNow the seconds. ")

            craft_d = int(string_craft_d)
            craft_h = int(string_craft_h)
            craft_m = int(string_craft_m)
            craft_s = int(string_craft_s)


            orbital_period_insert = (craft_d * 21600) + (craft_h * 3600) + (craft_m * 60) + craft_s

            orbital_period_rly = orbital_period_insert * (3/4)

            o_day = orbital_period_rly // (6 * 3600)
            orbital_period_rly = orbital_period_rly % (6 * 3600)

            o_hour = orbital_period_rly // 3600
            orbital_period_rly = orbital_period_rly % 3600

            o_minutes = orbital_period_rly // 60

            o_seconds = orbital_period_rly % 60

            o_day = math.floor(o_day)
            o_hour = math.floor(o_hour)
            o_minutes = math.floor(o_minutes)
            o_seconds = math.floor(o_seconds)


            if o_day < 1:
                print("\nYour relay satellite must have a orbital period " + str(o_hour) + "h " + str(o_minutes) + "min " + str(o_seconds) + "sec. So, all you have to do now is to release every relay with enough time to plot a maneuver node at the periapsis and add enough retrograde motion to set your satellite's orbital period to that.\n\nTo make sure everything is as it should, make a quicksave before releasing the second relay, and while in control of the inserting craft, set the first satellite as target. When you reach your orbit's periapsis again, the phase angle between you and the relay satellite should be " + phs_angle + ". To check it, on the mode control panel, click the Maneuver Mode button (purple button), then on the Approach info tab.")

            else:
                print("\nYour relay satellite must have a orbital period " + str(o_day) + "d " + str(o_hour) + "h " + str(o_minutes) + "min " + str(o_seconds) + "sec. So, all you have to do now is to release every relay with enough time to plot a maneuver node at the periapsis and add enough retrograde motion to set your satellite's orbital period to that.\n\nTo make sure everything is as it should, make a quicksave before releasing the second relay, and while in control of the inserting craft, set the first satellite as target. When you reach your orbit's periapsis again, the phase angle between you and the relay satellite should be " + phs_angle + ". To check it, on the mode control panel, click the Maneuver Mode button (purple button), then on the Approach info tab.")




        else:
            #print("alt > atmo_h") 
            print("\n\nYour inserting craft's orbit should have a Periapsis of " + str(alt) + " meters, and an Apoapsis of " + str(rly_height) + " meters to ensure optimal dispersion of satellites.")

            print("\n\nThis value, of course, is idealized. Ingame, the execution is a lot more finnicky and you cannot get a perfectly circular orbit where both the Periapsis and Apoapsis of your relay network are " + str(rly_height_int) + ", so, when setting this up, the most imporant aspect will be the orbital period relation between the relay's orbit and the inserting craft's orbit. To make sure that this program can help you do just that, after establishing the inserting craft's orbit with the values for the Apoapsis and Periapsis stated above, please answer the following question:\n\n") 

            string_craft_d = input("Ingame, how many days the orbital period of the inserting craft has (nothiing equals 0)? ")
            string_craft_h = input("\nNow the hours. ")
            string_craft_m = input("\nNow the minutes. ")
            string_craft_s = input("\nNow the seconds. ")

            craft_d = int(string_craft_d)
            craft_h = int(string_craft_h)
            craft_m = int(string_craft_m)
            craft_s = int(string_craft_s)

            orbital_period_insert = (craft_d * 21600) + (craft_h * 3600) + (craft_m * 60) + craft_s
            
            #print(str(orbital_period_insert))

            orbital_period_rly = orbital_period_insert * (3/2)
            
            #print(str(orbital_period_rly))

            o_day = orbital_period_rly // (6 * 3600)
            orbital_period_rly = orbital_period_rly % (6 * 3600)

            o_hour = orbital_period_rly // 3600
            orbital_period_rly = orbital_period_rly % 3600

            o_minutes = orbital_period_rly // 60

            o_seconds = orbital_period_rly % 60

            o_day = math.floor(o_day)
            o_hour = math.floor(o_hour)
            o_minutes = math.floor(o_minutes)
            o_seconds = math.floor(o_seconds)

            if o_day < 1:
                print("\nYour relay satellite must have a orbital period " + str(o_hour) + "h " + str(o_minutes) + "min " + str(o_seconds) + "sec. So, all you have to do now is to release every relay with enough time to plot a maneuver node at the periapsis and add enough prograde motion to set your satellite's orbital period to that.To make sure everything is as it should, make a quicksave before releasing the second relay, and while in control of the inserting craft, set the first satellite as target. When you reach your orbit's periapsis again, the phase angle between you and the relay satellite should be " + phs_angle + ". To check it, on the mode control panel, click the Maneuver Mode button (purple button), then on the Approach info tab.") 

            else:
                print("\nYour relay satellite must have a orbital period " + str(o_day) + "d " + str(o_hour) + "h " + str(o_minutes) + "min " + str(o_seconds) + "sec. So, all you have to do now is to release every relay with enough time to plot a maneuver node at the periapsis and add enough prograde motion to set your satellite's orbital period to that.\n\nTo make sure everything is as it should, make a quicksave before releasing the second relay, and while in control of the inserting craft, set the first satellite as target. When you reach your orbit's periapsis again, the phase angle between you and the relay satellite should be " + phs_angle + ". To check it, on the mode control panel, click the Maneuver Mode button (purple button), then on the Approach info tab.")





    else:
        
        if alt < 0:
            #print("alt < 0")
            orbital_period_insert = orbital_period_rly * (4/3)
            orbital_period_insert = round (orbital_period_insert,6)
            
            a_insert = ((current_sgp_int * (orbital_period_insert ** 2))/(4 * (math.pi ** 2))) ** (1/3)
            a_insert = round (a_insert,6)

            r_max = (2 * a_insert) - semimjr_axis

            alt = r_max - body_radius_int
            alt = round(alt,2)

            print("\n\nYour inserting craft's orbit should have an Apoapsis of " + str(alt) + " meters, and a Perapsis of " + str(rly_height) + " meters meters to ensure optimal dispersion of satellites.")

            print("\n\nThis value, of course, is idealized. Ingame, the execution is a lot more finnicky and you cannot get a perfectly circular orbit where both the Periapsis and Apoapsis of your relay network are " + str(rly_height_int) + ", so, when setting this up, the most imporant aspect will be the orbital period relation between the relay's orbit and the inserting craft's orbit. To make sure that this program can help you do just that, after establishing the inserting craft's orbit with the values for the Apoapsis and Periapsis stated above, please answer the following question:\n\n")        


            string_craft_d = input("Ingame, how many days the orbital period of the inserting craft has (nothiing equals 0)? ")
            string_craft_h = input("\nNow the hours. ")
            string_craft_m = input("\nNow the minutes. ")
            string_craft_s = input("\nNow the seconds. ")

            craft_d = int(string_craft_d)
            craft_h = int(string_craft_h)
            craft_m = int(string_craft_m)
            craft_s = int(string_craft_s)


            orbital_period_insert = (craft_d * 21600) + (craft_h * 3600) + (craft_m * 60) + craft_s

            orbital_period_rly = orbital_period_insert * (3/4)

            o_day = orbital_period_rly // (6 * 3600)
            orbital_period_rly = orbital_period_rly % (6 * 3600)

            o_hour = orbital_period_rly // 3600
            orbital_period_rly = orbital_period_rly % 3600

            o_minutes = orbital_period_rly // 60

            o_seconds = orbital_period_rly % 60

            o_day = math.floor(o_day)
            o_hour = math.floor(o_hour)
            o_minutes = math.floor(o_minutes)
            o_seconds = math.floor(o_seconds)


            if o_day < 1:
                print("\nYour relay satellite must have a orbital period " + str(o_hour) + "h " + str(o_minutes) + "min " + str(o_seconds) + "sec. So, all you have to do now is to release every relay with enough time to plot a maneuver node at the periapsis and add enough retrograde motion to set your satellite's orbital period to that.\n\nTo make sure everything is as it should, make a quicksave before releasing the second relay, and while in control of the inserting craft, set the first satellite as target. When you reach your orbit's periapsis again, the phase angle between you and the relay satellite should be " + phs_angle + ". To check it, on the mode control panel, click the Maneuver Mode button (purple button), then on the Approach info tab.")

            else:
                print("\nYour relay satellite must have a orbital period " + str(o_day) + "d " + str(o_hour) + "h " + str(o_minutes) + "min " + str(o_seconds) + "sec. So, all you have to do now is to release every relay with enough time to plot a maneuver node at the periapsis and add enough retrograde motion to set your satellite's orbital period to that.\n\nTo make sure everything is as it should, make a quicksave before releasing the second relay, and while in control of the inserting craft, set the first satellite as target. When you reach your orbit's periapsis again, the phase angle between you and the relay satellite should be " + phs_angle + ". To check it, on the mode control panel, click the Maneuver Mode button (purple button), then on the Approach info tab.")


        else:
            #print("alt > 0")
            print("\n\nYour inserting craft's orbit should have a Periapsis of " + str(alt) + " meters, and an Apoapsis of " + str(rly_height) + " meters to ensure optimal dispersion of satellites.")

            print("\n\nThis value, of course, is idealized. Ingame, the execution is a lot more finnicky and you cannot get a perfectly circular orbit where both the Periapsis and Apoapsis of your relay network are " + str(rly_height_int) + ", so, when setting this up, the most imporant aspect will be the orbital period relation between the relay's orbit and the inserting craft's orbit. To make sure that this program can help you do just that, after establishing the inserting craft's orbit with the values for the Apoapsis and Periapsis stated above, please answer the following question:\n\n")

            string_craft_d = input("Ingame, how many days the orbital period of the inserting craft has (nothiing equals 0)? ")
            string_craft_h = input("\nNow the hours. ")
            string_craft_m = input("\nNow the minutes. ")
            string_craft_s = input("\nNow the seconds. ")

            craft_d = int(string_craft_d)
            craft_h = int(string_craft_h)
            craft_m = int(string_craft_m)
            craft_s = int(string_craft_s)

            orbital_period_insert = (craft_d * 21600) + (craft_h * 3600) + (craft_m * 60) + craft_s

            orbital_period_rly = orbital_period_insert * (3/2)

            o_day = orbital_period_rly // (6 * 3600)
            orbital_period_rly = orbital_period_rly % (6 * 3600)

            o_hour = orbital_period_rly // 3600
            orbital_period_rly = orbital_period_rly % 3600

            o_minutes = orbital_period_rly // 60

            o_seconds = orbital_period_rly % 60

            o_day = math.floor(o_day)
            o_hour = math.floor(o_hour)
            o_minutes = math.floor(o_minutes)
            o_seconds = math.floor(o_seconds)

            if o_day < 1:
                print("\nYour relay satellite must have a orbital period " + str(o_hour) + "h " + str(o_minutes) + "min " + str(o_seconds) + "sec. So, all you have to do now is to release every relay with enough time to plot a maneuver node at the periapsis and add enough prograde motion to set your satellite's orbital period to that.\n\nTo make sure everything is as it should, make a quicksave before releasing the second relay, and while in control of the inserting craft, set the first satellite as target. When you reach your orbit's periapsis again, the phase angle between you and the relay satellite should be " + phs_angle + ". To check it, on the mode control panel, click the Maneuver Mode button (purple button), then on the Approach info tab.")

            else:
                print("\nYour relay satellite must have a orbital period " + str(o_day) + "d " + str(o_hour) + "h " + str(o_minutes) + "min " + str(o_seconds) + "sec. So, all you have to do now is to release every relay with enough time to plot a maneuver node at the periapsis and add enough prograde motion to set your satellite's orbital period to that.\n\nTo make sure everything is as it should, make a quicksave before releasing the second relay, and while in control of the inserting craft, set the first satellite as target. When you reach your orbit's periapsis again, the phase angle between you and the relay satellite should be " + phs_angle + ". To check it, on the mode control panel, click the Maneuver Mode button (purple button), then on the Approach info tab.")

    done = input("Are you finished? Y/N ")
    if ((done == "Y") or (done == "y")):
        finished = "true"




######################################  TO  DO  LIST  ############################################
##                                                                                              ##
##  write check for rly_height to make sure it isn't inside atmosphere                          ## ##                                                                                              ##
##  add check to see if OPM is currently installed and add support for it                       ##
##                                                                                              ##
##  add input to ask for the orbital period and give a proper answer to aim for                 ##
##                                                                                              ##
##################################################################################################


####################################  ACKNOWLEDGEMENTS  ##########################################
##                                                                                              ##
##  To Corrado33, for initiating me in the ways of Python, for basically spoonfeeding me        ##
##  whenever I asked them  anything, be about code or math, and for their inexhaustible         ##
##  patience.                                                                                   ##
##                                                                                              ##
##  To Eric Meyer and his resonant orbit calculator, against which I proof tested much of my    ##
##  math and results.                                                                           ##
##                                                                                              ##
##################################################################################################



##                                      APPENDICES                                              ##

##################################  VARIABLE DEFINITIONS  ########################################
##                                                                                              ##
##  planet_name: the celestial body around which the relay network will be set up.              ##
##                                                                                              ##
##  body_radius_int: radius of the selected celestia body.                                      ##
##                                                                                              ##
##  current_sgp_int: standard gravitational parameter of the selected body                      ##
##                                                                                              ##
##  rly_height: height ABOVE GROUND of the relay network assuming both Ap and Pe are the same.  ##
##                                                                                              ##
##  rly_height_int: intergerfied version of the above.                                          ##
##                                                                                              ##
##  semimjr_axis: the semi major axis of the relay network's orbit.                             ##
##                                                                                              ##
##  orbital_period_rly: the orbital period of the relay network                                 ##
##                                                                                              ##
##  orbital_period_insert: the orbital period of the satellite insertion craft.                 ##
##                                                                                              ##
##  a_insert: the semi major axis of the satellite insertion craft's orbit                      ##
##                                                                                              ##
##  r_min: the sum of the height of the periapsis of the insertion craft's with the body's      ##
##  radius.                                                                                     ##
##                                                                                              ##
##  alt: height of the periapsis of the insertion craft.                                        ##
##                                                                                              ##
##  soi: sphere of influence (from center of the body)                                          ##
##                                                                                              ##
##################################################################################################


######################################  EQUATIONS USED  ##########################################
##                                                                                              ##
##  Orbital period: T = 2pi * sqrroot  (semi major axis^3)/standard gravitational parameter     ##
##                                                                                              ##
##  Using the above, but solving for the semi major axis instead:                               ##
##              semi major axis = cuberoot ((std grav parameter * (orbital period^2))/4(pi^2))  ##
##                                                                                              ##
##  semi major axis: (a_insert + rly_height_int)/2                                              ##
##                                                                                              ##
##################################################################################################


##                                      DEPRECATED                                              ##

##1

#Reason: Better solution found that doesn't require the addition of new variables.

# elif alt < 0:
#     r_min = 2617.1 + body_radius_int

#     #print("2nd a_insert " + str(a_insert))

#     r_max = (2 * a_insert) - r_min

#     #print("r_max " + str(r_max))

#     alt = r_max - body_radius_int
#     alt = round(alt,2)

#     #print("Second alt " + str(alt))

#     print("Your desired orbit would place the inserting craft's Periapsis below ground, and as such the relay network's Apoapsis has been revised accordingly to match the highest point in the selected celestial body plus a margin of error. Your relay network's new Apoapsis is " + str(alt) + ", and your inserting craft's Periapsis should be" + str(r_min) + " meters")



##2

#Reason: Prototype sections used at early development for proof of concept. Removed to tidy up code.

#body_radius_int = int(body_radius)
#current_sgp_int = float(current_sgp)
#print(str(body_radius_int)+ " " + str(current_sgp_int) + " " + rly_height) 