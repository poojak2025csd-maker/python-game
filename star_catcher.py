import tkinter as tk
import random

W, H, SIZE = 500, 400, 24
root = tk.Tk()
root.title("STAR CATCHER")
root.resizable(False, False)
canvas = tk.Canvas(root, width=W, height=H, bg="#101827", highlightthickness=0)
canvas.pack()
score, lives, player_x = 0, 3, W // 2
stars, keys = [], set()
player_y = H - 45
game_over = False

def reset():
    global score, lives, player_x, stars, game_over
    score, lives, player_x, stars, game_over = 0, 3, W // 2, [], False
    draw()

def draw():
    canvas.delete("all")
    canvas.create_text(12, 12, anchor="nw", text=f"SCORE {score}   LIVES {lives}",
                       fill="white", font=("Arial", 14, "bold"))
    canvas.create_rectangle(player_x-35, player_y, player_x+35, player_y+14,
                            fill="#38bdf8", outline="")
    for x, y in stars:
        canvas.create_oval(x, y, x+SIZE, y+SIZE, fill="#facc15", outline="")
    if game_over:
        canvas.create_text(W//2, H//2, text=f"GAME OVER\nScore: {score}\nPress R to restart",
                           fill="white", font=("Arial", 22, "bold"), justify="center")

def move(e):
    global player_x
    if e.keysym == "Left": player_x = max(35, player_x-25)
    if e.keysym == "Right": player_x = min(W-35, player_x+25)

def tick():
    global score, lives, game_over
    if not game_over:
        if random.random() < 0.06: stars.append([random.randint(0, W-SIZE), -SIZE])
        for star in stars[:]:
            star[1] += 4
            x, y = star
            if y+SIZE >= player_y and y <= player_y+14 and x+SIZE >= player_x-35 and x <= player_x+35:
                stars.remove(star); score += 10
            elif y > H:
                stars.remove(star); lives -= 1
                if lives <= 0: game_over = True
        draw()
    root.after(35, tick)

root.bind("<Left>", move)
root.bind("<Right>", move)
root.bind("r", lambda e: reset())
root.bind("R", lambda e: reset())
draw()
tick()
root.mainloop()
