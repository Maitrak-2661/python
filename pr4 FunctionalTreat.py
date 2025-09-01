# Project: Functional Treat
# Student: Dev

DATA = {"shape":"1D","vals":[]}

def input_data():
    """Get 1D or 2D list from user."""
    global DATA
    m = input("1D=1 / 2D=2: ")
    if m=="2":
        r=int(input("rows: ")); t=[]
        for i in range(r):
            t.append([int(x) for x in input("row-"+str(i+1)+": ").split()])
        DATA={"shape":"2D","vals":t}
    else:
        DATA={"shape":"1D","vals":[int(x) for x in input("numbers: ").split()]}
    print("ok")

def basic_show():
    """Display len/min/max/sum and grid if 2D."""
    if DATA["shape"]=="1D":
        a=DATA["vals"]; 
        if not a: print("none"); return
        print(f"len={len(a)} min={min(a)} max={max(a)} sum={sum(a)} avg={round(sum(a)/len(a),2)}")
    else:
        g=DATA["vals"]; flat=[n for r in g for n in r]
        if not flat: print("none"); return
        print("total", len(flat), "min", min(flat), "max", max(flat), "sum", sum(flat))
        for r in g: print(r)

def rec(n): return 1 if n<=1 else n*rec(n-1)

def rec_menu():
    """Ask and print factorial."""
    n = int(input("n: ")); print("n!=", rec(n))

def lambox():
    """Lambda: keep <= threshold then add 5 via map."""
    if DATA["shape"]!="1D": print("need 1D"); return
    arr=DATA["vals"]; 
    if not arr: print("none"); return
    t=int(input("keep <= : "))
    k=list(filter(lambda v:v<=t,arr))
    print("kept:",k); print("plus5:",list(map(lambda v:v+5,k)))

def pack():
    """Return multi stats."""
    seq=DATA["vals"] if DATA["shape"]=="1D" else [n for r in DATA["vals"] for n in r]
    if not seq: return None
    return min(seq),max(seq),sum(seq),sum(seq)/len(seq)

def sort_now():
    """Sort 1D inplace or sorted rows for 2D."""
    if DATA["shape"]=="1D":
        a=DATA["vals"]; 
        if not a: print("none"); return
        a.sort(reverse=(input("2 for desc else asc: ")=="2")); print("sorted:",a)
    else:
        for r in [sorted(r) for r in DATA["vals"]]: print(r)

def show_args(*a): print("args:",a)
def show_kwargs(**k): print("stats:",k)

def show_menu():
    print("\n1.Input 2.Summary 3.Factorial 4.Filter 5.Sort 6.Stats 7.Docs 8.Exit")

def docs():
    for f in [input_data,basic_show,rec_menu,lambox,sort_now,pack,show_args,show_kwargs]:
        print(f.__name__,":",(f.__doc__ or '').strip())

while True:
    show_menu()
    s=input("-> ")
    if s=="1": input_data()
    elif s=="2": basic_show()
    elif s=="3": rec_menu()
    elif s=="4": lambox()
    elif s=="5": sort_now()
    elif s=="6":
        r=pack()
        if r: mn,mx,sm,av=r; show_args(mn,mx,sm,round(av,2)); show_kwargs(minimum=mn,maximum=mx,total=sm,average=round(av,2))
        else: print("none")
    elif s=="7": docs()
    elif s=="8": print("exit"); break
    else: print("again")

