
import cv2
import pygame

from vision.camera import Camera
from vision.hand_tracker import HandTracker
from vision.gesture_detector import GestureDetector

from game.shape_manager import ShapeManager
from game.renderer import Renderer


def main():

    camera = Camera()

    tracker = HandTracker()

    detector = GestureDetector()

    renderer = Renderer()

    shape_manager = ShapeManager()

    current_shape = None

    preview_x = 600
    preview_y = 400

    last_fist_state = False

    running = True

    while running:

        frame = camera.get_frame()

        if frame is None:
            continue

        frame, hands = tracker.process_frame(frame)

        frame_height, frame_width, _ = frame.shape

        for hand in hands:

            label = hand["label"]

            landmarks = hand["landmarks"]

            # LEFT HAND → SHAPE SELECTION
            if label == "Left":

                selected_shape = detector.detect_shape(
                    landmarks
                )

                if selected_shape:
                    current_shape = selected_shape

            # RIGHT HAND → MOVEMENT + PLACEMENT
            elif label == "Right":
                index_tip = landmarks.landmark[8]

                target_x = int(index_tip.x * renderer.WIDTH)
                target_y = int(index_tip.y * renderer.HEIGHT)

                preview_x = int(preview_x * 0.85 + target_x * 0.15)
                preview_y = int(preview_y * 0.85 + target_y * 0.15)

                current_fist = detector.is_fist(landmarks)

                if current_fist and not last_fist_state:
                    if current_shape:
                        shape_manager.add_shape(
                            current_shape,
                            preview_x,
                            preview_y
                        )

                last_fist_state = current_fist

        # KEYBOARD EVENTS
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_z:
                    shape_manager.undo()

                elif event.key == pygame.K_r:
                    shape_manager.clear()

                elif event.key == pygame.K_ESCAPE:
                    running = False

        renderer.render(
            shape_manager.shapes,
            current_shape,
            preview_x,
            preview_y
        )

        cv2.imshow(
            "Hand Tracking",
            frame
        )

        if cv2.waitKey(1) & 0xFF == 27:
            running = False

    camera.release()

    pygame.quit()

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()