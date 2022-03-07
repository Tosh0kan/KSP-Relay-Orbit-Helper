class Planets:
    def __init__(self, name: str, radius: int, sgp: float, soi: float, atmo_height: int):
        self.name = name
        self.radius = radius
        self.sgp = sgp
        self.soi = soi
        self.atmo_height = atmo_height
        self.moons = []
    
    def __repr__(self):
        return f"{self.name}, {self.radius}, {self.sgp}, {self.soi}, {self.atmoh},"

    def add_moon(self, moon):
        self.moons.append(moon)


class Moons(Planets):
    def __init__(self, name: str, radius: int, sgp: float, soi: float, atmo_height: int, apoap: float, periap: float):
        super().__init__(name, radius, sgp, soi, atmo_height)
        self.apoap = apoap
        self.periap = periap
        

class Satellites: #The relay and it's constituting satellites
    def __init__(self, name: str):
        self.name = name
        self.height = height
        self.mjr_axis = self.height + planet.radius
        self.orb_period = round(2 * pi * (((self.mjr_axis ** 3)/planet.sgp) ** (1/2)) ,2)
    
    def __repr__(self) -> str:
        return f"{self.name}, {self.height}, {self.mjr_axis}, {self.orb_period} "
    

class Dispenser:
    def __init__(self, name: str):
        self.name = name
        self.orb_period = round(craft.orb_period * 2/3 ,6)
        self.mjr_axis = round(((planet.sgp * (self.orb_period ** 2))/(4 * (pi ** 2))) ** (1/3) ,3)
        self.semimjr_axis = (2 * self.mjr_axis) - craft.mjr_axis
        self.alt = round(self.semimjr_axis - planet.radius ,2)

    def __repr__(self) -> str:
        return f"{self.name}, {self.mjr_axis}, {self.orb_period} "

    def get_orb_period(self, frac):
        self.orb_period = Satellites.orb_period * frac

    
def get_data():
    planet_input = input("Planet's or moon's name? ").casefold().title()
    height = float(input("Desired height of the relay? "))
    for planet in planet_list:
        if planet.name == planet_input:
            planet = planet
            break
    
    return height, planet

pi = 3.14159 
neg_inf = float("-inf")

planet_list = [
    Planets("Moho", 250000, 1.6860938e11, 9646663.0, neg_inf),
    Planets("Eve", 700000, 8.1717302e12, 85109365, 90000),
    Planets("Kerbin", 600000, 3.5316000e12, 84159286, 70000),
    Planets("Duna", 320000, 3.0136321e11, 47921949, 50000),
    Planets("Dres", 138000, 2.1484489e10, 32832840, neg_inf),
    Planets("Jool", 6000000, 2.8252800e14, 2.4559852e9, 200000)
]

moons_list = [
    Moons("Gilly", 13000, 8289449.8, 126123.27, neg_inf, 48825000, 14175000),
    Moons("Mun", 200000, 6.5138398e10, 2429559.1, neg_inf, 12000000, 12000000),
    Moons("Minmus", 60000, 1.7658000e9, 2247428.4, neg_inf, 47000000, 47000000),
    Moons("Ike", 130000, 1.8568369e10, 1049598.9, neg_inf, 3296000, 3104000),
    Moons("Laythe", 500000, 1.9620000e12, 3723645.8, 50000, 27184000, 27184000),
    Moons("Vall", 300000, 2.0748150e11, 2406401.4, neg_inf, 43152000, 43152000),
    Moons("Tylo", 600000, 2.8252800e12, 10856518, neg_inf, 68500000, 68500000),
    Moons("Bop", 65000, 2.4868349e9, 1221060.9, neg_inf, 158697500, 98308500),
    Moons("Pol", 44000, 2.4328494e10, 1042138.9, neg_inf, 210624207, 149155794)
]

moon_assign = [
    planet_list[1].add_moon(moons_list[0]),
    planet_list[2].add_moon(moons_list[1]),
    planet_list[2].add_moon(moons_list[2]),
    planet_list[3].add_moon(moons_list[3]),
    planet_list[5].add_moon(moons_list[4]),
    planet_list[5].add_moon(moons_list[5]),
    planet_list[5].add_moon(moons_list[6]),
    planet_list[5].add_moon(moons_list[7]),
    planet_list[5].add_moon(moons_list[8])
]





