def is_inside_crib(box, crib_area):
    x1, y1, x2, y2 = box
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2
    crib_x1, crib_y1, crib_x2, crib_y2 = crib_area
    return crib_x1 <= cx <= crib_x2 and crib_y1 <= cy <= crib_y2
