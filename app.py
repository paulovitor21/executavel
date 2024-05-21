# import tkinter
# import customtkinter

# # janela = tkinter.Tk()
# # janela.geometry("600x300")

# def clique():
#     print("Oi")

# # texto = tkinter.Label(janela, text="Hello, World!")
# # texto.pack(padx=10, pady=10)

# # botao = tkinter.Button(janela, text="Processar", command=clique)
# # botao.pack(padx=10, pady=10)
# # janela.mainloop()

# janela = customtkinter.CTk()
# janela.geometry("600x300")

# texto = customtkinter.CTkLabel(janela, text="Teste")
# texto.pack(padx=10, pady=10)

# botao = customtkinter.CTkButton(janela, text="Processar", command=clique)
# botao.pack(padx=10, pady=10)

# janela.mainloop()

import customtkinter as ctk
from tkinter import filedialog, messagebox

class FileSelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Selector")
        self.root.geometry("800x400")
        
        ctk.set_appearance_mode("dark")  # Define o modo de aparência para "dark"
        ctk.set_default_color_theme("blue")  # Define o tema de cor para "blue"

        # PDF file selection
        self.pdf_label = ctk.CTkLabel(root, text="Select PDF File:")
        self.pdf_label.grid(row=0, column=0, padx=10, pady=10)

        self.pdf_entry = ctk.CTkEntry(root, width=400)
        self.pdf_entry.grid(row=0, column=1, padx=10, pady=10)

        self.pdf_button = ctk.CTkButton(root, text="Browse", command=self.browse_pdf)
        self.pdf_button.grid(row=0, column=2, padx=10, pady=10)

        # Excel file selection
        self.excel_label = ctk.CTkLabel(root, text="Select Excel File:")
        self.excel_label.grid(row=1, column=0, padx=10, pady=10)

        self.excel_entry = ctk.CTkEntry(root, width=400)
        self.excel_entry.grid(row=1, column=1, padx=10, pady=10)

        self.excel_button = ctk.CTkButton(root, text="Browse", command=self.browse_excel)
        self.excel_button.grid(row=1, column=2, padx=10, pady=10)

        # Submit button
        self.submit_button = ctk.CTkButton(root, text="Submit", command=self.submit_files)
        self.submit_button.grid(row=2, column=1, pady=20)

    def browse_pdf(self):
        pdf_file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if pdf_file:
            self.pdf_entry.delete(0, ctk.END)
            self.pdf_entry.insert(0, pdf_file)

    def browse_excel(self):
        excel_file = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        if excel_file:
            self.excel_entry.delete(0, ctk.END)
            self.excel_entry.insert(0, excel_file)

    def submit_files(self):
        pdf_path = self.pdf_entry.get()
        excel_path = self.excel_entry.get()

        if pdf_path and excel_path:
            messagebox.showinfo("Files Submitted", f"PDF: {pdf_path}\nExcel: {excel_path}")
        else:
            messagebox.showwarning("Incomplete Submission", "Please select both PDF and Excel files.")

if __name__ == "__main__":
    root = ctk.CTk()
    app = FileSelectorApp(root)
    root.mainloop()
