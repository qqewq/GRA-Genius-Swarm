import multiprocessing as mp
from config import NUM_AGENTS_TARGET

def worker_process(agent_id):
    # Симуляция работы одного агента
    return f"Agent {agent_id} completed task."

def run_parallel_swarm(num_agents=None):
    if num_agents is None:
        num_agents = NUM_AGENTS_TARGET
    
    print(f"⚡ Запуск параллельного роя из {num_agents} агентов...")
    
    # Ограничим для демо, чтобы не повесить ПК
    demo_count = min(num_agents, 100) 
    
    with mp.Pool(processes=4) as pool:
        results = pool.map(worker_process, range(demo_count))
        
    print(f"✅ Выполнено {len(results)} задач параллельно.")
    return results