import tkinter as tk

"""
Task 2
Read the map2.txt file and convert to a map that you can navigate a
rectangle object through. Use images for your map.
You will want to make sure that your rectangle is above the map tiles
Legend:
0 Water
1 Plains
2 Forest
3 Hills
4 Mountains
5 Swamp
6 City
"""
w = tk.Tk()
w.geometry("325x355")
w.attributes('-topmost',True)
c = tk.Canvas(height=475,width=900,bg="#ffffff")
c.pack()

sprite = tk.PhotoImage(file="assets/sprite.png")
player = c.create_image(30,30, image = sprite)

def move(x, y):
    c.move(char, x, y)

# This dictionary stores the current pressed status of the (← ↑ → ↓) keys
# (pressed: True, released: False) and will be modified by Pressing or Releasing each key
pressedStatus = {"Up": False, "Down": False, "Left": False, "Right": False}

def pressed(event):
    # When the key "event.keysym" is pressed, set its pressed status to True
    pressedStatus[event.keysym] = True

def released(event):
    # When the key "event.keysym" is released, set its pressed status to False
    pressedStatus[event.keysym] = False

def set_bindings():
    # Bind the (← ↑ → ↓) keys's Press and Release events
    for player in ["Up", "Down", "Left", "Right"]:
        w.bind("<KeyPress-%s>" % player, pressed)
        w.bind("<KeyRelease-%s>" % player, released)


def keyPress(e):
    print(e)
    print(e.keycode, e.keysym, e.x, e.y)

def animate():
    # For each of the (← ↑ → ↓) keys currently being pressed (if pressedStatus[key] = True)
    # move in the corresponding direction
    if pressedStatus["Up"] == True: 
        x1, y1= c.coords(player)
        if y1 - 15 >= 0:
            c.move(player, 0, -5)


    if pressedStatus["Down"] == True: 
        x2, y2 = c.coords(player)
        if y2 + 15 <= c.winfo_height():
            c.move(player, 0, 5)

    if pressedStatus["Left"] == True:
        x1, y1 = c.coords(player)
        if x1 - 15 >= 0:
            c.move(player, -5, 0)

    if pressedStatus["Right"] == True:
        x2, y2 = c.coords(player)
        if x2 + 15 <= c.winfo_width():
            c.move(player, 5, 0)

    c.update()
    
    # This method calls itself again and again after a delay (80 ms in this case)
    w.after(80, animate)



set_bindings()
animate()




map = []

water = []
waterImg = tk.PhotoImage(file="assets/map.water.png")
with open('map2.txt', 'r') as f:
    for y, line in enumerate(f):
        for x, char in enumerate(line.strip()):
            if char == "0":
                x1 = x * 30
                y1 = y * 30
                x2 = x1 + 30
                y2 = y1 + 30
                water.append(c.create_image(x2, y2, image = waterImg))
                map.append((x, y))
    


plains = []
plains = tk.PhotoImage(file="assets/map.plains.png")
with open('map2.txt', 'r') as f:
    for y, line in enumerate(f):
        for x, char in enumerate(line.strip()):
            if char == "1":
                x1 = x * 30
                y1 = y * 30
                x2 = x1 + 30
                y2 = y1 + 30
                water.append(c.create_image(x2, y2, image = plains))
                map.append((x, y))

forest = []
forest = tk.PhotoImage(file="assets/map.forest.png")
with open('map2.txt', 'r') as f:
    for y, line in enumerate(f):
        for x, char in enumerate(line.strip()):
            if char == "2":
                x1 = x * 30
                y1 = y * 30
                x2 = x1 + 30
                y2 = y1 + 30
                water.append(c.create_image(x2, y2, image = forest))
                map.append((x, y))


hills = []
hills = tk.PhotoImage(file="assets/map.hills.png")
with open('map2.txt', 'r') as f:
    for y, line in enumerate(f):
        for x, char in enumerate(line.strip()):
            if char == "3":
                x1 = x * 30
                y1 = y * 30
                x2 = x1 + 30
                y2 = y1 + 30
                water.append(c.create_image(x2, y2, image = hills))
                map.append((x, y))



mountain = []
mountain = tk.PhotoImage(file="assets/map.mountain.png")
with open('map2.txt', 'r') as f:
    for y, line in enumerate(f):
        for x, char in enumerate(line.strip()):
            if char == "4":
                x1 = x * 30
                y1 = y * 30
                x2 = x1 + 30
                y2 = y1 + 30
                water.append(c.create_image(x2, y2, image = mountain))
                map.append((x, y))

swamp = []
swamp = tk.PhotoImage(file="assets/map.swamp.png")
with open('map2.txt', 'r') as f:
    for y, line in enumerate(f):
        for x, char in enumerate(line.strip()):
            if char == "5":
                x1 = x * 30
                y1 = y * 30
                x2 = x1 + 30
                y2 = y1 + 30
                water.append(c.create_image(x2, y2, image = swamp))
                map.append((x, y))



city = []
city = tk.PhotoImage(file="assets/map.city.png")
with open('map2.txt', 'r') as f:
    for y, line in enumerate(f):
        for x, char in enumerate(line.strip()):
            if char == "6":
                x1 = x * 30
                y1 = y * 30
                x2 = x1 + 30
                y2 = y1 + 30
                water.append(c.create_image(x2, y2, image = city))
                map.append((x, y))

c.tag_raise(player)
w.mainloop()