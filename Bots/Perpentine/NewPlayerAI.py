"In-progress new AI for orbis"
from PythonClientAPI.game.PointUtils import *
from PythonClientAPI.game.Entities import FriendlyUnit, EnemyUnit, Tile
from PythonClientAPI.game.Enums import Team
from PythonClientAPI.game.World import World
from PythonClientAPI.game.TileUtils import TileUtils

class LocationManager:

    def __init__(self, enemy_positions, curr_position):
        self.enemy_positions = enemy_positions
        self.curr_position = curr_position
        if curr_position[0] <=14 and curr_position[1] <= 14:
            self.corner = (4,4)
        elif curr_position[0] <=14 and curr_position[1] > 14:
            self.corner = (4,25)
        elif curr_position[0] > 14 and curr_position[1] <= 14:
            self.corner = (25,4)
        elif curr_position[0] > 14 and curr_position[1] > 14:
            self.corner = (25, 25)

    def get_my_board_quadrant(self):
        if self.corner[0] <=14 and self.corner[1] <= 14:
            return (1, 1)
        elif self.corner[0] <=14 and self.corner[1] > 14:
            corner = (1, 28)
        elif self.corner[0] >14 and self.corner[1] <= 14:
            corner = (28,1)
        elif self.corner[0] >14 and self.corner[1] > 14:
            corner = (28, 28)

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

class PlayerAI:

    def __init__(self, location_manager):
        self.location_manager = location_manager

    def fill_corner(self, turn_num) -> tuple:
        '''Fill the 16 squares in snake corner when starting the game'''
        board_quadrant_corner = self.location_manager.get_my_board_quadrant()  #t_left corner
        my_territory = self.location_manager.get_my_territory
        if (board_quadrant_corner == (0,0)) :
            if (turn_num == 1):
                return(self.) #start at 3,3



        #get position from each of the corners
        #take min position and then expand in that direction


    def do_move(self, world, friendly_unit, enemy_units):
        pass
