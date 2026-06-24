# 🎮 KALAAMUNAAA 
### [ MODE: MULTIPLAYER ARABIC SPEAKER — LEVEL: MA X ]

Selamat datang di aplikasi yang sudah saya buat. Berikut dokumentasi untuk menggunakan program ini:

---

## 📖 Deskripsi Projek
**Kalaamunaaa** adalah aplikasi pembelajaran bahasa Arab berbasis web inovatif yang dirancang khusus untuk mengasah *Maharah Kalam* (keterampilan berbicara) bagi siswa tingkat Kelas X Madrasah Aliyah (MA). 

Aplikasi ini mengusung konsep visual **Gaming & Playful Neon Interface** dengan perpaduan warna *Dark Discord/Steam* pekat yang dipadukan dengan aksen *Cyber Cyan* dan *Laser Pink* yang interaktif. Menggunakan framework **Streamlit**, Kalaamunaaa terintegrasi langsung dengan kecerdasan buatan **Google AI Studio (Gemini 2.5 Flash)** yang bertindak sebagai *Coach Virtual / Game NPC Partner* yang lemah lembut, sabar, dan santun dalam melatih percakapan siswa.

### ✨ Fitur Utama:
* **Cyberpunk Arcade Layout:** Antarmuka *Single-Page Layout* terpusat (tanpa menggunakan sidebar) dengan elemen boks menu horizontal yang mirip dengan *Lobby Game Konseptual*.
* **Sistem Akses Aman:** Autentikasi token di halaman utama menggunakan *Player Name* dan *Google AI Studio API Key* sebelum petualangan belajar dimulai.
* **Karakter Partner Pilihan:** Tersedia 2 pilihan karakter mentor virtual, yaitu **Ustadz Khalid** dan **Ustadzah Khaulah** yang membimbing secara interaktif.
* **3 Area Quest Materi (Kelas X MA):**
  1. *Al-Hayah Al-Yaumiyah* (Kehidupan Sehari-hari / الحياة اليومية)
  2. *Al-Mihnah* (Profesi / المهنة)
  3. *Al-Usroh* (Kehidupan Keluarga / الأسرة)
* **Anti-Lag & Auto-Retry System:** Dilengkapi proteksi logika tangguh yang otomatis mencoba mengirim ulang pesan jika server Google AI Studio sedang padat trafik (*high demand*).
* **Game Dialogue Box (Conversation History):** Mengingat seluruh riwayat percakapan dalam satu sesi agar alur tanya-jawab bahasa Arab mengalir natural.

---

## 🛠️ Prasyarat & Instalasi
Sebelum menjalankan aplikasi, pastikan perangkat komputer sudah terinstal Python (versi 3.10 ke atas sangat direkomendasikan).

### 1. Masuk ke Direktori Projek
Buka Command Prompt (CMD) Windows atau terminal pilihan Anda, lalu arahkan ke dalam folder proyek:
```bash
cd path/to/folder_projek

```

### 2. Instalasi Library Pendukung

Instal dua *library* utama yang dibutuhkan agar aplikasi dapat berjalan dengan mengetik perintah berikut di CMD:

```bash
pip install streamlit google-genai

```

---

## 🚀 Cara Menjalankan Aplikasi

1. Pastikan file aplikasi utama (`app.py`) berada di dalam direktori folder tersebut.
2. Jalankan perintah Streamlit berikut melalui jendela CMD Anda:

```cmd
   streamlit run app.py

```

3. Browser utama Anda (Chrome/Edge/Firefox) akan otomatis terbuka dan mengarah ke alamat lokal: `http://localhost:8501`.

---

## 💡 Panduan Penggunaan Aplikasi

1. **Lobby Login:** Pada kartu *Lobby Control* di bagian atas halaman awal, masukkan **Player Name** dan **Access Token (API Key)** valid yang didapatkan dari Google AI Studio. Klik tombol **"START GAME / HUBUNGKAN 🕹️"**.
2. **Pilih Quest Mode:** Setelah berhasil tersambung, pilih *Karakter Partner Bicara (NPC Persona)* dan *Area Quest Percakapan (Topik)* yang ingin kamu selesaikan melalui menu drop-down sejajar yang tersedia.
3. **Mulai Percakapan:** Partner pilihan akan memberikan kalimat salam pembuka (*greeting*). Ketik respons balasan Anda menggunakan bahasa Arab (atau bahasa Indonesia) pada kolom *chat input* paling bawah.
4. **Interaksi & Koreksi:** Bot AI akan merespons dialog Anda lengkap dengan teks Arab bersyarat (harakat), arti bahasa Indonesia, serta memberikan koreksi tata bahasa (*grammar*) yang lembut jika terdapat kekeliruan kosakata.
5. **Quit Game:** Jika ingin meriset sesi obrolan, mengganti akun player, atau mengakhiri permainan, klik tombol merah **"QUIT GAME & LOGOUT ❌"** yang berada tepat di bawah kolom input ketikan chat.

---

## ⚙️ Teknologi yang Digunakan

* **Language:** Python
* **Framework UI:** Streamlit (Custom CSS Arcade Gaming Theme)
* **AI Engine:** Google GenAI SDK (Model: `gemini-2.5-flash`)
* **Environment:** Windows Command Prompt (CMD)

Identitas Pengembang: 

Nama (NIM): Nabilah Luth Fiana Yusuf (1232030150), Nuraeni (1232030182)
Program Studi: Pendidikan Bahasa Arab
Mata Kuliah: Artificial Intelligence (Kecerdasan Buatan)
