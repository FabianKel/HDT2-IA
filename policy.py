import numpy as np
from value_iteration import move, ACTIONS

grid_size = 4
reward_goal = 1
reward_hole = -1
reward_step = -0.01
gamma = 0.9  # Factor de descuento

# Obtención de política óptima
def get_policy(env, values):
    policy = np.empty((grid_size, grid_size), dtype=object)
    for i in range(grid_size):
        for j in range(grid_size):
            if env[i,j] in [reward_goal, reward_hole]: continue
            best_action = None
            max_value = -np.inf
            for action in ACTIONS:
                x, y = move((i,j), action)
                value = env[x,y] + reward_step + gamma * values[x,y]
                if value > max_value:
                    max_value = value
                    best_action = action
            policy[i,j] = best_action
    return policy