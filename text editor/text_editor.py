from tkinter import *
from PIL import ImageTk,Image
root=Tk()

root.geometry("1300x900")
root.title("TEXT-EDITOR")
root.minsize(700,800)
def start():
    global Scroll
    f1=Frame(bg="black")
    f1.place(x=0,y=0,width=1300,height=900 )
    def cut():
      TextArea.event_generate(("<<Cut>>"))

    def copy():
      TextArea.event_generate(("<<Copy>>"))

    def paste():
      TextArea.event_generate(("<<Paste>>"))
    menu1=Menu(root)
    my_menu=Menu(menu1,tearoff=0)
    my_menu.add_command(label="cut",command=cut)
    my_menu.add_command(label="copy",command=copy)
    my_menu.add_command(label="paste",command=paste)
    #my_menu.add_command(label="size")
    root.config(menu=menu1)
    menu1.add_cascade(label="file",menu=my_menu)
    TextArea=Text(f1,font="lucida 13")
    file=None
    TextArea.pack(expand=True,fill="both")
    Scroll=Scrollbar( TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command= TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)
    


bg = ImageTk.PhotoImage(Image.open("office.jpg").resize((1300,800)))
canva1 = Canvas(root,width=1300,height=900)
canva1.pack(fill="both" )
canva1.create_image(640,400,image=bg)
img= ImageTk.PhotoImage(Image.open("th.jpeg").resize((200,50)))
canva1.create_image(500,300,image=img)
Button1=Button(root,image=img,bg="white",command=start)
canva1.create_window(500,300,window=Button1)
canva1.create_text(500,150,text="TEXT-EDITOR",font="DS-Digital 72 bold",fill="brown")
canva1.create_text(500,220,text="START HERE",font="DS-Digital 40 bold")



root.mainloop()