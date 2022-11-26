from fer import FER
import cv2

emotion_detector = FER(mtcnn=True)


def emotion_func(img_src):
    test_img_low_quality = cv2.imread(img_src)
    emotion_detector.detect_emotions(test_img_low_quality)
    dominant_emotion, emotion_score = emotion_detector.top_emotion(test_img_low_quality)
    print(dominant_emotion, emotion_score)
    return str(dominant_emotion)
