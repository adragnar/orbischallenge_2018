from PythonClientAPI.game.PointUtils import *
from PythonClientAPI.game.Entities import FriendlyUnit, EnemyUnit, Tile
from PythonClientAPI.game.Enums import Team
from PythonClientAPI.game.World import World
from PythonClientAPI.game.TileUtils import TileUtils


class PlayerAI:

    def __init__(self):
        self.turn_num = 0

    def fill_corner(self, friendly_unit) -> tuple:
        '''Fill the 16 squares in snake corner when starting the game. Executes move'''
        def horz_flip(tuple_list) :
            tuple_list = copy.deepcopy(tuple_list)
            for entry in tuple_list :
                entry.first = -1 * entry.first
            return tuple_list

        def vert_flip(tuple_list):
            tuple_list = copy.deepcopy(tuple_list)
            for entry in tuple_list:
                entry.second = -1 * entry.second
            return tuple_list

        board_quadrant_corner = self.location_manager.get_my_board_quadrant()  #t_left corner
        move_coords = [[(1,0), (0,1), (0,1), (-1,0), (-1,0), (-1,0), (0,-1), (0,-1), (0,-1), (0,-1)]] #All hardcoded move combos for each corner from (0,0) CW

        quad_1_coords = move_coords
        quad_2_coords = horz_flip(move_coords)
        quad_3_coords = vert_flip(move_coords)
        quad_4_coords = vert_flip(horz_flip(move_coords))

        if (board_quadrant_corner == (1,1)) :
            friendly_unit.move((friendly_unit.position + quad_1_coords[self.turn_num-1]))

        if (board_quadrant_corner == (1, 28)):
            friendly_unit.move((friendly_unit.position + quad_2_coords[self.turn_num - 1]))

        if (board_quadrant_corner == (28, 28)):
            friendly_unit.move((friendly_unit.position + quad_3_coords[self.turn_num - 1]))

        if (board_quadrant_corner == (28, 1)):
            friendly_unit.move((friendly_unit.position + quad_4_coords[self.turn_num - 1]))


    def do_move(self, world, friendly_unit, enemy_units):
        self.turn_num += 1
        if (self.turn_num < 10) :
            self.fill_corner(friendly_unit)
            return
        else:
            friendly_unit.move(friendly_unit.position + (0,-1))