import customtkinter as ctk
import datetime
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk
from customtkinter import CTkImage
from docx import Document
import fitz
import pandas as pd


data_hora_atual = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")

# função carregar arquivo
def carregar_pdf(pdf_entry, log_text, check_files):
    global pdf_path
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if pdf_path:
        pdf_entry.delete(0, ctk.END)
        pdf_entry.insert(0, pdf_path)
        log_text.configure(state="normal")
        log_text.insert(ctk.END, f"{data_hora_atual} - PDF importado com sucesso...\n", "log")
        log_text.configure(state="disabled")
        check_files()

def carregar_excel(excel_entry, log_text, check_files):
    global excel_path
    excel_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if excel_path:
        excel_entry.delete(0, ctk.END)
        excel_entry.insert(0, excel_path)
        log_text.configure(state="normal")
        log_text.insert(ctk.END, f"{data_hora_atual} - Excel importado com sucesso...\n", "log")
        log_text.configure(state="disabled")
        check_files()

def processar(log_text, export_btn):
    log_text.configure(state="normal")
    log_text.insert(ctk.END, f"{data_hora_atual} - Processamento iniciado...\n", "log")
    log_text.configure(state="disabled")
    log_text.configure(state="normal")
    log_text.insert(ctk.END, f"{data_hora_atual} - Arquivos processados com sucesso!\n", "log")
    log_text.configure(state="disabled")
    export_btn.configure(state=ctk.NORMAL)

def extrair_texto_pdf(pdf_path, texto_procurado):
    documento = fitz.open(pdf_path)
    for pagina in documento:
        texto = pagina.get_text()
        if texto_procurado in texto:
            # encontrar posicao do texto
            posicao_inicio = texto.find(texto_procurado)
            if posicao_inicio != -1:
                # extrair texto após import po
                posicao_fim = texto.find(" ", posicao_inicio + len(texto_procurado) + 1)
                texto_extraido = texto[posicao_inicio + len(texto_procurado) + 1:posicao_fim].strip()
                return texto_extraido.split()[0]
    return None

# Função para extrair a descrição da planilha Excel
def extrair_description(excel_path):
    df = pd.read_excel(excel_path)
    if 'description' in df.columns:
        return df['description'].dropna().tolist()  # Retorna todas as descrições como uma lista
    return None

def criar_documento_word(texto, file_path):
    doc = Document()
    doc.add_heading("Relatório de Processamento", 0)
    doc.add_paragraph('Este é um relatório de exemplo.')
    doc.add_paragraph(f'Import PO No: {texto}')
    # if texto_excel:
    #     for desc in texto_excel:
    #         doc.add_paragraph(f'Description: {desc}')
    doc.add_paragraph(f'Data e Hora de criação: {data_hora_atual}')
    doc.save(file_path)


def export_report(log_text, pdf_path):
    log_text.configure(state="normal")
    log_text.insert(ctk.END, f"{data_hora_atual} - Exportação do relatório iniciada...\n", "log")
    log_text.configure(state="disabled")

    # abri a caixa de dialogo do windows
    file_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word Files", "*.docx")])

    if file_path:
        texto = extrair_texto_pdf(pdf_path, "Import PO No")
        # texto_excel = extrair_description(excel_path)

        if texto:
            criar_documento_word(texto, file_path)
            
            log_text.configure(state="normal")
            log_text.insert(ctk.END, f"{data_hora_atual} - Relatório exportado com sucesso!\n", "log")
            log_text.configure(state="disabled")
        else:
            log_text.configure(state="normal")
            log_text.insert(ctk.END, f"{data_hora_atual} - Erro ao Exportar Relatório!\n", "log")
            log_text.configure(state="disabled")

def check_files(pdf_entry, excel_entry, process_btn):
    if pdf_entry.get() and excel_entry.get():
        process_btn.configure(state=ctk.NORMAL)

