import sys
sys.path.insert(0, '../')
from planet_wars import issue_order


def attack_weakest_enemy_planet(state):
    # (1) If we currently have a fleet in flight, abort plan.
    if len(state.my_fleets()) >= 1:
        return False

    # (2) Find my strongest planet.
    strongest_planet = max(state.my_planets(), key=lambda t: t.num_ships, default=None)

    # (3) Find the weakest enemy planet.
    weakest_planet = min(state.enemy_planets(), key=lambda t: t.num_ships, default=None)

    if not strongest_planet or not weakest_planet:
        # No legal source or destination
        return False
    else:
        # (4) Send half the ships from my strongest planet to the weakest enemy planet.
        return issue_order(state, strongest_planet.ID, weakest_planet.ID, strongest_planet.num_ships / 2)


def spread_to_weakest_neutral_planet(state):
    # (1) If we currently have a fleet in flight, just do nothing.
    if len(state.my_fleets()) >= 1:
        return False

    # (2) Find my strongest planet.
    strongest_planet = max(state.my_planets(), key=lambda p: p.num_ships, default=None)

    # (3) Find the weakest neutral planet.
    weakest_planet = min(state.neutral_planets(), key=lambda p: p.num_ships, default=None)

    if not strongest_planet or not maximum_growth:
        # No legal source or destination
        return False
    else:
        return issue_order(state, strongest_planet.ID, weakest_planet.ID, strongest_planet.num_ships / 2)
            #weakest_planet = state.neutral_planets(), key=lambda p: p.growth_rate, default=None
        # (4) Send half the ships from my strongest planet to the weakest enemy planet.

# def spread_to_biggest_neutral_planet(state):
#         # (1) If we currently have a fleet in flight, just do nothing.
#     if len(state.my_fleets()) >= 1:
#         return False

#     # (2) Find my strongest planet.
#     strongest_planet = max(state.my_planets(), key=lambda p: p.num_ships, default=None)

#     # (3) Find the weakest neutral planet.
#     neutrals_by_size = state.neutral_planets()
#     neutrals_by_size.sort(key=lambda p: p.growth_rate)
#     #maximum_growth = max(state.neutral_planets(), key=lambda p: p.growth_rate, default=None)

#     if not strongest_planet or not maximum_growth:
#         # No legal source or destination
#         return False
#     else:
#         for planet in neutrals_by_size:
#             if planet.num_ships+1 > strongest_planet.num_ships:
#                 return issue_order(state, strongest_planet.ID, planet.ID, planet.num_ships+1)

#         #weakest_planet = state.neutral_planets(), key=lambda p: p.growth_rate, default=None
#         # (4) Send half the ships from my strongest planet to the weakest enemy planet.

def aggresive(state):
    my_planets = iter(sorted(state.my_planets(), key=lambda p: p.num_ships))

    enemy_planets = [planet for planet in state.enemy_planets()
                      if not any(fleet.destination_planet == planet.ID for fleet in state.my_fleets())]
    enemy_planets.sort(key=lambda p: p.num_ships)

    target_planets = iter(enemy_planets)

    try:
        my_planet = next(my_planets)
        target_planet = next(target_planets)
        while True:
            required_ships = target_planet.num_ships + \
                                 state.distance(my_planet.ID, target_planet.ID) * target_planet.growth_rate + 1

            if my_planet.num_ships > required_ships:
                issue_order(state, my_planet.ID, target_planet.ID, required_ships)
                my_planet = next(my_planets)
                target_planet = next(target_planets)
            else:
                my_planet = next(my_planets)

    except StopIteration:
        return
