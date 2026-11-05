# Missão 0: Credenciamento

> **NEXUS LABS · Recursos Humanos · Mensagem automática**
>
> Bem-vindo à Nexus Labs, estagiário. Antes de receber acesso aos sistemas da empresa, você precisa montar sua estação de trabalho. Nenhuma demanda será liberada até que o verificador de ambiente confirme que está tudo em ordem.
>
> Boa sorte. Estamos de olho.

**Recompensa:** 100 XP · **Tempo estimado:** 60 a 90 minutos · **Dicas disponíveis:** peça ao Claude e informe o passo em que travou.

---

## Objetivos

1. Instalar o Python.
2. Instalar o Git.
3. Configurar o VS Code para Python.
4. Criar o repositório do projeto no GitHub e cloná-lo.
5. Criar e ativar um ambiente virtual.
6. Escrever e executar seu primeiro script.
7. Passar no verificador de ambiente.

> As instruções abaixo são para **Windows**. No **macOS**, use `python3` no lugar de `python` (antes de ativar o ambiente), `source .venv/bin/activate` para ativar o ambiente virtual e barras normais (`/`) nos caminhos. O instalador do Mac não tem a opção de PATH; ao final, rode o `Install Certificates.command` que aparece na pasta do Python.

---

## Passo 1: instalar o Python

1. Acesse **python.org/downloads** e clique no botão amarelo de download da versão estável mais recente (qualquer versão **3.11 ou superior** serve).
2. Abra o instalador. **Antes de clicar em instalar**, marque a caixa **"Add python.exe to PATH"** (adicionar o Python ao caminho do sistema). Esse é o erro mais comum de iniciantes: sem essa opção, o terminal não encontra o Python.
3. Clique em **Install Now** e aguarde.
4. Abra o **PowerShell** (menu Iniciar, digite "PowerShell") e confira:

```powershell
python --version
```

O resultado esperado é algo como `Python 3.13.x`. Se aparecer uma mensagem de erro ou abrir a Microsoft Store, volte ao item 2: o PATH não foi configurado.

## Passo 2: instalar o Git

1. Acesse **git-scm.com** e baixe o Git para Windows.
2. Instale mantendo as opções padrão.
3. Feche e abra o PowerShell de novo, depois confira:

```powershell
git --version
```

4. Configure sua identidade (ela aparece em cada commit do portfólio):

```powershell
git config --global user.name "Seu Nome"
```

```powershell
git config --global user.email "seu-email-do-github@exemplo.com"
```

## Passo 3: configurar o VS Code

1. Abra o VS Code e clique no ícone de **Extensões** na barra lateral (ou `Ctrl+Shift+X`).
2. Pesquise e instale a extensão **Python**, publicada pela **Microsoft**. Ela instala junto o Pylance, que dá autocompletar e aponta erros enquanto você digita.

## Passo 4: criar o repositório

1. No GitHub, crie um repositório chamado **`nexus-protocolo-python`**, público, sem README (vamos enviar o nosso).
2. **Me envie o nome do repositório aqui no chat.** Eu envio para ele a estrutura inicial que já preparei (documento de projeto, glossário e esta missão).
3. Depois, clone o repositório na sua máquina:

```powershell
cd ~\Documents
```

```powershell
git clone https://github.com/SEU-USUARIO/nexus-protocolo-python.git
```

```powershell
code nexus-protocolo-python
```

O último comando abre a pasta no VS Code. Daqui em diante, use o terminal do próprio VS Code (menu **Terminal > New Terminal**).

## Passo 5: criar o ambiente virtual

No terminal do VS Code, dentro da pasta do projeto:

```powershell
python -m venv .venv
```

Isso cria a pasta `.venv`, uma "caixa" isolada para as bibliotecas do projeto. Agora ative o ambiente:

```powershell
.venv\Scripts\Activate.ps1
```

Se der erro de "execução de scripts desabilitada", rode o comando abaixo uma única vez e tente ativar de novo:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

**Como saber se funcionou:** o início da linha do terminal passa a mostrar `(.venv)`. Sempre que abrir o projeto, ative o ambiente antes de trabalhar.

Por fim, atualize o instalador de pacotes:

```powershell
python -m pip install --upgrade pip
```

## Passo 6: seu primeiro script

Crie, na pasta desta missão, o arquivo **`ola_nexus.py`** e **digite** o código abaixo. Não copie e cole: digitar ajuda a memória a reaprender a sintaxe.

```python
# Meu primeiro script na Nexus Labs
nome = input("Digite seu nome, estagiário: ")
print(f"Credencial emitida para {nome}. Bem-vindo à Nexus Labs.")
```

Execute:

```powershell
python missoes\missao-00-ambiente\ola_nexus.py
```

### Ponte com Java

O mesmo programa em Java exigiria uma classe, um método `main`, um `Scanner` e ponto e vírgula:

```java
import java.util.Scanner;

public class OlaNexus {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Digite seu nome, estagiário: ");
        String nome = sc.nextLine();
        System.out.println("Credencial emitida para " + nome + ". Bem-vindo à Nexus Labs.");
    }
}
```

| Java | Python | Observação |
|---|---|---|
| `String nome = ...;` | `nome = ...` | Sem tipo declarado e sem ponto e vírgula. O Python descobre o tipo sozinho. |
| `Scanner` + `nextLine()` | `input("texto")` | O `input` já exibe a pergunta e devolve o que foi digitado, sempre como texto. |
| `"..." + nome + "..."` | `f"... {nome} ..."` | A *f-string* (o `f` antes das aspas) encaixa variáveis direto no texto. |
| `public static void main` | não existe | O Python executa o arquivo de cima para baixo. |

## Passo 7: verificador de ambiente

Com o ambiente virtual ativo, rode:

```powershell
python missoes\missao-00-ambiente\verificar_ambiente.py
```

Ele confere cada etapa e mostra o que falta. Quando aparecer **CREDENCIAMENTO APROVADO**, a missão está concluída.

## Entrega

Registre a conquista no Git (o `.venv` não vai junto, porque está no `.gitignore`):

```powershell
git add .
```

```powershell
git commit -m "Missão 0: ambiente configurado e primeiro script"
```

```powershell
git push
```

Depois, me mande aqui o resultado do verificador. Na próxima etapa, eu entrego a primeira versão do painel do jogo e a Apostila 1.

---

## Perguntas de entrevista sobre esta missão

Tente responder com suas palavras antes de seguir:

1. Para que serve um ambiente virtual em Python?
2. Qual é a diferença entre `pip` e `python`?
3. Por que o arquivo `.env` não deve ir para o GitHub?
4. O que é o PATH do sistema?
