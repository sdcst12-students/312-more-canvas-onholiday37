import tkinter as tk
from PIL import Image, ImageTk

w = tk.Tk()
w.attributes("-topmost", True)
w.geometry("400x300")

c = tk.Canvas(width=380, height=280)
c.pack()

def getSprite(x, y):
    # pngegg.png sprite sheet is 560 x 576 pixels, with 4 across and 4 down.
    # each image is 140 x 144 pixels    
    img = Image.open("assets/pngegg.png").convert("RGBA")
    xi = x * 140
    yi = y * 144
    img2 = img.crop([xi, yi, xi + 140, yi + 144])
    return ImageTk.PhotoImage(img2)    

def eggUpdate():
    global i
    i += 1
    i %= len(egg)
    c.itemconfig(img, image=egg[i])
    w.after(200, eggUpdate)

x = 0
y = 0
egg = []
# There are 4 sprite images:
# left foot forward
# neutral
# right foot forward
# we load all 4 sprites and then also add in the neutral as a 4th sprite
for i in range(4):
    firstX = i + 4 * x  # there are 4 sprites in an animation
    egg.append(getSprite(firstX, y))
egg.append(getSprite(firstX - 1, y))

img = c.create_image(140, 144, image=egg[0])
w.after(100, eggUpdate)

def animate():
    # For each of the (← ↑ → ↓) keys currently being pressed (if pressedStatus[key] = True)
    # move in the corresponding direction
    if pressedStatus["Up"]:
        _, y1 = c.coords(img)
        if y1 - 15 >= 0:
            c.move(img, 0, -15)
            x = 0
            y = 3
            egg.clear()
            for i in range(4):
                firstX = i + 4 * x  # there are 4 sprites in an animation
                egg.append(getSprite(firstX, y))

    if pressedStatus["Down"]:
        _, y2 = c.coords(img)
        if y2 + 15 <= c.winfo_height():
            c.move(img, 0, 15)
            y = 0
            x = 0
            egg.clear()
            for i in range(4):
                firstX = i + 4 * x  # there are 4 sprites in an animation
                egg.append(getSprite(firstX, y))

    if pressedStatus["Left"]:
        x1, _ = c.coords(img)
        if x1 - 15 >= 0:
            c.move(img, -15, 0)
            y = 1
            x = 0
            egg.clear()
            for i in range(4):
                firstX = i + 4 * x  # there are 4 sprites in an animation
                egg.append(getSprite(firstX, y))

    if pressedStatus["Right"]:
        x2, _ = c.coords(img)
        if x2 + 15 <= c.winfo_width():
            c.move(img, 15, 0)
            y = 2
            x = 0
            egg.clear()
            for i in range(4):
                firstX = i + 4 * x  # there are 4 sprites in an animation
                egg.append(getSprite(firstX, y))

    c.update()
    # This method calls itself again and again after a delay (80 ms in this case)
    w.after(400, animate)

# This dictionary stores the current pressed status of the (← ↑ → ↓) keys
# (pressed: True, released: False) and will be modified by pressing or releasing each key
pressedStatus = {"Up": False, "Down": False, "Left": False, "Right": False}

def pressed(event):
    # When the key "event.keysym" is pressed, set its pressed status to True
    pressedStatus[event.keysym] = True

def released(event):
    # When the key "event.keysym" is released, set its pressed status to False
    pressedStatus[event.keysym] = False

# Bind the (← ↑ → ↓) keys' Press and Release events
for player in ["Up", "Down", "Left", "Right"]:
    w.bind("<KeyPress-%s>" % player, pressed)
    w.bind("<KeyRelease-%s>" % player, released)

animate()
w.mainloop()