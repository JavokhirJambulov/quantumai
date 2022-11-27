# We used FER library to recognize the emotions of the people
# https://github.com/justinshenk/fer
from fer import FER
import cv2

# set the mtcnn false to use haar cascade to detect emotions
emotion_detector = FER(mtcnn=False)

# Function to detect emotions of the face
def emotion_func(img_src):
    #Using opencv to decode the images
    test_img_low_quality = cv2.imread(img_src)
    emotion_detector.detect_emotions(test_img_low_quality)
    # Will return the top emotion of the face
    dominant_emotion, emotion_score = emotion_detector.top_emotion(test_img_low_quality)
    print(dominant_emotion, emotion_score)
    return str(dominant_emotion)
