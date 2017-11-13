from fractions import Fraction


def answer(pegs):
    len_pegs = len(pegs)

    if len_pegs < 2 or len_pegs > 20:
        return [-1, -1]

    r = 0
    dist = []

    # calculate the distance
    for i in range(0, len_pegs - 1):
        dist.append(pegs[i + 1] - pegs[i])

    # if number of pegs are odd
    if len_pegs % 2 != 0:
        total = (- pegs[0] - pegs[len_pegs - 1])
    else:
        # for even number of pegs
        total = (- pegs[0] + pegs[len_pegs - 1])

    if len_pegs > 2:
        for i in range(1, len_pegs - 1):
            total += 2 * (-1) ** (i + 1) * pegs[i]

    r = Fraction(2 * (float(total) / 3 if len_pegs % 2 == 0 else total)).limit_denominator()

    if r < 1:
        return [-1, -1]
    else:
        gear = []
        gear.append(r)
        current_index = 0
        while current_index < len_pegs - 1:
            next_gear = dist[current_index] - gear[current_index]
            if next_gear > 1:
                gear.append(next_gear)
                current_index = current_index + 1
            else:
                return [-1, -1]

        return [r.numerator, r.denominator]


print(answer([4, 30, 50]))
