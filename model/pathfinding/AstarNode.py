from model.HexCell import HexCell
from model.HexGrid import HexGrid


class AstarNode:

    def heuristique(self) -> float:
        return self.cell.get_dist(self.objectif)

    def cout(self) -> float:
        if self.parent is None:
            return 0
        return self.parent.cout() + self.cell.getCostTime()

    h_funct = heuristique
    g_funct = cout

    def __init__(self, cell: HexCell, objectif: HexCell, parent=None) -> None:
        self.parent = parent
        self.cell = cell
        self.objectif = objectif

    def __eq__(self, o: object) -> bool:
        if o.__class__ is not self.__class__: return False
        o: AstarNode
        return (o.parent == self.parent) and (o.cell == self.cell)

    def getH(self) -> float:
        return self.h_funct()

    def getG(self) -> float:
        return self.g_funct()

    def getF(self) -> float:
        return self.h_funct() + self.g_funct()

def get_best_node(lstNode: list[AstarNode]) -> AstarNode

def get_path_Astar(grid: HexGrid, start: HexCell, objectif: HexCell) -> list[HexCell]:
    listOpen = []
    listClose = []

