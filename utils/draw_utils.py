import cv2

def draw_bounding_box(frame, box, color):
    x1, y1, x2, y2 = box
    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)

def draw_crib_area(frame, crib_area, color):
    cv2.rectangle(frame, (crib_area[0], crib_area[1]),
                  (crib_area[2], crib_area[3]), color, 2)

def draw_alert_text(frame, text, position=(50,50), color=(0,0,255)):
    cv2.putText(frame, text, position, cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
