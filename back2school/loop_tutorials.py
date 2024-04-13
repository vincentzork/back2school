def for_loop():
    for i in range (10):
        print(i)

def for_asdf():
    for a in "asdf":
        print(a)

def for_foo():
    for a in [0,1,2,"foo","bar"]:
        print(a)

def for_range():
    for a in range(5, 10, 2):
        print(a)

def for_list_total():
    total = 0
    for cost in prices:
        total += cost
    print(f"Total: ${total}")

prices = [10, 20, 61, 309]
for_list_total()






