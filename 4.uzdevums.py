ievads = int(input("Ievadi skaitli:"))

if ievads < 0:
    print("Faktorials nevarbūt skaitlis kas ir zem 0")
else:
    faktorials=1
    for skaitlis in range(1,ievads+1):
        faktorials *=skaitlis
    print(f"Skaitla {ievads} faktoriāls ir: {faktorials}")