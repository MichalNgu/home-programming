import tkinter as tk
import random

class SnakeGame(tk.Tk):
    def __init__(self, size=20):
        super().__init__()
        self.size = size
        self.title("Snake Game")
        self.canvas = tk.Canvas(self, width=size * 20, height=size * 20, bg="black")
        self.canvas.pack()
        self.snake = [(size // 2, size // 2)]
        self.food = self.generate_food()
        self.direction = "Right"
        self.bind("<Key>", self.change_direction)
        self.draw()

    def generate_food(self):
        while True:
            food = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
            if food not in self.snake:
                return food

    def draw(self):
        self.canvas.delete("all")
        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(x * 20, y * 20, x * 20 + 20, y * 20 + 20, fill="green")
        x, y = self.food
        self.canvas.create_oval(x * 20, y * 20, x * 20 + 20, y * 20 + 20, fill="red")
        self.move_snake()
        self.after(100, self.draw)

    def move_snake(self):
        x, y = self.snake[0]
        if self.direction == "Up":
            y -= 1
        elif self.direction == "Down":
            y += 1
        elif self.direction == "Left":
            x -= 1
        elif self.direction == "Right":
            x += 1
        if (x, y) == self.food:
            self.snake.append(self.snake[-1])
            self.food = self.generate_food()
        else:
            self.snake.pop()
        self.snake.insert(0, (x, y))

    def change_direction(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            if (event.keysym == "Up" and self.direction != "Down" or
                event.keysym == "Down" and self.direction != "Up" or
                event.keysym == "Left" and self.direction != "Right" or
                event.keysym == "Right" and self.direction != "Left"):
                self.direction = event.keysym

if __name__ == "__main__":
    game = SnakeGame()
    game.mainloop()
