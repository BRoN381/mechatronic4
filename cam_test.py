import cv2

# Initialize the video capture object
cap = cv2.VideoCapture(0)  # Use the correct camera index as discussed earlier

if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow("Camera Feed", frame)
    if cv2.waitKey(1) == ord("q"):
        break

# Release the video capture object when done
cap.release()
cv2.destroyAllWindows()
