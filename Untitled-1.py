import tkinter as tk

Type_Num = 1
Monster_Count = 1
ent = {}
Custom_Stats = 0

def Update_Code():
    custom = 0
    for i in M:
            custom += M[i].Custom_State
    if custom == 0:
        n = int(PC_Number.value)
        d = int(PC_Damage.value)
        th = int(PC_To_Hit.value)
        ac = int(PC_AC.value)
        hp = int(PC_Hp.value)
        Bias_PC = (n+1)/(2*n)
        num_Monsters = 0
        total_HP = 0
        total_Damage = 0
        for i in M:
            num_Monsters += int(M[i].Number.value)
            P_BH = 1-((int(M[i].AC.value)-th)/20)
            P_TH = 1-(ac-int(M[i].To_Hit.value))/20
            total_HP += int(M[i].Number.value)*int(M[i].HP.value)/P_BH
            total_Damage += P_TH*(int(M[i].Number.value)*int(M[i].Damage.value))
        Bias_Monsters = (num_Monsters+1)/(2*num_Monsters)
        Rounds = round(total_HP/(d*n))
        Bias = total_Damage*Bias_Monsters*Rounds/(hp*n*Bias_PC)
        if Bias < 0.6:
            Difficulty = "Too Easy"
        elif Bias >= 0.6 and Bias < 0.7:
            Difficulty = "Easy"
        elif Bias >= 0.7 and Bias < 0.8:
            Difficulty = "Medium"
        elif Bias >= 0.8 and Bias < 0.9:
            Difficulty = "Hard"
        elif Bias >= 0.9 and Bias < 1:
            Difficulty = "Deadly"
        else:
            Difficulty = "Too Hard"
        global lbl_Rounds_Output
        global lbl_Difficulty_Output
        lbl_Rounds_Output["text"] = str(Rounds)
        lbl_Difficulty_Output["text"] = Difficulty


class Ent:
    def __init__(self, row, name, default, frame, n):
        self.empty = 0
        self.locked = 0
        self.name = name
        self.value = default
        self.original_value = default
        self.state = "Default"
        if not self.name == "":
            self.lbl = tk.Label(frame, text=(self.name), width=7, anchor="e")
        self.ent = tk.Entry(frame,
            width=4,
            fg="#bdbdbd",
            justify="right",
            disabledforeground = "black",
            disabledbackground = "white") 
        self.ent.insert(0, self.value)
        self.ent.bind("<Button-1>", self.click)
        self.ent.bind("<Return>", lambda f=0, g=0: self.update(f,g))
        self.ent.bind("<Key>", lambda f=1, g=1: self.update(f,g))
        if not self.name == "":
            self.lbl.grid(row=row, column=0, stick="e", pady=4)
            self.ent.grid(row=row, column=1, pady=4, padx=6)
        else:
            self.ent.grid(row=0, column=row, pady=4, padx=14)

    def click(self,event):
        Reset()
        if self.locked == 0:
            self.ent["state"] = "normal"
            self.ent.delete(0, tk.END)
            self.ent["fg"] = "black"
        self.empty = 1
    def update(self,event,type):
        if type == 0:
            self.state = "Custom"
            self.value = self.ent.get()
            self.ent["state"] = "disabled"
            Update_Code()
        else:
            try:
                self.value = float(self.ent.get()+event.char)
                self.state = "Custom"
                Update_Code()
            except ValueError:
                pass


class Monster:
    def __init__(self,n):
        self.fr = tk.Frame(fr_NPC_Stats)
        self.Custom_State = 0
        self.Number = Ent(0,"", 1, self.fr, n)
        self.Damage = Ent(1,"", 7, self.fr, n)
        self.HP = Ent(2,"", 72, self.fr, n)
        self.To_Hit = Ent(3,"", 3, self.fr, n)
        self.AC = Ent(4,"", 12, self.fr, n)
        self.custom = tk.Button(self.fr, text="Custom", command=lambda f=n: Custom(f))
        self.custom.grid(row=0, column=5, pady=4)
        global Type_Num
        if Type_Num > 1:
            self.delete = tk.Button(self.fr, text="\u274C", command=lambda f=n: Delete(f))
            self.delete.grid(row=0, column=6, pady=4, padx=9)
            self.delete_button = 1
        else:
            self.empty = tk.Label(self.fr, text="")
            self.empty.grid(row=0, column=6, pady=4, padx=20)
            self.delete_button = 0
        self.fr.grid(row=n,column=0, padx=5)

def Add():
    global Type_Num
    global Monster_Count
    Type_Num += 1
    Monster_Count += 1
    M[Monster_Count] = Monster(Monster_Count)
    btn_add.grid(row=Monster_Count+1, column=0, pady=4, padx=15, sticky="e")
    for i in M:
        if M[i].delete_button == 0:
            M[i].empty.grid_forget
            M[i].delete = tk.Button(M[i].fr, text="\u274C", command=lambda f=i: Delete(f))
            M[i].delete.grid(row=0, column=6, pady=4, padx=9)
            M[i].delete_button = 1
    Update_Code()

def Delete(n):
    Update_Code()
    global Custom_Stats
    if M[n].Custom_State == 1:
        if Custom_Stats == 1:
            global fr_labels_custom
            fr_labels_custom.grid_forget()
        Custom_Stats -= 1
    global Type_Num
    global Monster_Count
    M[n].fr.grid_forget()
    if M[n].Custom_State == 1:
        M[n].fr_custom.grid_forget()
    del M[n]
    Type_Num -= 1
    btn_add.grid(row=Monster_Count+1, column=0, pady=4, padx=15, sticky="e")
    for i in M:
        if M[i].delete_button == 1 and Type_Num ==1:
            M[i].delete.grid_forget()
            M[i].empty = tk.Label(M[i].fr, text="")
            M[i].empty.grid(row=0, column=6, pady=4, padx=20)
            M[i].delete_button = 0
            Update_Code()
            break
    Update_Code()

def Custom(n):
    global Custom_Stats
    M[n].Custom_State = 1
    if Custom_Stats == 0:
        global fr_labels_custom
        fr_labels_custom = tk.Frame(fr_NPC_Stats)
        labels_custom = {0:"%To Hit",1:"%Be Hit",2:"Weight"}
        lbl = {}
        for i in labels_custom:
            lbl[i] = tk.Label(fr_labels_custom, text=labels_custom[i], width=7)
            lbl[i].pack(side=tk.LEFT)
        fr_labels_custom.grid(row=0, column=1, padx=10, pady=5, sticky="e")
    Custom_Stats += 1
    M[n].custom.grid_forget()
    M[n].Existing = tk.Button(M[n].fr, text="Existing", command=lambda f=n: Exising(f))
    M[n].Existing.grid(row=0, column=5, pady=4)
    M[n].fr_custom = tk.Frame(fr_NPC_Stats)
    M[n].P_TH = Ent(0,"", 65, M[n].fr_custom, n)
    M[n].P_BH = Ent(1,"", 50, M[n].fr_custom, n)
    M[n].P_Weight = Ent(2,"", 1, M[n].fr_custom, n)
    M[n].fr_custom.grid(row=n,column=1, padx=5)
    i = {0:M[n].AC,1:M[n].Damage,2:M[n].HP,3:M[n].To_Hit}
    for j in i:
        i[j].ent["state"] = ["disabled"]
        i[j].ent["disabledbackground"] = ["#e0e0e0"]
        i[j].locked = 1
    Update_Code()

def Exising(n):
    global Custom_Stats
    M[n].Custom_State = 0
    if Custom_Stats == 1:
        global fr_labels_custom
        fr_labels_custom.grid_forget()
    Custom_Stats -= 1
    M[n].Existing.grid_forget()
    M[n].fr_custom.grid_forget()
    M[n].Custom = tk.Button(M[n].fr, text="Custom", command=lambda f=n: Custom(f))
    M[n].Custom.grid(row=0, column=5, pady=4)
    i = {0:M[n].AC,1:M[n].Damage,2:M[n].HP,3:M[n].To_Hit}
    for j in i:
        i[j].ent["disabledbackground"] = ["white"]
        i[j].locked = 0
        i[j].ent["state"] = ["normal"]
    Update_Code()

def Reset():
    for i in M:
        for j in dir(M[i]):
            k = getattr(M[i],j)
            try:
                if k.empty == 1 and k.locked == 0:
                    k.empty = 0
                    k.ent.insert(0,k.value)
                    setattr(M[i],j,k)
            except(AttributeError):
                pass

window = tk.Tk()
window.title = ("Encounter Builder")
window.resizable(width=False, height=False)

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
fr_labels.grid(row=0, column=0, padx=10, pady=5, sticky="w")

M = {}
M[1] = Monster(1)
btn_add = tk.Button(fr_NPC_Stats, text="Add Monster Type", command=Add)
btn_add.grid(row=2, column=0, pady=4, padx=15, sticky="e")

lbl_NPC = tk.Label(window, text="ENEMY STATS", font=("Segoe", 11))
lbl_NPC.grid(row=0, column=1)
fr_NPC_Stats.grid(row=1, column=1, padx=5, pady=5, stick="nsew")

#Output
fr_Output = tk.Frame(window, relief="groove", borderwidth=1)

x = 8
lbl_Difficulty = tk.Label(fr_Output, text="Difficulty:", width=x, anchor="e")
lbl_Difficulty.grid(row=0, column=0, padx=5, pady=5)

lbl_Difficulty_Output = tk.Label(fr_Output, text="Medium", bg="white", width=x)
lbl_Difficulty_Output.grid(row=0, column=1, padx=5, pady=5)

lbl_Rounds = tk.Label(fr_Output, text="Rounds:", width=x, anchor="e")
lbl_Rounds.grid(row=1, column=0, padx=5, pady=5)

lbl_Rounds_Output = tk.Label(fr_Output, text="4", bg="white", width=x)
lbl_Rounds_Output.grid(row=1, column=1, padx=5, pady=5)

btn_Update = tk.Button(fr_Output, text="Update", command=Update_Code)
btn_Update.grid(row=3, column=0, pady=4, padx=15, columnspan = 2)

fr_Output.grid(row=1, column=2, padx=5, pady=5, stick="nsew")

#
window.mainloop()