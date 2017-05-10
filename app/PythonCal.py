import Tkinter as tk
import rumps
import calendar
import sys
import threading

# Root window
root = tk.Tk()
# root.withdraw()

class CalStatusBar(rumps.App):
    @rumps.clicked("Update Calendar")
    def update_cal(self, _):
        # threading.Thread(target=create_window).start()
        ef = EntryField(root)
        # ef.create_window()
        root.mainloop()

    @rumps.clicked("Today's Notifications")
    def get_today_events(self, _):
        rumps.notification("Awesome title", "amazing subtitle", "hi!!1")

class EntryField():
    def __init__(self, root):
        self.root = root

    # def create_window(self):
        ### Mark: - Window Creation
        self.root.title("Update Calendar")

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
                                                                     event_desc.get()))
        submit_button.pack()
        loop = 1

        # loop window
        # self.root.deiconify()
        # self.root.mainloop()

    def submit_cal_entry(date, name, desc):
        self.root.destroy()
        print(date)
        print(name)
        print(desc)

if __name__ == "__main__":
    app = CalStatusBar('PC')
    app.run()
    # create_window()

