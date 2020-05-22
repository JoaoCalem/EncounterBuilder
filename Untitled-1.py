import tkinter as tk

class Ent:
    def __init__(self, row, name, default, frame, n):
        self.name = name
        self.value = default
        self.state = "Default"
        if not self.name == "":
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
        if not self.name == "":
            self.lbl.grid(row=row, column=0, stick="e", pady=4)
            self.ent.grid(row=row, column=1, pady=4, padx=6)
        else:
            self.ent.grid(row=0, column=row, pady=4, padx=20)

    def click(self,event):
        if self.state == "Default" or self.ent["state"] == "disabled":
            self.ent["state"] = "normal"
            self.ent.delete(0, tk.END)
            self.ent["fg"] = "black"
        self.state = "Custom"
    def enter(self,event):
        self.value = self.ent.get()
        self.ent["state"] = "disabled"


class Monster:
    def __init__(self,n):
        self.fr = tk.Frame(fr_NPC_Stats)
        self.Number = Ent(0,"", 1, self.fr, n)
        self.Damage = Ent(1,"", 10, self.fr, n)
        self.HP = Ent(2,"", 20, self.fr, n)
        self.To_Hit = Ent(3,"", 3, self.fr, n)
        self.AC = Ent(4,"", 12, self.fr, n)
        self.fr.grid(row=n,column=0)

window = tk.Tk()
window.title = ("Encounter Builder")
window.minsize(200,100)

ent = {}

#PC
fr_PC_Stats = tk.Frame(window, relief="groove", borderwidth=1)

PC_Number = Ent(1,"Number", 4, fr_PC_Stats, "")
PC_Level = Ent(2,"Level", 1, fr_PC_Stats, "")
PC_Damage = Ent(3,"Damage", 7, fr_PC_Stats, "")
PC_Hp = Ent(4,"HP", 8, fr_PC_Stats, "")
PC_To_Hit = Ent(5,"To Hit", 5, fr_PC_Stats, "")
PC_AC = Ent(6,"AC", 13, fr_PC_Stats, "")
lbl_PC = tk.Label(window, text="PC STATS", font=("Segoe", 11))
lbl_PC.grid(row=0, column=0)
fr_PC_Stats.grid(row=1, column=0, padx=5, pady=5, stick="nsew")

#NPC
fr_NPC_Stats = tk.Frame(window, relief="groove", borderwidth=1)

fr_labels = tk.Frame(fr_NPC_Stats)
labels = {0:"Number",1:"Damage",2:"HP",3:"To Hit",4:"AC"}
lbl = {}
for i in labels:
    lbl[i] = tk.Label(fr_labels, text=labels[i], width=7)
    lbl[i].pack(side=tk.LEFT)
fr_labels.grid(row=0, column=0, padx=10, pady=5)

M = {}
M[1] = Monster(1)

lbl_NPC = tk.Label(window, text="ENEMY STATS", font=("Segoe", 11))
lbl_NPC.grid(row=0, column=1)
fr_NPC_Stats.grid(row=1, column=1, padx=5, pady=5, stick="nsew")

#Layout
window.mainloop()