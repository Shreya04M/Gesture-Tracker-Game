class GestureDetector:

    @staticmethod
    def count_fingers(hand_landmarks):

        tips = [8, 12, 16, 20]

        fingers = 0

        for tip in tips:

            if hand_landmarks.landmark[tip].y < \
               hand_landmarks.landmark[tip - 2].y:

                fingers += 1

        return fingers

    def detect_shape(self, hand_landmarks):

        count = self.count_fingers(
            hand_landmarks
        )

        if count == 0:
            return "Square"

        elif count == 1:
            return "Rectangle"

        elif count == 2:
            return "Triangle"

        elif count >= 4:
            return "Circle"

        return None

    def is_fist(self, hand_landmarks):

        return self.count_fingers(
            hand_landmarks
        ) == 0