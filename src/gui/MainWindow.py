from tkinter import *
from tkinter import filedialog


class MainWindow(object):
    def start(self):
        self.window = Tk()
        self.window.geometry('600x400')
        self.window.title('Smart FileManager')

        frame = Frame(self.window)
        frame.pack(expand=TRUE, fill=BOTH)

        # DIRECTORY PICKER
        browser_frame = Frame(frame, bg='red')
        browser_frame.place(anchor = 'c', relx = 0.5, rely = 0.65)

        self.directory_text = Entry(browser_frame, width = 50)
        # self.directory_text.config(state = DISABLED)
        self.directory_text.grid(column = 0, row = 0, padx = 10, pady = 10)

        browse_button = Button(browser_frame, text='Browse', command=self.onClick_browseBtn)
        browse_button.grid(column = 1, row = 0, padx = 10, pady = 10)

        # MAIN BUTTON
        button_frame = Frame(frame, bg='blue')
        button_frame.place(anchor = 'c', relx = 0.75, rely = 0.85)

        quit_button = Button(button_frame, text='QUIT :(', command=self.onClick_quitBtn)
        quit_button.pack(side = RIGHT, padx = 5)

        cluster_button = Button(button_frame, text='DO YOUR JOB!', command=self.onClick_clusterBtn)
        cluster_button.pack(side = RIGHT, padx = 5)

        self.window.mainloop()

    def onClick_browseBtn(self):
        dirpath = filedialog.askdirectory(initialdir=".", title="Select directory")
        self.directory_text.delete(0, END)
        self.directory_text.insert(0, dirpath)

    def onClick_clusterBtn(self):
        print('Dung tek dung tek dung... bedes bedes bedes... lulululululu.. woooo!!!!!')

    def onClick_quitBtn(self):
        self.window.destroy()
