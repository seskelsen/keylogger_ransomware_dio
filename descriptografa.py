from cryptography.fernet import Fernet
import os

#1. Carregar a chave de criptografia

def carregar_chave():
    return open("chave.key", "rb").read()

#2. Descriptografar um único arquivo

def descriptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados_criptografados = file.read()
    try:
        dados_descriptografados = f.decrypt(dados_criptografados)
        with open(arquivo, "wb") as file:
            file.write(dados_descriptografados)
        print(f"Arquivo {arquivo} descriptografado com sucesso.")
    except Exception as e:
        print(f"Erro ao descriptografar {arquivo}: {e}")

#3. Encontrar arquivos para descriptografar

def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            # Descriptografar apenas arquivos que não são scripts Python, chave ou mensagem de resgate
            if (not nome.endswith((".py", ".key")) and
                nome != "LEIA ISSO.TXT" and
                nome != "decrypt.py"):
                lista.append(caminho)
    return lista

#4. Remover mensagem de resgate

def remover_mensagem_resgate():
    if os.path.exists("LEIA ISSO.TXT"):
        os.remove("LEIA ISSO.TXT")
        print("Mensagem de resgate removida.")

#5. Função principal

def main():
    # Verificar se a chave existe
    if not os.path.exists("chave.key"):
        print("Erro: Arquivo chave.key não encontrado!")
        print("Não é possível descriptografar sem a chave.")
        return

    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")

    if not arquivos:
        print("Nenhum arquivo encontrado para descriptografar.")
        return

    print(f"Encontrados {len(arquivos)} arquivos para descriptografar.")

    for arquivo in arquivos:
        descriptografar_arquivo(arquivo, chave)

    remover_mensagem_resgate()
    print("Todos os arquivos foram descriptografados com sucesso!")

if __name__ == "__main__":
    main()
