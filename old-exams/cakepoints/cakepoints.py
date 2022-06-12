
with open('input.txt') as file:
    with open('output.txt', 'w') as out:
        for line in file:
            name, data = line.strip().split(':')
            frac, ops = data.split(' ')
            cashed, earned = map(int, frac.split('/'))

            earned += ops.count('+')
            cashed += ops.count('-')

            out.write(f"{name}:{cashed}/{earned}\n")

