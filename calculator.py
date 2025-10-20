# ...existing code...
def add(ns): return sum(ns)
def sub(ns):
    r = ns[0]
    for x in ns[1:]: r -= x
    return r
def mul(ns):
    r = 1
    for x in ns: r *= x
    return r
def div(ns):
    r = ns[0]
    for x in ns[1:]:
        if x == 0: raise ZeroDivisionError("division by zero")
        r /= x
    return r

ops = {'+': add, '-': sub, '*': mul, '/': div}
while True:
    op = input("Operator (+ - * /) or 'exit': ").strip()
    if op.lower() in ('exit', 'quit'): break
    if op not in ops:
        print("Use only +, -, *, /"); continue

    raw = input("Enter operands (space or comma separated): ").strip()
    parts = raw.replace(',', ' ').split()
    try:
        nums = [float(x) for x in parts]
    except ValueError:
        print("Invalid number found. Try again."); continue
    if not nums:
        print("No operands entered."); continue

    # require at least two operands for - and /
    if op in ('-', '/') and len(nums) < 2:
        print(f"Operator '{op}' needs at least two operands."); continue

    try:
        print("Result:", ops[op](nums))
    except Exception as e:
        print("Error:", e)
# ...existing code...