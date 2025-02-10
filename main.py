import tkinter as tk
from controllers.email_controller import EmailController
from models.email_model import EmailModel
from views.email_view import EmailView  # Disesuaikan dengan nama kelas di email_view.py

def main():
    try:
        root = tk.Tk()  # Membuat root window untuk Tkinter
        root.title("Bulk Email Sender")  # Tambahkan judul untuk window

        # Inisialisasi model, view, dan controller
        model = EmailModel()  # Pastikan EmailModel terdefinisi di email_model.py
        view = EmailView(root)  # Pastikan EmailApp terdefinisi di email_view.py
        controller = EmailController(model, view)  # Pastikan EmailController terdefinisi di email_controller.py

        root.mainloop()  # Menjalankan loop utama Tkinter
    except ImportError as e:
        print(f"Import error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
