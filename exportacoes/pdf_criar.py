# Exportando as bibliotecas
# Obs: é necessário instalar a biblioteca reportlab. Utilize pip install reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from pathlib import Path
import os

class Pdf_criar:
    def Criar(self, caminho, nome, escolaridade, desenvolvedor, trabalho, lingua):
        i, nomePDF = 0, 'arquivo'
        fileName = caminho + "\PDFs_Exportados\\" + nomePDF + "00" + ".pdf"
        fileObj = Path(fileName)

        while fileObj.is_file():
            i = i + 1
            if i < 10:
                fileName = caminho +"\PDFs_Exportados\\" + nomePDF + "0" + str(i) + ".pdf"
                fileObj = Path(fileName)
            else:
                fileName = caminho +"\PDFs_Exportados\\" + nomePDF + str(i) + ".pdf"
                fileObj = Path(fileName)
        else:
            if i < 10:
                cnv = canvas.Canvas(caminho + "\PDFs_Exportados\\" + nomePDF + "0" + str(i) + ".pdf", pagesize=A4)
                self.arquivoPDF = caminho + "\PDFs_Exportados\\" + nomePDF + "0" + str(i) + ".pdf"
                self.nomeArquivoPDF = nomePDF + "0" + str(i) + ".pdf"
            else:
                cnv = canvas.Canvas(caminho + "\PDFs_Exportados\\" + nomePDF + str(i) + ".pdf", pagesize=A4)
                self.arquivoPDF = caminho + "\PDFs_Exportados\\" + nomePDF + str(i) + ".pdf"
                self.nomeArquivoPDF = nomePDF + str(i) + ".pdf"
            
        def mp(mm):
            return mm/0.352777
            
        cnv.drawString(mp(20), mp(270), "Nome: " + nome)
        cnv.drawString(mp(20), mp(260), "Escolaridade: " + escolaridade)
        cnv.drawString(mp(20), mp(250), "Desenvolvedor: " + desenvolvedor)
        cnv.drawString(mp(20), mp(230), "Trabalha? - " + trabalho)
        cnv.drawString(mp(75), mp(230), "Do you speak English? - " + lingua)
        cnv.drawString(mp(20), mp(20), "Obrigado por responder nosso questionário! Atenciosamente, equipe Kerberos Sec.")

        cnv.save()
        
    def getArquivoPDF(self):
        return self.arquivoPDF

    def getNomeArquivoPDF(self):
        return self.nomeArquivoPDF