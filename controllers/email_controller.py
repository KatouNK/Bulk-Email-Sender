import tkinter as tk
from tkinter import filedialog, messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import threading
import os


class EmailController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.setup()

    def setup(self):
        self.view.browse_button.config(command=self.load_file)
        self.view.send_button.config(command=self.send_emails_async)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        if file_path:
            self.view.file_entry.delete(0, tk.END)
            self.view.file_entry.insert(0, file_path)
            emails = self.model.load_emails_from_excel(file_path)
            self.view.email_list_box.delete('1.0', tk.END)
            self.view.email_list_box.insert(tk.END, "\n".join(emails))

    def send_emails_async(self):
        # Menjalankan pengiriman email di thread terpisah untuk menjaga UI tetap responsif
        threading.Thread(target=self.send_emails).start()

    def send_emails(self):
        # Ambil email manual dari input 'Kepada'
        manual_email = self.view.to_entry.get().strip()

        # Validasi input
        if not self.model.emails and not manual_email:
            messagebox.showerror("Error", "Daftar email kosong. Muat file atau masukkan email manual.")
            return

        try:
            # Setup koneksi SMTP
            server = smtplib.SMTP('smtp.gmail.com', 587)  # Ganti dengan server SMTP
            server.starttls()
            server.login("miraenk7@gmail.com", "aphc frbz zpcq ptrf")  # Ganti dengan kredensial Anda

            # Daftar email yang akan dikirim (manual + dari file)
            emails_to_send = []
            if manual_email:
                emails_to_send.append(manual_email)  # Tambahkan email manual
            emails_to_send.extend(self.model.emails[:100])  # Tambahkan hingga 100 email dari daftar

            # Kirim email
            sent_count = 0
            for email in emails_to_send:
                msg = MIMEMultipart()
                msg['From'] = "miraenk7@gmail.com"
                msg['To'] = email
                msg['Subject'] = self.view.subject_entry.get()
                body = self.view.body_text.get('1.0', tk.END)
                msg.attach(MIMEText(body, 'plain'))

                # Kirim email
                server.sendmail("miraenk7@gmail.com", email, msg.as_string())
                sent_count += 1

            # Jika daftar email dari file digunakan, hapus yang sudah terkirim
            if self.model.emails:
                self.model.emails = self.model.emails[100:]

            server.quit()  # Tutup koneksi
            messagebox.showinfo("Success", f"Berhasil mengirim {sent_count} email.")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal mengirim email: {str(e)}")

            if server:
                server.quit()

    def attach_files(self, msg):
        # Menambahkan file terlampir ke pesan email
        for filepath in self.view.attachments:
            part = MIMEBase('application', "octet-stream")
            with open(filepath, 'rb') as file:
                part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(filepath)}"')
            msg.attach(part)

