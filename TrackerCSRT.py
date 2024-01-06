import cv2

cap = cv2.VideoCapture('./TrackingVideo.mp4')

if not cap.isOpened():
    print("Error opening video file")
    exit()

ret, frame = cap.read()

if not ret:
    print("Error reading frame from video source")
    exit()

# Select two ROIs from the first frame
bbox1 = cv2.selectROI("Select ROI for object 1", frame, fromCenter=False, showCrosshair=True)
bbox2 = cv2.selectROI("Select ROI for object 2", frame, fromCenter=False, showCrosshair=True)

# Create two tracker instances
tracker1 = cv2.TrackerCSRT_create()
tracker2 = cv2.TrackerCSRT_create()

# Initialize the trackers with the corresponding ROIs
ok1 = tracker1.init(frame, bbox1)
ok2 = tracker2.init(frame, bbox2)

# Specify the output video file
output_file = 'output.mp4'
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Update the trackers with the new frame
    ok1, bbox1 = tracker1.update(frame)
    ok2, bbox2 = tracker2.update(frame)

    # If the tracking was successful, draw bounding boxes
    if ok1:
        x1, y1, w1, h1 = [int(val) for val in bbox1]
        cv2.rectangle(frame, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 2)
    
    if ok2:
        x2, y2, w2, h2 = [int(val) for val in bbox2]
        cv2.rectangle(frame, (x2, y2), (x2 + w2, y2 + h2), (0, 0, 255), 2)

    # Write the modified frame to the output video file
    out.write(frame)

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
print("Output video path:", output_file)
