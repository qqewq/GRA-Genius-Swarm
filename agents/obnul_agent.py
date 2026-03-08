from .base_agent import BaseGRAAgent
from math_core.foam_functional import FoamFunctional
from math_core.multiverse_state import ProjectorHierarchy
import jax.numpy as jnp

class GRAObnulAgent(BaseGRAAgent):
    def __init__(self, level=0):
        super().__init__(f"Obnul-L{level}", "Local Zeroing")
        self.level = level
        self.foam_func = FoamFunctional(level)

    def act(self, state):
        """
        Выполняет шаг обнуления пены для текущего уровня.
        """
        current_states = state['multiverse'].get_level_states(self.level)
        if not current_states:
            return state
            
        # Создаем проектор для цели уровня
        dim = len(current_states[0])
        projector = ProjectorHierarchy(dim).get_projector()
        
        # Градиентный шаг для минимизации Φ
        new_states = self.foam_func.gradient_step(current_states, projector)
        
        state['multiverse'].update_level(self.level, new_states)
        state['messages'].append(f"[{self.name}] Обнуление пены уровня {self.level} выполнено.")
        return state