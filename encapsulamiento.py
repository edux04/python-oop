class Character:
    def __init__(self, width, height, color, speed):
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed


# Crear los personajes
player1 = Character(
    50,
    50,
    (255, 0, 0),
    2,
)

print(player1.speed)
