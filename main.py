import cv2
import compare_functions
import telegram_messenger
import emotion_detector
import time

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam.
cap = cv2.VideoCapture(0)
# To use a video file as input
# cap = cv2.VideoCapture('filename.mp4')

# To differentiate the last person and emotion
last_person = 'Not recognized'
last_emotion = 'neutral'
count_same_person =0
# To execute the code continuously
while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    cropped_image = gray

    # Draw the rectangle around each face and crop the image
    for (x, y, w, h) in faces:
        cropped_image = gray[y:y + h + 30, x:x + w + 30]
    
    # Save the image
    if len(faces) >= 1:
        status = cv2.imwrite('images/test.jpeg', cropped_image)
        print("image saved " + str(len(faces)))
        # To detect emotions
        current_emotion = emotion_detector.emotion_func('images/test.jpeg')
        # To detect faces of the people
        person_name = compare_functions.compare_images('images/test.jpeg')

        # To check if the face and emotion of the person  is the same
        if last_person == person_name and person_name != 'Unknown':
            # Used to count the same person
            count_same_person += 1
        else:
            count_same_person = 0
        print(count_same_person)
        if last_person != person_name or last_emotion != current_emotion:
            # If the face and emotion changes, it will send it to owner via Telegram
            if count_same_person<=3:
                time.sleep(1)
                telegram_messenger.send_emotion_and_person_on_door(person_name, current_emotion)
                telegram_messenger.send_image('images/test.jpeg')
            # To save the person's last known face and emotion
            last_person = person_name
            last_emotion = current_emotion
        time.sleep(1)
    else:
        print('no face recognized')

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff

    if k == 27:
        break
# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows
