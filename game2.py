import tkinter as tk
import random

class CircularMatrixGame:
    def __init__(self, root):
        self.root = root
        self.input_window = tk.Toplevel(self.root)
        self.input_window.title("Enter dimensions")

        tk.Label(self.input_window, text="Enter dimensions (max 20x20):").pack()

        self.n_entry = tk.Entry(self.input_window)
        self.n_entry.pack()
        self.m_entry = tk.Entry(self.input_window)
        self.m_entry.pack()

        tk.Button(self.input_window, text="Start game", command=self.start_game).pack()

    def start_game(self):
        try:
            n = int(self.n_entry.get())
            m = int(self.m_entry.get())
            if n < 1 or n > 20 or m < 1 or m > 20:
                raise ValueError
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid dimensions")
            return

        self.input_window.destroy()

        self.n = n
        self.m = m
        self.matrix = [[0 for _ in range(m)] for _ in range(n)]
        self.current_x = random.randint(0, n - 1)
        self.current_y = random.randint(0, m - 1)
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Define color palette
        self.color_palette = ["white", "lightblue", "blue", "darkblue", "purple", "magenta", "pink", "red", "orange", "yellow"]

        self.create_ui()

    def create_ui(self):
        self.canvas = tk.Canvas(self.root, width=self.n * 50, height=self.m * 50)
        self.canvas.pack()

        self.update_canvas()

        self.menu = tk.Frame(self.root)
        self.menu.pack(side=tk.RIGHT, padx=20)

        for direction in ["Arriba", "Abajo", "Izquierda", "Derecha"]:
            button = tk.Button(self.menu, text=direction, command=lambda dir=direction: (lambda: self.move(dir))())
            button.pack()

    def move(self, direction):
        direction_index = {"Arriba": 3, "Abajo": 1, "Izquierda": 2, "Derecha": 0}[direction]
        dx, dy = self.directions[direction_index]

        # Update current cell and neighbors
        for i in range(-1, 2):
            for j in range(-1, 2):
                x = (self.current_x + i) % self.n
                y = (self.current_y + j) % self.m
                self.matrix[x][y] = (self.matrix[x][y] + 1) % 10

        # Move to next cell
        self.current_x = (self.current_x + dx) % self.n
        self.current_y = (self.current_y + dy) % self.m

        # Update canvas
        self.update_canvas()

    def update_canvas(self):
        self.canvas.delete("all")

        for i in range(self.n):
            for j in range(self.m):
                value = self.matrix[i][j]
                color = self.color_palette[value]
                text_color = "white" if value >= 5 else "black"
                self.canvas.create_rectangle(j * 50, i * 50, (j + 1) * 50, (i + 1) * 50, fill=color)
                self.canvas.create_text(j * 50 + 25, i * 50 + 25, text=str(value), fill=text_color)

root = tk.Tk()
game = CircularMatrixGame(root)
root.mainloop()
