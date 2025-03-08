def open_doors(n):
    open_doors = [i for i in range(1, n+1) if (i**0.5).is_integer()]
    closed_doors = n - len(open_doors)
    
    print(f"Open doors: {open_doors}")
    print(f"Total Open: {len(open_doors)}")
    print(f"Total Closed: {closed_doors}")

open_doors(100)
