import  tkinter as tk

from interface.styling import *
from datetime import datetime

class Logging(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logging_text = tk.Text(self, height=10,width= 60, state=tk.DISABLED, bg=BG_COLOR, fg=FG_COLOR2, font=GLOBAL_FONT,highlightthickness=False,bd=0)
        self.logging_text.pack(side= tk.TOP)

    def add_log(self, message: str):
        self.logging_text.configure(state= tk.NORMAL)
        self.logging_text.insert("1.0",datetime.now().strftime("%a %H %M %S :: ") + message + "\n")
        self.logging_text.configure(state=tk.DISABLED)

    def delete_all_logs(self):
        self.logging_text.configure(state=tk.NORMAL)
        self.logging_text.delete(1.0, tk.END)
        self.logging_text.configure(state=tk.DISABLED)

