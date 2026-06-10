# ============================================================
# ORBIS SENTINEL - Otimização da Altura da Antena
# Global Solution 2026 - FIAP
# Marcos Vinícios Corrêa dos Santos - RM 571080
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

# ===========================================================================
# E(x) - Função que calcula a eficiência da antena.
#
# Retorna:
#   float: eficiência da antena
# =============================================================================
def E(x):
    return -(x**6)/6 + 3*x**5 - (85/4)*x**4 + 75*x**3 - 137*x**2 + 120*x

# ===========================================================================
# derivada_E(x) - Função que calcula a primeira derivada de E(x).
#
# Retorna:
#   float: primeira derivada de E(x)
# =============================================================================
def derivada_E(x):
    return -(x**5) + 15*x**4 - 85*x**3 + 225*x**2 - 274*x + 120

# =============================================================================
# segunda_derivada_E(x) - Função que calcula a segunda derivada de E(x).
#
# Retorna:
#   float: segunda derivada de E(x)
# =============================================================================
def segunda_derivada_E(x):
    return -5*x**4 + 60*x**3 - 255*x**2 + 450*x - 274

# =============================================================================
# newton_raphson(x0) - Função que calcula os pontos críticos de E(x).
#
# Retorna:
#   float: pontos críticos de E(x)
# =============================================================================
def newton_raphson(x0):
    x = x0

    for i in range(100):
        x_novo = x - derivada_E(x) / segunda_derivada_E(x)

        if abs(x_novo - x) < 0.000001:
            return x_novo

        x = x_novo

    return x

# =============================================================================
# classificar_ponto(x) - Função que classifica os pontos críticos.
#
# Retorna:
#   str: "Máximo Local" ou "Mínimo Local"
# =============================================================================
def classificar_ponto(x):
    if segunda_derivada_E(x) < 0:
        return "Máximo Local"
    else:
        return "Mínimo Local"

# ===========================================================================
# gerar_grafico() - Função que gera o gráfico de E(x).
# ===========================================================================
def gerar_grafico(pontos):
    x = np.linspace(0, 6, 1000)
    y = E(x)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label="E(x)")

    for ponto in pontos:
        plt.scatter(ponto, E(ponto), s=60)
        plt.text(ponto, E(ponto), f"({ponto:.1f})")

    plt.xlabel("Altura da antena (x100 m)")
    plt.ylabel("Eficiência")
    plt.title("Eficiência da Antena Orbis Sentinel")
    plt.grid()
    plt.legend()

    plt.show()

# =============================================================================
# main() - Função principal que executa o algoritmo de Newton-Raphson.
# =============================================================================
def main():
    print("=" * 60)
    print("ORBIS SENTINEL - MÉTODO DE NEWTON-RAPHSON")
    print("=" * 60)

    chutes = [0.5, 1.5, 3.0, 4.5, 5.5]
    pontos = []

    for chute in chutes:
        raiz = newton_raphson(chute)

        if not any(abs(raiz - p) < 0.001 for p in pontos):
            pontos.append(raiz)

    print("\nPONTOS CRÍTICOS ENCONTRADOS:\n")

    for ponto in pontos:
        print(f"x = {ponto:.4f}")
        print(f"E(x) = {E(ponto):.4f}")
        print(classificar_ponto(ponto))
        print("-" * 30)

    print("\nCONCLUSÃO:")

    print(
        "A altura de aproximadamente 300 metros "
        "apresentou boa eficiência e maior estabilidade, "
        "sendo recomendada para a instalação da antena."
    )

    gerar_grafico(pontos)

if __name__ == "__main__":
    main()