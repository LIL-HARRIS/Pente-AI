import tkinter as tk
import customtkinter as ctk

BOARD_SIZE = 19
spacing = 650/18
game_board = [
    [None for _ in range(BOARD_SIZE)]
    for _ in range(BOARD_SIZE)
]

# ---- Theme colors (edit these to restyle everything) ----
BG_DARK   = "#1E1E2E"   # window / frames
BG_PANEL  = "#302F42"   # label + button panels
BG_HOVER  = "#44435C"   # button hover
ACCENT    = "#F5C26B"   # title color
BOARD_BG  = "#DEB887"   # board wood color
GRID_COL  = "#5C4033"   # grid lines

window = tk.Tk()
window.title("Pente AI")
window.geometry("1000x750")
window.configure(bg=BG_DARK)
window.resizable(False, False)

board_frame = tk.Frame(window, bg=BG_DARK)
control_frame = tk.Frame(window, bg=BG_DARK,    
                        highlightthickness=2,          # border width
                        highlightbackground=ACCENT,    # border color
                        highlightcolor=ACCENT)

title = tk.Label(
    control_frame,
    text="PENTE AI",
    font=("Arial", 24, "bold"),
    bg=BG_DARK,
    fg=ACCENT
)

turn_label = ctk.CTkLabel(
    control_frame, text="White's Turn",
    font=("Arial", 14, "bold"),
    fg_color="#EDEDED", text_color=BG_DARK,
    corner_radius=18, height=56
)

white_captured_label = ctk.CTkLabel(
    control_frame, text="White Captured: 0",
    font=("Arial", 14, "bold"),
    fg_color=BG_PANEL, text_color="white",
    corner_radius=18, height=56
)

black_captured_label = ctk.CTkLabel(
    control_frame, text="Black Captured: 0",
    font=("Arial", 14, "bold"),
    fg_color=BG_PANEL, text_color="white",
    corner_radius=18, height=56
)


board = tk.Canvas(
    board_frame,
    width=650,
    height=650,
    bg=BOARD_BG,
    highlightthickness=2,
    highlightbackground="#8B5A2B"
)


board_frame.pack(side="left")
control_frame.pack(side="right")
title.pack(pady=25)
turn_label.pack(pady=20, padx=15, fill="x")
black_captured_label.pack(pady=10, padx=15, fill="x")
white_captured_label.pack(pady=10, padx=15, fill="x")

board_frame.configure(width=700, height=700)
control_frame.configure(width=250, height=700)
board_frame.pack_propagate(False)
control_frame.pack_propagate(False)


for i in range(19):
    board.create_line(0, i*spacing, 650, i*spacing, fill=GRID_COL, width=1)
    board.create_line(i*spacing, 0, i*spacing, 650, fill=GRID_COL, width=1)

board.pack(padx=25, pady=25)



def handle_board_click(event):
    row, column = get_board_position(event)

    # Send the move to game logic here
    # Receive the result

    # If the move is valid:
    # draw_stone(row, column, player)
    pass

def get_board_position(event):
    column = round(event.x / spacing)
    row =  round(event.y / spacing)
    return row,column

def draw_stone(row, column, player):
    x = column * spacing
    y = row * spacing
    if (player == "white"):
        board.create_oval(
            x-12,
            y-12,
            x+12,
            y+12,
            fill="white",
            outline="#333333",
            width = 2,
            tags="stone")
    else:
        board.create_oval(
            x-12,
            y-12,
            x+12,
            y+12,
            fill="black",
            outline="#333333",
            width = 2,
            tags="stone")


def update_turn_indicator(player):
    if player == "white":
        turn_label.configure(text="White's Turn", fg_color="#EDEDED", text_color=BG_DARK)
    elif player == "black":
        turn_label.configure(text="Black's Turn", fg_color="black", text_color="white")

def update_captured_stones(player, count):
    if player == "white":
        white_captured_label.configure(text=f"White Captured: {count}")
    elif player == "black":
        black_captured_label.configure(text=f"Black Captured: {count}")

def reset_board():
    board.delete("stone")

    update_turn_indicator("white")
    update_captured_stones("white", 0)
    update_captured_stones("black", 0)

reset_btn = ctk.CTkButton(
    control_frame, text="Reset the board", command=reset_board,
    font=("Arial", 12, "bold"),
    fg_color=BG_PANEL, hover_color=BG_HOVER, text_color="white",
    corner_radius=14, height=44
)

reset_btn.pack(pady=20, padx=15, fill="x")

board.bind("<Button-1>",handle_board_click)
window.mainloop()