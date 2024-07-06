import face_recognition
import cv2

# Load the image
image_path = "C:\\Users\\ronro\\Downloads\\DSC_8977 copy.JPG"
image = cv2.imread(image_path)

# Check if image loading was successful
if image is None:
    print(f"Error: Could not load image from {image_path}")
    exit()  

# Detect faces (no need for manual conversions)
face_locations = face_recognition.face_locations(image)

# Draw rectangles around the faces
for (top, right, bottom, left) in face_locations:
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

# Display the resulting image
cv2.imshow('Faces Detected', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
