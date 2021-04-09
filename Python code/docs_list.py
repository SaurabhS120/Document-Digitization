import tkinter
from tkinter.filedialog import askopenfilename
import show_img
import upload
def show_docs(uid):
    window=tkinter.Tk()
    list=tkinter.Listbox(window)
    doc_list=[]
    def refresh():
        import requests
        url = 'http://localhost/docs_list.php'
        r = requests.post(url,data={"uid":uid})
        print(r.text)
        doc_list.clear()
        list.delete(0,tkinter.END)
        for row in r.text.split(","):
            doc_list.append(row.split(":"))
        for i in range(len(doc_list)):
            list.insert(i,doc_list[i][0])
    def openimg(event):
        cs = list.curselection()
        for i in cs:
            show_img.show(doc_list[i][1])
    refresh()
    def uploadfile():
        window.quit()
        upload.upload(uid,refresh)
    list.bind('<Double-1>', openimg)
    upload_button=tkinter.Button(window,text="Upload",command=uploadfile)
    list.pack();
    upload_button.pack()
    window.mainloop()
# uid=input('Enter rfid uid : ')
# show_docs(uid)