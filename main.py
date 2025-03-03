from enviroment import create_environment
from value_iteration import value_iteration
from policy import get_policy
from agent import simulate_agent
from animation import animate_path


# Ejecución principal
if __name__ == "__main__":
    # Crear entorno
    env, start, goal, holes = create_environment()
    
    # Resolver MDP
    values = value_iteration(env)
    policy = get_policy(env, values)
    
    # Simular agente
    path = simulate_agent(env, policy, start)
    
    # Visualizar resultados
    print("Política óptima:")
    print(policy)
    print("\nCamino óptimo:", path)
    
    # Mostrar animación y guardar GIF (requiere pillow)
    animate_path(env, path, start, goal, holes, save_gif=True)