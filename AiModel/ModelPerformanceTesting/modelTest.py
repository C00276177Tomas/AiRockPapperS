from ultralytics import YOLO
import cv2

# Load your trained model (adjust the path if different)
model = YOLO("best (3).pt")

# Open the webcam (0 = default camera; change if you have multiple)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Run YOLO prediction on the frame
    results = model.predict(source=frame, conf=0.5, show=False, stream=True)

    # results is a generator; we loop through it
    for r in results:
        # Plot results on the frame
        annotated_frame = r.plot()

        # Show the frame
        cv2.imshow("YOLOv11 Detection", annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
