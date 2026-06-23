import cv2
import mediapipe as mp


class HandTracker:

    def __init__(self):

        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.mp_draw = mp.solutions.drawing_utils

    def process_frame(self, frame):

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.hands.process(rgb_frame)

        detected_hands = []

        if results.multi_hand_landmarks and results.multi_handedness:

            for landmarks, handedness in zip(
                    results.multi_hand_landmarks,
                    results.multi_handedness):

                label = handedness.classification[0].label

                detected_hands.append({
                    "label": label,
                    "landmarks": landmarks
                })

                self.mp_draw.draw_landmarks(
                    frame,
                    landmarks,
                    self.mp_hands.HAND_CONNECTIONS
                )

        return frame, detected_hands