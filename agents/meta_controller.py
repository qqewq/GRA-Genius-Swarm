from langchain_core.agents import AgentExecutor
from math_core.beauty_score import beauty_score
from config import COHERENCE_THRESHOLD

class MetaController:
    def __init__(self):
        self.name = "Meta-Controller"
        self.reset_count = 0

    def evaluate(self, state_dict):
        """
        Оценивает состояние роя.
        Если coherence < threshold, инициирует сброс (GRA-Obnul).
        """
        current_phi = state_dict.get("current_solution", {})
        
        # Оценка красоты/согласованности
        b_score = float(beauty_score(current_phi, ideal_name="elegant_symmetry"))
        
        print(f"[META] Beauty Score: {b_score:.4f} | Threshold: {COHERENCE_THRESHOLD}")
        
        if b_score < COHERENCE_THRESHOLD:
            self.reset_count += 1
            return {
                "action": "RESET",
                "reason": f"Low coherence ({b_score:.4f})",
                "target_node": "gra_obnul"
            }
        else:
            return {
                "action": "PROCEED",
                "reason": "High coherence achieved",
                "target_node": "END"
            }

    def log_stats(self):
        print(f"[META] Total Resets Triggered: {self.reset_count}")