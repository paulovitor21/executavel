import customtkinter as ctk
from interface.ui_components import create_left_frame, create_right_frame, create_log_frame
from modules.utils import get_resource_path


def create_interface():
    # Configuração da janela principal
    app = ctk.CTk()
    app.geometry("700x400")
    app.title("Import PO")
    ctk.set_appearance_mode("dark")

    # Definir ícone da janela
    icon_window = get_resource_path('assets/report.ico')
    app.iconbitmap(icon_window)

    # Frame esquerdo - barra lateral
    create_left_frame(app)

    # Frame logs de processamento
    log_text = create_log_frame(app)

    # Frame direito - principal
    create_right_frame(app, log_text)


    app.grid_columnconfigure(1, weight=1)
    app.grid_rowconfigure(1, weight=1)

    return app
