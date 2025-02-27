import numpy as np
import matplotlib.pyplot as plt

grid_size = 4

reward_goal = 1
reward_hole = -1

def create_environment(seed=42):
    np.random.seed(seed)
    
    # Inicializar la matriz del entorno
    env = np.zeros((grid_size, grid_size))
    
    # Definir el punto inicial y el punto de meta
    start = (0, 0)
    goal = (grid_size-1, grid_size-1)
    

    env[goal] = reward_goal
    
    # Se crean los hoyos de forma aleatoria
    num_holes = np.random.randint(1, 4)
    holes = []
    for _ in range(num_holes):
        while True:
            hole = (np.random.randint(0, grid_size), np.random.randint(0, grid_size))
            if hole != start and hole != goal and hole not in holes:
                env[hole] = reward_hole
                holes.append(hole)
                break
    
    return env, start, goal, holes

def plot_environment(env, start, goal, holes):
    fig, ax = plt.subplots()
    
    # Dibujar la cuadrícula
    for i in range(grid_size + 1):
        ax.axhline(i, color='black', lw=2)
        ax.axvline(i, color='black', lw=2)
    
    # Dibujar el punto inicial
    ax.text(start[1] + 0.5, grid_size - start[0] - 0.5, 'S', fontsize=14, ha='center', va='center', color='blue')
    
    # Dibujar el punto de meta
    ax.text(goal[1] + 0.5, grid_size - goal[0] - 0.5, 'G', fontsize=14, ha='center', va='center', color='green')
    
    # Dibujar los hoyos
    for hole in holes:
        ax.text(hole[1] + 0.5, grid_size - hole[0] - 0.5, 'H', fontsize=14, ha='center', va='center', color='red')
    
    # Configuraciones del gráfico
    ax.set_xlim(0, grid_size)
    ax.set_ylim(0, grid_size)
    ax.set_xticks(np.arange(grid_size))
    ax.set_yticks(np.arange(grid_size))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_title("Entorno Frozen Lake")
    plt.show()

# Crear el entorno y mostrarlo gráficamente
env, start, goal, holes = create_environment()
plot_environment(env, start, goal, holes)