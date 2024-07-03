import customtkinter as ctk
from tkinter.scrolledtext import ScrolledText
from PIL import Image
from customtkinter import CTkImage
from modules.funtion import carregar_pdf, process_export, only_numbers, add_placeholder, adicionar_id, validate_entries
from modules.utils import get_resource_path

def create_left_frame(app):
    # Frame esquerdo - barra lateral
    frame_esquerdo = ctk.CTkFrame(app, width=500)
    frame_esquerdo.grid(row=0, column=0, rowspan=2, sticky="nswe")

    # Ajuste de proporção das colunas e linhas do frame_esquerdo
    frame_esquerdo.grid_rowconfigure(0, weight=1)
    frame_esquerdo.grid_rowconfigure(1, weight=0)
    frame_esquerdo.grid_rowconfigure(2, weight=0)
    frame_esquerdo.grid_rowconfigure(3, weight=0)
    frame_esquerdo.grid_columnconfigure(0, weight=1)

    logo_path = get_resource_path("assets/logo.png")
    logo_image = Image.open(logo_path)
    logo_image = logo_image.resize((173, 45))
    logo_ctk_image = CTkImage(light_image=logo_image, size=(173, 45))
    logo_label = ctk.CTkLabel(frame_esquerdo, image=logo_ctk_image, text="")
    logo_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="n")

    # Centralização do texto do título e versão
    titulo_label = ctk.CTkLabel(frame_esquerdo, text="Import PO", font=ctk.CTkFont(size=20, weight="bold"))
    titulo_label.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="n")

    versao_label = ctk.CTkLabel(frame_esquerdo, text="versão 1.0")
    versao_label.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="s")

def create_right_frame(app, log_text):
    # Frame direito - principal
    frame_direito = ctk.CTkFrame(app)
    frame_direito.grid(row=0, column=1, padx=10, pady=10, sticky="nswe")

    # Ajuste das colunas - frame direito
    frame_direito.grid_columnconfigure(0, weight=1)
    frame_direito.grid_columnconfigure(1, weight=3)
    frame_direito.grid_columnconfigure(2, weight=0)

    # Texto - ID da Requisição
    requisicao_id_label = ctk.CTkLabel(frame_direito, text="DRC Number")
    requisicao_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

    # Validar apenas números
    vcmd = (frame_direito.register(lambda char, current_text: only_numbers(char, current_text)), '%S', '%P')

    # StringVar para o campo de ID da Requisição
    requisicao_id_var = ctk.StringVar()

    # Campo para inserir o ID da Requisição
    requisicao_id_entry = ctk.CTkEntry(
        frame_direito,
        textvariable=requisicao_id_var,
        validate="key",
        validatecommand=vcmd)
    requisicao_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")
    add_placeholder(requisicao_id_entry, "Digite o ID")  # Adiciona o placeholder corretamente

    # Botão adicionar ID da Requisição (inicialmente desabilitado)
    adicionar_id_btn = ctk.CTkButton(
        frame_direito,
        text="Adicionar ID",
        command=lambda: adicionar_id(requisicao_id_entry, log_text),
        fg_color="red", font=ctk.CTkFont(weight="bold"),
        state="disabled")  # Desabilitado inicialmente
    adicionar_id_btn.grid(row=0, column=2, padx=5, pady=5)

    # Texto - selecionar PDF
    pdf_label = ctk.CTkLabel(frame_direito, text="PDF")
    pdf_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

    # StringVar para PDF
    pdf_var = ctk.StringVar()

    # Campo para inserir o PDF
    pdf_entry = ctk.CTkEntry(frame_direito, textvariable=pdf_var)
    pdf_entry.grid(row=1, column=1, padx=5, pady=5, sticky="we")
    add_placeholder(pdf_entry, "Selecione o PDF")  # Adiciona o placeholder corretamente

    # Botão importar PDF
    carregar_pdf_btn = ctk.CTkButton(frame_direito, text="Importar", command=lambda: carregar_pdf(pdf_entry, log_text, lambda: validate_entries(pdf_entry, requisicao_id_var, adicionar_id_btn, process_export_btn)), fg_color="red", font=ctk.CTkFont(weight="bold"))
    carregar_pdf_btn.grid(row=1, column=2, padx=5, pady=5)

    frame_btn = ctk.CTkFrame(frame_direito, fg_color="transparent")
    frame_btn.grid(row=3, column=0, columnspan=3, padx=5, pady=20)

    # Botão processar e exportar
    process_export_btn = ctk.CTkButton(
        frame_btn,
        text="Exportar Relatório",
        state=ctk.DISABLED,
        command=lambda: process_export(log_text, requisicao_id_entry, pdf_entry),
        fg_color="red", font=ctk.CTkFont(weight="bold"))
    process_export_btn.pack(side=ctk.LEFT, padx=10)

    # Configurar rastreamento para validar entradas
    pdf_var.trace_add('write', lambda *args: validate_entries(pdf_entry, requisicao_id_var, adicionar_id_btn, process_export_btn))
    requisicao_id_var.trace_add('write', lambda *args: validate_entries(pdf_entry, requisicao_id_var, adicionar_id_btn, process_export_btn))

    # Centralização dos botões processar e exportar
    frame_direito.grid_columnconfigure(0, weight=1)
    frame_direito.grid_rowconfigure(2, weight=1)

def create_log_frame(app):
    # Frame logs de processamento
    frame_logs = ctk.CTkFrame(app)
    frame_logs.grid(row=1, column=1, padx=10, pady=10, sticky="nswe")

    log_label = ctk.CTkLabel(frame_logs, text="Registro de Processamento")
    log_label.pack(pady=5)

    log_text = ScrolledText(frame_logs, height=10)
    log_text.pack(expand=True, fill="both", padx=10, pady=10)
    log_text.configure(state="disabled")
    log_text.tag_configure("log", font=("Helvetica", 12))

    return log_text


