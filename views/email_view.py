import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import os


class EmailView:
    def __init__(self, master):
        self.master = master
        self.master.title("Email Sender")

        # Input untuk 'Kepada'
        tk.Label(master, text="Kepada:").grid(row=0, column=0, sticky='e')
        self.to_entry = tk.Entry(master, width=50)
        self.to_entry.grid(row=0, column=1, sticky='we', columnspan=2)

        # Input untuk 'Subjek'
        tk.Label(master, text="Subjek:").grid(row=1, column=0, sticky='e')
        self.subject_entry = tk.Entry(master, width=50)
        self.subject_entry.grid(row=1, column=1, sticky='we', columnspan=2)

        # Text box untuk isi email
        tk.Label(master, text="Isi Email:").grid(row=2, column=0, sticky='ne')
        self.body_text = scrolledtext.ScrolledText(master, height=10, width=50)
        self.body_text.grid(row=2, column=1, columnspan=2, sticky='we')

        # Input untuk file path (browse file Excel)
        tk.Label(master, text="File Path:").grid(row=3, column=0, sticky='e')
        self.file_entry = tk.Entry(master, width=50)
        self.file_entry.grid(row=3, column=1, sticky='we', columnspan=2)

        # Tombol Browse untuk memilih file
        self.browse_button = tk.Button(master, text="Browse File")
        self.browse_button.grid(row=4, column=0, sticky='we')

        # Area untuk daftar email
        tk.Label(master, text="Daftar Email:").grid(row=5, column=0, sticky='ne')
        self.email_list_box = scrolledtext.ScrolledText(master, height=10, width=50)
        self.email_list_box.grid(row=5, column=1, columnspan=2, sticky='we')

        # Tombol untuk menambahkan lampiran
        self.attach_button = tk.Button(master, text="Attach PDF", command=self.attach_file)
        self.attach_button.grid(row=6, column=0, sticky='we')

        # Label untuk menampilkan nama file lampiran
        self.file_label = tk.Label(master, text="")
        self.file_label.grid(row=6, column=1, columnspan=2, sticky='w')

        # Tombol Kirim Email
        self.send_button = tk.Button(master, text="Kirim Email")
        self.send_button.grid(row=7, column=1, columnspan=2, sticky='we')

        self.attachments = []  # Menyimpan daftar file lampiran

    def attach_file(self):
        """Memungkinkan pengguna memilih file PDF untuk dilampirkan."""
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.attachments.append(file_path)
            self.file_label.config(text=os.path.basename(file_path))

    def show_success_message(self):
        """Menampilkan pesan sukses setelah email terkirim."""
        messagebox.showinfo("Success", "Email berhasil dikirim!")

    def show_error_message(self, error):
        """Menampilkan pesan error jika terjadi kegagalan."""
        messagebox.showerror("Error", f"Terjadi kesalahan: {error}")
