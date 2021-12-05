class InvalidSign(Exception):
    pass
class InvalidCoordinate(Exception):
    pass
class PreoccupiedCell(Exception):
    pass

class GameStatus(Exception):
    def __init__(self, sign):
        self.sign = sign
class Victory(GameStatus):
    pass
class Draw(GameStatus):
    pass