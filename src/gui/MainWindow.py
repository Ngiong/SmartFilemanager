from tkinter import *
from tkinter import filedialog, messagebox

import os

from smart.filemanager import SmartFileManager


class MainWindow(object):
    def start(self):
        self.window = Tk()
        self.window.geometry('600x400')
        self.window.title('Smart FileManager')

        frame = Frame(self.window)
        frame.pack(expand=TRUE, fill=BOTH)

        background_image = PhotoImage(file = '../res/bgimage.png')
        background_label = Label(frame, image = background_image)
        background_label.pack(expand=TRUE, fill=BOTH)

        # DIRECTORY PICKER
        browser_frame = Frame(frame, bg='#009143', bd=1)
        browser_frame.config(highlightbackground='black')
        browser_frame.place(anchor = 'c', relx = 0.35, rely = 0.65)

        self.directory_text = Entry(browser_frame, width = 50)
        self.directory_text.grid(column = 0, row = 0, padx = 10, pady = 10)

        browse_button = Button(browser_frame, text='Browse', command=self.onClick_browseBtn)
        browse_button.grid(column = 1, row = 0, padx = 10, pady = 10)

        # K PARAMETER INPUT
        k_parameter_frame = Frame(frame)
        k_parameter_frame.place(anchor = 'c', relx = 0.1, rely = 0.85)

        k_label = Label(k_parameter_frame, text = '# Clusters = ')
        k_label.grid(row = 0, column = 0)

        self.k_text = Entry(k_parameter_frame, width = 5)
        self.k_text.insert(0, 3)
        self.k_text.grid(row = 0, column = 1)

        # MAIN BUTTON
        button_frame = Frame(frame)
        button_frame.place(anchor = 'c', relx = 0.85, rely = 0.85)

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
        try:
            if not self.directory_text.get() or not self.k_text.get():
                raise Exception('Directory path and # Clusters cannot be NULL.')
            if not os.path.isdir(self.directory_text.get()):
                raise Exception('Directory path does not exist.')
            if int(self.k_text.get()) <= 0:
                raise Exception('# Clusters must be greater than 0.')

            messagebox.showinfo('Clustering...', 'SIAPPP BOSS!! Ditunggu yach... :)')

            # Do clustering here :)
            sfm = SmartFileManager(self.directory_text.get(), use_gui=True)
            sfm.manage(int(self.k_text.get()))

            messagebox.showinfo('DONE', 'SUDAH SELESAI BOSS!!')

        except Exception as e:
            messagebox.showerror('Exception caught', str(e))

    def onClick_quitBtn(self):
        self.window.destroy()
