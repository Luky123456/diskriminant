import tkinter as tk

win = tk. Tk()

at = tk.Label(win, text = "Zadaj koeficient a:")
at.pack()

a = tk.Entry(win)
a.pack()

bt = tk.Label(win, text = "Zadaj koeficient b:")
bt.pack()

b = tk.Entry(win)
b.pack()

ct = tk.Label (win,text = "Zadaj koeficient c:")
ct.pack()

c = tk.Entry(win)
c.pack()

def executor():
    print(a.get(),b.get(),c.get())
    ka = int(a.get())
    kb = int(b.get())
    kc = int(c.get())
    d = kb**2 - 4*ka*kc
    if d <0:
        label = tk.Label(win, text="Nemá riešenie v R")
        label.pack()
    elif d==0:
        jednox = -kb / (2 * ka)
        label = tk.Label(win, text = jednox)
        label.pack()
    else:
        xjedna = ((-kb+d**0.5)/(2*ka))
        xdva = ((-kb-d**0.5)/(2*ka))
        xx = xjedna,xdva
        label = tk.Label(win, text = xx)
        label.pack()

button = tk.Button(win, text = "Vyriešiť", command = executor)
button.pack()

win.mainloop()