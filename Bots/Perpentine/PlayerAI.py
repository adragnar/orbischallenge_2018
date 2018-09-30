from PythonClientAPI.game.PointUtils import *
from PythonClientAPI.game.Entities import FriendlyUnit, EnemyUnit, Tile
from PythonClientAPI.game.Enums import Team
from PythonClientAPI.game.World import World
from PythonClientAPI.game.TileUtils import TileUtils

import numpy as np

class LocationManager:

    def __init__(self, enemy_list, curr_player):
        self.enemy_positions = [x.position for x in enemy_list]
        self.curr_position = curr_player.position
        if self.curr_position[0] <=14 and self.curr_position[1] <= 14:
            self.corner = (4,4)
        elif self.curr_position[0] <=14 and self.curr_position[1] > 14:
            self.corner = (4,25)
        elif self.curr_position[0] > 14 and self.curr_position[1] <= 14:
            self.corner = (25,4)
        elif self.curr_position[0] > 14 and self.curr_position[1] > 14:
            self.corner = (25, 25)

        #set expansion directions
        if (self.corner == (4,4)) :
            self.expand_dir_x = "right"
            self.expand_dir_y = "down"

        elif (self.corner == (4, 25)):
            self.expand_dir_x = "right"
            self.expand_dir_y = "up"

        elif (self.corner == (25, 4)):
            self.expand_dir_x = "left"
            self.expand_dir_y = "down"

        elif (self.corner == (25, 25)):
            self.expand_dir_x = "left"
            self.expand_dir_y = "up"

    def get_my_board_quadrant(self):
        if self.corner[0] <=14 and self.corner[1] <= 14:
            return (1, 1)
        elif self.corner[0] <=14 and self.corner[1] > 14:
            return (1, 28)
        elif self.corner[0] >14 and self.corner[1] <= 14:
            return (28,1)
        elif self.corner[0] >14 and self.corner[1] > 14:
            return (28, 28)

    def update(self, friendly_unit, enemy_units):
        self.curr_position = friendly_unit.position
        self.enemy_positions = [x.position for x in enemy_units]

    def update_corner(self, friendly_unit):
        curr = friendly_unit.position
        for point in friendly_unit.territory:
            # check which point is closer to (14, 14) by the taxicab norm
            if abs(point[0] - 14) + abs(point[1] - 14) <= abs(point[0] - 14) + abs(point[1] - 14):
                curr = point
        return curr

    def get_closest_threat(self, world, friendly_unit):
        points = friendly_unit.body
        li_ = [world.path.get_shortest_path_distance(x) for x in self.enemy_positions]
        return min(li_)

    def get_expansion_directions(self):
        return (self.expand_dir_x, self.expand_dir_y)

class PlayerAI:

    def __init__(self):
        self.turn_num = 0
        self.location_manager = None

    def fill_corner(self, friendly_unit):
        '''Fill the 16 squares in snake corner when starting the game. Executes move'''

        board_quadrant_corner = self.location_manager.get_my_board_quadrant()  #t_left corner
        top_left_coords = [(4,3), (4,2), (4,1), (3,1), (2,1), (1,1), (1,2), (1,3), (1,4), (2,4)]
        top_right_coords = [(25,3), (25,2), (25,1), (26,1), (27,1), (28,1), (28,2), (28,3), (28,4), (27,4)]
        bottom_left_coords = [(3,25), (2,25), (1,25), (1, 26), (1,27), (1,28), (2,28), (3,28), (4,28), (4, 27)]
        bottom_right_coords = [(25,26), (25,27), (25,28), (26,28), (27,28), (28,28), (28,27), (28,26), (28,25), (27,25)]

        print(board_quadrant_corner)
        if (board_quadrant_corner == (1,1)) :
            next_step = top_left_coords[self.turn_num-1]
            friendly_unit.move(next_step)

        elif (board_quadrant_corner == (1, 28)):
            next_step = bottom_left_coords[self.turn_num - 1]
            friendly_unit.move(next_step)

        elif (board_quadrant_corner == (28, 28)):
            pass

        elif (board_quadrant_corner == (28, 1)):
            next_step = top_right_coords[self.turn_num - 1]
            friendly_unit.move(next_step)

        elif (board_quadrant_corner == (28, 28)):
            next_step = bottom_right_coords[self.turn_num - 1]
            friendly_unit.move(next_step)


    def do_move(self, world, friendly_unit, enemy_units):
        self.turn_num += 1
        if self.location_manager == None :
            self.location_manager = LocationManager(enemy_units, friendly_unit)

        if (self.turn_num < 11) :
            self.fill_corner(friendly_unit)
        elif friendly_unit.position in friendly_unit.territory and friendly_unit.position != self.location_manager.corner:
            friendly_unit.move(world.path.get_next_point_in_shortest_path(friendly_unit.position, self.location_manager.corner))
        else:
            friendly_unit.move(friendly_unit.position + (0,-1))

        



