from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Restaurant Scheduler")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="").grid(column=0, row=0)
ttk.Button(mainframe, text="1").grid(column=1, row=0)
ttk.Button(mainframe, text="2").grid(column=2, row=0)
ttk.Button(mainframe, text="3").grid(column=3, row=0)
ttk.Button(mainframe, text="4").grid(column=4, row=0)
ttk.Label(mainframe, text="").grid(column=5, row=0)

for _column in range(5):
    ttk.Label(mainframe, text="").grid(column=_column, row=1)

ttk.Button(mainframe, text="5").grid(column=0, row=2, columnspan=2, rowspan=2)
ttk.Label(mainframe, text="").grid(column=2, row=2)
ttk.Label(mainframe, text="").grid(column=2, row=3)
ttk.Label(mainframe, text="").grid(column=3, row=2)
ttk.Label(mainframe, text="").grid(column=3, row=3)
ttk.Button(mainframe, text="6").grid(column=4, row=2, columnspan=2, rowspan=2)

for _column in range(5):
    ttk.Label(mainframe, text="").grid(column=_column, row=4)

ttk.Button(mainframe, text="7").grid(column=0, row=5, columnspan=2)
ttk.Label(mainframe, text="").grid(column=2, row=5)
ttk.Label(mainframe, text="").grid(column=3, row=5)
ttk.Button(mainframe, text="7").grid(column=4, row=5, columnspan=2)

root.mainloop()