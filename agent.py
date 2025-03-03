from value_iteration import move

grid_size = 4

# Simulación del agente
def simulate_agent(env, policy, start):
    state = start
    path = [state]
    while state != (grid_size-1, grid_size-1):
        action = policy[state]
        state = move(state, action)
        path.append(state)
    return path