
TICK = "-"


def draw_line(length, label=""):
    line = TICK * length
    if label:
        line += " " + label
    print(line)
    pass


def draw_interval(length):
    if length <= 0:
        # Do nothing
        pass
    elif length == 1:
        draw_line(length)
    else:
        draw_interval(length-1)
        draw_line(length)
        draw_interval(length-1)
    pass


def draw_ruler(scale, major_tick=4):
    # Draw line 0
    draw_line(major_tick, "0")

    for i in range(1, scale+1):
        draw_interval(major_tick-1)
        draw_line(major_tick, str(i))
    pass


if __name__ == "__main__":
    draw_ruler(2, 4)
    print("#########")

    draw_ruler(1, 5)
    print("#########")

    draw_ruler(10, 1)