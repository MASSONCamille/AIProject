from datetime import time
from tkinter import *
from math import cos, sin, pi, sqrt

from model.HexCell import HexCell
from model.HexGrid import HexGrid
from model.pathfinding.AstarNode import get_path_Astar


class HexDraw(Canvas):
    _tag_delimiter = ";"
    _selected_color = "green"
    _path_color = "#C64343"

    def __init__(self, master, modele: HexGrid, side_length=25, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.side_l = side_length
        self.modele = modele

        self.is_init = False
        self.selected_cells: list[int] = []
        self.path_cells: list[int] = []

        self.bind("<Button-1>", self.l_click)
        self.bind("<Button-2>", self.m_click)
        self.bind("<Button-3>", self.r_click)

    def draw_hexgrid(self) -> None:
        for cell in self.modele.celllist:
            self.create_polygon(
                self.hex_from_center_pt(**(self.coord_grid_to_pixel_pt(cell.x, cell.y))),
                fill=cell.getColor(),
                outline='black',
                width=1,
                tags=self.tag_from_coord(cell.x, cell.y),
            )

    def resetColor(self) -> None:
        self.selected_cells: list[HexCell] = []
        self.path_cells: list[HexCell] = []
        self.refresh()

    def refresh(self) -> None:
        if not self.is_init:
            self.draw_hexgrid()
            self.is_init = True

        for cell in self.modele.celllist:
            self.itemconfigure(
                self.get_id_from_coord(cell.x, cell.y),
                fill=cell.getColor(),
                outline='black',
                width=1,
            )

        self.path_cells = []
        if len(self.selected_cells) == 2:
            celllist = get_path_Astar(
                grid=self.modele,
                start=self.modele.get_cell_from_coord(**self.get_coord_from_id(self.selected_cells[0])),
                objectif=self.modele.get_cell_from_coord(**self.get_coord_from_id(self.selected_cells[1])),
            )
            if celllist is not None:
                for cell in celllist:
                    self.path_cells.append(self.get_id_from_coord(cell.x, cell.y))

        self.paint_cell_list(self.path_cells, self._path_color, mode=1)
        self.paint_cell_list(self.selected_cells, self._selected_color, mode=1)

    def paint_cell_list(self, cells: list[int], color: str, mode=0) -> None:
        if mode == 0:
            for cell in cells:
                self.itemconfigure(cell, fill=color)
        if mode == 1:
            for cell in cells:
                self.itemconfigure(cell, outline=color, width=2.5)

    # -------------------------------------------------
    # fonctions pour passer des case-modele au case-vue

    def coord_grid_to_pixel_pt(self, x: int, y: int) -> dict:
        # x_center = self.winfo_width() / 2
        # y_center = self.winfo_height() / 2
        x_center = 0
        y_center = 0
        width_size = (sqrt(3) * self.side_l) / 2

        x_coord = x_center + (2 * x * width_size) + (y * width_size)
        y_coord = y_center + ((3 / 2) * self.side_l * y)

        return {"x": x_coord, "y": y_coord}

    def hex_from_center_pt(self, x, y) -> list:
        points = []
        for i in range(0, 6):
            angle_rad = pi / 3 * (i + .5)
            x_p = x + self.side_l * cos(angle_rad)
            y_p = y + self.side_l * sin(angle_rad)
            points.extend([x_p, y_p])
        return points

    def tag_from_coord(self, x: int, y: int) -> str:
        return str(x) + self._tag_delimiter + str(y)

    def tag_to_coord(self, tags: str) -> dict:
        sep = tags.split(self._tag_delimiter)
        return {"x": int(sep[0]), "y": int(sep[1])}

    def get_id_from_coord(self, x, y) -> int:
        return int(self.find_withtag(self.tag_from_coord(x, y))[0])

    def get_coord_from_id(self, id) -> dict:
        return self.tag_to_coord(self.gettags(id)[0])

    # --------------------------
    # fonctions appeler au click

    def l_click(self, evt):  # left click
        clicked = int(self.find_closest(evt.x, evt.y)[0])

        if clicked in self.selected_cells:
            self.selected_cells.remove(clicked)

        elif self.modele.get_cell_from_coord(**self.get_coord_from_id(clicked)).isWalkable():
            if len(self.selected_cells) == 2:
                self.selected_cells.pop(0)
            self.selected_cells.append(clicked)

        self.refresh()

    def r_click(self, evt):  # right click
        clicked = int(self.find_closest(evt.x, evt.y)[0])

        if clicked not in self.selected_cells:
            cell = self.modele.get_cell_from_coord(**(self.tag_to_coord(self.gettags(clicked)[0])))
            cell.ctype = cell.ctype.get_next_cell_type()

        self.refresh()

    def m_click(self, evt):  # middle click
        clicked = int(self.find_closest(evt.x, evt.y)[0])

        print(self.modele.get_cell_from_coord(**(self.tag_to_coord(self.gettags(clicked)[0]))))

        self.resetColor()
