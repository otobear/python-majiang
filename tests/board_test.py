import unittest

from majiang import *

pmn_file='tests/pmn_files/example_2.pmn'
board = Board(pmn_file)
class BoardTestCase(unittest.TestCase):
    def step1_init(self):
        self.assertEqual(board.is_valid, True)
        self.assertEqual(board.get_turn(), None)
        self.assertEqual(board.get_action(), None)
        self.assertEqual(board.get_private_tile_list(EAST), ['c7', 'd3', 'd4', 'd5', 'd6', 'd7', 'd7', 'b3', 'b6', 'b8', 'b9', 'w2', 'r1'])
        self.assertEqual(board.get_taken_tile(EAST), None)

    def step2_next_action(self):
        board.next_action(3)
        self.assertEqual(board.is_valid, True)
        self.assertEqual(board.get_turn(), SOUTH)
        self.assertEqual(board.get_action(), TAKE)
        self.assertEqual(board.get_private_tile_list(EAST), ['c7', 'd3', 'd4', 'd5', 'd6', 'd7', 'd7', 'b3', 'b6', 'b8', 'b9', 'w2', 'r2'])
        self.assertEqual(board.get_taken_tile(EAST), None)
        self.assertEqual(str(board.get_discarded_tile()), 'r1')

    def step3_prev_action(self):
        board.prev_action(2)
        self.assertEqual(board.is_valid, True)
        self.assertEqual(board.get_turn(), EAST)
        self.assertEqual(board.get_action(), TAKE)
        self.assertEqual(board.get_private_tile_list(EAST), ['c7', 'd3', 'd4', 'd5', 'd6', 'd7', 'd7', 'b3', 'b6', 'b8', 'b9', 'w2', 'r1'])
        self.assertEqual(str(board.get_taken_tile(EAST)), 'r2')

    def step4_to_first_action(self):
        board.to_first_action()
        self.assertEqual(board.is_valid, True)
        self.assertEqual(board.get_turn(), None)
        self.assertEqual(board.get_action(), None)
        self.assertEqual(board.get_private_tile_list(EAST), ['c7', 'd3', 'd4', 'd5', 'd6', 'd7', 'd7', 'b3', 'b6', 'b8', 'b9', 'w2', 'r1'])
        self.assertEqual(board.get_taken_tile(EAST), None)

    def step5_to_last_action(self):
        board.to_last_action()
        self.assertEqual(board.is_valid, True)
        self.assertEqual(board.get_turn(), SOUTH)
        self.assertEqual(board.get_action(), HU)
        self.assertEqual(board.get_private_tile_list(SOUTH), ['c7', 'c8', 'c9', 'd1', 'd2', 'd5', 'd5', 'd8', 'd8', 'd8', 'b4', 'b5', 'b6'])
        self.assertEqual(board.get_private_tile_list(NORTH), ['c4', 'c5', 'c6', 'd1', 'd2', 'b8', 'b8'])
        self.assertEqual(board.get_meld_tile_list(NORTH), [['b8', 'b7', 'b9'], ['d8', 'd7', 'd9']])
        self.assertEqual(board.get_discard_tile_list(SOUTH), ['r2', 'r1', 'r3', 'w1', 'w2', 'w1', 'd7', 'b5', 'w1', 'c6'])
        fans = [39, 62, 76, 77, 39, 63, 70, 77]
        self.assertEqual(board.get_fan(), [[], [(fans[0], 8, 1), (fans[1], 2, 1), (fans[2], 1, 1), (fans[3], 1, 1)], [], [(fans[4], 8, 1), (fans[5], 2, 1), (fans[6], 1, 1), (fans[7], 1, 1)]])
        self.assertEqual(board.get_fan_zh(), [
            [],
            [(FAN_NAME_ZH[fans[0] - 1], 8, 1), (FAN_NAME_ZH[fans[1] - 1], 2, 1), (FAN_NAME_ZH[fans[2] - 1], 1, 1), (FAN_NAME_ZH[fans[3] - 1], 1, 1)],
            [],
            [(FAN_NAME_ZH[fans[4] - 1], 8, 1), (FAN_NAME_ZH[fans[5] - 1], 2, 1), (FAN_NAME_ZH[fans[6] - 1], 1, 1), (FAN_NAME_ZH[fans[7] - 1], 1, 1)]
        ])
        self.assertEqual(board.is_end(), True)
        self.assertEqual(board.get_starting(), [0, 0, 0, 0])
        self.assertEqual(board.get_result(), [-32, 36, -8, 36])
        self.assertEqual(board.get_penalty(), [0, 0, 0, 0])

    def _steps(self):
        for name in dir(self):
            if name.startswith('step'):
                yield name, getattr(self, name)

    def test_steps(self):
        for name, step in self._steps():
            step()

if __name__ == '__main__':
    unittest.main()
