# Flower Federation Dashboard

Dashboard simulasi Federated Analytics dengan 1 Flower Server dan 3 Client.

## Fitur
- Visualisasi topologi 1 server dan 3 client.
- Animasi pengiriman query dan respons client.
- Tombol Mulai Simulasi dan Reset.
- Log aktivitas simulasi.
- Histogram hasil lokal dan ringkasan agregasi.

## Menjalankan di komputer lokal

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Deploy ke Streamlit Community Cloud

1. Unggah `app.py`, `dashboard.html`, `requirements.txt`, dan `README.md` ke repository GitHub.
2. Buka https://share.streamlit.io/ dan login dengan GitHub.
3. Pilih **Create app**.
4. Pilih repository, branch `main`, dan Main file path `app.py`.
5. Klik **Deploy**.

## Catatan simulasi

Ini adalah simulasi antarmuka untuk pembelajaran. Animasi dan angka contoh berjalan di browser; dashboard ini tidak membuat koneksi ke Flower Server sungguhan atau Flower Dashboard backend.
