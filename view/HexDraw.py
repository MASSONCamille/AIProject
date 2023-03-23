from tkinter import *
from math import cos, sin, pi, sqrt

from model.HexCell import HexCell
from model.HexGrid import HexGrid


class HexDraw(Canvas):
    _tag_delimiter = ";"

    def __init__(self, master, side_length=50, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.side_l = side_length

        self.bind("<Button-1>", self.__lclick)
        self.bind("<Button-3>", self.__rclick)

    def __draw_hexcell(self, cell: HexCell) -> None:
        self.create_polygon(
            self.__hex_from_center_pt(**(self.__coord_grid_to_pixel_pt(cell.x, cell.y))),
            fill=cell.getColor(),
            outline='black',
            width=1,
            tags=self.__tag_from_coord(cell.x, cell.y),
        )

    def init_draw_hexgrid(self, grid: HexGrid) -> None:
        for celllist in grid.celllist:
            for cell in celllist:
                self.__draw_hexcell(cell)

    def __coord_grid_to_pixel_pt(self, x: int, y: int) -> dict:
        x_center = self.winfo_width() / 2
        y_center = self.winfo_height() / 2
        width_size = (sqrt(3) * self.side_l) / 2

        x_coord = x_center + (2 * x * width_size) + (y * width_size)
        y_coord = y_center + ((3 / 2) * self.side_l * y)

        return {"x": x_coord, "y": y_coord}

    def __hex_from_center_pt(self, x, y) -> list:
        points = []
        for i in range(0, 6):
            angle_rad = pi / 3 * (i + .5)
            x_p = x + self.side_l * cos(angle_rad)
            y_p = y + self.side_l * sin(angle_rad)
            points.extend([x_p, y_p])
        return points

    def __tag_from_coord(self, x:int, y:int) -> str:
        return str(x) + self._tag_delimiter + str(y)

    def __tag_to_coord(self, tags:str) -> dict:
        sep = tags.split(self._tag_delimiter)
        return {"x": int(sep[0]), "y": int(sep[1])}

    def __lclick(self, evt):
        clicked = int(self.find_closest(evt.x, evt.y)[0])
        self.itemconfigure(clicked, fill="#6666CD")
        print(self.__tag_to_coord(self.gettags(clicked)[0]))


    def __rclick(self, evt):
        print("test r")
