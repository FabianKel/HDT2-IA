import numpy as np


grid_size = 4
reward_goal = 1
reward_hole = -1
reward_step = -0.01
gamma = 0.9  # Factor de descuento
# Definir las acciones posibles
ACTIONS = {
    'UP': 0,
    'DOWN': 1,
    'LEFT': 2,
    'RIGHT': 3
}

# Función de transición
def move(state, action):
    x, y = state
    if action == 'UP': x = max(0, x-1)
    elif action == 'DOWN': x = min(grid_size-1, x+1)
    elif action == 'LEFT': y = max(0, y-1)
    elif action == 'RIGHT': y = min(grid_size-1, y+1)
    return (x, y)

# Algoritmo de iteración de valores
def value_iteration(env, theta=1e-6):
    values = np.zeros((grid_size, grid_size))
    while True:
        delta = 0
        for i in range(grid_size):
            for j in range(grid_size):
                if env[i,j] in [reward_goal, reward_hole]: continue
                v = values[i,j]
                max_value = -np.inf
                for action in ACTIONS:
                    x, y = move((i,j), action)
                    reward = env[x,y] + reward_step
                    max_value = max(max_value, reward + gamma * values[x,y])
                values[i,j] = max_value
                delta = max(delta, abs(v - values[i,j]))
        if delta < theta: break
    return values