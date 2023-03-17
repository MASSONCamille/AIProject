from enum import Enum


class CellType(Enum):
    NEUTRAL_G = {"id": 1, "color": "#101010", "speed_coef": 1, "walkable": True}
    FLOOD_G = {"id": 2, "color": "#0000FF", "speed_coef": 0, "walkable": False}
    GRASS_G = {"id": 3, "color": "#00FF00", "speed_coef": 0.5, "walkable": True}


class HexCell:
    default_ct: CellType = CellType.NEUTRAL_G

    def __init__(self, x: int, y: int, ctype: CellType = default_ct) -> None:
        self.x = x
        self.y = y
        self.ctype = ctype

    def __eq__(self, o: object) -> bool:
        if o.__class__ is not self.__class__: return False
        o: HexCell
        if o.x != self.x or o.y != self.y: return False
        return True

    def __str__(self) -> str:
        return "x:{x} | y:{y} | ground:{g}".format(x=self.x, y=self.y, g=self.ctype.name)

    def getCostTime(self) -> float: # G function equivalent
        return 1. / self.ctype.value["speed_coef"]