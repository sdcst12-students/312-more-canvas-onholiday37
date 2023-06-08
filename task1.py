import tkinter as tk
"""
Task 1
Read the map1.txt file and convert to a map that you can navigate a
rectangle object through.
"""
w = tk.Tk()
w.geometry("925x475")
w.attributes('-topmost',True)


c = tk.Canvas(height=475,width=900,bg="#ffdddd")
c.pack()
f = open('map1.txt')
map = []
walls = []


with open('map1.txt', 'r') as f:
    for y, line in enumerate(f):
        for x, char in enumerate(line.strip()):
            if char == '*':
                x1 = x * 20 + 5
                y1 = y * 20 + 5
                x2 = x1 + 20
                y2 = y1 + 20
                walls.append(c.create_rectangle(x1, y1, x2, y2, fill="#aa00aa"))
                map.append((x, y))

w.mainloop()