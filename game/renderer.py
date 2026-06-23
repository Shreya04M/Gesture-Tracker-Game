import pygame


class Renderer:

    WIDTH = 1200
    HEIGHT = 800

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode(
            (self.WIDTH, self.HEIGHT)
        )

        pygame.display.set_caption(
            "Gesture Builder"
        )

        self.font = pygame.font.SysFont(
            "Arial",
            24
        )

    def draw_shape(self, shape_type, x, y, preview=False):

        if shape_type == "Square":

            color = (120, 120, 255) if preview else (50, 100, 255)

            pygame.draw.rect(
                self.screen,
                color,
                (x - 30, y - 30, 60, 60)
            )

        elif shape_type == "Rectangle":

            color = (255, 220, 100) if preview else (255, 200, 0)

            pygame.draw.rect(
                self.screen,
                color,
                (x - 50, y - 25, 100, 50)
            )

        elif shape_type == "Circle":

            color = (255, 120, 120) if preview else (255, 80, 80)

            pygame.draw.circle(
                self.screen,
                color,
                (x, y),
                35
            )

        elif shape_type == "Triangle":

            color = (120, 255, 120) if preview else (80, 220, 80)

            pygame.draw.polygon(
                self.screen,
                color,
                [
                    (x, y - 40),
                    (x - 40, y + 40),
                    (x + 40, y + 40)
                ]
            )

    def render(
        self,
        placed_shapes,
        preview_shape,
        preview_x,
        preview_y
    ):

        self.screen.fill((18, 18, 22))

        info_text = self.font.render(
            "LEFT: Select | RIGHT: Move | FIST: Place | Z: Undo | R: Clear",
            True,
            (180, 180, 180)
        )

        self.screen.blit(info_text, (20, 10))

        shape_text = self.font.render(
            f"Current Shape: {preview_shape}",
            True,
            (255, 255, 255)
        )

        self.screen.blit(shape_text, (20, 45))

        for shape in placed_shapes:

            self.draw_shape(
                shape.shape_type,
                shape.x,
                shape.y
            )

        if preview_shape:

            self.draw_shape(
                preview_shape,
                preview_x,
                preview_y,
                True
            )

            pygame.draw.circle(
                self.screen,
                (255, 255, 255),
                (preview_x, preview_y),
                4
            )

        pygame.display.flip()