import cv2
import compare_functions
import telegram_messenger
import emotion_detector

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam.
cap = cv2.VideoCapture(0)
# To use a video file as input
# cap = cv2.VideoCapture('filename.mp4')

last_person = 'Not recognized'
last_emotion = 'neutral'
while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    cropped_image = gray

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cropped_image = gray[y:y + h + 30, x:x + w + 30]
    
    # save the image
    if len(faces) >= 1:
        status = cv2.imwrite('images/test.jpeg', cropped_image)
        print("image saved " + str(len(faces)))
        current_emotion = emotion_detector.emotion_func('images/test.jpeg')
        person_name = compare_functions.compare_images('images/test.jpeg')
        if (last_person != person_name or last_emotion != current_emotion):
            telegram_messenger.send_emotion_and_person_on_door(person_name, current_emotion)
            telegram_messenger.send_image('images/test.jpeg')
            last_person = person_name
            last_emotion = current_emotion
    else:
        print('no face recognized')

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff

    if k == 27:
        break
# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows
