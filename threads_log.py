import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import customtkinter as ctk
from PIL import Image, ImageDraw, ImageFont
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import concurrent.futures
import os

# Função para criar o frame de logs
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

    return frame_logs, log_text

# Função para processar o relatório
def process_report(log_text):
    log_text.configure(state="normal")
    log_text.insert(tk.END, "Iniciando processamento do relatório...\n", "log")
    # Simular processamento do relatório
    log_text.insert(tk.END, "Processando...\n", "log")
    log_text.insert(tk.END, "Relatório processado com sucesso.\n", "log")
    log_text.configure(state="disabled")

    # Salvar o conteúdo do log como uma imagem
    image_path = save_log_to_image(log_text)

    # Enviar o log por e-mail de forma concorrente
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(send_email_with_attachment, image_path)

# Função para salvar o conteúdo do log como uma imagem
def save_log_to_image(log_text):
    log_content = log_text.get("1.0", tk.END)
    
    # Configurar fonte e tamanho da imagem
    font = ImageFont.truetype("arial.ttf", 14)
    max_width = 800
    line_height = font.getbbox("A")[3] - font.getbbox("A")[1]
    
    lines = log_content.splitlines()
    spacing = 20  # Aumentar o espaçamento entre as linhas
    img_height = (line_height + spacing) * len(lines) + 20  # 20 para padding

    # Criar uma imagem com o tamanho calculado
    img = Image.new("RGB", (max_width, img_height), "white")
    draw = ImageDraw.Draw(img)

    # Desenhar cada linha de texto na imagem
    y = 10
    for line in lines:
        draw.text((10, y), line, fill="black", font=font)
        y += line_height + spacing  # Adicionar espaçamento entre linhas

    # Salvar a imagem
    image_path = "log_content.png"
    img.save(image_path)
    
    return image_path

# Função para enviar um e-mail com anexo
def send_email_with_attachment(file_path):
    from_address = "seu_email@gmail.com"
    to_address = "destinatario@gmail.com"
    subject = "Log de Processamento"
    body = "Segue em anexo o log de processamento."

    # Configurar a mensagem
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEBase('application', 'octet-stream'))

    # Anexar o arquivo
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(file_path, 'rb').read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="{}"'.format(os.path.basename(file_path)))
    msg.attach(part)

    # Configurar o servidor SMTP
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_address, "sua_senha")
        server.sendmail(from_address, to_address, msg.as_string())

# Exemplo de uso
if __name__ == "__main__":
    # Inicialização da aplicação Tkinter
    app = tk.Tk()
    app.geometry("800x600")

    # Criar frame de logs
    frame_logs, log_text = create_log_frame(app)

    # Adicionar botão para iniciar o processamento do relatório
    process_button = ctk.CTkButton(app, text="Processar Relatório", command=lambda: process_report(log_text))
    process_button.grid(row=0, column=1, padx=10, pady=10)

    # Iniciar o loop principal da aplicação
    app.mainloop()