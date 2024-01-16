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


class Ground:
    def __init__(self, friction):
        self.friction = friction

    def applyFriction(self, character):
        character.speed *= self.friction


# Crear la instancia de la clase Ground
ground = Ground(friction=0.9)

# Aplicar la fricción a los personajes
ground.applyFriction(player1)

print(player1.speed)
