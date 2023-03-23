from tkinter import *
import math

class HexagonGridCanvas(Canvas):
    def __init__(self, master, side_length=50, rows=5, cols=5, **kwargs):
        super().__init__(master, **kwargs)
        self.side_length = side_length
        self.rows = rows
        self.cols = cols

    def axial_to_pixel(self, q, r):
        x = self.winfo_width() / 2 + self.side_length * math.sqrt(3) * (q + r/2) # Calcul des coordonnées x en utilisant les coordonnées axiales
        y = self.winfo_height() / 2 + self.side_length * 1.5 * r # Calcul des coordonnées y en utilisant les coordonnées axiales
        return x, y

    def draw_hexagon_grid(self):
        for q in range(-self.cols//2, self.cols//2+1):
            for r in range(-self.rows//2, self.rows//2+1):
                x_center, y_center = self.axial_to_pixel(q, r)
                points = []
                for i in range(6):
                    angle_rad = math.pi / 3 * (i + .5)
                    x = x_center + self.side_length * math.cos(angle_rad)
                    y = y_center + self.side_length * math.sin(angle_rad)
                    points.extend([x, y])
                self.create_polygon(points, fill='blue', outline='black', width=2)

if __name__ == '__main__':
    root = Tk()
    canvas = HexagonGridCanvas(root, side_length=30, rows=5, cols=5, width=500, height=500)
    canvas.pack()

    root.update()
    canvas.draw_hexagon_grid()

    root.mainloop()
