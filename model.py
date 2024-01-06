class GameModel:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x_coordinate = width // 2
        self.y_coordinate = height
        self.is_left_pressed = False
        self.is_right_pressed = False
        self.speed = 10
        self.imgBackground = "./img/background.jpg"

    def update_position(self):
        if self.x_coordinate == 0:
            self.x_coordinate = self.width
        elif self.x_coordinate == self.width:
            self.x_coordinate = 0

        if self.is_left_pressed:
            self.x_coordinate -= self.speed
        elif self.is_right_pressed:
            self.x_coordinate += self.speed