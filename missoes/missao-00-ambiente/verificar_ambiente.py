"""Verificador de ambiente da Missão 0 (NEXUS: Protocolo Python).

Confere se a estação de trabalho do estagiário está pronta.
Leia este arquivo com calma: na Semana 1 você vai entender cada linha.
"""

import shutil  # ferramentas para lidar com arquivos e programas do sistema
import subprocess  # permite executar outros programas a partir do Python
import sys  # informações sobre o próprio Python em execução
from pathlib import Path  # forma moderna de trabalhar com caminhos de pastas

PASTA_MISSAO = Path(__file__).parent
XP_POR_ETAPA = 20


def checar_versao_python():
    """O Python precisa ser 3.11 ou superior."""
    versao = sys.version_info
    ok = versao >= (3, 11)
    detalhe = f"versão {versao.major}.{versao.minor}.{versao.micro}"
    if not ok:
        detalhe += " (instale a 3.11 ou superior)"
    return ok, detalhe


def checar_ambiente_virtual():
    """Dentro de um venv, sys.prefix é diferente de sys.base_prefix."""
    ok = sys.prefix != sys.base_prefix
    detalhe = "ativo" if ok else "inativo (rode .venv\\Scripts\\Activate.ps1)"
    return ok, detalhe


def checar_pip():
    """Tenta executar 'python -m pip --version'."""
    resultado = subprocess.run(
        [sys.executable, "-m", "pip", "--version"],
        capture_output=True,
        text=True,
    )
    ok = resultado.returncode == 0
    detalhe = resultado.stdout.split(" from ")[0] if ok else "pip não encontrado"
    return ok, detalhe


def checar_git():
    """Procura o programa 'git' nas pastas do PATH."""
    ok = shutil.which("git") is not None
    detalhe = "instalado" if ok else "não encontrado (instale pelo git-scm.com)"
    return ok, detalhe


def checar_primeiro_script():
    """O arquivo ola_nexus.py precisa existir e usar input() e print()."""
    arquivo = PASTA_MISSAO / "ola_nexus.py"
    if not arquivo.exists():
        return False, "ola_nexus.py não encontrado nesta pasta"
    codigo = arquivo.read_text(encoding="utf-8")
    faltando = [funcao for funcao in ("input(", "print(") if funcao not in codigo]
    if faltando:
        return False, f"o script precisa usar: {', '.join(faltando)}"
    return True, "encontrado e com input() e print()"


def main():
    etapas = [
        ("Python 3.11+", checar_versao_python),
        ("Ambiente virtual", checar_ambiente_virtual),
        ("Instalador pip", checar_pip),
        ("Git", checar_git),
        ("Primeiro script", checar_primeiro_script),
    ]

    print("\n=== NEXUS LABS · VERIFICADOR DE AMBIENTE ===\n")
    xp_total = 0
    aprovadas = 0

    for nome, funcao in etapas:
        ok, detalhe = funcao()
        marcador = "[OK]   " if ok else "[FALHA]"
        print(f"{marcador} {nome:<18} {detalhe}")
        if ok:
            xp_total += XP_POR_ETAPA
            aprovadas += 1

    print(f"\nEtapas aprovadas: {aprovadas}/{len(etapas)}")
    print(f"XP obtido: {xp_total}")

    if aprovadas == len(etapas):
        print("\n>> CREDENCIAMENTO APROVADO. Missão 0 concluída. +100 XP")
    else:
        print("\n>> Credenciamento pendente. Corrija as falhas e rode de novo.")


if __name__ == "__main__":
    main()
