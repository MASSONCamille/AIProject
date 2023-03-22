from tkinter import *
from math import cos, sin, pi, sqrt

from model.HexCell import HexCell
from model.HexGrid import HexGrid


class HexDraw(Canvas):
    def __init__(self, master, side_length=50, **kwargs) -> None:
        super.__init__(master, **kwargs)
        self.side_l = side_length

    def draw_hexcell(self, cell: HexCell) -> None:
        pass

    def draw_hexgrid(self, grid: HexGrid) -> None:
        pass

    def coord_grid_to_pixel_pt(self, x: int, y: int) -> dict:
        x_center = self.winfo_width() / 2
        y_center = self.winfo_height() / 2
        width_size = (sqrt(3) * self.side_l) / 2

        x_coord = x_center + (2 * x * width_size) + (y * width_size)
        y_coord = y_center + ((3 / 2) * self.side_l * y)

        return {"x": x_coord, "y": y_coord}

    def hex_from_center_pt(self, x, y) -> list:
        points = []
        for i in range(0, 6):
            angle_rad = pi / 3 * (i + .5)
            x_p = x + self.side_length * cos(angle_rad)
            y_p = y + self.side_length * sin(angle_rad)
            points.extend([x_p, y_p])
        return points
