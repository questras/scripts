"""
A simple script to remind you to stand up at regular thresholds.
It shows a small window with text to remind you to stand up.
It shows at threshold specified in *reminder_threshold*.
"""

import tkinter as tk
import time

reminder_threshold = 30  # in minutes
reminder_text = 'Stand up!'

while True:
    time.sleep(reminder_threshold * 60)

    window = tk.Tk()
    tk.Label(window, text=reminder_text).pack()
    tk.Button(window, text='ok', command=window.destroy).pack()
    window.geometry('300x100+900+500')

    window.mainloop()
