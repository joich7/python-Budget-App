orange = [{"withdraw":1, "beer":5},{"withdraw": 5}, {"skunk":4}, {"withdraw": 5}, {"ribbet": 56}]
sum = 0


def check():
    sum = 0
    for i in orange:
        if "withdraw" in i.keys():
            sum += i["withdraw"]
    return sum
print(check())