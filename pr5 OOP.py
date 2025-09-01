
class PersonA:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        cls = "PersonA"
        return cls + "(" + "name=" + str(self.name) + ", age=" + str(self.age) + ")"

class EmployeeA(PersonA):
    def __init__(self, name, age, code="", pay=0.0):
        super().__init__(name, age)
        self.__badge = str(code)
        self.__package = float(pay)

    # encapsulation
    def code(self): return self.__badge
    def code_set(self, new_code): self.__badge = str(new_code)
    def pay(self): return self.__package
    def pay_set(self, value):
        value = float(value)
        if value < 0: print("Invalid pay")
        else: self.__package = value

    # 'overloading' via alternative constructors
    @classmethod
    def from_core(cls, name, age, code):
        return cls(name, age, code, 0.0)
    @classmethod
    def hydrate(cls, d):
        return cls(d.get("name",""), d.get("age",0), d.get("employee_id",""), d.get("salary",0))

    def __str__(self):
        return "EmployeeA(name=" + str(self.name) + ", age=" + str(self.age) + ", code=" + str(self.__badge) + ", pay=$" + str(self.__package) + ")"
    # comparison operators -> pay based
    def __eq__(self, other): return isinstance(other, EmployeeA) and self.pay() == other.pay()
    def __lt__(self, other): return isinstance(other, EmployeeA) and self.pay() < other.pay()
    def __gt__(self, other): return isinstance(other, EmployeeA) and self.pay() > other.pay()

    def exhibit(self): print(self)

class ManagerA(EmployeeA):
    def __init__(self, name, age, code, pay, dept):
        super().__init__(name, age, code, pay)
        self.dept = dept
    def exhibit(self):
        print(super().__str__() + " | team: " + str(self.dept))

class DeveloperA(EmployeeA):
    def __init__(self, name, age, code, pay, lang):
        super().__init__(name, age, code, pay)
        self.lang = lang
    def exhibit(self):
        print(super().__str__() + " | code lang: " + str(self.lang))

print("check:", issubclass(ManagerA, EmployeeA), issubclass(DeveloperA, EmployeeA))

roster = []
registry = {}

def banner():
    print("\n--- People Registry ---")
    print("1) New PersonA")
    print("2) New EmployeeA")
    print("3) New ManagerA")
    print("4) New DeveloperA")
    print("5) Show")
    print("6) Compare Pay")
    print("7) Exit")

while True:
    banner()
    pick = input("Choose: ").strip()
    if pick == "1":
        nm = input("Name: "); ag = int(input("Age: "))
        roster.append(PersonA(nm, ag))
        print("saved")
    elif pick == "2":
        nm = input("Name: "); ag = int(input("Age: "))
        cd = input("ID Code: "); py = float(input("Package: "))
        e = EmployeeA(nm, ag, cd, py); registry[e.code()] = e; print("ok")
    elif pick == "3":
        nm = input("Name: "); ag = int(input("Age: "))
        cd = input("ID Code: "); py = float(input("Package: ")); dp = input("Team: ")
        m = ManagerA(nm, ag, cd, py, dp); registry[m.code()] = m; print("ok")
    elif pick == "4":
        nm = input("Name: "); ag = int(input("Age: "))
        cd = input("ID Code: "); py = float(input("Package: ")); lg = input("Code Lang: ")
        d = DeveloperA(nm, ag, cd, py, lg); registry[d.code()] = d; print("ok")
    elif pick == "5":
        print("a) PersonAs  b) EmployeeA by id  c) all EmployeeA")
        sub = input("-> ").strip().lower()
        if sub == "a":
            if not roster: print("none")
            for i, p in enumerate(roster, 1): print(i, p)
        elif sub == "b":
            key = input("id: "); obj = registry.get(key)
            if obj: obj.exhibit()
            else: print("not found")
        else:
            if not registry: print("empty")
            for v in registry.values(): v.exhibit()
    elif pick == "6":
        a = input("id1: "); b = input("id2: ")
        x = registry.get(a); y = registry.get(b)
        if not x or not y: print("missing")
        else:
            if x == y: print("same pay")
            elif x > y: print(a, "earns more than", b)
            else: print(a, "earns less than", b)
    elif pick == "7":
        print("bye"); break
    else:
        print("wrong")
