import pandas as pd

class EmailModel:
    def __init__(self):
        self.emails = []

    def load_emails_from_excel(self, file_path):
        # Membaca file Excel dan mengembalikan daftar email
        data = pd.read_excel(file_path)
        self.emails = data['EMAIL'].dropna().tolist()
        return self.emails
