from tkinter import *
from model.HexCell import HexCell, CellType
from model.HexGrid import HexGrid
from view.HexDraw import HexDraw

if __name__ == '__main__':
    grid = HexGrid(3,3)

    root = Tk()
    canvas = HexDraw(root, width=500, height=500)
    canvas.pack()
    root.update()

    canvas.init_draw_hexgrid(grid)

    root.mainloop()
