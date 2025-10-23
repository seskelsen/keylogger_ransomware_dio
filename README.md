Descrição do Projeto
O objetivo deste laboratório é implementar, documentar e compartilhar experimentos práticos simulando o comportamento de malwares em ambiente seguro e 100% educacional. Foram desenvolvidas as seguintes etapas:

Ransomware Simulado: Criptografa/descriptografa arquivos testes, gera mensagem de resgate simulada.

Keylogger Simulado: Captura pressionamento de teclas em arquivo .txt, tornando o script furtivo e realizando envio automático dos dados por e-mail.

Reflexão sobre Defesa: Registro das principais medidas para prevenção e resposta a ataques, incluindo antivírus, firewall, sandboxing e conscientização do usuário.

Funcionalidades Desenvolvidas

Ransomware
Criação de arquivos testes
Criptografia com biblioteca Cryptography (Fernet)
Mensagem de resgate simulada e processo reverso (descriptografia)

Keylogger
Captura de teclas com pynput
Armazenamento em arquivo
Tornando o script invisível
Envio de dados via e-mail com smtplib

Exemplos de Uso
Execute o script ransomware.py para simular o processo de sequestro e recuperação de arquivos.

Execute o script keylogger.py em ambiente controlado para capturar pressionamento de teclas e enviar os dados coletados para um e-mail configurado.
Para enviar os e-mails é necessário colocar uma senha de app e endereço de e-mail do Google. 

Estratégias de Defesa
Utilização de ferramentas de antivírus e firewall bem configurados
Ambiente sandbox para testes
Atualização constante dos sistemas operacionais e softwares

Conscientização do usuário sobre riscos e engenharia social

Monitoramento de scripts e processos suspeitos
