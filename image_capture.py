import cv2

# Create a VideoCapture object to access the webcam (by default, it's the first camera)
cap = cv2.VideoCapture(0)

image_count = 0

# Define the custom save location (change this to your desired folder)
save_location = "D:/pet/"
while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Display the captured frame in a window
    cv2.imshow("Webcam", frame)

    # Check for the key press (spacebar to save an image, 'q' to quit)
    key = cv2.waitKeyEx(1)
    if key == 32:  # 32 is the key code for the spacebar
        image_count += 1
        image_filename = f"captured_image_{image_count}.png"
        # Combine the custom save location and the filename
        full_save_path = save_location + image_filename

        cv2.imwrite(full_save_path, frame)
        print(f"Image saved as {full_save_path}")
    elif key == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()