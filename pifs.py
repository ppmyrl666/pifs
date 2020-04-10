c_get_16sj = 1000  # constant in get_16sj


def decimal(x):
    if x < 0:
        raise Exception("Invalid input to decimal", x)
    else:
        return x - int(x)


# avoid too large x in get_16sj calculation
def get_16x_mod_y(x, y):
    # y != 1
    output = 1
    if x == 0:
        return output
    else:
        while x > 0:
            output = (16 * output) % y
            x -= 1
        return output


def get_16sj(j, d):
    output = 0
    for k in range(0, d + 1):
        output = output + get_16x_mod_y(d - k, 8 * k + j) / (8 * k + j)
        output = decimal(output)
    for k in range(d + 1, d + c_get_16sj):
        output = output + (16 ** (d - k)) / (8 * k + j)
        output = decimal(output)
    return output


def n_in_pi(n):
    if n == 1:
        return 3
    else:
        d = n - 2
        fd = 4 + 4 * decimal(get_16sj(1, d)) - 2 * decimal(get_16sj(4, d)) - decimal(get_16sj(5, d)) - decimal(get_16sj(6, d))
        fd = decimal(fd)
        fd = int(fd * 16)
        return fd


for x in range(1, 100):
    print(hex(n_in_pi(x))[2:], end="")
    if x == 1:
        print(".", end="")
