import unittest

from majiang.consts import *
from majiang.game_tile_manager import *

game_tile_manager = GameTileManager()

class GameTileManagerTestCase(unittest.TestCase):

    def step1_init(self):
        self.assertEqual(game_tile_manager.deck_tile.tile_num(), TOTAL_TILE_NUM)
        for player in SEATS:
            self.assertEqual(game_tile_manager.discard_tile[player].tile_num(), 0)
            self.assertEqual(game_tile_manager.private_tile[player].tile_num(), 0)
            self.assertEqual(len(game_tile_manager.meld_tile[player]), 0)

    def step2_take(self):
        game_tile_manager.take(EAST, Tile('c1'))
        self.assertEqual(game_tile_manager.deck_tile.tile_num(), TOTAL_TILE_NUM - 1)
        self.assertEqual(str(game_tile_manager.private_tile[EAST].taken_tile), 'c1')
        self.assertEqual(game_tile_manager.private_tile[EAST].tile_num(), 0)

    def step3_discard(self):
        game_tile_manager.take(EAST, Tile('c1'))
        game_tile_manager.take(EAST, Tile('c1'))
        game_tile_manager.take(EAST, Tile('c2'))
        game_tile_manager.discard(EAST, Tile('c1'))
        self.assertEqual(game_tile_manager.deck_tile.tile_num(), TOTAL_TILE_NUM - 4)
        self.assertEqual(game_tile_manager.private_tile[EAST].tile_num(), 3)

    def _steps(self):
        for name in dir(self):
            if name.startswith('step'):
                yield name, getattr(self, name)

    def test_steps(self):
        for name, step in self._steps():
            step()

if __name__ == '__main__':
    unittest.main()
