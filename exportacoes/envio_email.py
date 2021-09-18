#Importando bibliotecas padrões do Python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Obs: Estamos enviando e-mails a partir do servidor de Correio Eletrônico do Gmail, ou seja,
# você deverá acessar a parte de "Segurança" do seu e-mail e ativar o "Acesso a app menos seguro".
# Feito esse pequeno passo, você estará apto a estar utilizando esse script.

# Nossa classe que fará o envio do e-mail
class enviar_email:

    # Construtor
    def __init__(self, email, senha, anexo, nomeAnexo):
        # A partir da instanciação da nossa classe, você deve passar as informações de email e senha, caminho do anexo e o nome do anexo.
        self.email = email
        self.senha = senha
        self.anexo = anexo
        self.nomeAnexo = nomeAnexo

    # O método que enviará, de fato, o nosso email (recebe 3 argumentos)
    def enviarEmail(self, assunto, mensagem, destinatario):
        # Estrutura do nosso e-mail.
        corpo = mensagem
        msg = MIMEMultipart()
        msg['Subject'] = assunto
        msg['From'] = self.email
        msg['To'] = destinatario
        password = self.senha
        msg.attach(MIMEText(corpo,'html'))

        # Abrindo o arquivo em modo leitura(r - read) e binário(b - binary)
        Anexo_fp = open(self.anexo, 'rb')
        # Codificando o anexo para o email
        Anexo = MIMEBase('application', 'octet-stream')
        Anexo.set_payload(Anexo_fp.read())
        encoders.encode_base64(Anexo)

        # Cabeçalho no tipo anexo do email
        Anexo.add_header('Content-Disposition', f'attachment; filename={self.nomeAnexo}')
        # Fechando o arquivo
        Anexo_fp.close()

        # Coloca o anexo no corpo do email
        msg.attach(Anexo)

        # Se conectando ao servidor de Correio Eletrônico e enviando a mensagem
        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print("Email enviado!")