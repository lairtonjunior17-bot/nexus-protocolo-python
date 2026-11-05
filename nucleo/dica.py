"""Sistema de dicas do NEXUS.

Uso:
    python nucleo/dica.py missao-01 A 1

Mostra a dica e desconta o XP correspondente. Cada dica só é cobrada uma vez:
se você pedir a mesma dica de novo, ela aparece sem novo desconto.
"""

import json
import sys
from pathlib import Path

from progresso import RAIZ, registrar_conquista

CUSTOS = {"1": 5, "2": 15}


def main():
    if len(sys.argv) != 4:
        print("Uso: python nucleo/dica.py <missao> <parte> <nivel>")
        print("Exemplo: python nucleo/dica.py missao-01 A 1")
        return

    missao, parte, nivel = sys.argv[1], sys.argv[2].upper(), sys.argv[3]
    pastas = list((RAIZ / "missoes").glob(f"{missao}*"))
    if not pastas:
        print(f"Missão '{missao}' não encontrada.")
        return

    arquivo = pastas[0] / "dicas.json"
    dicas = json.loads(arquivo.read_text(encoding="utf-8"))
    texto = dicas.get(parte, {}).get(nivel)
    if texto is None or nivel not in CUSTOS:
        print("Dica não encontrada. Use a parte (A, B...) e o nível (1 ou 2).")
        return

    custo = CUSTOS[nivel]
    nova = registrar_conquista(
        f"dica-{missao}-{parte}-{nivel}",
        f"Dica {nivel} da {missao}, parte {parte}",
        -custo,
    )
    aviso = f"-{custo} XP" if nova else "já paga, sem novo desconto"
    print(f"\n=== DICA {nivel} · {missao} · parte {parte} ({aviso}) ===\n")
    print(texto)
    print()


if __name__ == "__main__":
    main()
