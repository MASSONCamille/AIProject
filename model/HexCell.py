from enum import Enum


class CellType(Enum):
    NEUTRAL_G = {"id": 0, "color": "#E0E0EE", "speed_coef": 1, "walkable": True}
    WALL_G = {"id": 1, "color": "#353739", "speed_coef": 0, "walkable": False}
    GRASS_G = {"id": 2, "color": "#069869", "speed_coef": 0.5, "walkable": True}

    @classmethod
    def get_cell_type_by_id(cls, cell_type_id):
        for cell_type in cls:
            if cell_type.value["id"] == cell_type_id:
                return cell_type
        return None

    def get_next_cell_type(self):
        return CellType.get_cell_type_by_id(
            (self.value["id"] + 1) % len(CellType)
        )


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

    def getCostTime(self) -> float:  # G function equivalent
        return 1. / self.ctype.value["speed_coef"]

    def isWalkable(self) -> bool:
        return self.ctype.value["walkable"]

    def getColor(self) -> str:
        return self.ctype.value["color"]

    def get_dist(self, cell) -> float:
        cell: HexCell
        return (
                abs(self.x - cell.x)
                + abs(self.x + self.y - cell.x - cell.y)
                + abs(self.y - cell.y)
        ) / 2
