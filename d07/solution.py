def read_and_parse_file(file_path):
    circuit = {}

    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            ops, wire = line.strip().split(' -> ')
            circuit[wire] = ops.split(' ')

    return circuit


def evaluate(wire, evaluated, circuit):
    try:
        return int(wire)
    except ValueError:
        pass

    result = 0

    if wire not in evaluated:
        ops = circuit[wire]

        if len(ops) == 1:
            result = evaluate(ops[0], evaluated, circuit)

        elif len(ops) == 2:
            op = ops[0]
            right = evaluate(ops[1], evaluated, circuit)

            if op == 'NOT':
                result = ~right

        else:
            left = evaluate(ops[0], evaluated, circuit)
            op = ops[1]
            right = evaluate(ops[2], evaluated, circuit)

            if op == 'AND':
                result = left & right
            if op == 'OR':
                result = left | right
            if op == 'RSHIFT':
                result = left >> right
            if op == 'LSHIFT':
                result = left << right

        evaluated[wire] = result

    return evaluated[wire]


def solve():
    circuit = read_and_parse_file('input.txt')

    a = evaluate('a', dict(), circuit)

    print(f'After evaluating, wire A has value {a}')

    a = evaluate('a', dict(), circuit)
    circuit['b'] = [str(a)]
    a = evaluate('a', dict(), circuit)

    print(f'After overriding wire B, wire A has value {a}')


solve()
