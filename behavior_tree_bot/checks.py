def if_neutral_planet_available(state):
    return any(state.neutral_planets())


def have_largest_fleet(state):
    return sum(planet.num_ships for planet in state.my_planets()) \
             + sum(fleet.num_ships for fleet in state.my_fleets()) \
           > sum(planet.num_ships for planet in state.enemy_planets()) \
             + sum(fleet.num_ships for fleet in state.enemy_fleets())

# def can_capture_biggest(state):
# 	strongest_planet = max(state.my_planets(), key=lambda p: p.num_ships, default=None)
# 	maximum_growth = max(state.neutral_planets(), key=lambda p: p.growth_rate, default=None)
# 	if maximum_growth.num_ships+1 > strongest_planet.num_ships:
# 		return True
# 	return False