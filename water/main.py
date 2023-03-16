import direct.directbase.DirectStart
from pandac.PandaModules import *
from direct.showbase.DirectObject import DirectObject

# Paramètres de la simulation
CELL_SIZE = 1
WATER_LEVEL = 200
GRAVITY = 9.81
WATER_DENSITY = 1000
DAMPING = 0.03
dt = 0.1

# Création de la grille de cellules
num_rows = 50
num_cols = 50
cells = [[0] * num_cols for i in range(num_rows)]

# Création de la scène
base.setBackgroundColor(0, 0, 1)
camera.setPos(0, -100, 50)
camera.setHpr(0, -90, 0)
plane = loader.loadModel("models/plane")
plane.setScale(num_cols * CELL_SIZE, num_rows * CELL_SIZE, 1)
plane.reparentTo(render)

# Boucle principale
class WaterSimulation(DirectObject):
    def __init__(self):
        self.accept("escape", self.quit)
        taskMgr.add(self.update, "update")

    def update(self, task):
        # Simulation de l'eau
        for row in range(num_rows):
            for col in range(num_cols):
                # Calcul de la force gravitationnelle
                force = WATER_DENSITY * GRAVITY * CELL_SIZE**2
                # Calcul de la hauteur de la cellule
                height = WATER_LEVEL - cells[row][col]
                # Application de la force gravitationnelle
                acceleration = force / WATER_DENSITY
                velocity = acceleration * dt
                # Application de l'amortissement
                velocity = velocity - DAMPING * velocity
                # Mise à jour de la hauteur de la cellule
                cells[row][col] += velocity

                # Déformation du plan de la scène
                x = col * CELL_SIZE
                y = row * CELL_SIZE
                plane.setZ(x, y, cells[row][col])

        return task.cont

    def quit(self):
        base.userExit()

ws = WaterSimulation()
run()
