"""Verificador da Missão 1: O cadastro quebrado.

Executa os seus scripts com dados de teste, como se uma pessoa estivesse
digitando, e compara a saída com o resultado esperado.
"""

import subprocess
import sys
from pathlib import Path

PASTA = Path(__file__).resolve().parent
sys.path.insert(0, str(PASTA.parent.parent / "nucleo"))
from progresso import registrar_conquista  # noqa: E402

# Cada teste: (texto digitado, trechos que precisam aparecer na saída)
TESTES = {
    "A": {
        "arquivo": "cadastro_quebrado.py",
        "titulo": "Parte A: consertar o script do estagiário anterior",
        "casos": [
            ("Ana\n300\n0.75\n", ["Cliente: Ana", "Consumo anual: 3600 kWh", "Gasto anual: R$ 2700.00"]),
            ("Bruno\n150\n0.92\n", ["Cliente: Bruno", "Consumo anual: 1800 kWh", "Gasto anual: R$ 1656.00"]),
        ],
    },
    "B": {
        "arquivo": "cadastro_cliente.py",
        "titulo": "Parte B: criar a ficha de cliente",
        "casos": [
            (
                "Ana\n30\n250.5\n",
                [
                    "Ficha do cliente: Ana",
                    "Idade: 30 anos",
                    "Ano de nascimento aproximado: 1996",
                    "Conta mensal: R$ 250.50",
                    "Gasto anual: R$ 3006.00",
                ],
            ),
            (
                "Carlos Lima\n45\n189.9\n",
                [
                    "Ficha do cliente: Carlos Lima",
                    "Idade: 45 anos",
                    "Ano de nascimento aproximado: 1981",
                    "Conta mensal: R$ 189.90",
                    "Gasto anual: R$ 2278.80",
                ],
            ),
        ],
    },
}

XP_POR_PARTE = 50


def normalizar(texto):
    """Ignora maiúsculas e espaços repetidos, para focar no conteúdo."""
    return " ".join(texto.lower().split())


def ultima_linha_do_erro(stderr):
    linhas = [linha for linha in stderr.strip().splitlines() if linha.strip()]
    return linhas[-1] if linhas else "erro desconhecido"


def verificar_parte(chave, config):
    arquivo = PASTA / config["arquivo"]
    print(f"\n--- {config['titulo']} ({config['arquivo']}) ---")

    if not arquivo.exists():
        print(f"[FALHA]  Arquivo {config['arquivo']} não encontrado nesta pasta.")
        return False

    for numero, (entrada, esperados) in enumerate(config["casos"], start=1):
        resultado = subprocess.run(
            [sys.executable, str(arquivo)],
            input=entrada,
            capture_output=True,
            text=True,
            timeout=10,
        )
        if resultado.returncode != 0:
            print(f"[FALHA]  Teste {numero}: o script parou com erro.")
            print(f"         {ultima_linha_do_erro(resultado.stderr)}")
            return False

        saida = normalizar(resultado.stdout)
        faltando = [e for e in esperados if normalizar(e) not in saida]
        if faltando:
            print(f"[FALHA]  Teste {numero}: a saída não contém:")
            for trecho in faltando:
                print(f"         '{trecho}'")
            return False
        print(f"[OK]     Teste {numero} aprovado.")

    return True


def main():
    print("\n=== NEXUS LABS · VERIFICADOR DA MISSÃO 1 ===")
    aprovadas = 0
    for chave, config in TESTES.items():
        if verificar_parte(chave, config):
            aprovadas += 1
            nova = registrar_conquista(f"missao-01-{chave}", config["titulo"], XP_POR_PARTE)
            if nova:
                print(f">> +{XP_POR_PARTE} XP registrados no painel.")
            else:
                print(">> Parte já registrada anteriormente.")

    print(f"\nPartes aprovadas: {aprovadas}/{len(TESTES)}")
    if aprovadas == len(TESTES):
        print(">> MISSÃO 1 CONCLUÍDA. O setor de Cadastro agradece.")


if __name__ == "__main__":
    main()
