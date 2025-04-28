class Colors:
    dark_grey = (26, 31, 40)  # PRAZNO
    green = (47, 230, 23)  # L
    red = (232, 18, 18)  # S
    orange = (226, 116, 17)  # I
    yellow = (237, 234, 4)  # D
    white = (255, 255, 255)
    dark_blue = (44, 44, 127)
    light_blue = (59, 85, 162)

    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow]
