import Tkinter as tk
import rumps
import calendar 
import sys
from threading import Thread
from multiprocessing import Process
import time

# Root window
# root = tk.Tk()
# root.withdraw()

class CalStatusBar(rumps.App):
    @rumps.clicked("Update Calendar")
    def update_cal(self, _):
        try:
            print "trying"
            t1 = Process(target = threading_entries, args = (root,))
            t1.start()
        except error:
            print "error"

    @rumps.clicked("Today's Notifications")
    def get_today_events(self, _):
        rumps.notification("Awesome title", "amazing subtitle", "hi!!1")

    @rumps.clicked("Quit app")
    def quit(self, _):
        try:
            # root.destroy()
            rumps.quit_application()
        except error:
            print "error"

class EntryField():
    def __init__(self, root):
        ### Mark: - Entry Fields
        label_date = tk.Label(root, text='Date: ')
        label_date.pack()
        date_ent = tk.Entry(root)
        date_ent.pack()
        # date.insert(INSERT, 'Date')

        label_name = tk.Label(root, text='Event Name: ')
        label_name.pack()
        event_name = tk.Entry(root)
        event_name.pack()
        # date.insert(INSERT, 'Name')

        label_desc = tk.Label(root, text='Description: ')
        label_desc.pack()
        event_desc = tk.Entry(root)
        event_desc.pack()
        # date.insert(INSERT, 'Description')

        ### Mark: - Buttons
        # Cancel update
        cancel_button = tk.Button(root, text='Cancel', command = root.destroy)
        cancel_button.pack()

        # Submit button
        submit_button = tk.Button(root, text='Submit', 
                                  command = lambda: self.submit_cal_entry(date_ent.get(),
                                                                     event_name.get(),
                                                                     event_desc.get(),
                                                                     root))
        submit_button.pack()

        # loop window
        root.deiconify()
        # root.mainloop()

    def submit_cal_entry(self, date, name, desc, root):
        root.destroy()
        print(date)
        print(name)
        print(desc)

def threading_entries(root):
    print "threading"
    app = EntryField(root)
    print "threading"
    root.mainloop()
    print "threading"

if __name__ == "__main__":
    app = CalStatusBar('PC', quit_button=None)
    app.run()
    # root = tk.Tk()
    # t1 = Process(target = threading_entries, args = (root,))
    # t1.start()
    # time.sleep(15)

