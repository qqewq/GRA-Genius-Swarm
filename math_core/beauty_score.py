import jax.numpy as jnp
from jax import nn

def embed_structure(struct_data):
    """
    Простая функция эмбеддинга структуры (заглушка для реальной модели).
    Возвращает вектор представления структуры.
    """
    # В реальности здесь будет вызов небольшой нейросети или преобразование графа
    if isinstance(struct_data, dict):
        vec = jnp.array(list(struct_data.values()), dtype=jnp.float32)
    else:
        vec = jnp.array(struct_data, dtype=jnp.float32)
    
    # Нормализация
    return vec / (jnp.linalg.norm(vec) + 1e-8)

def beauty_score(struct, ideal_name="elegant_symmetry"):
    """
    Вычисляет B(s) = σ( Σ w_i * sim(h_i, ideal) )
    Возвращает значение от 0 до 1. >0.95 считается гениальным.
    """
    # Идеальные векторы для разных концепций (предобученные)
    ideals = {
        "elegant_symmetry": jnp.array([1.0, 0.8, 0.9, 0.95]),
        "deep_truth": jnp.array([0.9, 0.95, 0.85, 1.0]),
        "chaos_order": jnp.array([0.7, 0.7, 0.9, 0.8])
    }
    
    ideal_vec = ideals.get(ideal_name, ideals["elegant_symmetry"])
    struct_vec = embed_structure(struct)
    
    # Скалярное произведение как мера сходства
    similarity = jnp.dot(struct_vec, ideal_vec)
    
    # Сигмоида для нормализации
    score = nn.sigmoid(similarity * 5.0) # Усиливаем контраст
    
    return score