import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter.ttk as ttk
# ======== Galvenais logs ========
logs = tk.Tk()
logs.title("Pārtikas noliktavas pārvaldība")
logs.geometry("1000x700")

# ======== Datu glabāšana ========
produkti = []
iekartas = []
izvietojums = []

# ======== Funkcijas =========

def pievienot_produktu():
    nosaukums = produkts_entry.get()
    termins = termins_entry.get()
    daudzums = daudzums_entry.get()

    if nosaukums and termins and daudzums:
        produkti.append((nosaukums, termins, daudzums))
        atjaunot_produktu_sarakstu()
        atjaunot_izvietojuma_izveles()
        produkts_entry.delete(0, tk.END)
        termins_entry.delete(0, tk.END)
        daudzums_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Kļūda", "Lūdzu, aizpildi visus laukus!")

def pievienot_iekartu():
    nosaukums = iekartas_entry.get()
    tips = tips_entry.get()
    temperatura = temperatura_entry.get()

    if nosaukums and tips and temperatura:
        iekartas.append((nosaukums, tips, temperatura))
        atjaunot_iekartu_sarakstu()
        atjaunot_izvietojuma_izveles()
        iekartas_entry.delete(0, tk.END)
        tips_entry.delete(0, tk.END)
        temperatura_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Kļūda", "Lūdzu, aizpildi visus laukus!")

def izvietot_produktu():
    produkts = produkta_izvele.get()
    iekarta = iekartas_izvele.get()

    if produkts and iekarta:
        izvietojums.append((produkts, iekarta))
        atjaunot_izvietojuma_sarakstu()
    else:
        messagebox.showwarning("Kļūda", "Lūdzu, izvēlies gan produktu, gan iekārtu!")

def atjaunot_produktu_sarakstu():
    produktu_saraksts.delete(*produktu_saraksts.get_children())
    for produkts in produkti:
        produktu_saraksts.insert('', tk.END, values=produkts)

def atjaunot_iekartu_sarakstu():
    iekartu_saraksts.delete(*iekartu_saraksts.get_children())
    for iekarta in iekartas:
        iekartu_saraksts.insert('', tk.END, values=iekarta)

def atjaunot_izvietojuma_sarakstu():
    izvietojuma_saraksts.delete(*izvietojuma_saraksts.get_children())
    for ieraksts in izvietojums:
        izvietojuma_saraksts.insert('', tk.END, values=ieraksts)

def atjaunot_izvietojuma_izveles():
    produkti_nosaukumi = [p[0] for p in produkti]
    iekartu_nosaukumi = [i[0] for i in iekartas]
    produkta_izvele['values'] = produkti_nosaukumi
    iekartas_izvele['values'] = iekartu_nosaukumi

# ======== UI – Rāmis ar ievades laukiem =========

produktu_ramis = tk.LabelFrame(logs, text="📦 Produktu katalogs", padx=10, pady=10)
produktu_ramis.grid(row=0, column=0, padx=10, pady=10, sticky="n")

iekartu_ramis = tk.LabelFrame(logs, text="❄️ Iekārtu katalogs", padx=10, pady=10)
iekartu_ramis.grid(row=0, column=1, padx=10, pady=10, sticky="n")

izvietojuma_ramis = tk.LabelFrame(logs, text="📍 Produktu izvietošana iekārtās", padx=10, pady=10)
izvietojuma_ramis.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="we")

# ======== Ievades lauku izveide =========

def izveidot_ievades_lauku(parent, label_text, row):
    ievades_konteineris = tk.Frame(parent)
    ievades_konteineris.grid(row=row, column=0, columnspan=2, pady=2, sticky="w")
    tk.Label(ievades_konteineris, text=label_text).pack(side="left")
    entry = tk.Entry(ievades_konteineris, width=30)
    entry.pack(side="left", padx=5)
    return entry

produkts_entry = izveidot_ievades_lauku(produktu_ramis, "📝 Nosaukums:", 0)
termins_entry = izveidot_ievades_lauku(produktu_ramis, "📅 Derīguma termiņš:", 1)
daudzums_entry = izveidot_ievades_lauku(produktu_ramis, "🔢 Daudzums:", 2)

iekartas_entry = izveidot_ievades_lauku(iekartu_ramis, "🔧 Nosaukums:", 0)
tips_entry = izveidot_ievades_lauku(iekartu_ramis, "📦 Tips:", 1)
temperatura_entry = izveidot_ievades_lauku(iekartu_ramis, "🌡 Temperatūra:", 2)

tk.Button(produktu_ramis, text="➕ Pievienot produktu", command=pievienot_produktu).grid(row=3, columnspan=2, pady=10)
tk.Button(iekartu_ramis, text="➕ Pievienot iekārtu", command=pievienot_iekartu).grid(row=3, columnspan=2, pady=10)

# ======== Treeview (saraksti) =========

produktu_saraksts = ttk.Treeview(produktu_ramis, columns=("Nosaukums", "Termiņš", "Daudzums"), show="headings", height=5)
for col in ("Nosaukums", "Termiņš", "Daudzums"):
    produktu_saraksts.heading(col, text=col)
produktu_saraksts.grid(row=4, columnspan=2, pady=5)

iekartu_saraksts = ttk.Treeview(iekartu_ramis, columns=("Nosaukums", "Tips", "Daudzums"), show="headings", height=5)
for col in ("Nosaukums", "Tips", "Daudzums"):
    iekartu_saraksts.heading(col, text=col)
iekartu_saraksts.grid(row=4, columnspan=2, pady=5)

# ======== Izvietojums sadaļa =========

tk.Label(izvietojuma_ramis, text="Izvēlies produktu").grid(row=0, column=0, padx=5, pady=5)
produkta_izvele = ttk.Combobox(izvietojuma_ramis, state="readonly")
produkta_izvele.grid(row=0, column=1, padx=5, pady=5)

tk.Label(izvietojuma_ramis, text="Izvēlies iekārtu").grid(row=1, column=0, padx=5, pady=5)
iekartas_izvele = ttk.Combobox(izvietojuma_ramis, state="readonly")
iekartas_izvele.grid(row=1, column=1, padx=5, pady=5)

tk.Button(izvietojuma_ramis, text="📌 Izvietot produktu", command=izvietot_produktu).grid(row=2, columnspan=2, pady=10)

izvietojuma_saraksts = ttk.Treeview(izvietojuma_ramis, columns=("Produkts", "Iekārta"), show="headings")
izvietojuma_saraksts.heading("Produkts", text="Produkts")
izvietojuma_saraksts.heading("Iekārta", text="Iekārta")
izvietojuma_saraksts.grid(row=3, columnspan=2, pady=10)

# ======== STILS UN TEMATIKAS =========

style = ttk.Style()
style.theme_use("clam")

def apply_widget_style(widget):
    try:
        widget_class = widget.winfo_class()
        if widget_class == "Label":
            widget.configure(font=("Segoe UI", 10, "bold"))
        elif widget_class == "Button":
            widget.configure(font=("Segoe UI", 10, "bold"), relief="flat", bd=0)
        elif widget_class == "Entry":
            widget.configure(font=("Segoe UI", 10), relief="flat", insertbackground="#000000")
    except tk.TclError:
        pass

def stils_gaisais():
    logs.configure(bg="#e0f2fe")
    for ramis in [produktu_ramis, iekartu_ramis, izvietojuma_ramis]:
        ramis.configure(bg="#fef9c3")
    style.configure("Treeview", background="#ffffff", foreground="#1e293b",
                    rowheight=25, fieldbackground="#f0f9ff", font=('Segoe UI', 10))
    style.configure("Treeview.Heading", font=('Segoe UI', 10, 'bold'),
                    background="#38bdf8", foreground="white")

def stils_tumsais():
    stils = ttk.Style()
    stils.theme_use("clam")  # Nodrošina, ka var mainīt label krāsas

    # Kopējais fons
    stils.configure(".", background="#1E293B", foreground="white")

    # Pogas stils
    stils.configure("TButton", background="#1E40AF", foreground="white", padding=6)
    stils.map("TButton", background=[("active", "#1D4ED8")])

    # LabelFrame stils ar pielāgotu nosaukuma krāsu
    stils.configure("Custom.TLabelframe", background="#1E293B", borderwidth=2, relief="groove")
    stils.configure("Custom.TLabelframe.Label", foreground="white", background="#1E293B", font=('Arial', 10, 'bold'))

    # Tabulas (Treeview) stils
    stils.configure("Treeview", background="#334155", fieldbackground="#334155", foreground="white")
    stils.configure("Treeview.Heading", background="#1E40AF", foreground="white", font=('Arial', 10, 'bold'))

    return stils


def stils_dabiskais():
    logs.configure(bg="#d9f99d")
    for ramis in [produktu_ramis, iekartu_ramis, izvietojuma_ramis]:
        ramis.configure(bg="#ecfccb")
    style.configure("Treeview", background="#f0fdf4", foreground="#14532d",
                    rowheight=25, fieldbackground="#dcfce7", font=('Segoe UI', 10))
    style.configure("Treeview.Heading", font=('Segoe UI', 10, 'bold'),
                    background="#22c55e", foreground="white")

def nomainit_tematu(temats):
    if temats == "Gaišā":
        stils_gaisais()
    elif temats == "Tumšā":
        stils_tumsais()
    elif temats == "Dabīgā":
        stils_dabiskais()
    for frame in [produktu_ramis, iekartu_ramis, izvietojuma_ramis]:
        for child in frame.winfo_children():
            apply_widget_style(child)

# Noklusējuma tēma
nomainit_tematu("Gaišā")

# ======== Izvēlne tēmas maiņai =========
izvelne = tk.Menu(logs)
logs.config(menu=izvelne)

tematika_menu = tk.Menu(izvelne, tearoff=0)
izvelne.add_cascade(label="🎨 Tematika", menu=tematika_menu)
tematika_menu.add_command(label="🌤 Gaišā", command=lambda: nomainit_tematu("Gaišā"))
tematika_menu.add_command(label="🌑 Tumšā", command=lambda: nomainit_tematu("Tumšā"))
tematika_menu.add_command(label="🌿 Dabīgā", command=lambda: nomainit_tematu("Dabīgā"))

# ======== Palaist logu =========
logs.mainloop()
