# Project: Logic Box
# Student: Dev

print("Welcome to the Pattern Generator and Number Analyzer!")

while True:
    print("\nSelect: 1.Generate Pattern  2.Analyze Range  3.Exit")
    opt = input("Enter: ")
    if opt == "1":
        rows = int(input("Enter rows: "))
        if rows <= 0:
            print("Using break to stop pattern.")
            break
        i = 1
        while i <= rows:
            j = 1
            while j <= i:
                print("*", end="")
                j += 1
            print()
            i += 1
    elif opt == "2":
        a = int(input("Start: ")); b = int(input("End: "))
        if a >= b:
            print("Invalid range -> continue")
            continue
        s = 0
        for k in range(a, b+1):
            print(k, "Odd" if k % 2 else "Even")
            s += k
        print("Total from", a, "to", b, "=", s)
    elif opt == "3":
        print("Exiting..."); break
    else:
        print("Try again")
