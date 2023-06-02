result = []

def divider(a, b):
    if a < b:
        raise ValueError("ValueError: a < b")
    if b > 100:
        raise IndexError("IndexError: b > 100")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, (): 15, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except ValueError as e:
        print(e)
    except IndexError as e:
        print(e)
    except Exception as e:
        print("Exception:", e)

print(result)
