import ctypes
import os
import random
import string
import tkinter as tk
from tkinter import messagebox

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
BG_IMAGE_PATH = "C:\\pythonprojects\\labs\\lab3\\back.gif"
BG_MUSIC_PATH = "C:\\pythonprojects\\labs\\lab3\\тёмный_принц_отвратительный_король.mp3"


def play_background_music():
    music_dir = os.path.dirname(BG_MUSIC_PATH)
    supported_exts = (".mp3", ".wav")
    for file_name in os.listdir(music_dir):
        if file_name.lower().endswith(supported_exts):
            audio_path = os.path.join(music_dir, file_name)
            mci = ctypes.windll.winmm.mciSendStringW
            mci("close bgm", None, 0, 0)
            mci(f'open "{audio_path}" type mpegvideo alias bgm', None, 0, 0)
            mci("play bgm repeat", None, 0, 0)
            break


def generate_single_block():
    random_digit = random.choice(string.digits)
    random_letters = random.choices(string.ascii_uppercase, k=3)
    block_chars = [random_digit] + random_letters
    random.shuffle(block_chars)
    return "".join(block_chars)


def generate_full_key():
    key_blocks = [generate_single_block() for _ in range(4)]
    return "-".join(key_blocks)


def on_generate_click(entry_widget):
    new_key = generate_full_key()
    entry_widget.config(state="normal")
    entry_widget.delete(0, tk.END)
    entry_widget.insert(0, new_key)
    entry_widget.config(state="readonly")


def on_copy_click(root, entry_widget):
    current_key = entry_widget.get().strip()
    if current_key:
        root.clipboard_clear()
        root.clipboard_append(current_key)
        messagebox.showinfo("Успех", "Ключ скопирован в буфер обмена!")


def build_interface(root):
    canvas = tk.Canvas(
        root,
        width=WINDOW_WIDTH,
        height=WINDOW_HEIGHT,
        highlightthickness=0,
        bg="#1e1e24",
    )
    canvas.pack(fill="both", expand=True)

    if os.path.exists(BG_IMAGE_PATH):
        bg_image = tk.PhotoImage(file=BG_IMAGE_PATH)
        root.bg_image_ref = bg_image
        canvas.create_image(
            WINDOW_WIDTH // 2,
            WINDOW_HEIGHT // 2,
            image=bg_image,
        )

    control_frame = tk.Frame(root, bg="#111116", padx=20, pady=20)

    title_label = tk.Label(
        control_frame,
        text="GAME ACTIVATION KEYGEN",
        font=("Consolas", 15, "bold"),
        fg="#00ffcc",
        bg="#111116",
    )
    title_label.pack(pady=(0, 10))

    format_label = tk.Label(
        control_frame,
        text="Format: XXXX-XXXX-XXXX-XXXX",
        font=("Consolas", 9),
        fg="#888888",
        bg="#111116",
    )
    format_label.pack(pady=(0, 15))

    key_entry = tk.Entry(
        control_frame,
        font=("Consolas", 16, "bold"),
        justify="center",
        width=25,
        bd=2,
        relief="solid",
        fg="#00ffcc",
        bg="#1a1a24",
        readonlybackground="#1a1a24",
    )
    key_entry.pack(pady=(0, 15), ipady=4)

    buttons_frame = tk.Frame(control_frame, bg="#111116")
    buttons_frame.pack()

    btn_generate = tk.Button(
        buttons_frame,
        text="GENERATE",
        font=("Consolas", 11, "bold"),
        bg="#00ffcc",
        fg="#000000",
        activebackground="#00cca3",
        activeforeground="#000000",
        relief="flat",
        padx=15,
        pady=5,
        cursor="hand2",
        command=lambda: on_generate_click(key_entry),
    )
    btn_generate.pack(side=tk.LEFT, padx=5)

    btn_copy = tk.Button(
        buttons_frame,
        text="COPY",
        font=("Consolas", 11, "bold"),
        bg="#2d2d3a",
        fg="#ffffff",
        activebackground="#3d3d4e",
        activeforeground="#ffffff",
        relief="flat",
        padx=15,
        pady=5,
        cursor="hand2",
        command=lambda: on_copy_click(root, key_entry),
    )
    btn_copy.pack(side=tk.LEFT, padx=5)

    canvas.create_window(
        WINDOW_WIDTH // 2,
        WINDOW_HEIGHT // 2,
        window=control_frame,
    )

    on_generate_click(key_entry)


if __name__ == "__main__":
    play_background_music()
    root_window = tk.Tk()
    root_window.title("Keygen")
    root_window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    root_window.resizable(False, False)
    build_interface(root_window)
    root_window.mainloop()
    ctypes.windll.winmm.mciSendStringW("close bgm", None, 0, 0)