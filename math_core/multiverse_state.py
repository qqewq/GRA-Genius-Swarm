import jax.numpy as jnp
from config import K_LEVELS

class MultiverseState:
    """
    Управляет полным состоянием мультиверса Ψ = {Ψ(a)} для всех мультииндексов.
    """
    def __init__(self, dimensions_per_level):
        """
        dimensions_per_level: dict {level: dim_vector}
        """
        self.levels = {}
        self.dimensions = dimensions_per_level
        
        # Инициализация случайными состояниями
        for l in range(K_LEVELS + 1):
            dim = self.dimensions.get(l, 10)
            count = 2 ** l # Примерное число подсистем на уровне
            # Создаем набор состояний для уровня l
            self.levels[l] = [jnp.random.normal(size=(dim,)) for _ in range(count)]

    def get_level_states(self, level):
        return self.levels.get(level, [])

    def update_level(self, level, new_states):
        self.levels[level] = new_states

class ProjectorHierarchy:
    """
    Создает иерархию проекторов P_G для целей каждого уровня.
    В реальной реализации это зависит от конкретной задачи (математика, физика).
    Здесь заглушка: единичная матрица или случайный подпространство.
    """
    def __init__(self, dim):
        self.dim = dim
        # Проектор на "идеальное" решение (заглушка: первые 5 базисных векторов)
        rank = min(5, dim)
        P = jnp.zeros((dim, dim))
        P = P.at[:rank, :rank].set(jnp.eye(rank))
        self.matrix = P

    def get_projector(self):
        return self.matrix