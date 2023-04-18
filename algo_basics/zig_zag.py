with open('input.txt', 'r') as input_f, open('output.txt', 'w') as output_f:
    n, a, b = [row.strip().split() for row in input_f.readlines()]
    zig_zag = list()
    for i in range(int(n[0])):
        zig_zag.extend([a[i], b[i]])
    output_f.write(' '.join(zig_zag))
