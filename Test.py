from model.HexCell import HexCell, CellType


def printlistcell(lst):
    if len(lst) == 0: print("vide")
    for i in lst:
        print(i)
    print()

if __name__ == '__main__':
    lst1 = [HexCell(0,0), HexCell(1,1)]
    a = lst1[0]
    b = lst1[1]
    lst2 = []
    printlistcell(lst1)
    printlistcell(lst2)
    print("_______________")


    lst1.remove(a)
    lst2.append(a)
    printlistcell(lst1)
    printlistcell(lst2)
    print("_______________")

    c = HexCell(0,0, ctype=CellType.WALL_G)
    print(c in lst1)
    print(c in lst2)
    print("_______________")

    d = lst1.pop(b)
    print(d)
    printlistcell(lst1)
    printlistcell(lst2)

