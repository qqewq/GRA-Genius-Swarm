import jax.numpy as jnp
from jax import grad, jit
from config import K_LEVELS, LAMBDA_0, ALPHA_DECAY

class FoamFunctional:
    """
    Вычисляет функционал пены Φ для уровня l и его градиент.
    Φ(l)(Ψ, G) = Σ |<Ψ(a)| P_G |Ψ(b)>|^2 для a != b
    """
    
    def __init__(self, level_idx):
        self.l = level_idx
        self.weight = LAMBDA_0 * (ALPHA_DECAY ** level_idx)

    def compute_foam(self, states, projector_matrix):
        """
        states: список векторов состояния Ψ для подсистем уровня l
        projector_matrix: матрица проектора P_G
        """
        n = len(states)
        foam_val = 0.0
        
        # Векторизованное вычисление для скорости (JAX)
        # Для демонстрации используем цикл, в продакшене - jax.vmap
        for i in range(n):
            for j in range(i + 1, n):
                psi_a = states[i]
                psi_b = states[j]
                
                # <Psi_a | P | Psi_b>
                overlap = jnp.dot(jnp.conj(psi_a), jnp.dot(projector_matrix, psi_b))
                foam_val += jnp.abs(overlap) ** 2
                
        return self.weight * foam_val

    @jit
    def gradient_step(self, states, projector_matrix, lr=0.01):
        """
        Один шаг градиентного спуска для минимизации пены.
        Ψ(t+1) = Ψ(t) - η * ∇Φ
        """
        def loss_fn(all_states):
            # Распаковка для вычисления (упрощено для примера)
            # В реальности нужно передавать структуру состояний
            return self.compute_foam(list(all_states), projector_matrix)

        # Вычисление градиентов по всем состояниям одновременно
        grads = grad(loss_fn)(tuple(states))
        
        new_states = []
        for i, state in enumerate(states):
            update = state - lr * grads[i]
            # Нормализация состояния после шага
            new_states.append(update / jnp.linalg.norm(update))
            
        return new_states