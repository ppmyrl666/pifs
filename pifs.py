c_get_16sj = 100  # constant in get_16sj
d_get_16x_mod_y = {}


# calculate pi using BBP formula
def decimal(x):
    if x < 0:
        raise Exception("Invalid input to decimal", x)
    else:
        return x - int(x)


# avoid too large x in get_16sj calculation
def get_16x_mod_y(x, y):
    if x == 0:
        d_get_16x_mod_y[(x, y)] = 1
        return 1

    if (x, y) in d_get_16x_mod_y:
        return d_get_16x_mod_y[(x, y)]
    else:
        d_get_16x_mod_y[(x, y)] = (d_get_16x_mod_y[(x - 1, y)] * 16) % y
        return d_get_16x_mod_y[(x, y)]
    """
    # y != 1
    output = 1
    if x == 0:
        return output
    else:
        while x > 0:
            output = (16 * output) % y
            x -= 1
        return output
    """


def get_16sj(j, d):
    output = 0

    for k in range(d, -1, -1):
        output = output + get_16x_mod_y(d - k, 8 * k + j) / (8 * k + j)
        output = decimal(output)
    for k in range(d + 1, d + c_get_16sj):
        output = output + (16 ** (d - k)) / (8 * k + j)
        output = decimal(output)
    return output


def n_in_pi(n):
    if n == 0:
        return 3
    else:
        d = n - 1
        fd = 4 + 4 * decimal(get_16sj(1, d)) - 2 * decimal(get_16sj(4, d)) - decimal(get_16sj(5, d)) - decimal(
            get_16sj(6, d))
        fd = decimal(fd)
        fd = int(fd * 16)
        return fd


def find_s_in_pi(s):
    len_s = len(s)
    pos = 0
    pi = {0: 3}
    found = False

    while not found:

        if pos % 10 == 0:
            print("search to ", pos)

        for i in range(0, len_s):
            if pos + i in pi:
                pass
            else:
                pi[pos + i] = n_in_pi(pos + i)

            if pi[pos + i] == s[i]:
                if i == (len_s - 1):
                    found = True
            else:
                del pi[pos]
                pos += 1
                break

    return pos


s = [5, 5, 6, 15]
pos = find_s_in_pi(s)
print("s with length", len(s), "found in pos", pos)

"""
for x in range(0, pos+len(s)+1):
    print(hex(n_in_pi(x))[2:], end="")
    if x == 0:
        print(".", end="")
"""
