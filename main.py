import cv2
from config.settings import CRIB_AREA, CAMERA_ID, ALERT_COLOR, SAFE_COLOR, CRIB_COLOR
from detection.yolo_detector import YOLODetector
from detection.crib_checker import is_inside_crib
from utils.draw_utils import draw_bounding_box, draw_crib_area, draw_alert_text
from utils.alert_utils import alert_console, alert_sound

cap = cv2.VideoCapture(CAMERA_ID)

detector = YOLODetector()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = detector.detect(frame)
    alert = False

    for det in results.boxes:
        x1, y1, x2, y2 = det.xyxy[0].tolist()
        cls = int(det.cls[0])
        if cls == 0:
            box = (x1, y1, x2, y2)
            color = SAFE_COLOR
            if not is_inside_crib(box, CRIB_AREA):
                alert = True
                color = ALERT_COLOR
                draw_alert_text(frame, "ALERT! Baby left crib!")
            draw_bounding_box(frame, box, color)

    draw_crib_area(frame, CRIB_AREA, CRIB_COLOR)

    if alert:
        alert_console("ALERT! Baby left the crib!")
        alert_sound()

    cv2.imshow("Baby Monitor", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
