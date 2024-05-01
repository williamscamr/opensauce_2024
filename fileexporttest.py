import cv2
import requests
import numpy as np

# Function to prepare frame for export to API
def prepare_frame(frame):
    # Convert frame to JPEG format
    _, encoded_image = cv2.imencode('.jpg', frame)
    # Convert encoded image data to bytes
    image_bytes = encoded_image.tobytes()
    return image_bytes

# Function to send frame to API
def send_frame_to_api(frame):
    # Replace 'your_api_endpoint' with the actual API endpoint
    api_endpoint = 'your_api_endpoint'
    # Prepare frame for export to API
    image_bytes = prepare_frame(frame)
    # Make the API call
    response = requests.post(api_endpoint, files={'frame': image_bytes})
    # Handle the response as needed
    print(response.status_code)

# Example usage:
# Capture the video feed
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if frame is captured successfully
    if not ret:
        break

    # Send frame to API
    send_frame_to_api(frame)

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()