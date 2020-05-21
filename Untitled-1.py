import tkinter as tk

window = tk.Tk()
window.title = ("Encounter Builder")

ent = {}

#PC
fr_PC = tk.Frame(window)

lbl_PC = tk.Label(fr_PC, text="Player Stats")
class Ent:
    def __init__(self, name):
        self.name = name
        self.Default = True
        ent[name] = tk.Entry(fr_PC,
            width=5,
            fg="#bdbdbd",
            disabledforeground = "black",
            disabledbackground = "white") 
        ent[name].insert(0, "1")
        ent[name].bind("<Button-1>", self.click)
        ent[name].bind("<Return>", self.enter)
        ent[name].grid(row=1, column=1)

    def click(self,event):
        if self.Default == True or ent[self.name]["state"] == "disabled":
            ent[self.name]["state"] = "normal"
            ent[self.name].delete(0, tk.END)
            ent[self.name]["fg"] = "black"
        self.Default = False
    def enter(self,event):
        ent[self.name]["state"] = "disabled"

PC_Level = Ent("PC_Level")
lbl_PC.grid(row=0, column=0, columnspan=2)
lbl_PC_Level = tk.Label(fr_PC, text=("Level"))
lbl_PC_Level.grid(row=1, column=0)

#NPC
fr_NPC = tk.Frame(window)
lbl_NPC = tk.Label(fr_NPC, text="Enemy Stats")
lbl_NPC.pack()

#Layout
fr_PC.grid(row=0, column=0)
fr_NPC.grid(row=0, column=1)

window.mainloop()