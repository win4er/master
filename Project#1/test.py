import cv2

config_file = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model = 'frozen_inference_graph.pb'

model = cv2.dnn_DetectionModel(frozen_model, config_file)

classLabels = []
file_name = 'Labels.txt'
with open(file_name, 'rt') as fpt:
    classLabels = fpt.read().rstrip('\n').split('\n')

model.setInputSize(300, 300)
model.setInputScale(1.0 / 127.5)  # 255 / 2 = 127.5
model.setInputMean((127.5, 127.5, 127.5))  # mobilenet => [-1, 1]
model.setInputSwapRB(True)


cap = cv2.VideoCapture()

if not cap.isOpened():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 450)
if not cap.isOpened():
    raise IOError('Cannot open video')

font_scale = 3
font = cv2.FONT_HERSHEY_PLAIN
while True:
    ret, frame = cap.read()

    ClassIndex, confidence, bbox = model.detect(frame, confThreshold=0.5)

    if len(ClassIndex) != 0:
        for ClassInd, conf, boxes in zip(ClassIndex.flatten(), confidence.flatten(), bbox):
            if ClassInd <= len(classLabels)-1:
                cv2.rectangle(frame, boxes, (255, 0, 0), 2)
                cv2.putText(
                    frame,
                    classLabels[ClassInd-1],
                    (boxes[0]+10, boxes[1]+40),
                    font,
                    fontScale=font_scale,
                    color=(0, 255, 0),
                    thickness=2
                )
                cv2.putText(
                    frame,
                    str((conf * 100) // 1) + '%',
                    (boxes[0] + 200, boxes[1] + 30),
                    cv2.FONT_HERSHEY_COMPLEX,
                    1,
                    (0, 255, 0),
                    2
                )
    cv2.imshow('Object Detection', frame)

    if cv2.waitKey(2) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
