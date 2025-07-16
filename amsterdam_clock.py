import tkinter as tk
import math
import pytz
from datetime import datetime
import time

# Set up Amsterdam timezone
timezone = pytz.timezone('Europe/Amsterdam')

WIDTH = 400
HEIGHT = 450
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2 - 25
CLOCK_RADIUS = 180

class Clock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Amsterdam Clock (Analog & Digital)")
        self.resizable(False, False)
        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGHT, bg='white')
        self.canvas.pack()
        self.digital_label = tk.Label(self, font=("Arial", 24), bg='white')
        self.digital_label.place(x=0, y=HEIGHT-50, width=WIDTH, height=50)
        self.draw_clock_face()
        self.update_clock()

    def draw_clock_face(self):
        # Draw the outer circle
        self.canvas.create_oval(CENTER_X - CLOCK_RADIUS, CENTER_Y - CLOCK_RADIUS,
                                CENTER_X + CLOCK_RADIUS, CENTER_Y + CLOCK_RADIUS, width=4)
        # Draw hour marks
        for i in range(12):
            angle = math.radians(i * 30 - 90)
            x1 = CENTER_X + (CLOCK_RADIUS - 20) * math.cos(angle)
            y1 = CENTER_Y + (CLOCK_RADIUS - 20) * math.sin(angle)
            x2 = CENTER_X + (CLOCK_RADIUS - 5) * math.cos(angle)
            y2 = CENTER_Y + (CLOCK_RADIUS - 5) * math.sin(angle)
            self.canvas.create_line(x1, y1, x2, y2, width=3)
            # Draw numbers
            num_x = CENTER_X + (CLOCK_RADIUS - 40) * math.cos(angle)
            num_y = CENTER_Y + (CLOCK_RADIUS - 40) * math.sin(angle)
            self.canvas.create_text(num_x, num_y, text=str(i if i != 0 else 12), font=("Arial", 16, "bold"))

    def update_clock(self):
        self.canvas.delete("hands")
        now = datetime.now(timezone)
        hour = now.hour % 12
        minute = now.minute
        second = now.second

        # Digital clock
        self.digital_label.config(text=now.strftime("%H:%M:%S"))

        # Angles for hands
        sec_angle = math.radians(second * 6 - 90)
        min_angle = math.radians(minute * 6 + second * 0.1 - 90)
        hour_angle = math.radians((hour * 30) + (minute * 0.5) - 90)

        # Second hand
        sec_x = CENTER_X + (CLOCK_RADIUS - 40) * math.cos(sec_angle)
        sec_y = CENTER_Y + (CLOCK_RADIUS - 40) * math.sin(sec_angle)
        self.canvas.create_line(CENTER_X, CENTER_Y, sec_x, sec_y, fill='red', width=2, tags="hands")

        # Minute hand
        min_x = CENTER_X + (CLOCK_RADIUS - 60) * math.cos(min_angle)
        min_y = CENTER_Y + (CLOCK_RADIUS - 60) * math.sin(min_angle)
        self.canvas.create_line(CENTER_X, CENTER_Y, min_x, min_y, fill='blue', width=4, tags="hands")

        # Hour hand
        hour_x = CENTER_X + (CLOCK_RADIUS - 100) * math.cos(hour_angle)
        hour_y = CENTER_Y + (CLOCK_RADIUS - 100) * math.sin(hour_angle)
        self.canvas.create_line(CENTER_X, CENTER_Y, hour_x, hour_y, fill='black', width=6, tags="hands")

        # Center dot
        self.canvas.create_oval(CENTER_X-8, CENTER_Y-8, CENTER_X+8, CENTER_Y+8, fill='black', tags="hands")

        self.after(1000, self.update_clock)

if __name__ == "__main__":
    app = Clock()
    app.mainloop() 