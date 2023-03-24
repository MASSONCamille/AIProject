from tkinter import *
from model.HexCell import HexCell, CellType
from model.HexGrid import HexGrid
from view.HexDraw import HexDraw

if __name__ == '__main__':
    grid = HexGrid(10, 10)

    root = Tk()

    canvas = HexDraw(master=root, modele=grid, width=500, height=500)
    canvas.pack()

    root.update()

    canvas.refresh()

    root.mainloop()

