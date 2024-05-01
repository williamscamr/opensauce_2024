import cv2, time
import requests
import numpy as np

def prepare_frame(frame):
    # Convert frame to JPEG format
    _, encoded_image = cv2.imencode('.jpg', frame)
    # Convert encoded image data to bytes
    image_bytes = encoded_image.tobytes()
    return image_bytes

# Function to send frame to API
def send_frame_to_api(frame):
    # Replace 'your_api_endpoint' with the actual API endpoint
    api_endpoint = "https://api.brickognize.com/predict/"
    # Prepare frame for export to API
    image_bytes = prepare_frame(frame)
    #request body
    payload = {"query_image": ("frame.jpg", image_bytes, "image/jpeg")}
    # Make the API call
    response = requests.post(api_endpoint, files=payload)
    # Handle the response as needed
    if response.status_code == 200:
        print("your did it")
        response_json = response.json()
    
        # Access the 'items' array
        items = response_json["items"]
    
        # Iterate over the items (if there are multiple)
        for item in items:
            # Retrieve the name of the item
            name = item["name"]
            print("Name:", name)
    else:
        print(f"status code: {response.status_code}")
        print("Error: ", response.text)

first_frame = None


video = cv2.VideoCapture(0)
waitAsecondFrame = 0;
contourCount = 0;

while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        if waitAsecondFrame == 10:
            first_frame = gray
        waitAsecondFrame+=1
        continue

    #get delta frame
    delta_frame = cv2.absdiff(first_frame,gray)

    #in future, use this to go "ok the brick is on screen, wait until
    #there is barely a difference in the background again before
    #sending another image over to brickognize. also make sure to get a clear
    #position of where the brick is so you can send as clear of a picture
    #as possible
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)

    #find all objects, might use this might not
    cnts , _ =cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    
    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        (x, y, w, h)=cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3)

    cv2.imshow("Delta Frame",delta_frame)
    cv2.imshow("Capturing",gray)
    cv2.imshow("Threshold",thresh_frame)
    cv2.imshow("Color Frame", frame)

    key=cv2.waitKey(1)
    #print(gray)
    #print(delta_frame)

    

    if key==ord('a'):
        send_frame_to_api(frame)
        break

    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows

