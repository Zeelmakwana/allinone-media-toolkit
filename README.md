# 🎥 All-In-One Media Converter (Tkinter GUI)

A feature-rich **Tkinter-based GUI tool** that provides multiple powerful conversion utilities in one app:

- 🎬 Download YouTube Videos (with thumbnail preview)
- 🎧 Convert MP4 to MP3
- 📄 Convert PDF to Word (.docx)
- 📑 Convert Word to PDF
- 🖼️ Convert PDF to Images
- 🔗 Generate Colorful QR Codes

---

## 🚀 Features at a Glance

✔ YouTube Video Downloader with Thumbnail Preview  
✔ MP4 ➝ MP3 Audio Converter  
✔ PDF ➝ Word and Word ➝ PDF Conversion  
✔ PDF ➝ JPG Image Export  
✔ QR Code Generator with Custom Colors  
✔ Beautiful Image-Based GUI using Tkinter  
✔ Beginner-Friendly and Easy to Use

---

## 📦 Installation & Setup Guide

### 📁 Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/AllInOneConverter.git
cd AllInOneConverter
```

---

### 🐍 Step 2: Install Python Dependencies

Make sure you are using **Python 3.10+**.

Install required packages with:

```bash
pip install -r requirements.txt
```

---

### 📸 Step 3: Setup Poppler (Required for PDF ➝ Image Conversion)

1. Download Poppler for Windows:  
   🔗 https://github.com/oschwartz10612/poppler-windows/releases

2. Extract the ZIP file.

3. Locate the `bin` folder inside extracted directory. Example:  
   ```
   C:\poppler-23.01.0\Library\bin
   ```

4. Add the Poppler bin path to **Environment Variables**:  
   - Search: **Edit system environment variables**
   - Click: **Environment Variables**
   - Under **System Variables** → Select `Path` → Edit → New → Paste the bin path

5. Update this line in `all.py` with your Poppler path:

```python
poppler_path = r"C:\poppler-23.01.0\Library\bin"
```

---

### 🎞️ Step 4: Setup FFmpeg (Required for Video/Audio Conversions)

1. Download FFmpeg:  
   🔗 https://www.gyan.dev/ffmpeg/builds/

2. Download the **release full build (ZIP)** and extract it.

3. Copy the full path to the `bin` folder. Example:  
   ```
   C:\ffmpeg-7.1.1-full_build\bin
   ```

4. Add this path to **Environment Variables** (just like Poppler):  
   - Search: **Edit system environment variables**
   - Go to **Environment Variables**
   - Under **System Variables** → `Path` → Edit → New → Paste the path

5. Test FFmpeg installation by running:

```bash
ffmpeg -version
```

---

## ▶️ Running the Application

Once everything is set up, simply run:

```bash
python all.py
```

✅ Enjoy the GUI with all features enabled!

---

## 📁 Project Structure

```
AllInOneConverter/
├── all.py                 # Main GUI application
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── bgmain.jpg             # Main background
├── ytdowbg.png            # YouTube downloader background
├── qrcodebg.png           # QR Code generator background
├── vtoa.png               # MP4 to MP3 icon
├── yttodow.png            # YouTube download icon
├── ptow.png               # PDF to Word icon
├── wtop.png               # Word to PDF icon
├── ptoi.png               # PDF to Image icon
├── qrcode.png             # QR code icon
└── (All other GUI assets)
```





