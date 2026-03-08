import random

def simulate_superconductor_search():
    print("🔬 Симуляция поиска сверхпроводника (Tc > 300K)...")
    best_tc = 0
    for i in range(10000):
        # Случайный поиск в пространстве параметров
        tc = random.uniform(100, 400)
        if tc > best_tc:
            best_tc = tc
        if tc > 300:
            print(f"💥 НАЙДЕН МАТЕРИАЛ! Tc = {tc:.2f}K")
            return tc
    print(f"Лучший результат: Tc = {best_tc:.2f}K")
    return best_tc