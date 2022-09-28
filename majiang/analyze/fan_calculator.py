"""MCR fan calculator.
"""

class AbstractFanCalculator(object):
    def __init__(self, board, player):
        self.board = board
        self.player = player

class MCRFanCalculator(AbstractFanCalculator):
    def __init__(self, board, player):
        super().__init__(board, player)
