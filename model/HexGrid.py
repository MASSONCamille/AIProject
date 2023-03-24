from enum import Enum

from model.HexCell import HexCell


class GridType(Enum):
    RECTANGLE = 1
    HEXAGON = 2
    RHOMBUS = 3


class HexGrid:
    default_gt = GridType.RHOMBUS

    def __init__(self, h: int, w: int, gtype: GridType = default_gt) -> None:
        self.height: int = h
        self.width: int = w
        self.gtype: GridType = gtype
        self.celllist: list[HexCell] = []
        self.initList()

    def initList(self) -> bool:
        if len(self.celllist) != 0:
            return False

        if self.gtype is GridType.RECTANGLE:
            pass

        elif self.gtype is GridType.RHOMBUS:
            for i in range(0, self.width):
                for j in range(0, self.height):
                    cell: HexCell = HexCell(i, j)
                    self.celllist.append(cell)

        elif self.gtype is GridType.HEXAGON:
            pass

        else:
            return False
        return True

    def __eq__(self, o: object) -> bool:
        if o.__class__ is not self.__class__: return False
        o: HexGrid
        if (self.width != o.width) or (self.height != o.height) or (self.gtype != o.gtype): return False
        return True

    def __str__(self) -> str:
        res = ""
        for sc in self.celllist:
            for c in sc:
                res += "{c}\n".format(c=c)
        return res

    def get_cell_from_coord(self, x: int, y: int) -> HexCell:
        return self.celllist[self.celllist.index(HexCell(x, y))]
