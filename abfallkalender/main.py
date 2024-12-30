import os

old2new_description = {
    "Grünbündel nur Tannenbaumabfuhr nicht vergessen!": "🌲 Grünbündel nur Tannenbaumabfuhr",
    "Papier Vorverlegung nicht vergessen!": "🟦 Blaue Tonne (Vorverlegung)",
    "Papier nicht vergessen!": "🟦 Blaue Tonne",
    "Leichtverpackungen Vorverlegung nicht vergessen!": "🟨 Gelbe Tonne (Vorverlegung)",
    "Leichtverpackungen nicht vergessen!": "🟨 Gelbe Tonne",
    "Restabfall Vorverlegung nicht vergessen!": "⬛ Graue Tonne (Vorverlegung)",
    "Restabfall nicht vergessen!": "⬛ Graue Tonne",
    "Bioabfall Vorverlegung nicht vergessen!": "🟫 Braune Tonne (Vorverlegung)",
    "Bioabfall nicht vergessen!": "🟫 Braune Tonne"
}

old2new_summary = {"Papier" : "🟦 Blaue Tonne",
                   "Leichtverpackungen" : "🟨 Gelbe Tonne",
                   "Restabfall" : "⬛ Graue Tonne",
                   "Bioabfall" : "🟫 Braune Tonne",
                   "Grünbündel" : "🌲 Grünbündel (Tannenbaumabfuhr)"}

def main():
    directory = os.path.dirname(os.getcwd()) + "/ics"
    data = []
    with open(f"{directory}/calendar.ics", "r", encoding="utf-8") as f:
        data = f.readlines()
    print(len(data))

    interesting_items = []
    for line in data:
        if line.startswith("SUMMARY:"):
            print(line, end="")
            interesting_items.append(line)
    print("-" * 50)
    for item in list(set(interesting_items)):
        print(item, end="")

    for i, line in enumerate(data):
        """
        for old, new in old2new_description.items():
            data[i] = data[i].replace(old, new)
        """
        for old, new in old2new_summary.items():
            data[i] = data[i].replace(old, new)

    with open(f"{directory}/output.ics", "w", encoding="utf-8") as f:
        for line in data:
            f.write(line)
    print("output.ics written.")

if __name__ == '__main__':
    main()
