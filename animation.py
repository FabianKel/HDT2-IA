import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


grid_size = 4
reward_goal = 1
reward_hole = -1
reward_step = -0.01
gamma = 0.9  # Factor de descuento

# Visualización animada con capacidad de guardar GIF
def animate_path(env, path, start, goal, holes, save_gif=False):
    fig, ax = plt.subplots()
    
    # Dibujar la cuadrícula
    for i in range(grid_size + 1):
        ax.axhline(i, color='black', lw=2)
        ax.axvline(i, color='black', lw=2)
    
    # Dibujar elementos estáticos
    ax.text(start[1]+0.5, grid_size-start[0]-0.5, 'S', ha='center', va='center', 
            color='blue', fontsize=14, weight='bold')
    ax.text(goal[1]+0.5, grid_size-goal[0]-0.5, 'G', ha='center', va='center', 
            color='green', fontsize=14, weight='bold')
    for hole in holes:
        ax.text(hole[1]+0.5, grid_size-hole[0]-0.5, 'H', ha='center', va='center', 
                color='red', fontsize=14, weight='bold')
    
    # Configuración del gráfico
    ax.set_xlim(0, grid_size)
    ax.set_ylim(0, grid_size)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Trayectoria del Agente en Frozen Lake")
    
    # Preparar animación
    point, = ax.plot([], [], 'bo', markersize=20)
    
    def init():
        point.set_data([], [])
        return point,
    
    def update(frame):
        x, y = path[frame]
        # Convertir coordenadas a formato de gráfico
        plot_y = grid_size - x - 0.5
        plot_x = y + 0.5
        point.set_data([plot_x], [plot_y])  # Corregir aquí: usar listas
        return point,
    
    ani = FuncAnimation(fig, update, frames=len(path), 
                       init_func=init, blit=True, interval=500)
    
    if save_gif:
        try:
            ani.save('trayectoria_agente.gif', writer='pillow', fps=2)
            print("GIF guardado correctamente!")
        except Exception as e:
            print(f"Error al guardar GIF: {e}")
    
    plt.show()
