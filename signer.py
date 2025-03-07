import tkinter as tk
from tkinter import filedialog, messagebox
import ftplib
import qrcode
import PyPDF2
from fpdf import FPDF
import os

# FTP server detallarını öz serverinizə uyğun düzəldin! Yoxsa proqram işləməyəcək
FTP_HOST = "xxxxxxx"
FTP_USER = "xxxxxxx"
FTP_PASS = "xxxxxxx"
UPLOAD_DIR = "htdocs/uploads/" 
DOWNLOAD_URL = "http://serveradress/upload/" 

def upload_to_ftp(file_path, file_name):
    with ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS) as ftp:
        ftp.cwd(UPLOAD_DIR)
        with open(file_path, "rb") as file:
            ftp.storbinary(f"STOR {file_name}", file)
    return DOWNLOAD_URL + file_name

def generate_qr_code(link, qr_path):
    qr = qrcode.make(link)
    qr.save(qr_path)

def add_qr_to_pdf(pdf_path, qr_path, output_path):
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    pdf_writer = PyPDF2.PdfWriter()
    
    for page in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page])
    
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    

    pdf.image(qr_path, x=15, y=50, w=30)
    

    pdf.set_xy(50, 55)
    pdf.set_font("helvetica", size=11)
    pdf.cell(0, 10, text="This document is signed by Name, Surname")
    pdf.set_xy(50, 65)
    pdf.cell(0, 10, text="and Legally valid.")
    
    temp_qr_pdf = "temp_qr.pdf"
    pdf.output(temp_qr_pdf)
    
    qr_pdf_reader = PyPDF2.PdfReader(temp_qr_pdf)
    pdf_writer.add_page(qr_pdf_reader.pages[0])
    
    with open(output_path, "wb") as output_file:
        pdf_writer.write(output_file)
    
    os.remove(temp_qr_pdf)

def process_pdf(pdf_path):
    if not os.path.exists(pdf_path):
        return "Error: PDF file can't be found."
    
    try:
        file_name = os.path.basename(pdf_path)
        uploaded_url = upload_to_ftp(pdf_path, file_name)
        qr_path = "qr_code.png"
        generate_qr_code(uploaded_url, qr_path)
        output_pdf = "signed_" + file_name
        add_qr_to_pdf(pdf_path, qr_path, output_pdf)
        os.remove(qr_path)
        return f"Success! Final document: {output_pdf}"
    except Exception as e:
        return f"Error: {str(e)}"

def upload_document():
    file_path = filedialog.askopenfilename(
        title="Select PDF Document",
        filetypes=[("PDF files", "*.pdf")]
    )
    
    if file_path:
        result = process_pdf(file_path)
        if result.startswith("Error"):
            messagebox.showerror("Error", result)
        else:
            messagebox.showinfo("Success", result)

def create_gui():
    root = tk.Tk()
    root.title("PDF Signer")
    root.geometry("500x400")
    root.configure(bg="#2c3e50")
    
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

    main_frame = tk.Frame(root, bg="#2c3e50", padx=40, pady=40)
    main_frame.pack(expand=True, fill="both")
    

    title_label = tk.Label(
        main_frame,
        text="PDF Signer",
        font=("Helvetica", 24, "bold"),
        fg="#ecf0f1", 
        bg="#2c3e50"
    )
    title_label.pack(pady=(0, 10))
    

    subtitle_label = tk.Label(
        main_frame,
        text="Upload and sign your PDF documents securely",
        font=("Helvetica", 12),
        fg="#bdc3c7",
        bg="#2c3e50"
    )
    subtitle_label.pack(pady=(0, 30))
    

    upload_button = tk.Button(
        main_frame,
        text="Select PDF File",
        command=upload_document,
        font=("Helvetica", 12),
        bg="#3498db",  
        fg="white",
        activebackground="#2980b9",
        activeforeground="white",
        relief=tk.FLAT,
        padx=20,
        pady=10,
        cursor="hand2"  
    )
    upload_button.pack(pady=20)
    
    status_label = tk.Label(
        main_frame,
        text="Ready to process documents",
        font=("Helvetica", 10),
        fg="#95a5a6",  
        bg="#2c3e50"
    )
    status_label.pack(pady=(30, 0))
    
    root.mainloop()

if __name__ == "__main__":
    create_gui()
