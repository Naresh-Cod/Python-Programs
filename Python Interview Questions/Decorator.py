def decorator(func):
    def distinction(marks):
        for m in marks:
            if m >= 75:
                print("Distinction")
        func(marks)
    return distinction

@decorator
def result(marks):
    for m in marks:
        if m >= 33:
            pass
        else:
            print("FAIL")
            break
    else:
        print("PASS")
result([34, 55, 75, 80])