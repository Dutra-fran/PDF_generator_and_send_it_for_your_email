# Importando alguns scripts Python do diretório 'exportacoes'
from exportacoes.envio_email import enviar_email
from exportacoes.pdf_criar import Pdf_criar
from exportacoes import *
import os

os.system("chdir > caminho.txt")
caminho = open("caminho.txt", 'r').read().splitlines()

print("""
        PDF Super Generator :v

Seja super bem-vindo ao script que vai gerar um arquivo PDF pegando alguns tipos de dados.
Obs: O script é super seguro! Qualquer dúvida quanto a isso, leia o código-fonte dos scripts.
--------------------
""")

# Solicitando o email e a senha do Gmail
print("Informe o email e a senha do seu Gmail e algumas outras coisas relacionadas ao envio de email.")
email = input("Email: ")
senha = input("Senha: ")
destinatario = input("Email do destinatario: ")
assunto = input("Assunto do e-mail: ")
mensagem = input("Escreva uma breve mensagem: ")

print("--------------------\n")
print("A seguir, serão feito perguntas que irão ser colocadas no arquivo PDF. Obs: o arquivo PDF será gerado no diretório 'PDFs_Exportados'")
nome = input("Informe seu nome: ")
escolaridade = input("Informe sua escolaridade: ")
desenvolvedor = input("Você desenvolve em quais linguagens? (caso você desenvolva em mais de uma linguagem, informe a linguagem e prossiga com vírgulas): ")
trabalho = input("Você trabalha? ")
lingua = input("Do you speak English? (Você fala inglês?): ")
print("--------------------\n")

# Instanciando a classe Pdf_criar
PDF = Pdf_criar()
# Criando o arquivo PDF
PDF.Criar(caminho[0], nome, escolaridade, desenvolvedor, trabalho, lingua)

# Instanciando a classe enviar_email 
Em = enviar_email(email, senha, PDF.getArquivoPDF(), PDF.getNomeArquivoPDF())
# Enviando a mensagem
Em.enviarEmail(assunto, assunto, destinatario)