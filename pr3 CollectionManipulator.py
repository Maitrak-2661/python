# Project: Collection Manipulator
# Student: Dev

student_name = "Dev"

print("Simple Organizer for Students")

bag = []

while True:
    print("\n[1]Add [2]Display [3]Update [4]Delete [5]Subjects [6]Exit")
    op = input("-> ")
    if op == "1":
        i = int(input("ID: ")); n = input("Name: "); a = int(input("Age: ")); g = input("Grade: ")
        d = input("DOB (YYYY-MM-DD): "); s = input("Subjects: ")
        pair = (i, d)
        subs = list(set([p.strip() for p in s.split(",") if p.strip()]))
        bag.append({"pair": pair, "name": n, "age": a, "grade": g, "subjects": subs})
        print("Saved.")
    elif op == "2":
        if not bag: print("Empty."); continue
        for it in bag:
            i, d = it["pair"]
            print("Student ID: %s | Name: %s | Age: %s | Grade: %s | DOB: %s | Subjects: %s" % (i, it["name"], it["age"], it["grade"], d, ", ".join(it["subjects"])))
    elif op == "3":
        who = int(input("ID to change: ")); ok=False
        for it in bag:
            if it["pair"][0] == who:
                ok=True
                ch = input("1 Age 2 Subjects: ")
                if ch == "1": it["age"] = int(input("New age: "))
                elif ch == "2": it["subjects"] = list(set([q.strip() for q in input("New subjects: ").split(",") if q.strip()]))
                print("Updated."); break
        if not ok: print("Not found.")
    elif op == "4":
        who = int(input("ID to delete: ")); idx=-1
        for i in range(len(bag)):
            if bag[i]["pair"][0] == who: idx=i; break
        if idx!=-1: del bag[idx]; print("Deleted.")
        else: print("Missing.")
    elif op == "5":
        unique = set()
        for it in bag: unique |= set(it["subjects"])
        print("Subjects Offered:", ", ".join(sorted(unique)) if unique else "None")
    elif op == "6":
        print("Goodbye"); break
    else:
        print("Try again.")
