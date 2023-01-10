from DRCF import *

m = 5
def grab_tool(tool):
    if tool == 1:
        pos_boven_j = posj(5.8, 52.5, 41.5, 0.0, 85.9, 7.5)
        pos_boven_t = posx(687.3, 69.8, 251.9, 5.8, 179.9, 7.5)

        pos_j = posj(5.8, 55.2, 49.6, 0.0, 75.2, 7.5)
        pos_t = posx(687.3, 69.8, 168.2, 5.8, 180.0, 7.5)

        pos_rotated_j = posj(5.8, 55.2, 49.6, 0.0, 75.2, 7.5 + 45)
        pos_rotated_t = posx(687.3, 69.8, 168.2, 5.8, 180.0, 52.4)

        pos_boven_rotated_j = posj(5.8, 52.5, 41.5, 0.0, 85.9, 7.5 + 45)
        pos_boven_rotated_t = posx(687.3, 69.8, 251.9, 5.8, 180.0, 52.4)
    elif tool == 2:
        pos_boven_j = posj(-1.7, 51.9, 43.4, -0.0, 84.7, -90.0)
        pos_boven_t = posx(687.0, -20.4, 247.0, 1.2, -180.0, -87.1)

        pos_j = posj(-1.7, 54.6, 50.7, 0.0, 74.7, -90.0)
        pos_t = posx(687.1, -20.4, 168.6, 177.9, -180.0, 90.1)

        pos_rotated_j = posj(-1.7, 54.6, 50.7, 0.0, 74.7, -90.0 + 45)
        pos_rotated_t = posx(687.1, -20.4, 168.6, 177.9, -180.0, 134.0)

        pos_boven_rotated_j = posj(-1.7, 51.9, 43.4, -0.0, 84.7, -90.0 + 45)
        pos_boven_rotated_t = posx(687.1, -20.4, 247.0, 178.5, 180.0, 134.0)

    movej(pos_boven_j, a=10, v=10 * m)
    movel(pos_t, a=10, v=10 * m)
    # Cilinder
    movej(pos_rotated_j, a=10, v=10 * m)
    movel(pos_boven_rotated_t, a=10, v=10 * m)

def dump_tool(tool):
    if tool == 1:
        pos_boven_j = posj(5.8, 52.5, 41.5, 0.0, 85.9, 7.5)
        pos_boven_t = posx(687.3, 69.8, 251.9, 5.8, 179.9, 7.5)

        pos_j = posj(5.8, 55.2, 49.6, 0.0, 75.2, 7.5)
        pos_t = posx(687.3, 69.8, 168.2, 5.8, 180.0, 7.5)

        pos_rotated_j = posj(5.8, 55.2, 49.6, 0.0, 75.2, 7.5 + 45)
        pos_rotated_t = posx(687.3, 69.8, 168.2, 5.8, 180.0, 52.4)

        pos_boven_rotated_j = posj(5.8, 52.5, 41.5, 0.0, 85.9, 7.5 + 45)
        pos_boven_rotated_t = posx(687.3, 69.8, 251.9, 5.8, 180.0, 52.4)
    elif tool == 2:
        pos_boven_j = posj(-1.7, 51.9, 43.4, -0.0, 84.7, -90.0)
        pos_boven_t = posx(687.0, -20.4, 247.0, 1.2, -180.0, -87.1)

        pos_j = posj(-1.7, 54.6, 50.7, 0.0, 74.7, -90.0)
        pos_t = posx(687.1, -20.4, 168.6, 177.9, -180.0, 90.1)

        pos_rotated_j = posj(-1.7, 54.6, 50.7, 0.0, 74.7, -90.0 + 45)
        pos_rotated_t = posx(687.1, -20.4, 168.6, 177.9, -180.0, 134.0)

        pos_boven_rotated_j = posj(-1.7, 51.9, 43.4, -0.0, 84.7, -90.0 + 45)
        pos_boven_rotated_t = posx(687.1, -20.4, 247.0, 178.5, 180.0, 134.0)

    movej(pos_boven_rotated_j, a = 10, v = 10 * m)
    movel(pos_rotated_t, a = 10, v = 10 * m)
    # Cilinder
    movej(pos_j, a = 10, v = 10 * m)
    movel(pos_boven_t, a = 10, v = 10 * m)

