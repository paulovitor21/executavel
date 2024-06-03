import customtkinter as ctk
from tkinter.scrolledtext import ScrolledText
from PIL import Image
from customtkinter import CTkImage
from modules.funtion import carregar_pdf, carregar_excel, processar, export_report, check_files
from modules.utils import get_resource_path

def create_interface():
    # configuração janela principal
    app = ctk.CTk()
    app.geometry("800x500")
    app.title("Import PO")
    ctk.set_appearance_mode("dark")

    # frame esquerdo - barra lateral
    frame_esquerdo = ctk.CTkFrame(app, width=500)
    frame_esquerdo.grid(row=0, column=0, rowspan=2, sticky="nswe")

    # ajuste de proporção das colunas e linhas do frame_esquerdo
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

    versao_label = ctk.CTkLabel(frame_esquerdo, text=("versão 1.0"))
    versao_label.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="s")

    # frame direito - principal
    frame_direito = ctk.CTkFrame(app)
    frame_direito.grid(row=0, column=1, padx=10, pady=10, stick="nswe")

    # ajuste das colunas - frame direito
    frame_direito.grid_columnconfigure(0, weight=1)
    frame_direito.grid_columnconfigure(1, weight=3)
    frame_direito.grid_columnconfigure(2, weight=0)

    # Texto - selecionar PDF
    pdf_label = ctk.CTkLabel(frame_direito, text="PDF")
    pdf_label.grid(row=0, column=0, padx=5, pady=5, stick="e")

    # campo para inserir o pdf
    pdf_entry = ctk.CTkEntry(frame_direito)
    pdf_entry.grid(row=0, column=1, padx=5, pady=5, stick="we")

    # Botão importar pdf
    carregar_pdf_btn = ctk.CTkButton(frame_direito, text="Importar", command=lambda: carregar_pdf(pdf_entry, log_text, lambda: check_files(pdf_entry, excel_entry, process_btn)), fg_color="red", font=ctk.CTkFont(weight="bold"))
    carregar_pdf_btn.grid(row=0, column=2, padx=5, pady=5)

    # Texto - selecionar Excel
    excel_label = ctk.CTkLabel(frame_direito, text="Excel")
    excel_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

    # campo para inserir o excel
    excel_entry = ctk.CTkEntry(frame_direito)
    excel_entry.grid(row=1, column=1, padx=5, pady=5, sticky="we")

    # Botão importar excel
    carregar_excel_btn = ctk.CTkButton(frame_direito, text="Importar", command=lambda: carregar_excel(excel_entry, log_text, lambda: check_files(pdf_entry, excel_entry, process_btn)), fg_color="red", font=ctk.CTkFont(weight="bold"))
    carregar_excel_btn.grid(row=1, column=2, padx=5, pady=5)

    frame_btn = ctk.CTkFrame(frame_direito, fg_color="transparent")
    frame_btn.grid(row=2, column=0, columnspan=3, padx=5, pady=20)

    process_btn = ctk.CTkButton(frame_btn, text="Processar", state=ctk.DISABLED, command=lambda: processar(log_text, export_btn), fg_color="red", font=ctk.CTkFont(weight="bold"))
    process_btn.pack(side=ctk.LEFT, padx=10)

    export_btn = ctk.CTkButton(
        frame_btn, 
        text="Exportar Relatório", 
        state=ctk.DISABLED, 
        command=lambda: export_report(log_text, pdf_entry.get()), 
        fg_color="red", font=ctk.CTkFont(weight="bold"))
    export_btn.pack(side=ctk.LEFT, padx=10)

    # centralização dos botões processar e exportar
    frame_direito.grid_columnconfigure(0, weight=1)
    frame_direito.grid_rowconfigure(2, weight=1)

    # frame logs de processamento
    frame_logs = ctk.CTkFrame(app)
    frame_logs.grid(row=1, column=1, padx=10, pady=10, sticky="nswe")

    log_label = ctk.CTkLabel(frame_logs, text="Registro de Processamento")
    log_label.pack(pady=5)

    log_text = ScrolledText(frame_logs, height=10)
    log_text.pack(expand=True, fill="both", padx=10, pady=10)
    log_text.configure(state="disabled")
    # config font do log
    # Configurar a fonte da tag 'log'
    log_text.tag_configure("log", font=("Helvetica", 12))

    app.grid_columnconfigure(1, weight=1)
    app.grid_rowconfigure(1, weight=1)

    return app

if __name__ == "__main__":
    app = create_interface()
    app.mainloop()