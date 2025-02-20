planet_in_solar = ["Mercury", "Mars"]

def add_planet(planet):
    planet_in_solar.append(planet)

add_planet("Jupiter")
add_planet("Saturn")

def display_planets():
    for planet in planet_in_solar:
        print(f"-{planet}")



def add_more_planets(planets):
    planet_in_solar.extend(planets)

planets=["Neptune","Pluto"]
add_more_planets(planets)

def insert_planet(index,planet):
    planet_in_solar.insert(index, planet)

insert_planet(1,"Venus")
insert_planet(2,"Earth")
insert_planet(6,"Uranus")

del planet_in_solar[8]
display_planets()

rocky_planets=planet_in_solar[0:4]

def display_rocky_planets():
    for planet in rocky_planets:
        print(f"-{planet}")

display_rocky_planets()

# Example spacecraft list
spacecraft = [
   ("Cassini", "Saturn"),
   ("Viking", "Mars"),
   ("MESSENGER","Mercury","Venus"),
   ("Mariner 10","Mercury","Venus"),
   ("Venera 1-16","Venus"),
   ("Mariner 2","Venus"),
   ("Mariner 5","Venus"),
   ("Pioneer Venus 1 and 2","Venus"),
   ("Vega 1 and 2","Venus"),
   ("Galileo","Venus"),
   ("Magellan","Venus"),
   ("Cassini","Venus","Jupiter","Saturn"),
   ("Venus Express","Venus"),
   ("Parker Solar Probe","Venus"),
   ("Mariner 4","Mars"),
   ("Mariner 6 and 7","Mars"),
   ("Mariner 9","Mars"),
   ("Viking 1 and 2","Mars"),
   ("Mars Pathfinder","Mars"),
   ("Mars Odyssey","Mars"),
   ("Spirit, Opportunity","Mars"),
   ("Phoenix","Mars"),
   ("Curiosity","Mars"),
   ("InSight","Mars"),
   ("Perseverance","Mars"),
   ("Pioneer 10","Jupiter"),
   ("Pioneer 11","Jupiter","Saturn"),
   ("Voyager 1","Jupiter","Saturn"),
   ("Voyager 2","Jupiter","Saturn","Uranus","Neptune"),
   ("Ulysses","Jupiter"),
   ("Galileo","Jupiter"),
   ("New Horizons","Jupiter","Pluto"),
   ("Juno","Jupiter"),
   ("Pioneer 11","Saturn"),
]

def visited_planets():
    for spacecraft_info in spacecraft:
        spacecraft_name= spacecraft_info[0]
        planets_visited=spacecraft_info[1:]# Getting planets visited by this spacecraft
        print(f"{spacecraft_name} has visited" )
        print("-------------")
        for planet in planets_visited:
            print(planet)
        print()

visited_planets()