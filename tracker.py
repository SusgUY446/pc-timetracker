import tkinter as tk
import time
import tkinter.messagebox as messagebox
from colorama import Fore, Back, Style



class PCUsageTracker:
    def __init__(self, root, maxtime):

        self.root = root
        self.root.title("PC Usage Tracker")
        self.root.geometry("300x100")

        self.maxtime = maxtime

        self.label = tk.Label(root, text="Time on pc: 00:00:00")
        self.label.pack()

        self.gesamt_zeit_in_sekunden = 0
        self.running = True
        self.start_time = time.time()


        self.update_time()

    def update_time(self):
        if self.running:
            current_time = int(time.time() - self.start_time)
            self.gesamt_zeit_in_sekunden += current_time
            hours, remainder = divmod(self.gesamt_zeit_in_sekunden, 3600)
            minutes, seconds = divmod(remainder, 60)
            time_str = f"{hours:02}:{minutes:02}:{seconds:02}"
            self.label.config(text="Time on pc: " + time_str)
            if self.gesamt_zeit_in_sekunden > self.maxtime:
                self.show_break_popup()
            self.start_time = time.time()
        self.root.after(1000, self.update_time)

    def stop_timer(self):
        self.running = False

    def start_timer(self):
        self.start_time = time.time() - (time.time() - self.start_time)
        self.running = True

    def show_break_popup(self):
        messagebox.showinfo("Time for a Break", "Time for a break!")

if __name__ == "__main__":
    


    print(Fore.GREEN + 'Time until break reminder (in seconds)')
    maxtime_input = input()



    if maxtime_input != None:
        
        maxtime_input = int(maxtime_input)
        root = tk.Tk()
        tracker = PCUsageTracker(root, maxtime=maxtime_input)



    root.mainloop()
