import requests
import tkinter


def isblocked(uid):
    url = 'http://localhost/blocked.php'
    r = requests.post(url, data={"uid": uid})
    if(r.text=='true'):
        from tkinter import messagebox
        messagebox.showerror("Blocked", "This card is blocked")
        return True
    return False
class BlockingApp:
    def __init__(self,root):
        self.root=root
        self.root.withdraw()
        self.window = tkinter.Tk()
        self.uid_label = tkinter.Label(self.window, text='UID : ')
        self.uid_entry = tkinter.Entry(self.window)
        self.block_button=tkinter.Button(self.window,text="Block",command=self.block)
        self.unblock_button=tkinter.Button(self.window,text="Unlock",command=self.unblock)
        self.uid_label.pack()
        self.uid_entry.pack()
        self.block_button.pack()
        self.unblock_button.pack()
        def close():
            self.root.deiconify()
            self.window.destroy()
        self.window.protocol("WM_DELETE_WINDOW", close)

    def block(self):
        if self.uid_entry.get()=="":
            from tkinter import messagebox
            messagebox.showerror(title="blank uid",message="please enter uid")
            return
        url = 'http://localhost/block.php'
        r = requests.post(url, data={"uid": self.uid_entry.get()})
        print('uid' + self.uid_entry.get())
        print(r.text)
        if (r.text == 'true'):
            from tkinter import messagebox
            messagebox.showinfo("Blocked", "This card is blocked successfully")

    def unblock(self):
        if self.uid_entry.get()=="":
            from tkinter import messagebox
            messagebox.showerror(title="blank uid",message="please enter uid")
            return
        url = 'http://localhost/unblock.php'
        r = requests.post(url, data={"uid": self.uid_entry.get()})
        if (r.text == 'true'):
            from tkinter import messagebox
            messagebox.showinfo("Unblocked", "This card is unblocked successfully")
def controls(root):
    BlockingApp(root).window.mainloop()