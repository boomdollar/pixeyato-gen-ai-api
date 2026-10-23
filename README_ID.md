# PIXEYATO GEN AI API — Paket awal

Paket ini adalah backend FastAPI untuk menjadi penghubung aplikasi Android PIXEYATO GEN AI ke layanan pemrosesan gambar.

## Yang sudah tersedia
- `GET /health` — cek server dan status konfigurasi AI.
- `POST /v1/images/generate` — generasi gambar melalui penyedia AI yang dikonfigurasi.
- `POST /v1/images/enhance` — peningkatan dasar warna, kontras, dan ketajaman.
- `POST /v1/images/remove-background` — penghapusan background menggunakan rembg.
- `GET /files/{filename}` — mengambil hasil gambar.
- `POST /v1/images/edit` — sengaja mengembalikan status 503 sampai model edit gambar diintegrasikan; tidak berpura-pura berhasil.

## Penting, jujur soal status
API ini adalah paket backend siap-deploy, bukan server yang sudah online. Generasi gambar membutuhkan API key penyedia AI yang valid dan kemungkinan biaya. Penghapusan background dapat membutuhkan unduhan model dan RAM cukup. API key jangan pernah ditanam di APK.

## Deploy dengan cara paling mudah (tanpa mengetik perintah)
1. Buka akun GitHub dan buat repository baru bernama `pixeyato-gen-ai-api`.
2. Unggah semua isi folder ZIP ini ke repository.
3. Buat layanan Web dari repository tersebut di penyedia hosting yang mendukung Docker, misalnya Render.
4. Atur environment variables di dashboard hosting:
   - `PIXEYATO_API_KEY`: buat string acak yang panjang.
   - `OPENAI_API_KEY`: isi key milik sendiri jika ingin fitur generate aktif.
5. Deploy. Setelah selesai, buka alamat server + `/health`. Harus terlihat `"ok": true`.
6. Buka alamat server + `/docs` untuk melihat dokumentasi endpoint interaktif.

Jika ingin menghindari langkah teknis ini, kirim screenshot layar hosting yang sedang dibuka; saya akan pandu satu langkah per satu langkah.

## Menghubungkan Android
Base URL aplikasi harus berupa alamat HTTPS server yang sudah berhasil deploy. Aplikasi mengirim header `X-API-Key` dengan kunci aplikasi. Untuk produksi, jangan gunakan satu kunci admin bersama semua pengguna; selanjutnya tambahkan login/token pengguna dan kuota kredit.

## Tes endpoint
Di `/docs`:
- Tes `GET /health` tanpa API key.
- Untuk endpoint yang dilindungi, tekan `Authorize` jika tersedia atau masukkan header `X-API-Key`.
- Generate: isi prompt, pilih ukuran, kualitas, lalu jalankan.
- Enhance/remove background: unggah file JPG/PNG/WEBP.

## Belum termasuk
- Login akun pengguna, pembayaran, kredit/kuota, riwayat cloud, moderasi, penghapusan otomatis file, dan integrasi image-edit AI penuh.
- Endpoint edit sengaja belum aktif hingga penyedia/model edit benar-benar diintegrasikan.
- Paket ini belum diuji di hosting eksternal dan tidak menghasilkan APK Android.
