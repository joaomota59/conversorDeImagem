'''
instale as seguintes bibliotecas no py com os comandos:
pip install Pillow
'''
from tkinter import filedialog
from tkinter import *
from PIL import Image
from tkinter import messagebox
import tkinter.ttk as ttk

def openFile():
    msg["text"] = 'Processando...'
    image_formats= [("Imagens","*.jpg;*.jpeg;*.png;*.gif;*.apng;*.tiff;*.tif;*.bmp;*.xcf;.*webp")]
    k =  filedialog.askopenfilename(title = "Selecione uma imagem",filetypes=image_formats)
    try:
        pixels=[]    
        im = Image.open(k)
        for i in im.getdata():
            pixels.append(list(i))
        width, height = im.size
        pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
        ##continuar para pegar os pixels e ler como img
        
        w = open('matrizDeCores.txt','w')
        w.writelines(str(pixels))
        w.close()
        messagebox.showinfo('OK','Matriz criada com sucesso!\nConfira o arquivo MatrizdeCores.txt no diretório corrente!')
        msg["text"] = ''
    except:
        msg["text"] = ''
        pass

#main
window = Tk()
window.title("Imagem na Matriz 3D RGB/RGBA ~ BY: JL")
k = ttk.Button(window,text='Selecionar Imagem',command = openFile,cursor="hand2")
window.geometry('400x200+300+50')
k.pack()
msg = ttk.Label(window,text='')
msg.pack()
window.mainloop()   



#salva matrix 3D de cores da imagem no txt
