import sys; import os
import json
from math import pi

#==< Classes Definitions >==#
class Planets(object):
    def __init__(self, name, radius, sgp, soi, atmo_height, moons=()):
        self.name = name
        self.radius = radius
        self.sgp = sgp
        self.soi = soi
        self.atmo_height = float(atmo_height)
        self.moons = moons
    
    def __repr__(self):
        return  f"{self.name}, {self.radius} m, {self.sgp}, {self.soi}, {self.atmo_height}, Moons: {', '.join([moon['name'] for moon in self.moons])}"

class Moons(Planets):
    def __init__(self, name, radius, sgp, soi, atmo_height, apoapsis, periapsis):
        super().__init__(name, radius, sgp, soi, float(atmo_height))
        self.apoapsis = apoapsis
        self.periapsis = periapsis

    def __repr__(self):
        return  f"{self.name}, {self.radius} m, {self.sgp}, {self.soi}, {self.atmo_height}, {self.apoapsis}, {self.periapsis}"

class Eqn(object):
    @staticmethod 
    def get_rly_semimjr_axis(): 
        rly_semimjr_axis = target.radius + rly_height
        return rly_semimjr_axis
    
    @staticmethod
    def get_rly_period():
        rly_period = 2 * pi * (((rly_semimjr_axis ** 3)/target.sgp) ** (1/2))
        return round(rly_period,4)
    
    @staticmethod
    def get_insert_data():
        insert_period = round((rly_period * (4/3)), 4)
        insert_semimjr_axis = round(((target.sgp * (insert_period **2))/(4 * (pi ** 2))) ** (1/3),4)
        r_max = (2 * insert_semimjr_axis) - rly_semimjr_axis
        alt = round(r_max - target.radius,2)

        if alt >= target.soi:
            insert_period = round((rly_period * (2/3)), 4)
            insert_semimjr_axis = round(((target.sgp * (insert_period **2))/(4 * (pi ** 2))) ** (1/3),4)
            r_min = (2 * insert_semimjr_axis) - rly_semimjr_axis
            alt = round(r_min - target.radius,2)
        
        return alt

#==< Functions Definitions >==#
def get_inputs():
    bad_planet = True
    while bad_planet == True:
        input_name = input("Planet or moon name? ").capitalize()
        for element in planets_objects + moons_objects:
            if element.name == input_name:
                target = element
                bad_planet = False
                break

        if bad_planet == True:
            print("The name typed doesn't match any of the known bodies. Please, try again.\n")
    
    bad_height = True
    while bad_height == True:
        input_height = float(input("What's the desired height, in meters, for the relay above ground? "))
        if input_height <= target.radius:
            print(f"""The desired height would put your relay orbit below the minimum orbit around {target.name}, leading to signal occlusion. Please, pick a new height (min. {target.radius + 10000}m).\n""")

        elif input_height >= (target.soi - target.radius):
            print(f"""The desired height would put your relay orbit outside of {target.name}'s sphere of influence. Please, pick a new height (max. {(target.soi - target.radius) - 10000}m).\n""")

        elif input_height <= target.atmo_height:
            print(f"""The desired height would put your relay orbit inside the atmosphere limit. Please, pick a new height. (min. {target.atmo_height + 10000}m).\n""")

        else:
            bad_height = False
        
    return target, input_height

def resource_path(relative_path):
    '''Get absolute path to resource, works for dev and for PyInstaller'''
    #Credits go to https://stackoverflow.com/a/60953781/10925021
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

#==< File Openings >==#
with open(resource_path('Planets.json'), 'r') as p: 
    planets_f = json.load(p)

with open(resource_path('Moons.json'), 'r') as m: 
    moons_f = json.load(m)

# Planet Objects #TODO Make a loop that automatically populates stuff
planets_objects = []
for planet in planets_f.values():
  # moon is now the inner dicts, example below
  new_planet = Planets(**planet)
  planets_objects.append(new_planet)

#Moon Objects #TODO Make a loop that automatically populates stuff
moons_objects = []
for moon in moons_f.values():
  # moon is now the inner dicts, example below
  new_moon = Moons(**moon)
  moons_objects.append(new_moon)


print("\nDisclaimer: This program can only calculate orbits based on a 3 satellite relay network. As such, the resulting values can only be used for such a configuration.") 

while True:
    target, rly_height = get_inputs()
    rly_semimjr_axis = Eqn.get_rly_semimjr_axis()
    rly_period = Eqn.get_rly_period()
    alt = Eqn.get_insert_data()
    if alt > rly_height:  
        print(f"""Your inserting craft, aka The Mothership, should've an Apoapsis of {alt} m and a Periapsis of {rly_height} m above ground to ensure optimal satellite dispersion
        """)
    if alt < rly_height:
        print(f"""Your inserting craft, aka The Mothership, should've an Apoapsis of {rly_height} m and a Periapsis of {alt} m above ground to ensure optimal satellite dispersion
        """)