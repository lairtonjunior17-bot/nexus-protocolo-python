"""Núcleo de progresso do NEXUS.

Guarda o XP, as conquistas e as habilidades do jogador em painel/progresso.json
e gera painel/progresso.js, que o painel web lê para se desenhar.

Na Semana 2, este arquivo será substituído por uma integração com o Supabase.
Até lá, ele é um bom exemplo de automação: Python lendo e escrevendo arquivos.
"""

import json
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ARQUIVO_JSON = RAIZ / "painel" / "progresso.json"
ARQUIVO_JS = RAIZ / "painel" / "progresso.js"


def carregar():
    """Lê o progresso salvo. Se o arquivo não existir, começa do zero."""
    if ARQUIVO_JSON.exists():
        return json.loads(ARQUIVO_JSON.read_text(encoding="utf-8"))
    return {"jogador": "", "conquistas": [], "habilidades": []}


def salvar(dados):
    """Grava o JSON e gera o arquivo .js que o painel carrega."""
    texto = json.dumps(dados, ensure_ascii=False, indent=2)
    ARQUIVO_JSON.write_text(texto + "\n", encoding="utf-8")
    ARQUIVO_JS.write_text(
        "// Arquivo gerado automaticamente por nucleo/progresso.py. Não edite.\n"
        f"window.PROGRESSO = {texto};\n",
        encoding="utf-8",
    )


def xp_total(dados):
    """Soma o XP de todas as conquistas."""
    return sum(conquista["xp"] for conquista in dados["conquistas"])


def registrar_conquista(id_conquista, titulo, xp):
    """Registra uma conquista uma única vez. Devolve True se ela for nova."""
    dados = carregar()
    ja_existe = any(c["id"] == id_conquista for c in dados["conquistas"])
    if ja_existe:
        return False
    dados["conquistas"].append(
        {"id": id_conquista, "titulo": titulo, "xp": xp, "data": date.today().isoformat()}
    )
    salvar(dados)
    return True


def registrar_habilidade(nome):
    """Adiciona uma habilidade, se ela ainda não tiver sido desbloqueada."""
    dados = carregar()
    if nome in dados["habilidades"]:
        return False
    dados["habilidades"].append(nome)
    salvar(dados)
    return True


if __name__ == "__main__":
    # Rodar este arquivo diretamente mostra um resumo do progresso.
    dados = carregar()
    print(f"Jogador: {dados['jogador']}")
    print(f"XP total: {xp_total(dados)}")
    for conquista in dados["conquistas"]:
        print(f"  {conquista['xp']:+5d} XP  {conquista['titulo']}")
