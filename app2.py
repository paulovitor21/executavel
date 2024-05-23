# import customtkinter as ctk
# from tkinter import filedialog, messagebox
# from tkinter.scrolledtext import ScrolledText

# # Funções para carregar arquivos e processar
# def carregar_pdf():
#     global pdf_path
#     pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
#     if pdf_path:
#         pdf_entry.delete(0, ctk.END)
#         pdf_entry.insert(0, pdf_path)
#         verificar_arquivos()

# def carregar_excel():
#     global excel_path
#     excel_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
#     if excel_path:
#         excel_entry.delete(0, ctk.END)
#         excel_entry.insert(0, excel_path)
#         verificar_arquivos()

# def verificar_arquivos():
#     if pdf_entry.get() and excel_entry.get():
#         processar_btn.configure(state=ctk.NORMAL)

# def processar():
#     # Coloque seu código de processamento aqui
#     log_text.insert(ctk.END, "Processamento iniciado...\n")
#     # Simulação de processamento
#     log_text.insert(ctk.END, "Arquivos processados com sucesso!\n")
#     exportar_btn.configure(state=ctk.NORMAL)

# def exportar():
#     # Coloque seu código de exportação aqui
#     log_text.insert(ctk.END, "Exportação do relatório iniciada...\n")
#     # Simulação de exportação
#     log_text.insert(ctk.END, "Relatório exportado com sucesso!\n")

# # Configuração da janela principal
# app = ctk.CTk()
# app.geometry("800x500")
# app.title("Import PO")
# # app._set_appearance_mode("dark")  # Define o modo de aparência para "dark"

# # Frame esquerdo (barra lateral)
# frame_esquerdo = ctk.CTkFrame(app, width=150)
# frame_esquerdo.grid(row=0, column=0, rowspan=2, sticky="nswe")

# titulo_label = ctk.CTkLabel(frame_esquerdo, text="Import PO", font=ctk.CTkFont(size=20, weight="bold"))
# titulo_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# versao_label = ctk.CTkLabel(frame_esquerdo, text="Versão 1.0")
# versao_label.grid(row=1, column=0, padx=10, pady=10, sticky="s")

# # Frame direito (principal)
# frame_direito = ctk.CTkFrame(app)
# frame_direito.grid(row=0, column=1, padx=10, pady=10, sticky="nswe")

# # Campo para selecionar PDF
# pdf_label = ctk.CTkLabel(frame_direito, text="PDF")
# pdf_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

# pdf_entry = ctk.CTkEntry(frame_direito, width=300)
# pdf_entry.grid(row=0, column=1, padx=5, pady=5)

# carregar_pdf_btn = ctk.CTkButton(frame_direito, text="Importar", command=carregar_pdf)
# carregar_pdf_btn.grid(row=0, column=2, padx=5, pady=5)

# # Campo para selecionar Excel
# excel_label = ctk.CTkLabel(frame_direito, text="Excel")
# excel_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

# excel_entry = ctk.CTkEntry(frame_direito, width=300)
# excel_entry.grid(row=1, column=1, padx=5, pady=5)

# carregar_excel_btn = ctk.CTkButton(frame_direito, text="Importar", command=carregar_excel)
# carregar_excel_btn.grid(row=1, column=2, padx=5, pady=5)

# # Frame para os botões de processar e exportar
# frame_botoes = ctk.CTkFrame(frame_direito)
# frame_botoes.grid(row=2, column=0, columnspan=3, padx=5, pady=20)

# # Botões de processar e exportar lado a lado
# processar_btn = ctk.CTkButton(frame_botoes, text="Processar", state=ctk.DISABLED, command=processar)
# processar_btn.pack(side=ctk.LEFT, padx=10)

# exportar_btn = ctk.CTkButton(frame_botoes, text="Exportar Relatório", state=ctk.DISABLED, command=exportar)
# exportar_btn.pack(side=ctk.LEFT, padx=10)

# # Frame inferior (logs de processamento)
# frame_inferior = ctk.CTkFrame(app)
# frame_inferior.grid(row=1, column=1, padx=10, pady=10, sticky="nswe")

# log_label = ctk.CTkLabel(frame_inferior, text="Logs do processamento")
# log_label.pack(pady=5)

# log_text = ScrolledText(frame_inferior, height=10)
# log_text.pack(expand=True, fill="both", padx=10, pady=10)

# # Ajuste das proporções das colunas e linhas
# app.grid_columnconfigure(1, weight=1)
# app.grid_rowconfigure(1, weight=1)

# # Executar o aplicativo
# app.mainloop()

### VERSAO ESTÁVEL ####
# import customtkinter as ctk
# from tkinter import filedialog, messagebox
# from tkinter.scrolledtext import ScrolledText

# # Funções para carregar arquivos e processar
# def carregar_pdf():
#     global pdf_path
#     pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
#     if pdf_path:
#         pdf_entry.delete(0, ctk.END)
#         pdf_entry.insert(0, pdf_path)
#         verificar_arquivos()

# def carregar_excel():
#     global excel_path
#     excel_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
#     if excel_path:
#         excel_entry.delete(0, ctk.END)
#         excel_entry.insert(0, excel_path)
#         verificar_arquivos()

# def verificar_arquivos():
#     if pdf_entry.get() and excel_entry.get():
#         processar_btn.configure(state=ctk.NORMAL)

# def processar():
#     # Coloque seu código de processamento aqui
#     log_text.insert(ctk.END, "Processamento iniciado...\n")
#     # Simulação de processamento
#     log_text.insert(ctk.END, "Arquivos processados com sucesso!\n")
#     exportar_btn.configure(state=ctk.NORMAL)

# def exportar():
#     # Coloque seu código de exportação aqui
#     log_text.insert(ctk.END, "Exportação do relatório iniciada...\n")
#     # Simulação de exportação
#     log_text.insert(ctk.END, "Relatório exportado com sucesso!\n")

# # Configuração da janela principal
# app = ctk.CTk()
# app.geometry("800x500")
# app.title("Import PO")
# ctk.set_appearance_mode("dark")  # Define o modo de aparência para "dark"

# # Frame esquerdo (barra lateral)
# frame_esquerdo = ctk.CTkFrame(app, width=150)
# frame_esquerdo.grid(row=0, column=0, rowspan=2, sticky="nswe")

# # Ajuste das proporções das colunas e linhas no frame_esquerdo
# frame_esquerdo.grid_rowconfigure(0, weight=1)
# frame_esquerdo.grid_rowconfigure(1, weight=0)
# frame_esquerdo.grid_columnconfigure(0, weight=1)

# titulo_label = ctk.CTkLabel(frame_esquerdo, text="Import PO", font=ctk.CTkFont(size=20, weight="bold"))
# titulo_label.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

# versao_label = ctk.CTkLabel(frame_esquerdo, text="Versão 1.0")
# versao_label.grid(row=1, column=0, padx=10, pady=10, sticky="s")

# # Frame direito (principal)
# frame_direito = ctk.CTkFrame(app)
# frame_direito.grid(row=0, column=1, padx=10, pady=10, sticky="nswe")

# # Campo para selecionar PDF
# pdf_label = ctk.CTkLabel(frame_direito, text="PDF")
# pdf_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

# pdf_entry = ctk.CTkEntry(frame_direito, width=300)
# pdf_entry.grid(row=0, column=1, padx=5, pady=5)

# carregar_pdf_btn = ctk.CTkButton(frame_direito, text="Importar", command=carregar_pdf, fg_color="red")
# carregar_pdf_btn.grid(row=0, column=2, padx=5, pady=5)

# # Campo para selecionar Excel
# excel_label = ctk.CTkLabel(frame_direito, text="Excel")
# excel_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

# excel_entry = ctk.CTkEntry(frame_direito, width=300)
# excel_entry.grid(row=1, column=1, padx=5, pady=5)

# carregar_excel_btn = ctk.CTkButton(frame_direito, text="Importar", command=carregar_excel, fg_color="red")
# carregar_excel_btn.grid(row=1, column=2, padx=5, pady=5)

# # Frame para os botões de processar e exportar sem cor de fundo
# frame_botoes = ctk.CTkFrame(frame_direito, fg_color="transparent")
# frame_botoes.grid(row=2, column=0, columnspan=3, padx=5, pady=20)

# # Botões de processar e exportar lado a lado
# processar_btn = ctk.CTkButton(frame_botoes, text="Processar", state=ctk.DISABLED, command=processar, fg_color="red")
# processar_btn.pack(side=ctk.LEFT, padx=10)

# exportar_btn = ctk.CTkButton(frame_botoes, text="Exportar Relatório", state=ctk.DISABLED, command=exportar, fg_color="red")
# exportar_btn.pack(side=ctk.LEFT, padx=10)

# # Frame inferior (logs de processamento)
# frame_inferior = ctk.CTkFrame(app)
# frame_inferior.grid(row=1, column=1, padx=10, pady=10, sticky="nswe")

# log_label = ctk.CTkLabel(frame_inferior, text="Logs do processamento")
# log_label.pack(pady=5)

# log_text = ScrolledText(frame_inferior, height=10)
# log_text.pack(expand=True, fill="both", padx=10, pady=10)

# # Ajuste das proporções das colunas e linhas
# app.grid_columnconfigure(1, weight=1)
# app.grid_rowconfigure(1, weight=1)

# # Executar o aplicativo
# app.mainloop()


import customtkinter as ctk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText

# Funções para carregar arquivos e processar
def carregar_pdf():
    global pdf_path
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if pdf_path:
        pdf_entry.delete(0, ctk.END)
        pdf_entry.insert(0, pdf_path)
        verificar_arquivos()

def carregar_excel():
    global excel_path
    excel_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if excel_path:
        excel_entry.delete(0, ctk.END)
        excel_entry.insert(0, excel_path)
        verificar_arquivos()

def verificar_arquivos():
    if pdf_entry.get() and excel_entry.get():
        processar_btn.configure(state=ctk.NORMAL)

def processar():
    # Coloque seu código de processamento aqui
    log_text.insert(ctk.END, "Processamento iniciado...\n")
    # Simulação de processamento
    log_text.insert(ctk.END, "Arquivos processados com sucesso!\n")
    exportar_btn.configure(state=ctk.NORMAL)

def exportar():
    # Coloque seu código de exportação aqui
    log_text.insert(ctk.END, "Exportação do relatório iniciada...\n")
    # Simulação de exportação
    log_text.insert(ctk.END, "Relatório exportado com sucesso!\n")

# Configuração da janela principal
app = ctk.CTk()
app.geometry("800x500")
app.title("Import PO")
ctk.set_appearance_mode("dark")  # Define o modo de aparência para "dark"

# Frame esquerdo (barra lateral)
frame_esquerdo = ctk.CTkFrame(app, width=500)
frame_esquerdo.grid(row=0, column=0, rowspan=2, sticky="nswe")

# Ajuste das proporções das colunas e linhas no frame_esquerdo
frame_esquerdo.grid_rowconfigure(0, weight=1)
frame_esquerdo.grid_rowconfigure(1, weight=0)
frame_esquerdo.grid_columnconfigure(0, weight=1)

titulo_label = ctk.CTkLabel(frame_esquerdo, text="Import PO", font=ctk.CTkFont(size=20, weight="bold"))
titulo_label.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

versao_label = ctk.CTkLabel(frame_esquerdo, text="Versão 1.0")
versao_label.grid(row=1, column=0, padx=10, pady=10, sticky="s")

# Frame direito (principal)
frame_direito = ctk.CTkFrame(app)
frame_direito.grid(row=0, column=1, padx=10, pady=10, sticky="nswe")

# Ajuste das proporções das colunas e linhas no frame_direito
frame_direito.grid_columnconfigure(0, weight=1)
frame_direito.grid_columnconfigure(1, weight=3)
frame_direito.grid_columnconfigure(2, weight=0)

# Campo para selecionar PDF
pdf_label = ctk.CTkLabel(frame_direito, text="PDF")
pdf_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

pdf_entry = ctk.CTkEntry(frame_direito)
pdf_entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")

carregar_pdf_btn = ctk.CTkButton(frame_direito, text="Importar", command=carregar_pdf, fg_color="red")
carregar_pdf_btn.grid(row=0, column=2, padx=5, pady=5)

# Campo para selecionar Excel
excel_label = ctk.CTkLabel(frame_direito, text="Excel")
excel_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

excel_entry = ctk.CTkEntry(frame_direito)
excel_entry.grid(row=1, column=1, padx=5, pady=5, sticky="we")

carregar_excel_btn = ctk.CTkButton(frame_direito, text="Importar", command=carregar_excel, fg_color="red")
carregar_excel_btn.grid(row=1, column=2, padx=5, pady=5)

# Frame para os botões de processar e exportar sem cor de fundo
frame_botoes = ctk.CTkFrame(frame_direito, fg_color="transparent")
frame_botoes.grid(row=2, column=0, columnspan=3, padx=5, pady=20)

# Botões de processar e exportar lado a lado
processar_btn = ctk.CTkButton(frame_botoes, text="Processar", state=ctk.DISABLED, command=processar, fg_color="red")
processar_btn.pack(side=ctk.LEFT, padx=10)

exportar_btn = ctk.CTkButton(frame_botoes, text="Exportar Relatório", state=ctk.DISABLED, command=exportar, fg_color="red")
exportar_btn.pack(side=ctk.LEFT, padx=10)

# Centralizando horizontalmente os botões
frame_direito.grid_columnconfigure(0, weight=1)
frame_direito.grid_rowconfigure(2, weight=1)

# Frame inferior (logs de processamento)
frame_inferior = ctk.CTkFrame(app)
frame_inferior.grid(row=1, column=1, padx=10, pady=10, sticky="nswe")

log_label = ctk.CTkLabel(frame_inferior, text="Logs do processamento")
log_label.pack(pady=5)

log_text = ScrolledText(frame_inferior, height=10)
log_text.pack(expand=True, fill="both", padx=10, pady=10)

# Ajuste das proporções das colunas e linhas
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(1, weight=1)

# Executar o aplicativo
app.mainloop()


