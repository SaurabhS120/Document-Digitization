import tkinter
import threading
# Importing Libraries
import serial
import time
def wait():
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
class RfidDetails:
    def __init__(self):
        super().__init__()
        self.uid=None
class RFIDscanningThread(threading.Thread):
    def __init__(self,arduino,rfidDetails,window):
        super().__init__()
        self.arduino =arduino
        self.stop=False
        self.uid=''
        self.rfidDetails=rfidDetails
        self.window=window
    def run(self):
        # print uid
        data = b''
        while (len(data) == 0):
            if self.stop:
                self.dead=True
                return
            data = self.arduino.readline()
        self.uid=str(data.decode('utf-8').strip())
        self.rfidDetails.uid=self.uid
        window.quit()

class RFIDScanner:
    def __init__(self,rfidDetails,window):
        super().__init__()
        self.arduino = serial.Serial(port='COM13', baudrate=9600, timeout=.1)
        self.scannerThread=None
        self.rfidDetails=rfidDetails
        self.window=window
    def start_scan(self):
        print("start scan")
        if self.scannerThread!=None:
            if(self.scannerThread.is_alive()):
                self.scannerThread.stop=True
        self.arduino.write(bytes("start", 'utf-8'))
        # new code
        start_time = time.time()
        success = False
        while (time.time() - start_time < 10):
            data = self.arduino.readline()
            if (data.decode('utf-8').strip() == 'SCAN'):
                print('scanning started')
                success = True
                break
        if not success:
            print("scanning not started")
            return

        self.scannerThread=RFIDscanningThread(self.arduino,self.rfidDetails,self.window)
        self.scannerThread.start()
    def stop_scan(self):
        self.stop=True
        self.arduino.write(bytes("stop", 'utf-8'))
        if self.scannerThread!=None:
            if(self.scannerThread.is_alive()):
                self.scannerThread.stop=True
        # new code
        start_time = time.time()
        success = False
        while (time.time() - start_time < 10):
            data = self.arduino.readline()
            if (data.decode('utf-8').strip() == 'STOP'):
                print('scanning Stopped')
                success = True
                break
        if not success:
            print("Cant stop scanning")
            return

window=tkinter.Tk()
rfidDetalis=RfidDetails()
rfidScanner=RFIDScanner(rfidDetalis,window)
def start_scan():
    rfidScanner.start_scan()
    wait()
start_button=tkinter.Button(window,text="Start",command=start_scan)
start_button.pack()
def stop_scan():
    rfidScanner.stop_scan()
    wait()
stop_button=tkinter.Button(window,text="stop",command=stop_scan)
stop_button.pack()
def close_event():
    rfidScanner.stop_scan()

    exit(0)
window.protocol("WM_DELETE_WINDOW", close_event)
print("starting...")
wait()
window.mainloop()
window.destroy()
window.quit()
print(rfidDetalis.uid)
import docs_list
docs_list.show_docs(rfidDetalis.uid)
