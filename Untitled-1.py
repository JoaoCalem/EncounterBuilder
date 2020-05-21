import tkinter as tk

def entry_click(name):
    print(name)
    #ent[name].delete(0, tk.END)

window = tk.Tk()
window.title = ("Encounter Builder")

ent = {}

#PC
fr_PC = tk.Frame(window)

lbl_PC = tk.Label(fr_PC, text="Player Stats")

name = "PC_Level"
ent[name] = tk.Entry(fr_PC, width=5, fg="#636363")
ent[name].insert(0, "1")
ent[name].bind("<Button-1>", lambda f=name: entry_click(f))
lbl_PC_Level = tk.Label(fr_PC, text=("Level"))

lbl_PC.grid(row=0, column=0, columnspan=2)
lbl_PC_Level.grid(row=1, column=0)
ent[name].grid(row=1, column=1)

#NPC
fr_NPC = tk.Frame(window)
lbl_NPC = tk.Label(fr_NPC, text="Enemy Stats")
lbl_NPC.pack()

#Layout
fr_PC.grid(row=0, column=0)
fr_NPC.grid(row=0, column=1)

window.mainloop()