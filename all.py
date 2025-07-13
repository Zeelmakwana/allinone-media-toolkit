# from tkinter.filedialog import *
from tkinter import *
from tkinter import ttk,font
import moviepy.editor
import tkinter.messagebox as messagebox
from yt_dlp import YoutubeDL
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk
import requests
from io import BytesIO
import os
import tqdm
import qrcode
from pdf2docx import Converter
from docx2pdf import convert
from pdf2image import convert_from_path
from pdf2image.exceptions import PDFPageCountError, PDFSyntaxError, PDFInfoNotInstalledError

aio = Tk()
image1 = Image.open("bgmain.jpg")
image1 = ImageTk.PhotoImage(image1)
screen_width = aio.winfo_screenwidth()
screen_height = aio.winfo_screenheight()
aio.geometry(f"{screen_width}x{screen_height}")
mainbg = Label(aio, image=image1).pack()


def vtoa():
    try:
        opvi = askopenfilename()
        vid = moviepy.editor.VideoFileClip(opvi)
        aud = vid.audio
        sf = asksaveasfilename(defaultextension=".mp3",
                               filetypes=[("MP3 Audio")])
        if sf:
            # Write audio file to the user-defined location and filename
            aud.write_audiofile(sf)
    except Exception:
        messagebox.showerror("warning", "please select a mp4 file")


photo = PhotoImage(file="vtoa.png")
sp = photo.subsample(9, 10)
b2 = Button(aio, command=vtoa, relief="raised",
            image=sp, bd=5).place(x=20, y=50)


from yt_dlp import YoutubeDL  # ✅ new import

def ytdow():
    global image2, thumbnail, link_v, ytt, l2, l3, video_info

    def start_download():
        global video_info
        link = link_v.get().strip()
        if not link:
            messagebox.showerror("Error", "Please enter a YouTube URL.")
            return
        try:
            ydl_opts = {'quiet': True}
            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(link, download=False)
                video_info = info
                ytt.set(info['title'])

                # Thumbnail image
                thumb_url = info['thumbnail']
                response = requests.get(thumb_url)
                img = Image.open(BytesIO(response.content)).resize((750, 425))
                thumbnail_img = ImageTk.PhotoImage(img)

                l2.configure(image=thumbnail_img)
                l2.image = thumbnail_img  # Keep a reference
                l2.place(x=130, y=90)

                l3.place(x=120, y=140)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch video info:\n{e}")

    def dow():
        try:
            if not video_info:
                messagebox.showwarning("Warning", "Please load video info first.")
                return

            sf1 = asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 Video", "*.mp4")])
            if not sf1:
                return

            ydl_opts = {
                'outtmpl': sf1,  # Save path provided by user
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
                'merge_output_format': 'mp4'
            }

            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_info['webpage_url']])

            messagebox.showinfo("Success", "Video downloaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Download failed:\n{e}")

    yt = Toplevel(aio)
    screen_width = 1000
    screen_height = 650
    yt.geometry(f"{screen_width}x{screen_height}+270+110")

    image2 = Image.open("ytdowbg.png").resize((1000, 650))
    image2 = ImageTk.PhotoImage(image2)
    ytbg = Label(yt, image=image2)
    ytbg.image = image2  # keep reference
    ytbg.place(x=0, y=0)

    ttk.Label(yt, text="YT video link:", font=('Arial 15')).place(x=110, y=30)

    link_v = ttk.Entry(yt, width=55, font=('Arial 15'))
    link_v.place(x=250, y=30)

    ytt = StringVar()
    l3 = Label(yt, textvariable=ytt, font=('Helvetica 15 bold'), fg='white', bg='red', wraplength=750)
    l3.place_forget()

    l2 = Label(yt, height=425, width=750)
    l2.place_forget()

    Button(yt, text="Convert", command=start_download, bg="#4CAF50", fg="white", font=("Arial", 15, "bold")).place(x=880, y=25)

    style = ttk.Style()
    style.configure('MyButtonStyle.TButton', font=('Arial', 15, 'bold'), padding=10)
    ttk.Button(yt, text="Download", command=dow, style='MyButtonStyle.TButton').place(x=400, y=590)




photo = PhotoImage(file="yttodow.png")
sp2 = photo.subsample(9, 10)
b3 = Button(aio, command=ytdow, relief="raised",
            image=sp2, bd=5).place(x=20, y=300)


def qrcodegen():
    global image2

    def genqr():
        try:
            global qcimg
            link2 = link_c.get()
            if not link2:
                raise ValueError("Link cannot be empty")
            qc = qrcode.QRCode(
                version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=13, border=2)

            qc.add_data(link2)
            qc.make(fit=True)
            qcimg = qc.make_image(fill_color=fgcolor.get(),
                                  back_color=bgcolor.get())
            qcimg_tk = ImageTk.PhotoImage(qcimg)
            qrlabel = Label(qr, image=qcimg_tk)
            qrlabel.image = qcimg_tk
            qrlabel.place(x=300, y=80)
        except Exception as e:
            messagebox.showwarning("somthing went wrong", str(e))

    def saveqr():
        try:
            sf2 = asksaveasfilename(defaultextension=".png",
                                    filetypes=[("PNG Image")])
            if not sf2:
                return
            qcimg.save(sf2)
        except Exception as e:
            messagebox.showwarning("somthing went wrong", str(e))
    qr = Toplevel(aio)
    screen_width = 1000
    screen_height = 650
    qr.geometry(f"{screen_width}x{screen_height}")
    x = 270
    y = 110
    qr.geometry("+%d+%d" % (x, y))
    image2 = Image.open("qrcodebg.png")
    new_width = 1000
    new_height = 650
    resized_image = image2.resize((new_width, new_height))
    image2 = ImageTk.PhotoImage(resized_image)
    qrbg = Label(qr, image=image2)
    qrbg.place(x=0, y=0)

    l3 = ttk.Label(qr, text="Provide link:-",
                   font=('Arial 15'), style='My.TLabel')
    l3.place(x=110, y=30)

    # Create the entry widget with the custom style and increased height

    link_c = ttk.Entry(qr, width=55, font=('Arial 15'))
    link_c.place(x=250, y=30)
    l4 = ttk.Label(qr, text="Enter QR Color :-",
                   font=('Arial 14'), style='My.TLabel')
    l4.place(x=25, y=120)
    fgcolor = ttk.Entry(qr, width=10, font=('Arial 14'))
    fgcolor.place(x=40, y=150)

    l5 = ttk.Label(qr, text="Enter Background Color:-",
                   font=('Arial 14'), style='My.TLabel')
    l5.place(x=20, y=250)
    bgcolor = ttk.Entry(qr, width=10, font=('Arial 15'))
    bgcolor.place(x=60, y=280)

    gqr = Button(qr, text=" Generate", font=('Helvetica 20 bold'),
                 foreground='red', background='green', padx=10, pady=5, command=genqr)
    gqr.place(x=50, y=400)
    sqr = Button(qr, text="download", font=('Helvetica 20 bold'),
                 foreground='blue', background='yellow', padx=10, pady=5, command=saveqr)
    sqr.place(x=50, y=500)
    l6 = ttk.Label(qr, text="Note: Please Change Color Combination IF There Was Any Issue While Scanning",
                   font=('Arial', 18), style='My.TLabel', foreground='red', background='black')
    l6.place(x=40, y=585)


photo2 = PhotoImage(file="qrcode.png")
sp3 = photo2.subsample(9, 10)
b4 = Button(aio, command=qrcodegen, relief="raised",
            image=sp3, bd=5).place(x=20, y=550)


def ptow():
    # Ask the user to select a PDF file
    pdf_file = askopenfilename(defaultextension=".pdf", filetypes=[
                               ("PDF Files", "*.pdf")])
    if pdf_file:
        # Ask the user to save the converted Word document
        doc_file = asksaveasfilename(defaultextension=".docx", filetypes=[
                                     ("Word Document", "*.docx")])
        if doc_file:
            # Convert the PDF to Word using pdf2doc module
            converter = Converter(pdf_file)
            converter.convert(doc_file, start=0, end=None)
            converter.close()
            messagebox.showinfo(
                "Success", "PDF converted to Word successfully!")


def wtop():
    docx = askopenfilename(defaultextension=".docx", filetypes=[
                           ("docx document", "*.docx")])
    if docx:
        pdf = asksaveasfilename(defaultextension=".pdf", filetypes=[
                                ("PDF files", "*.pdf")])
        if pdf:
            convert(docx, pdf)
            messagebox.showinfo(
                "Success", "PDF converted to Word successfully!")


photo2 = PhotoImage(file="ptow.png")
sp4 = photo2.subsample(9, 10)
b5 = Button(aio, command=ptow, relief="raised",
            image=sp4, bd=5).place(x=1270, y=50)


photo2 = PhotoImage(file="wtop.png")
sp5 = photo2.subsample(9, 10)
b5 = Button(aio, command=wtop, relief="raised",
            image=sp5, bd=5).place(x=1270, y=300)


def ptoi():
    pdf_file2 = askopenfilename(defaultextension=".pdf", filetypes=[
                                ("PDF Files", "*.pdf")])
    if pdf_file2:
        img_file = asksaveasfilename(defaultextension=".jpg", filetypes=[
                                     ("JPEG file", "*.jpg")])
        if img_file:
            try:
                coni = convert_from_path(
                    pdf_file2, poppler_path=r"E:\my projects\all in one\poppler-23.01.0\Library\bin")
                for i, img in enumerate(coni):
                    page_file = os.path.splitext(
                        img_file)[0] + f"_page{i+1}.jpg"
                    img.save(page_file)
                messagebox.showinfo(
                    "Success", "PDF converted to image successfully!")
            except (PDFPageCountError, PDFSyntaxError, PDFInfoNotInstalledError) as e:
                messagebox.showerror(
                    "Error", f"An error occurred while converting PDF to image: {str(e)}")


photo2 = PhotoImage(file="ptoi.png")
sp6 = photo2.subsample(9, 10)
b6 = Button(aio, relief="raised",
            image=sp6, command=ptoi, bd=5).place(x=1270, y=550)

l7 = ttk.Label(aio, text="All In One Converter", font=('Arial', 35), style='My.TLabel', foreground='red', compound='center', background='green')
l7.place(x=500, y=5)


 

aio.mainloop()
