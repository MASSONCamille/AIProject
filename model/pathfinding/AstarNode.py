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
        return (o.cell == self.cell)

    def getH(self) -> float:
        return self.h_funct()

    def getG(self) -> float:
        return self.g_funct()

    def getF(self) -> float:
        return self.h_funct() + self.g_funct()

    def isBetterThat(self, o: object) -> bool:
        if self.__class__ != o.__class__: return True
        o: AstarNode
        if self.getF() < o.getF():
            return True
        elif self.getF() == o.getF():
            if self.getG() < o.getG():
                return True
        return False

    def get_cell_list(self) -> list[HexCell]:
        lstres: list[HexCell] = []
        lstres.append(self.cell)
        if self.parent is not None:
            lstres.extend(self.parent.get_cell_list())
        return lstres


def get_best_node(lstNode: list[AstarNode]) -> AstarNode:
    if len(lstNode) <= 0: return None
    best = lstNode[0]
    for node in lstNode:
        if node.isBetterThat(best):
            best = node
    return best

def find_equivalent_node(node: AstarNode, lstnode: list[AstarNode]) -> AstarNode:
    for n in lstnode:
        if n == node:
            return n
    return None

def get_path_Astar(grid: HexGrid, start: HexCell, objectif: HexCell) -> list[HexCell]:
    listOpen = []
    listClose = []


    listOpen.append(AstarNode(start, objectif))

    while len(listOpen) > 0:
        node = get_best_node(listOpen)

        if node.getH() == 0:
            print("trouver avec un cout de {f}".format(f=node.getF()))
            return node.get_cell_list()

        listOpen.remove(node)
        listClose.append(node)

        for cellson in grid.get_all_w_neighbours(node.cell):
            son = AstarNode(cellson, objectif, node)
            if son not in listClose:
                if son in listOpen:
                    concurent = find_equivalent_node(son, listOpen)
                    if son.isBetterThat(concurent):
                        listOpen.remove(concurent)
                        listOpen.append(son)
                else:
                    listOpen.append(son)
    return None


