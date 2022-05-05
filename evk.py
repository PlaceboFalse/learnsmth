def EVK(a, b):
    # pirnt(a, b)
    if b == 0:
        return print(a)
    else:
        c = a % b
        EVK(b, c)


if __name__ == "__main__":
    EVK(100, 150)
