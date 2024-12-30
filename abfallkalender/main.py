import os

def main():
    directory = os.path.dirname(os.getcwd()) + "/ics"
    data = []
    with open(f"{directory}/calendar.ics", "r") as f:
        data = f.readlines()
    print(len(data))

    interesting_items = []
    for line in data:
        if line.startswith("DESCRIPTION"):
            print(line, end="")
            interesting_items.append(line)

    print("-" * 50)
    for item in list(set(interesting_items)):
        print(item, end="")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
