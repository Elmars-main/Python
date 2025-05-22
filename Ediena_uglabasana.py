import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import os

# ======== Galvenais logs ========
logs = tk.Tk()
logs.title("Pārtikas noliktavas pārvaldība")
logs.geometry("1100x750")

# ======== Konfigurācijas fails ========
config_fails = "konfiguracija.json"

def ieladet_konfiguraciju():
    if os.path.exists(config_fails):
        with open(config_fails, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"valoda": "LV", "tema": "light green"}

def saglabat_konfiguraciju(valoda, tema):
    with open(config_fails, "w", encoding="utf-8") as f:
        json.dump({"valoda": valoda, "tema": tema}, f)

# ======== Valodu atbalsts ========
valodas = {
    "LV": {
        "produktu_katalogs": "📦 Produktu katalogs",
        "iekartu_katalogs": "❄️ Iekārtu katalogs",
        "izvietosana": "📍 Produktu izvietošana iekārtās",
        "nosaukums": "📝 Nosaukums:",
        "termins": "📅 Derīguma termiņš:",
        "daudzums": "🔹 Daudzums:",
        "tips": "📦 Tips:",
        "temperatura": "🌡 Temperatūra:",
        "pievienot_produktu": "➕ Pievienot produktu",
        "pievienot_iekartu": "➕ Pievienot iekārtu",
        "izveleties_produktu": "Izvēlies produktu",
        "izveleties_iekartu": "Izvēlies iekārtu",
        "izvietot_produktu": "📌 Izvietot produktu",
        "tematika": "🎨 Tematika",
        "valoda": "🌐 Valoda",
        "jauns_produkts": "Jauns produkts",
        "ievadi_produktu": "Ievadi produkta nosaukumu:"
    },
    "EN": {
        "produktu_katalogs": "📦 Product Catalog",
        "iekartu_katalogs": "❄️ Equipment Catalog",
        "izvietosana": "📍 Product Placement in Equipment",
        "nosaukums": "📝 Name:",
        "termins": "📅 Expiry Date:",
        "daudzums": "🔹 Quantity:",
        "tips": "📦 Type:",
        "temperatura": "🌡 Temperature:",
        "pievienot_produktu": "➕ Add Product",
        "pievienot_iekartu": "➕ Add Equipment",
        "izveleties_produktu": "Choose Product",
        "izveleties_iekartu": "Choose Equipment",
        "izvietot_produktu": "📌 Place Product",
        "tematika": "🎨 Theme",
        "valoda": "🌐 Language",
        "jauns_produkts": "New Product",
        "ievadi_produktu": "Enter product name:"
    },
    "RU": {
        "produktu_katalogs": "📦 Каталог продуктов",
        "iekartu_katalogs": "❄️ Каталог оборудования",
        "izvietosana": "📍 Размещение продуктов",
        "nosaukums": "📝 Название:",
        "termins": "📅 Срок годности:",
        "daudzums": "🔹 Количество:",
        "tips": "📦 Тип:",
        "temperatura": "🌡 Температура:",
        "pievienot_produktu": "➕ Добавить продукт",
        "pievienot_iekartu": "➕ Добавить оборудование",
        "izveleties_produktu": "Выбери продукт",
        "izveleties_iekartu": "Выбери оборудование",
        "izvietot_produktu": "📌 Разместить продукт",
        "tematika": "🎨 Темы",
        "valoda": "🌐 Язык",
        "jauns_produkts": "Новый продукт",
        "ievadi_produktu": "Введите название продукта:"
    }
}

produkts_uz_iekartas = {
    "Piens": ["Ledusskapis"],
    "Gaļa": ["Saldētava", "Ledusskapis"],
    "Dārzeņi": ["Ledusskapis"],
    "Maize": ["Pārtikas plaukts"],
    "Zupa": ["Tvaika katls", "Plīts"],
    "Jogurts": ["Ledusskapis"],
    "Siers": ["Ledusskapis"],
    "Zivis": ["Saldētava"],
    "Augļi": ["Ledusskapis"],
    "Saldumi": ["Pārtikas plaukts"]
}

konfig = ieladet_konfiguraciju()
aktiv_langu = konfig.get("valoda", "LV")

standarta_iekartas = [
    ("Ledusskapis", "Uzglabāšana", "4"),
    ("Saldētava", "Uzglabāšana", "-18"),
    ("Plīts", "Gatavošana", "70"),
    ("Cepeškrāsns", "Gatavošana", "180"),
    ("Grils", "Gatavošana", "150"),
    ("Tvaika katls", "Gatavošana", "100"),
    ("Trauku mazgājamā mašīna", "Mazgāšana", "65"),
    ("Virtuves galds", "Apstrāde", "25"),
    ("Pārtikas plaukts", "Glabāšana", "20"),
    ("Transportēšanas konteiners", "Transportēšana", "5")
]

produkti = ["Piens", "Gaļa", "Dārzeņi", "Siers", "Zivis", "Augļi", "Jogurts", "Sviests", "Saldumi", "Maize"]
iekartas = standarta_iekartas.copy()
izvietojums = []

# ======== GUI funkcijas ========
noklusetie_produkti = {
    "LV": ["Piens", "Gaļa", "Dārzeņi", "Siers", "Zivis", "Augļi", "Jogurts", "Sviests", "Saldumi", "Maize"],
    "EN": ["Milk", "Meat", "Vegetables", "Cheese", "Fish", "Fruits", "Yogurt", "Butter", "Sweets", "Bread"],
    "RU": ["Молоко", "Мясо", "Овощи", "Сыр", "Рыба", "Фрукты", "Йогурт", "Масло", "Сладости", "Хлеб"]
}

produkti = noklusetie_produkti.get(aktiv_langu, noklusetie_produkti["LV"]).copy()

# ...existing code...

# Noklusētās iekārtas katrai valodai
noklusetas_iekartas = {
    "LV": [
        ("Ledusskapis", "Uzglabāšana", "4"),
        ("Saldētava", "Uzglabāšana", "-18"),
        ("Plīts", "Gatavošana", "70"),
        ("Cepeškrāsns", "Gatavošana", "180"),
        ("Grils", "Gatavošana", "150"),
        ("Tvaika katls", "Gatavošana", "100"),
        ("Trauku mazgājamā mašīna", "Mazgāšana", "65"),
        ("Virtuves galds", "Apstrāde", "25"),
        ("Pārtikas plaukts", "Glabāšana", "20"),
        ("Transportēšanas konteiners", "Transportēšana", "5")
    ],
    "EN": [
        ("Fridge", "Storage", "4"),
        ("Freezer", "Storage", "-18"),
        ("Stove", "Cooking", "70"),
        ("Oven", "Cooking", "180"),
        ("Grill", "Cooking", "150"),
        ("Steamer", "Cooking", "100"),
        ("Dishwasher", "Washing", "65"),
        ("Kitchen Table", "Processing", "25"),
        ("Food Shelf", "Storage", "20"),
        ("Transport Container", "Transport", "5")
    ],
    "RU": [
        ("Холодильник", "Хранение", "4"),
        ("Морозильник", "Хранение", "-18"),
        ("Плита", "Готовка", "70"),
        ("Духовка", "Готовка", "180"),
        ("Гриль", "Готовка", "150"),
        ("Пароварка", "Готовка", "100"),
        ("Посудомоечная машина", "Мойка", "65"),
        ("Кухонный стол", "Обработка", "25"),
        ("Полка для еды", "Хранение", "20"),
        ("Транспортный контейнер", "Транспортировка", "5")
    ]
}

iekartas = noklusetas_iekartas.get(aktiv_langu, noklusetas_iekartas["LV"]).copy()

# ...existing code...

def mainit_valodu(val):
    global aktiv_langu, produkti, iekartas
    aktiv_langu = val
    tekstus = valodas[val]
    # Atjauno produktus un iekārtas pēc valodas
    produkti = noklusetie_produkti.get(val, noklusetie_produkti["LV"]).copy()
    iekartas = noklusetas_iekartas.get(val, noklusetas_iekartas["LV"]).copy()
    produkta_izvele["values"] = produkti
    iekartas_izvele["values"] = [i[0] for i in iekartas]
    produktu_ramis.config(text=tekstus["produktu_katalogs"])
    iekartu_ramis.config(text=tekstus["iekartu_katalogs"])
    izvietojuma_ramis.config(text=tekstus["izvietosana"])
    pogas["produkts"].config(text=tekstus["pievienot_produktu"])
    pogas["iekarta"].config(text=tekstus["pievienot_iekartu"])
    pogas["izvietot"].config(text=tekstus["izvietot_produktu"])
    etiķetes["produkts"].config(text=tekstus["izveleties_produktu"])
    etiķetes["iekarta"].config(text=tekstus["izveleties_iekartu"])
    logs.title(tekstus["produktu_katalogs"])
    saglabat_konfiguraciju(aktiv_langu, logs.cget("bg"))

# ...existing code...

def pievienot_iekartas():
    teksts = valodas[aktiv_langu]
    iekartu_nosaukumi = [i[0] for i in standarta_iekartas]
    izvele = simpledialog.askstring(
        teksts["pievienot_iekartu"],
        f"{teksts['izveleties_iekartu']}:\n{', '.join(iekartu_nosaukumi)}\n\nVai ievadi jaunu iekārtu manuāli:"
    )

    if izvele in iekartu_nosaukumi:
        for nos, tips, temp in standarta_iekartas:
            if nos == izvele:
                jauns_nos = simpledialog.askstring("Rediģēt", f"Ievadi iekārtas nosaukumu ({nos}):") or nos
                jauns_tips = simpledialog.askstring("Rediģēt", f"Ievadi iekārtas tipu ({tips}):") or tips
                jauna_temp = simpledialog.askstring("Rediģēt", f"Ievadi temperatūru ({temp}):") or temp
                iekartas.append((jauns_nos, jauns_tips, jauna_temp))
                break
    elif izvele:
        iekartas.append((izvele, "Cits", ""))
    else:
        iekartas.clear()
        iekartas.extend(standarta_iekartas)

    iekartas_izvele["values"] = [i[0] for i in iekartas]
    messagebox.showinfo("Info", "Iekārtas pievienotas!")

def pievienot_produktus():
    teksts = valodas[aktiv_langu]
    new = simpledialog.askstring(teksts["jauns_produkts"], teksts["ievadi_produktu"])
    if new:
        produkti.append(new)
        produkta_izvele["values"] = produkti
        messagebox.showinfo("Info", f"{teksts['pievienot_produktu']} '{new}'!")

def ieteikt_iekartu(event=None):
    produkts = produkta_izvele.get()
    if produkts in produkts_uz_iekartas:
        iespejamie = produkts_uz_iekartas[produkts]
        for i, iek in enumerate(iekartas):
            if iek[0] in iespejamie:
                iekartas_izvele.current(i)
                break

def mainit_tematu(krasa):
    logs.configure(bg=krasa)
    for widget in logs.winfo_children():
        if isinstance(widget, tk.LabelFrame) or isinstance(widget, tk.Frame):
            widget.configure(bg=krasa)
        for child in widget.winfo_children():
            try:
                child.configure(bg=krasa)
            except:
                pass
    saglabat_konfiguraciju(aktiv_langu, krasa)

from PIL import Image, ImageTk

# ...existing code...

# Ielādē attēlu, samazini līdz 32x32 un uzstādi kā loga ikonu
icon_img = Image.open(r"C:\Users\T\Downloads\Ediena_uzglabasana\logo.png")
icon_img = icon_img.resize((32, 32))  # vai (16, 16) ja vēlies vēl mazāku
icon = ImageTk.PhotoImage(icon_img)
logs.iconphoto(True, icon)

# ...pārējie UI elementi...
produktu_ramis = tk.LabelFrame(logs, text="", padx=10, pady=10)
produktu_ramis.grid(row=1, column=0, padx=10, pady=10, sticky="n")

iekartu_ramis = tk.LabelFrame(logs, text="", padx=10, pady=10)
iekartu_ramis.grid(row=1, column=1, padx=10, pady=10, sticky="n")

izvietojuma_ramis = tk.LabelFrame(logs, text="", padx=10, pady=10)
izvietojuma_ramis.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="n")


izvelne = tk.Menu(logs)
logs.config(menu=izvelne)

valodas_menu = tk.Menu(izvelne, tearoff=0)
izvelne.add_cascade(label="🌐 Valoda", menu=valodas_menu)
valodas_menu.add_command(label="Latviešu", command=lambda: mainit_valodu("LV"))
valodas_menu.add_command(label="English", command=lambda: mainit_valodu("EN"))
valodas_menu.add_command(label="Русский", command=lambda: mainit_valodu("RU"))

tematika_menu = tk.Menu(izvelne, tearoff=0)
izvelne.add_cascade(label="🎨 Tematika", menu=tematika_menu)
tematika_menu.add_command(label="🌤 Gaišā", command=lambda: mainit_tematu("#f0f8ff"))
tematika_menu.add_command(label="🌑 Tumšā", command=lambda: mainit_tematu("#2e2e2e"))
tematika_menu.add_command(label="🌿 Dabīgā", command=lambda: mainit_tematu("#dcedc8"))

etiķetes = {}
pogas = {}

etiķetes["produkts"] = tk.Label(izvietojuma_ramis, text="")
etiķetes["produkts"].grid(row=0, column=0)
produkta_izvele = ttk.Combobox(izvietojuma_ramis, state="readonly")
produkta_izvele.grid(row=0, column=1)
produkta_izvele["values"] = produkti
produkta_izvele.bind("<<ComboboxSelected>>", ieteikt_iekartu)

etiķetes["iekarta"] = tk.Label(izvietojuma_ramis, text="")
etiķetes["iekarta"].grid(row=1, column=0)
iekartas_izvele = ttk.Combobox(izvietojuma_ramis, state="readonly")
iekartas_izvele.grid(row=1, column=1)
iekartas_izvele["values"] = [i[0] for i in iekartas]

pogas["izvietot"] = tk.Button(
    izvietojuma_ramis,
    text="",
    command=lambda: izvietojums.append((produkta_izvele.get(), iekartas_izvele.get()))
)
pogas["izvietot"].grid(row=2, columnspan=2, pady=5)

pogas["produkts"] = tk.Button(produktu_ramis, text="", command=pievienot_produktus)
pogas["produkts"].grid(row=0, columnspan=2, pady=10)

pogas["iekarta"] = tk.Button(iekartu_ramis, text="", command=pievienot_iekartas)
pogas["iekarta"].grid(row=0, columnspan=2, pady=10)

mainit_valodu(aktiv_langu)
logs.configure(bg=konfig.get("tema", "#dcedc8"))
logs.mainloop()
