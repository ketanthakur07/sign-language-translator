import cv2
import mediapipe as mp

class SignLanguageDetector:
    def __init__(self):
        self.hands = mp.solutions.hands.Hands()
        self.drawing = mp.solutions.drawing_utils

    def detect(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)

        label = "No Sign"
        if results.multi_hand_landmarks:
            for hand in results.multi_hand_landmarks:
                self.drawing.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)
                label = "Sign Detected"

        return frame, label
