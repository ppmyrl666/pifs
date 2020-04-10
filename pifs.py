# calculate pi using BBP formula
c_get_16sj = 100  # constant in get_16sj
d_get_16x_mod_y = {}  # dictionary to accelerate power->mod calculation
print_search_flag = True  # if you want to monitor the speed of search
print_search_gap = 100
max_power_in_2 = 25  # search at max 2^25 step after pi


def decimal(x):
    if x < 0:
        raise Exception("Invalid input to decimal", x)
    else:
        return x - int(x)


# calculate (16^x) mod y
def get_16x_mod_y(x, y):
    # way4
    if y == 1:
        return 0

    if x == 0:
        return 1

    pow_all = x
    pow_1 = 1
    r = 1

    for i in range(0, max_power_in_2):
        if pow_all < pow_1:
            break
        pow_1 *= 2

    pow_1 /= 2
    for j in range(1, i + 1):
        if pow_all >= pow_1:
            r = (r*16) % y
            pow_all = pow_all - pow_1
        pow_1 /= 2
        if pow_1 >= 1:
            r = (r*r) % y

    return r

    # way3
    """
    if x == 0:
        return 1
    elif x == 1:
        return 16 % y
    else:
        pow_all = x
        pow_1_pre = 2
        pow_1 = 2
        n = 0

        for i in range(0, max_power_in_2):
            if pow_all > pow_1:
                n += 1
                pow_1_pre = pow_1
                pow_1 = pow_1 * 2
            elif pow_all == pow_1:
                n += 1
                pow_1_pre = pow_1
                break
            else:
                break

        pow_2 = pow_all - pow_1_pre

        r1 = 16 % y
        for i in range(0, n):
            r1 = (r1**2) % y

        if pow_2 == 0:
            r = r1
        else:
            r2 = get_16x_mod_y(pow_2, y)
            r = (r1*r2) % y

        return r
    """

    # way2
    """
    if x == 0:
        d_get_16x_mod_y[(x, y)] = 1
        return 1
    if (x, y) in d_get_16x_mod_y:
        return d_get_16x_mod_y[(x, y)]
    else:
        d_get_16x_mod_y[(x, y)] = (d_get_16x_mod_y[(x - 1, y)] * 16) % y
        return d_get_16x_mod_y[(x, y)]
    """

    # way1
    """
    # y != 1
    print(x,y,end="")
    output = 1
    if x == 0:
        print(" ",output)
        return output
    else:
        while x > 0:
            output = (16 * output) % y
            x -= 1
        print(" ", output)
        return output
    """


# calculate decimal part of BBP(BBP is divided into four parts with j=1,2,5,6)
def get_16sj(j, d):
    output = 0
    for k in range(d, -1, -1):
        output = output + get_16x_mod_y(d - k, 8 * k + j) / (8 * k + j)
        output = decimal(output)
    for k in range(d + 1, d + c_get_16sj):
        output = output + (16 ** (d - k)) / (8 * k + j)
        output = decimal(output)
    return output


# calculate the nth hex number in pi,n start with 0
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


# find hex string in hex pi sequence
def find_s_in_pi(s):
    len_s = len(s)
    pos = 0
    pi = {0: 3}
    found = False

    while not found:

        if pos % print_search_gap == 0 and print_search_flag == True:
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


# main
s_raw = input("please input hex string:\n")
s = []
for word in s_raw:
    s.append(int(word, 16))
pos = find_s_in_pi(s)
print("s with length", len(s), "found in pos", pos)

"""
for x in range(0, pos+len(s)+1):
    print(hex(n_in_pi(x))[2:], end="")
    if x == 0:
        print(".", end="")
"""
# 3.243f6a8885a308d313198a2e03707344a4093822299f31d008
