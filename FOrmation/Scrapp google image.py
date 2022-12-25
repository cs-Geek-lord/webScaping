from gi_scraper import Scraper

from tkinter import *
import os

def Scrap():
    key = txtfld1.get()
    number = int(txtfld2.get())
    key = key.split(",")

    scraper = Scraper(process_count=4)
    for query in key:
        
        scraped_response = scraper.scrape(query=query,count=number)
        currentPath = os.path.realpath(os.path.dirname(__file__))
        scraped_response.write(path=currentPath+"/images", filename="query").download(path=currentPath +"/images", thread_count=1)
        scraped_response.get()
    scraper.close()

# important since the library implements multiprocessing
if __name__ == "__main__":

    # creating Scraper object
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
