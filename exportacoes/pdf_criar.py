# Exportando as bibliotecas
# Obs: é necessário instalar a biblioteca reportlab. Utilize pip install reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from pathlib import Path

# Nossa classe que cuidará da criação do arquivo PDF
# POO para reutilização de código
class Pdf_criar:
    # Método que fará a criação do PDF, de fato, personalizado através do recebimento dos argumentos
    def Criar(self, caminho, nome, escolaridade, desenvolvedor, trabalho, lingua):
        # Variaveis para dar o nome ao arquivo e para verificar se um arquivo PDF com o nome informado já existe
        i, nomePDF = 0, 'arquivo'
        fileName = caminho + "\PDFs_Exportados\\" + nomePDF + "00" + ".pdf"
        fileObj = Path(fileName)

        # Se um arquivo já existir com o nome informado, o bloco abaixo será executado
        while fileObj.is_file():
            i = i + 1
            # Bloco condicional para formatar o nome do arquivo
            if i < 10:
                fileName = caminho +"\PDFs_Exportados\\" + nomePDF + "0" + str(i) + ".pdf"
                fileObj = Path(fileName)
            else:
                fileName = caminho +"\PDFs_Exportados\\" + nomePDF + str(i) + ".pdf"
                fileObj = Path(fileName)
        # Se a condição while retornar "False", então, significa que o arquivo não existe e o bloco abaixo será executado.
        else:
            # Bloco condicional para formatar o nome do arquivo
            if i < 10:
                # Informa como será as características do arquivo PDF
                cnv = canvas.Canvas(caminho + "\PDFs_Exportados\\" + nomePDF + "0" + str(i) + ".pdf", pagesize=A4)
                # Pega o caminho onde o arquivo PDF está salvo
                self.arquivoPDF = caminho + "\PDFs_Exportados\\" + nomePDF + "0" + str(i) + ".pdf"
                # Pega somente o nome do arquivo PDF
                self.nomeArquivoPDF = nomePDF + "0" + str(i) + ".pdf"
            else:
                cnv = canvas.Canvas(caminho + "\PDFs_Exportados\\" + nomePDF + str(i) + ".pdf", pagesize=A4)
                self.arquivoPDF = caminho + "\PDFs_Exportados\\" + nomePDF + str(i) + ".pdf"
                self.nomeArquivoPDF = nomePDF + str(i) + ".pdf"
        
        # Função para converter 'pontos' para 'milimetros'
        def mp(mm):
            return mm/0.352777
            
        # Corpo do PDF
        cnv.drawString(mp(20), mp(270), "Nome: " + nome)
        cnv.drawString(mp(20), mp(260), "Escolaridade: " + escolaridade)
        cnv.drawString(mp(20), mp(250), "Desenvolvedor: " + desenvolvedor)
        cnv.drawString(mp(20), mp(230), "Trabalha? - " + trabalho)
        cnv.drawString(mp(75), mp(230), "Do you speak English? - " + lingua)
        cnv.drawString(mp(20), mp(20), "Obrigado por responder nosso questionário! Atenciosamente, equipe Kerberos Sec.")

        # Cria o arquivo PDF
        cnv.save()
        
    # Método para pegar o caminho do arquivo PDF
    def getArquivoPDF(self):
        return self.arquivoPDF

    # Método para pegar o nome do arquivo PDF
    def getNomeArquivoPDF(self):
        return self.nomeArquivoPDF