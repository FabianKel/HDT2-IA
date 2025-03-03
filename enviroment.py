import numpy as np

# Definir el tamaño del entorno
grid_size = 4

# Definir las recompensas
reward_goal = 1
reward_hole = -1

def create_environment(seed=40):
    np.random.seed(seed)
    env = np.zeros((grid_size, grid_size))
    start = (0, 0)
    goal = (grid_size-1, grid_size-1)
    env[goal] = reward_goal

    # Generación de hoyos
    num_holes = np.random.randint(1, 4)
    holes = []
    for _ in range(num_holes):
        while True:
            hole = (np.random.randint(grid_size), np.random.randint(grid_size))
            if hole not in [start, goal] and hole not in holes:
                env[hole] = reward_hole
                holes.append(hole)
                break
    return env, start, goal, holes