import tkinter as tk

class Ent:
    def __init__(self, row, name, default, frame):
        self.name = name
        self.value = default
        self.state = "Default"
        self.lbl = tk.Label(frame, text=(self.name), width=7, anchor="e")
        self.ent = tk.Entry(frame,
            width=2,
            fg="#bdbdbd",
            justify="right",
            disabledforeground = "black",
            disabledbackground = "white") 
        self.ent.insert(0, self.value)
        self.ent.bind("<Button-1>", self.click)
        self.ent.bind("<Return>", self.enter)
        self.lbl.grid(row=row, column=0, stick="e", pady=4)
        self.ent.grid(row=row, column=1, pady=4, padx=6)

    def click(self,event):
        if self.state == "Default" or self.ent["state"] == "disabled":
            self.ent["state"] = "normal"
            self.ent.delete(0, tk.END)
            self.ent["fg"] = "black"
        self.state = "Custom"
    def enter(self,event):
        self.state = self.ent.get()
        self.ent["state"] = "disabled"

window = tk.Tk()
window.title = ("Encounter Builder")
window.minsize(200,100)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.rowconfigure(0, weight=1)

ent = {}

#PC
fr_PC = tk.Frame(window)
fr_PC_Stats = tk.Frame(fr_PC, relief="groove", borderwidth=1)

PC_Number = Ent(1,"Number", 4, fr_PC_Stats)
PC_Level = Ent(2,"Level", 1, fr_PC_Stats)
PC_Damage = Ent(3,"Damage", 7, fr_PC_Stats)
PC_Hp = Ent(4,"HP", 8, fr_PC_Stats)
PC_To_Hit = Ent(5,"To Hit", 5, fr_PC_Stats)

lbl_PC = tk.Label(fr_PC, text="PC STATS", font=("Segoe", 11))
lbl_PC.grid(row=0, column=0, sticky="n")
fr_PC_Stats.grid(row=2, column=0, sticky="n", pady=5)

#NPC
fr_NPC = tk.Frame(window)
lbl_NPC = tk.Label(fr_NPC, text="Enemy Stats", height=2, anchor="n")
lbl_NPC.pack()

#Layout
pad_Main = 10
fr_PC.grid(row=0, column=0, sticky="e", padx=pad_Main, pady=pad_Main)
fr_NPC.grid(row=0, column=1, sticky="w", padx=pad_Main, pady=pad_Main)

window.mainloop()