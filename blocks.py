from block import Block
from position import Position


class LBlock(Block):
    def __init__(self):
        super().__init__(id=1)
        self.cells = {
            0: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],
            1: [Position(2, 1), Position(1, 1), Position(0, 1), Position(0, 0)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],
            3: [Position(1, 2), Position(1, 1), Position(1, 0), Position(0, 2)],
            4: [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)],
            5: [Position(2, 2), Position(2, 1), Position(1, 1), Position(0, 1)],
            6: [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)],
            7: [Position(2, 0), Position(1, 2), Position(1, 1), Position(1, 0)],
        }


class SBlock(Block):
    def __init__(self):
        super().__init__(id=2)
        self.cells = {
            0: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
            1: [Position(0, 2), Position(1, 2), Position(1, 1), Position(2, 1)],
            2: [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],
            3: [Position(1, 1), Position(1, 0), Position(2, 2), Position(2, 1)],
            4: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)],
            5: [Position(0, 1), Position(1, 1), Position(1, 0), Position(2, 0)],
            6: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
            7: [Position(0, 1), Position(0, 0), Position(1, 2), Position(1, 1)],
        }


class IBlock(Block):
    def __init__(self):
        super().__init__(id=3)
        self.cells = {
            0: [Position(0, 1), Position(1, 1), Position(2, 1)],
            1: [Position(0, 1), Position(1, 1), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2)],
            3: [Position(1, 0), Position(1, 1), Position(1, 2)],
            4: [Position(0, 1), Position(1, 1), Position(2, 1)],
            5: [Position(0, 1), Position(1, 1), Position(2, 1)],
            6: [Position(1, 0), Position(1, 1), Position(1, 2)],
            7: [Position(1, 0), Position(1, 1), Position(1, 2)],
        }


class DBlock(Block):
    def __init__(self):
        super().__init__(id=4)
        self.cells = {
            0: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)],
            1: [Position(2, 1), Position(1, 1), Position(1, 0), Position(0, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
            3: [Position(1, 2), Position(1, 1), Position(1, 0), Position(0, 1)],
            4: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)],
            5: [Position(2, 1), Position(1, 2), Position(1, 1), Position(0, 1)],
            6: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],
            7: [Position(2, 1), Position(1, 2), Position(1, 1), Position(1, 0)],
        }
