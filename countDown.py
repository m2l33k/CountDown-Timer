import tkinter as tk
from tkinter import messagebox

class CountdownTimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        self.root.geometry("300x200")

        self.create_widgets()

    def create_widgets(self):
        # Time Entry
        self.label = tk.Label(self.root, text="Enter time in seconds:", font=('Helvetica', 12))
        self.label.pack(pady=10)

        self.time_var = tk.StringVar()
        self.time_entry = tk.Entry(self.root, textvariable=self.time_var, font=('Helvetica', 14))
        self.time_entry.pack(pady=10)

        # Start Button
        self.start_button = tk.Button(self.root, text="Start Countdown", command=self.start_countdown)
        self.start_button.pack(pady=20)

        # Display Time Remaining
        self.time_remaining_label = tk.Label(self.root, text="", font=('Helvetica', 18))
        self.time_remaining_label.pack(pady=20)

    def start_countdown(self):
        try:
            countdown_time = int(self.time_var.get())
            self.time_var.set("")
            self.update_countdown(countdown_time)
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number of seconds.")

    def update_countdown(self, remaining_time):
        if remaining_time > 0:
            minutes, seconds = divmod(remaining_time, 60)
            time_format = f"{minutes:02}:{seconds:02}"
            self.time_remaining_label.config(text=time_format)
            self.root.after(1000, self.update_countdown, remaining_time - 1)
        else:
            self.time_remaining_label.config(text="00:00")
            messagebox.showinfo("Countdown Timer", "Time's up!")

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimerApp(root)
    root.mainloop()
