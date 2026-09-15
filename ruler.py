def ruler(n_inches, m_length):
    draw_line(m_length, 0)
    for j in range(n_inches):
        draw_interval(m_length - 1)
        draw_line(m_length, j + 1)

def draw_interval(m):
    if m <= 0:
        return
    draw_interval(m - 1)
    draw_line(m)
    draw_interval(m - 1)

def draw_line(n, label=-1):
    print('-' * n, end='')
    if label >= 0:
        print(f" {label}", end='')
    print()

ruler(10, 3)