import customtkinter as ctk
from tkinter.scrolledtext import ScrolledText
from PIL import Image
from customtkinter import CTkImage
from modules.funtion import carregar_pdf, carregar_excel, processar, export_report, validate_entries
from modules.utils import get_resource_path

def only_numbers(char, current_text):
    return char.isdigit() and len(current_text) < 6

# Função para adicionar o ID (exemplo)
def adicionar_id(requisicao_id_entry, log):
    id_value = requisicao_id_entry.get()
    log.configure(state="normal")
    log.insert("end", f"ID Adicionado: {id_value}\n", "log")
    log.configure(state="disabled")

def create_interface():
    # Configuração da janela principal
    app = ctk.CTk()
    app.geometry("800x500")
    app.title("Import PO")
    ctk.set_appearance_mode("dark")

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

    # Frame direito - principal
    frame_direito = ctk.CTkFrame(app)
    frame_direito.grid(row=0, column=1, padx=10, pady=10, sticky="nswe")

    # Ajuste das colunas - frame direito
    frame_direito.grid_columnconfigure(0, weight=1)
    frame_direito.grid_columnconfigure(1, weight=3)
    frame_direito.grid_columnconfigure(2, weight=0)

    # Função para habilitar/desabilitar o botão com base na entrada
    def check_id_length(*args):
        if len(requisicao_id_var.get()) == 5:  # Assumindo que o ID deve ter 5 dígitos
            adicionar_id_btn.configure(state="normal")
        else:
            adicionar_id_btn.configure(state="disabled")

    # Texto - ID da Requisição
    requisicao_id_label = ctk.CTkLabel(frame_direito, text="ID da Requisição")
    requisicao_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

    # Validar apenas números
    vcmd = (frame_direito.register(lambda char, current_text: only_numbers(char, current_text)), '%S', '%P')

    # # StringVar para monitorar o campo de entrada
    # requisicao_id_var = ctk.StringVar()
    # requisicao_id_var.trace_add('write', check_id_length)

    # StringVar para o campo de ID da Requisição
    requisicao_id_var = ctk.StringVar()
    requisicao_id_var.trace_add('write', lambda *args: validate_entries(pdf_entry, excel_entry, requisicao_id_var, adicionar_id_btn, process_btn))

    # Campo para inserir o ID da Requisição
    requisicao_id_entry = ctk.CTkEntry(
        frame_direito,
        textvariable=requisicao_id_var,
        validate="key",
        validatecommand=vcmd)
    requisicao_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")

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
    pdf_var.trace_add('write', lambda *args: validate_entries(pdf_entry, excel_entry, requisicao_id_var, adicionar_id_btn, process_btn))
    # Campo para inserir o PDF
    pdf_entry = ctk.CTkEntry(frame_direito, textvariable=pdf_var)
    pdf_entry.grid(row=1, column=1, padx=5, pady=5, sticky="we")

    # Botão importar PDF
    carregar_pdf_btn = ctk.CTkButton(frame_direito, text="Importar", command=lambda: carregar_pdf(pdf_entry, log_text, lambda: validate_entries(pdf_entry, excel_entry, requisicao_id_entry, adicionar_id_btn, process_btn)), fg_color="red", font=ctk.CTkFont(weight="bold"))
    carregar_pdf_btn.grid(row=1, column=2, padx=5, pady=5)

    # Texto - selecionar Excel
    excel_label = ctk.CTkLabel(frame_direito, text="Excel")
    excel_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

    # StringVar para Excel
    excel_var = ctk.StringVar()
    excel_var.trace_add('write', lambda *args: validate_entries(pdf_entry, excel_entry, requisicao_id_var, adicionar_id_btn, process_btn))
    # Campo para inserir o Excel
    excel_entry = ctk.CTkEntry(frame_direito, textvariable=excel_var)
    excel_entry.grid(row=2, column=1, padx=5, pady=5, sticky="we")

    # Botão importar Excel
    carregar_excel_btn = ctk.CTkButton(
        frame_direito, 
        text="Importar", 
        command=lambda: carregar_excel(
            excel_entry, 
            log_text, 
            lambda: validate_entries(
                pdf_entry, 
                excel_entry, 
                requisicao_id_entry,
                adicionar_id_btn, 
                process_btn)), 
                fg_color="red", 
                font=ctk.CTkFont(weight="bold"))
    carregar_excel_btn.grid(row=2, column=2, padx=5, pady=5)

    
    frame_btn = ctk.CTkFrame(frame_direito, fg_color="transparent")
    frame_btn.grid(row=3, column=0, columnspan=3, padx=5, pady=20)

    process_btn = ctk.CTkButton(
        frame_btn, 
        text="Processar", 
        state=ctk.DISABLED, 
        command=lambda: processar(log_text, export_btn), 
        fg_color="red", font=ctk.CTkFont(weight="bold"))
    process_btn.pack(side=ctk.LEFT, padx=10)

    # Botão exportar relatório
    export_btn = ctk.CTkButton(
        frame_btn,
        text="Exportar Relatório",
        state=ctk.DISABLED,
        command=lambda: export_report(log_text, requisicao_id_entry.get(), pdf_entry.get()),
        fg_color="red", font=ctk.CTkFont(weight="bold"))
    export_btn.pack(side=ctk.LEFT, padx=10)

    pdf_var.trace_add('write', lambda *args: validate_entries(pdf_entry, excel_entry, requisicao_id_entry, adicionar_id_btn, process_btn))
    excel_var.trace_add('write', lambda *args: validate_entries(pdf_entry, excel_entry, requisicao_id_entry, adicionar_id_btn, process_btn))
    requisicao_id_var.trace_add('write', lambda *args: validate_entries(pdf_entry, excel_entry, requisicao_id_entry, adicionar_id_btn, process_btn))

    # Centralização dos botões processar e exportar
    frame_direito.grid_columnconfigure(0, weight=1)
    frame_direito.grid_rowconfigure(2, weight=1)

    # Frame logs de processamento
    frame_logs = ctk.CTkFrame(app)
    frame_logs.grid(row=1, column=1, padx=10, pady=10, sticky="nswe")

    log_label = ctk.CTkLabel(frame_logs, text="Registro de Processamento")
    log_label.pack(pady=5)

    log_text = ScrolledText(frame_logs, height=10)
    log_text.pack(expand=True, fill="both", padx=10, pady=10)
    log_text.configure(state="disabled")
    log_text.tag_configure("log", font=("Helvetica", 12))

    app.grid_columnconfigure(1, weight=1)
    app.grid_rowconfigure(1, weight=1)

    return app

if __name__ == "__main__":
    app = create_interface()
    app.mainloop()
