import json

class Planets(object):
    def __init__(self, name, radius, sgp, soi, atmo_height, moons=()):
        self.name = name
        self.radius = radius
        self.sgp = sgp
        self.soi = soi
        self.atmo_height = atmo_height
        self.moons = moons
    
    def __repr__(self):
        return  f"{self.name}, {self.radius} m, {self.sgp}, {self.soi}, {self.atmo_height}, Moons: {', '.join([moon['name'] for moon in self.moons])}"

class Moons(Planets):
    def __init__(self, name, radius, sgp, soi, atmo_height, apoapsis, periapsis):
        super().__init__(name, radius, sgp, soi, atmo_height)
        self.apoapsis = apoapsis
        self.periapsis = periapsis

    def __repr__(self):
        return  f"{self.name}, {self.radius} m, {self.sgp}, {self.soi}, {self.atmo_height}, {self.apoapsis}, {self.periapsis}"

with open('Planets.json', 'r') as p:
    planets = json.load(p)

with open('Moons.json', 'r') as m:
    moons = json.load(m)

# Planet Objects
moho = Planets(**planets["Planets"]["Moho"])
eve = Planets(**planets["Planets"]["Eve"])
kerbin = Planets(**planets["Planets"]["Kerbin"])
duna = Planets(**planets["Planets"]["Duna"])
dres = Planets(**planets["Planets"]["Dres"])
jool = Planets(**planets["Planets"]["Jool"])

#Moon Objects
gilly = Moons(**moons["Moons"]["Gilly"])
mun = Moons(**moons["Moons"]["Mun"])
minmus = Moons(**moons["Moons"]["Minmus"])
ike = Moons(**moons["Moons"]["Ike"])
laythe = Moons(**moons["Moons"]["Laythe"])
vall = Moons(**moons["Moons"]["Vall"])
tylo = Moons(**moons["Moons"]["Tylo"])
bop = Moons(**moons["Moons"]["Bop"])
pol = Moons(**moons["Moons"]["Pol"])

print()