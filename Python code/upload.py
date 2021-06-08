import tkinter
from tkinter.filedialog import askopenfilename
import time
#uid=input('Enter rfid uid : ')
def upload(uid,root_refresh):
    filename=''
    window1=tkinter.Tk()
    tkinter.Label(window1,text="Document name").pack()
    docname=tkinter.Entry(window1)
    docname.pack()
    def openFile():
        if docname.get()=="":
            from tkinter import messagebox
            messagebox.showerror(title="File name blank",message="Please enter filename")
            return
        filename=askopenfilename(title='choose document to upload',filetypes=[('image files','*.png;*.jpg;*.jpeg;*.bmp')])
        print(filename)
        import requests
        url = 'http://localhost/upload.php'
        files = {'file': open(filename, 'rb')}
        r = requests.post(url, files=files,data={"name":docname.get(),"uid":uid})
        print(r.text)
        window1.destroy()
        window1.quit()
        root_refresh()
    uploadButton=tkinter.Button(window1,text="Upload",command=openFile)
    uploadButton.pack()
    window1.mainloop()