import cv2 #type:ignore
import face_recognition #type:ignore

# Initialize video capture
video_capture = cv2.VideoCapture(0)  # 0 for default webcam

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Find all face locations in the frame
    face_locations = face_recognition.face_locations(frame)

    a =1
    # Draw rectangles around the faces
    for top, right, bottom, left in face_locations:
        
        a+=1
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, a), 2)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close windows
video_capture.release()
cv2.destroyAllWindows()
