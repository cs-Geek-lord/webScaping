try:
   from bing_image_downloader import downloader
except ImportError:
    import pip
    failed = pip.main(["install", 'bing_image_downloader'])
    from bing_image_downloader import downloader
from tkinter import *


def Scrap():
    key = txtfld1.get()
    number = int(txtfld2.get())
    downloader.download(key, limit=number,  output_dir='./dataset', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)

window=Tk()

lbl = Label(window, text="Entrer Votre mot clé: ")
lbl.place(x=40, y=50)

lbl = Label(window, text="Entrer Votre nombre d'image: ")
lbl.place(x=40, y=100)

txtfld1=Entry(window, bd=5)
txtfld1.place(x=250, y=50)

txtfld2=Entry(window, bd=5)
txtfld2.place(x=250, y=100)

btn=Button(window, text="Télécharger", fg='blue', command=Scrap)
btn.place(x=280, y=150)

window.title('Scrapping')
window.geometry("600x250+700+450")
window.mainloop()




