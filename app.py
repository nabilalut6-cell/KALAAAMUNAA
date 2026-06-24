import streamlit as st
from google import genai
import time

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Kalaamunaaa - Gaming Maharah Kalam X MA",
    page_icon="🎮",
    layout="wide" 
)

# --- CUSTOM CSS: GAMING & PLAYFUL NEON INTERFACE (STEAM & DISCORD VIBES) ---
st.markdown("""
    <style>
    /* Latar belakang gelap pekat khas aplikasi game / Discord Dark Mode */
    .stApp {
        background: radial-gradient(circle at top, #1b1c23 0%, #0f1015 100%);
        background-attachment: fixed;
    }
    
    /* Header Utama Kalaamunaaa Bergaya Judul Game */
    .main-title {
        color: #00f2fe; /* Cyan Neon */
        font-family: 'Impact', 'Segoe UI', sans-serif;
        text-align: center;
        font-weight: 900;
        font-size: 3.5rem;
        margin-top: 10px;
        margin-bottom: 0px;
        text-shadow: 0px 0px 15px rgba(0, 242, 254, 0.6);
        letter-spacing: 2px;
    }
    .sub-title {
        color: #ff007f; /* Pink Neon / Laser */
        padding: 25px 20px;
        border-radius: 14px;
        min-height: 140px;
        flex-direction: column;
        justify-content: center;
        border: 1px solid #00f2fe;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.4);
    }
    .info-badge-purple {
        background: linear-gradient(135deg, #ff007f 0%, #9b004f 100%); /* Laser Pink */
        color: white;
        padding: 25px 20px;
        border-radius: 14px;
        text-align: center;
        font-weight: bold;
        min-height: 140px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        border: 1px solid #ff007f;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.4);
    }
    
    /* Penyesuaian Kolom Ketikan & Dropdown Sesuai Konsol Game */
    input, select, textarea {
        color: #00f2fe !important; /* Teks menyala hijau/biru neon */
        background-color: #15161b !important;
        border: 1px solid #ff007f !important;
        font-family: monospace;
    }
    
/* --- PERBAIKAN TOTAL CHAT INPUT (ANTI-MELOROT / SEJAJAR) --- */
    
    /* Mengincar kontainer pembungkus utama chat input bawaan Streamlit */
    div[data-testid="stChatInput"] {
        border: 2px solid #ff007f !important; /* Border pink dipasang di luar boks */
        background-color: #15161b !important;
        border-radius: 12px !important;
        box-shadow: 0 0 10px rgba(255, 0, 127, 0.2);
        padding: 5px !important;
    }

    /* Mengatur text field di dalamnya agar transparan & tidak merusak tata letak tombol panah */
    div[data-testid="stChatInput"] textarea {
        color: #00f2fe !important; /* Teks menyala cyan neon */
        background-color: transparent !important; /* Dibuat transparan agar menyatu */
        display: flex;
        font-weight: bold;
        text-align: center;
        text-align: center;
    }
        color: #1b1c23;
        background: linear-gradient(135deg, #00f2fe 0%, #0072ff 100%); /* Cyber Cyan */
    .info-badge-blue {
        font-size: 1.3rem;
        font-weight: bold;
        margin-bottom: 35px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.4);
        border: none !important; /* Menghilangkan border ganda yang bikin melorot */
        letter-spacing: 1.5px;
        border: 1px solid #ff007f;
        text-shadow: 0px 0px 10px rgba(255, 0, 127, 0.4);
    }
        font-family: monospace;
        justify-content: center;
        min-height: 140px;
        display: flex;
        flex-direction: column;
    
    /* Panel Kontrol Atas (Top Control Lobby) */
    .top-navbar-card {
        background: rgba(30, 31, 41, 0.85);
        border: 2px solid #ff007f; /* Garis laser pink */
        border-radius: 16px;
        padding: 25px;
        margin-bottom: 25px;
        text-align: center;
        font-weight: bold;
        box-shadow: 0 0 20px rgba(255, 0, 127, 0.15);
        backdrop-filter: blur(10px);
        box-shadow: none !important;
        border-radius: 14px;

    }
    

    /* Mengatur dropdown seleksi standar (select) agar tetap konsisten */

    select {
        color: #00f2fe !important;

        background-color: #15161b !important;
        border: 1px solid #ff007f !important;
        font-family: monospace;

    }

    
    /* Menyesuaikan warna tombol panah agar ikut menyala bergaya gaming */
    div[data-testid="stChatInput"] button {
        background-color: transparent !important;
        color: #00f2fe !important; /* Panah berwarna cyan */
        border: none !important;
    }
    div[data-testid="stChatInput"] button:hover {
        color: #ff007f !important; /* Berubah jadi pink saat disorot */
    }

    label {
        color: #00f2fe !important;
        font-weight: bold !important;
        letter-spacing: 0.5px;
    }
    
    /* Tombol Mulai (Start Game) */
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #00f2fe, #ff007f) !important;
        color: #ffffff !important;
        font-weight: 900 !important;
        letter-spacing: 1px;
        border: none !important;
        border-radius: 10px !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
        transition: all 0.3s ease !important;

    }

    div.stButton > button:first-child:hover {
        transform: scale(1.01) !important;

        box-shadow: 0 0 20px rgba(0, 242, 254, 0.5) !important;

    }

    

    /* Tombol Keluar Sesi (Quit Game) */

    div.stButton > button[kind="primary"] {

        background: #2a2c35 !important;
        color: #ff007f !important;

        font-weight: bold !important;
        border: 1px solid #ff007f !important;

        border-radius: 10px !important;

    }
    div.stButton > button[kind="primary"]:hover {

        background: #ff007f !important;
        color: white !important;

        box-shadow: 0 0 15px rgba(255, 0, 127, 0.4) !important;

    }


    /* Hilangkan elemen standar Streamlit */
    footer {visibility: hidden;}
    header {background-color: transparent !important;}
    </style>

""", unsafe_allow_html=True)

# --- INISIALISASI SESSION STATE ---
if "messages" not in st.session_state:

    st.session_state.messages = []

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "current_persona" not in st.session_state:

    st.session_state.current_persona = ""
if "current_topic" not in st.session_state:

    st.session_state.current_topic = ""

# --- HALAMAN UTAMA APPLICATION ---
st.markdown("<h1 class='main-title'>🗣️ Kalaamunaaa (كَلَامُنَا)</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Praktik Maharah Kalam Seru & Interaktif — Kelas X MA</p>", unsafe_allow_html=True)

# --- TATA LETAK ATAS: LOBBY & LOGIN PANEL ---
st.markdown("<div class='top-navbar-card'>", unsafe_allow_html=True)

if not st.session_state.logged_in:
    form_col1, form_col2 = st.columns(2)
    with form_col1:
        username = st.text_input("PLAYER NAME", placeholder="Masukkan ID / Nama Kamu")
    with form_col2:
        api_key = st.text_input("ACCESS TOKEN (API KEY)", type="password", placeholder="AIzaSy...")
        
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("START GAME / HUBUNGKAN 🕹️", use_container_width=True):
        if username and api_key:
            st.session_state.username = username
            st.session_state.api_key = api_key
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Gagal! Isi nama player dan Token kamu untuk membuka gerbang game!")
    st.markdown("</div>", unsafe_allow_html=True) # Tag kontainer ditutup dengan benar di halaman utama


    # Grid Menu Info Utama ala Quest Selection

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<div class='info-badge-blue'>⚡ LIVE CHAT INTERACTION<br><br><span style='font-weight:normal; font-size:0.85rem;'>Praktik bahasa Arab seru berformat RPG Chatting, latih kelancaran bicaramu secara real-time!</span></div>", unsafe_allow_html=True)

    with col2:

        st.markdown("<div class='info-badge'>📚 MATERI LENGKAP X MA<br><br><span style='font-weight:normal; font-size:0.85rem;'>Selesaikan 3 stage obrolan berbobot: Al-Hayah Al-Yaumiyah, Al-Mihnah, dan Al-Usroh!</span></div>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='info-badge-purple'>🤖 CHOOSE YOUR BOT PARTNER<br><br><span style='font-weight:normal; font-size:0.85rem;'>Dua Coach handal siap memandu petualangan kalammu: Ustadz Khalid atau Ustadzah Khaulah.</span></div>", unsafe_allow_html=True)

else:
    st.markdown(f"<h4 style='text-align: center; color: white; margin-top:0;'>🟢 Player <span style='color: #00f2fe;'>{st.session_state.username}</span> Connected! Siap untuk Memulai Petualangan! 🏆</h4>", unsafe_allow_html=True)
    
    select_col1, select_col2 = st.columns(2)
    with select_col1:
        ustadz_pilihan = st.selectbox(
            "Pilih Karakter Partner Bicara (NPC Persona):",
            ["Ustadz Khalid", "Ustadzah Khaulah"]
        )
    with select_col2:
        materi_pilihan = st.selectbox(
            "Pilih Area Quest Percakapan (Topik):",
            [
                "Al-Hayah Al-Yaumiyah (Kehidupan Sehari-hari / الحياة اليومية)", 

                "Al-Mihnah (Profesi / المهنة)",

                "Al-Usroh (Kehidupan Keluarga / الأسرة)"

            ]

        )

    st.markdown("</div>", unsafe_allow_html=True) 


    # PROMPT UTAMA SYSTEM AI (Logika Tetap Terjaga)

    gender_pembimbing = "seorang Ustadz laki-laki bernama Ustadz Khalid" if ustadz_pilihan == "Ustadz Khalid" else "seorang Ustadzah perempuan bernama Ustadzah Khaulah"
    
    system_instruction = f"""
    Anda adalah {gender_pembimbing}, seorang guru bahasa Arab yang sangat lemah lembut, sabar, santun, dan penuh kasih sayang dalam mendidik siswa kelas X MA.
    Tugas Anda adalah melatih 'Maharah Kalam' (keterampilan berbicara) siswa bernama {st.session_state.username} mengenai topik: {materi_pilihan}.
    
    Aturan Percakapan:
    1. Selalu gunakan bahasa Arab yang sesuai untuk tingkat MA, sertakan harakat, dan berikan terjemahan bahasa Indonesia di bawahnya.
    2. Berikan koreksi yang sangat lembut jika siswa salah dalam menyusun kalimat atau kosakata.
    3. Ajukan satu pertanyaan pendek di setiap akhir pesan untuk memicu siswa membalas.
    4. Selalu tunjukkan apresiasi seperti 'ممتاز!' atau 'Barakallahu fiik'.
    """

    if st.session_state.current_persona != ustadz_pilihan or st.session_state.current_topic != materi_pilihan:
        st.session_state.current_persona = ustadz_pilihan
        st.session_state.current_topic = materi_pilihan
        
        greeting_msg = f"Assalamu'alaikum wr. wb. Player {st.session_state.username}! 🎮 Saya {ustadz_pilihan} siap jadi partner sparring kamu di Quest Kalam tentang *{materi_pilihan}*. Yuk, ketik balasan pertamamu untuk memulai permainan!"
        st.session_state.messages = [{"role": "assistant", "content": greeting_msg}]

    # AREA RUANG OBROLAN CHAT
    st.markdown("<h3 style='color: #00f2fe;'>💬 Game Dialogue Box:</h3>", unsafe_allow_html=True)
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Input Kotak Ketikan Siswa
    user_input = st.chat_input("Tulis balasan bahasa Arab atau Indonesia kamu di sini...")

    
    # Tombol keluar dari alur normal di bawah input chat

    st.markdown("<div style='margin-top: 15px; margin-bottom: 25px;'>", unsafe_allow_html=True)

    if st.button("QUIT GAME & LOGOUT ❌", type="primary", use_container_width=True):

        st.session_state.clear()
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)


    # Logika Pengiriman Pesan
    if user_input:
        with st.chat_message("user"):

            st.markdown(user_input)

        st.session_state.messages.append({"role": "user", "content": user_input})
        
        try:
            client = genai.Client(api_key=st.session_state.api_key)
            
            full_context = system_instruction + "\n\nBerikut riwayat percakapan:\n"
            for msg in st.session_state.messages:
                full_context += f"{msg['role']}: {msg['content']}\n"
            
            bot_response = ""
            for attempt in range(3):
                try:

                    response = client.models.generate_content(

                        model="gemini-2.5-flash",

                        contents=f"{full_context}\nSiswa mengatakan: {user_input}\nBerikan respons Anda sebagai pengajar:"

                    )
                    bot_response = response.text

                    break
                except Exception as e:

                    if "503" in str(e) and attempt < 2:

                        time.sleep(2)
                        continue
                    else:

                        raise e


            if bot_response:
                with st.chat_message("assistant"):
                    st.markdown(bot_response)
                st.session_state.messages.append({"role": "assistant", "content": bot_response})
                st.rerun()
            
        except Exception as e:
            st.error(f"Terjadi kesalahan koneksi API: {e}. Silakan coba kirim ulang pesan beberapa saat lagi.")
