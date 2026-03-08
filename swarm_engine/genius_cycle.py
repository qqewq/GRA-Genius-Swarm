from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated, List
import operator
from agents.meta_controller import MetaController
from agents.obnul_agent import run_obnul # Заглушки импортов
from agents.heisenberg_agent import run_heisenberg
from agents.llm_genius import run_llm_genius
from config import NUM_AGENTS_TARGET

class SwarmState(TypedDict):
    messages: Annotated[List[str], operator.add]
    current_solution: dict
    iteration: int
    coherence_score: float

def build_genius_graph():
    workflow = StateGraph(SwarmState)
    
    # Добавляем узлы
    workflow.add_node("gra_obnul", run_obnul)
    workflow.add_node("gra_heisenberg", run_heisenberg)
    workflow.add_node("llm_genius", run_llm_genius)
    
    meta_agent = MetaController()
    
    def meta_router(state):
        result = meta_agent.evaluate(state)
        if result["action"] == "RESET":
            return "gra_obnul"
        return END

    # Определяем связи (Цикл Гения)
    # 1. Обнуление -> Гейзенберг
    workflow.add_edge("gra_obnul", "gra_heisenberg")
    
    # 2. Гейзенберг -> LLM
    workflow.add_edge("gra_heisenberg", "llm_genius")
    
    # 3. LLM -> Мета-контроль (Условный переход)
    workflow.add_conditional_edges(
        "llm_genius",
        meta_router,
        {"gra_obnul": "gra_obnul", "__end__": END}
    )
    
    # Точка входа
    workflow.set_entry_point("gra_obnul")
    
    return workflow.compile()

if __name__ == "__main__":
    print(f"🚀 Запуск GRA-Genius-Swarm (Target: {NUM_AGENTS_TARGET} agents)...")
    app = build_genius_graph()
    
    initial_state = {
        "messages": ["Initiating Multiverse Obnulenko Protocol"],
        "current_solution": {},
        "iteration": 0,
        "coherence_score": 0.0
    }
    
    # Запуск цикла (симуляция одного прохода для демо)
    # В реальности здесь будет цикл while или рекурсивный вызов для N агентов
    try:
        final_state = app.invoke(initial_state, config={"recursion_limit": 50})
        print("✅ Цикл завершен. Финальное состояние:", final_state['current_solution'])
    except Exception as e:
        print(f"⚠️ Ошибка в цикле (ожидаемо для обучения): {e}")