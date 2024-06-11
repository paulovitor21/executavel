def carregar_pdf(pdf_entry, log_text, check_files):
    def update_pdf_path(path):
        pdf_entry.delete(0, ctk.END)
        pdf_entry.insert(0, path)
        log_text.configure(state="normal")
        log_text.insert(ctk.END, f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - PDF importado com sucesso...\n", "log")
        log_text.configure(state="disabled")
        check_files()

    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if pdf_path:
        update_pdf_path(pdf_path)
    
    def on_drop(event):
        update_pdf_path(event.data)
    
    pdf_entry.drop_target_register(DND_ALL)
    pdf_entry.dnd_bind("<<Drop>>", on_drop)