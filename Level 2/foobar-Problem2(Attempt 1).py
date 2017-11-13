def answer(pegs):
    len_pegs = len(pegs)
    if (len_pegs) == 1:
        return [-1, -1]
    else:
        dist = []
        gear = [0 for i in range(0, len_pegs)]
        min_dist = pegs[1] - pegs[0]
        min_index = 0
        for i in range(0, len_pegs - 1):
            dist.append(pegs[i + 1] - pegs[i])
            if dist[i] < min_dist:
                min_dist = dist[i]
                min_index = i
        # print (dist)

        for radius in range(1, min_dist):
            current_index = min_index
            # print (radius, current_index )
            gear[current_index] = radius
            while current_index > 0:
                gear[current_index - 1] = dist[current_index - 1] - gear[current_index]
                current_index = current_index - 1

            current_index = min_index
            while current_index < len_pegs - 1:
                gear[current_index + 1] = dist[current_index] - gear[current_index]
                current_index = current_index + 1

            # print(gear)

            if gear[0] == gear[len_pegs - 1] * 2:
                #   print([gear[0],1])
                return [gear[0], 1]
                break
        else:
            return [-1, -1]


print(answer([4, 50]))
