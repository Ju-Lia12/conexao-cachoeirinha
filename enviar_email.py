import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_email(html):
    # Configurações do email
    email_de = 'cachoeirinhaconexao@gmail.com'
    senha = 'ytkl djsd jclm btus'  
    email_para = ['julia.souza121@gmail.com', 'gusxmorais@gmail.com']
    assunto = 'Relatório Conexão Cachoeirinha'

    # with open("./template_email_preenchido.html", "r", encoding="utf-8") as f:
    #     html = f.read()

    # Criar mensagem
    msg = MIMEMultipart('alternative')
    msg['From'] = 'cachoeirinhaconexao@gmail.com'
    msg['To'] = ", ".join(email_para)
    msg['Subject'] = assunto

    # Adicionar HTML ao email
    msg.attach(MIMEText(html, 'html'))

    # Enviar email via SMTP Gmail
    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()  # Conexão segura
        servidor.login(email_de, senha)
        servidor.sendmail(email_de, email_para, msg.as_string())
        servidor.quit()
        print("Email enviado com sucesso!")
    except Exception as e:
        print("Erro ao enviar email:", e)




