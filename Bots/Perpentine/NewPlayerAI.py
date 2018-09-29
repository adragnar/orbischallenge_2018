"In-progress new AI for orbis"
from PythonClientAPI.game.PointUtils import *
from PythonClientAPI.game.Entities import FriendlyUnit, EnemyUnit, Tile
from PythonClientAPI.game.Enums import Team
from PythonClientAPI.game.World import World
from PythonClientAPI.game.TileUtils import TileUtils

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
