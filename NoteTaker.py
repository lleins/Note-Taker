from tkinter import *
import os.path
from os.path import exists
from tkinter import scrolledtext  # For Beta Version the password is always "Pass"
import os


'''
Updated Last: December 31, 2022

*Made Windows appear in center of screen*
'''





def Check_txt_Files_Lenght():
    dir_path = "C:\\Notes\\"
    res = []
    for file in os.listdir(dir_path):
        if file.endswith(".txt"):
            res.append(file + "\n")
    return (len(res))

def Check_txt_Files():
    dir_path = "C:\\Notes\\"
    res = []
    for file in os.listdir(dir_path):
        if file.endswith(".txt"):
            res.append(file + "\n")
    return (''.join(res))



def Close_Main_Window():
    MainWindow.destroy()

dir = os.path.join("C:\\","Notes")

if os.path.exists(dir):
    ""
else:
    os.mkdir(dir)
    path = "C:\\Notes\\"


def File_Exists(File_Name):
    exists = os.path.isfile("C:\\Notes\\" + File_Name)
    return exists



def New_Note():
    def Close_Create_Window():
        CreateWindow.destroy()

    def File_Exists(name):
        exists = os.path.isfile("C:\\Notes\\" + name + ".txt")
        return exists

    def Create_New_Note():
        if (File_Exists(name_fld.get()) == True):
            lbl_Error_Rename = Label(CreateWindow, text="Name already exists",
                                     font=("Calibri", 9, "bold"), bg='grey15', fg="red2")
            lbl_Error_Rename.place(x=90, y=60)
            lbl_Error_Rename.after(2500, lambda: lbl_Error_Rename.destroy())

        elif (File_Exists(name_fld.get()) == False):
            New_File_Creation = "C:\\Notes\\" + name_fld.get() + ".txt"
            Open_Gmail_File = open(New_File_Creation, "w")
            Open_Gmail_File.close()
            CreateWindow.wm_attributes('-alpha', 0)
            MainWindow.wm_attributes('-alpha', 0.0)
            Note_fld = scrolledtext.ScrolledText(MainWindow, bd=1, fg='grey90', font=("Arial", 11, 'bold'),
                                                 bg="grey20", width=24,
                                                 height=16)  # bodyfld.get(1.0, "end-1c")   Use this format when grabbing entered text from textbox
            Note_fld.place(x=35, y=50)
            Note_fld.insert(1.0, Check_txt_Files())
            Note_fld.config(state=DISABLED)
            Note_fld.config(insertbackground="light goldenrod")  # Changes test cursor color

            def Write_File(File_Path, Text_toFile):
                file_content = open(File_Path, "w")  # Writes text to a given .txt file
                file_content.write(Text_toFile)
                file_content.close()

            def Read_File(File_Path):
                file_content = open(File_Path, "r")
                if (exists(File_Path)):  # opens/reads a file with a given file path....
                    return (file_content.read())
                else:
                    raise Exception("Error, File not present or empty....")

            def Close_Note_Window():
                open_fld.delete(0, END)
                CreateWindow.destroy()
                NoteWindow.destroy()
                MainWindow.wm_attributes('-alpha', .9)

            def Save():
                Write_File("C:\\Notes\\" + name_fld.get() + ".txt", Note_fld.get(1.0, "end-1c"))
                lbl_top_header = Label(NoteWindow, text="Saved..", bd=1, fg='green2', font=("Arial", 8, 'bold'),
                                       bg="grey15", anchor="w")
                lbl_top_header.place(x=300, y=60)
                lbl_top_header.after(2500, lambda: lbl_top_header.destroy())

            def Rename():

                def File_Exists(name):
                    exists = os.path.isfile("C:\\Notes\\" + name + ".txt")
                    return exists

                def Rename_Official():
                    if (File_Exists(rename_fld.get()) == False):
                        Original = "C:\\Notes\\" + name_fld.get() + ".txt"
                        New = "C:\\Notes\\" + rename_fld.get() + ".txt"
                        os.rename(Original, New)
                        Note_fld = scrolledtext.ScrolledText(MainWindow, bd=1, fg='grey90', font=("Arial", 11, 'bold'),
                                                             bg="grey20", width=24,
                                                             height=16)  # bodyfld.get(1.0, "end-1c")   Use this format when grabbing entered text from textbox
                        Note_fld.place(x=35, y=50)
                        Note_fld.insert(1.0, Check_txt_Files())
                        Note_fld.config(state=DISABLED)
                        Note_fld.config(insertbackground="light goldenrod")  # Changes test cursor color
                        NoteWindow.destroy()
                        open_fld.delete(0, END)
                        RenameWindow.destroy()
                        NoteWindow.destroy()

                    elif (File_Exists(rename_fld.get()) == True):
                        lbl_Error_Rename = Label(RenameWindow, text="Name already exists",
                                                 font=("Calibri", 9, "bold"), bg='grey15', fg="red2")
                        lbl_Error_Rename.place(x=90, y=60)
                        lbl_Error_Rename.after(2500, lambda: lbl_Error_Rename.destroy())

                def Close_Rename_Window():
                    RenameWindow.destroy()

                RenameWindow = Toplevel()

                RenameWindow_app_width = 300
                RenameWindow_app_height = 200

                RenameWindow_screen_width = RenameWindow.winfo_screenwidth()
                RenameWindow_screen_height = RenameWindow.winfo_screenheight()

                RenameWindow_x = int((RenameWindow_screen_width / 2) - (RenameWindow_app_width / 2))
                RenameWindow_y = int((RenameWindow_screen_height / 2) - (RenameWindow_app_height / 2))

                lbl_top_Title = Label(RenameWindow, text="Rename " + name_fld.get() + ".txt", bd=1, fg='light goldenrod',
                                      font=("Arial", 14, 'bold'), bg="grey20", width=20)  # open_fld.get()
                lbl_top_Title.place(x=30, y=25)

                lbl_Note_Rename = Label(RenameWindow, text="*Note*\nDo not include\nFile extension.\n Name Only",
                                        font=("Calibri", 7, "bold"), bg='grey15', fg="red2")
                lbl_Note_Rename.place(x=220, y=130)

                rename_fld = Entry(RenameWindow, bd=1, fg='grey90', font=("Arial", 11, 'bold'), bg="grey20", width=20)
                rename_fld.config(insertbackground="light goldenrod")
                rename_fld.place(x=65, y=90)

                btn_Rename = Button(RenameWindow, text="Re-Name", font=("Arial", 8, 'bold'), fg='white', bg='blue',
                                    height=1, relief="flat", command=Rename_Official)  # Azure3
                btn_Rename.place(x=115, y=135)

                RenameWindow.wm_attributes('-alpha', 1)  # Transparency
                RenameWindow.protocol("WM_DELETE_WINDOW",
                                      Close_Rename_Window)  # controling the function of the close window icon (top right of window)
                RenameWindow.resizable(False, False)  # Cannot change size of the Window(It is locked)
                RenameWindow.title('Confirm')  # Add Username to top of WebPage
                RenameWindow.geometry(f'{RenameWindow_app_width}x{RenameWindow_app_height}+{RenameWindow_x}+{RenameWindow_y}')
                RenameWindow.configure(bg='grey15')
                RenameWindow.mainloop()

            def Delete():
                def Close_Confirm_Window():
                    ConfirmWindow.destroy()

                def Confirm_Delete():
                    def Remove_File(File_Name):
                        path = "C:\\Notes\\" + File_Name
                        os.remove(path)

                    Remove_File(name_fld.get() + ".txt")
                    Note_fld = scrolledtext.ScrolledText(MainWindow, bd=1, fg='grey90', font=("Arial", 11, 'bold'),
                                                         bg="grey20", width=24,
                                                         height=16)  # bodyfld.get(1.0, "end-1c")   Use this format when grabbing entered text from textbox
                    Note_fld.place(x=35, y=50)
                    Note_fld.insert(1.0, Check_txt_Files())
                    Note_fld.config(state=DISABLED)
                    Note_fld.config(insertbackground="light goldenrod")  # Changes test cursor color
                    ConfirmWindow.destroy()
                    NoteWindow.destroy()
                    MainWindow.wm_attributes('-alpha', .9)
                    open_fld.delete(0, END)

                ConfirmWindow = Tk()

                ConfirmWindow_app_width = 300
                ConfirmWindow_app_height = 200

                ConfirmWindow_screen_width = ConfirmWindow.winfo_screenwidth()
                ConfirmWindow_screen_height = ConfirmWindow.winfo_screenheight()

                ConfirmWindow_x = int((ConfirmWindow_screen_width / 2) - (ConfirmWindow_app_width / 2))
                ConfirmWindow_y = int((ConfirmWindow_screen_height / 2) - (ConfirmWindow_app_height / 2))

                lbl_top_Confirm = Label(ConfirmWindow, text="Are you Sure?", bd=1, fg='light goldenrod',
                                        font=("Arial", 14, 'bold'), bg="grey20", width=20)
                lbl_top_Confirm.place(x=30, y=25)

                btn_No = Button(ConfirmWindow, text="No", font=("Arial", 8, 'bold'), fg='white', bg='red', height=1,
                                width=5, relief="flat", command=Close_Confirm_Window)  # Azure3
                btn_No.place(x=80, y=100)

                btn_Yes = Button(ConfirmWindow, text="Yes", font=("Arial", 8, 'bold'), fg='white', bg='green', height=1,
                                 width=5, relief="flat", command=Confirm_Delete)  # Azure3
                btn_Yes.place(x=180, y=100)

                ConfirmWindow.wm_attributes('-alpha', 1)  # Transparency
                ConfirmWindow.protocol("WM_DELETE_WINDOW",
                                       Close_Confirm_Window)  # controling the function of the close window icon (top right of window)
                ConfirmWindow.resizable(False, False)  # Cannot change size of the Window(It is locked)
                ConfirmWindow.title('Confirm')  # Add Username to top of WebPage
                ConfirmWindow.geometry(f'{ConfirmWindow_app_width}x{ConfirmWindow_app_height}+{ConfirmWindow_x}+{ConfirmWindow_y}')
                ConfirmWindow.configure(bg='grey15')
                ConfirmWindow.mainloop()

            NoteWindow = Toplevel()

            NoteWindow_app_width = 400
            NoteWindow_app_height = 500

            NoteWindow_screen_width = NoteWindow.winfo_screenwidth()
            NoteWindow_screen_height = NoteWindow.winfo_screenheight()

            NoteWindow_x = int((NoteWindow_screen_width / 2) - (NoteWindow_app_width / 2))
            NoteWindow_y = int((NoteWindow_screen_height / 2) - (NoteWindow_app_height / 2))

            Note_fld = scrolledtext.ScrolledText(NoteWindow, bd=1, fg='grey90', font=("Arial", 11, 'bold'), bg="grey20",
                                                 width=39,
                                                 height=20)  # bodyfld.get(1.0, "end-1c")   Use this format when grabbing entered text from textbox
            Note_fld.place(x=35, y=90)
            Note_fld.insert(1.0, Read_File("C:\\Notes\\" + name_fld.get() + ".txt"))
            Note_fld.config(insertbackground="light goldenrod")  # Changes test cursor color

            lbl_top_header = Label(NoteWindow, text=name_fld.get() + ".txt", bd=1, fg='light goldenrod',
                                   font=("Arial", 14, 'bold'),
                                   bg="grey20", width=27, anchor="w")
            lbl_top_header.place(x=38, y=25)

            btn_Delete = Button(NoteWindow, text="Delete", font=("Arial", 8, 'bold'), fg='white', bg='red', height=1,
                                width=5, relief="flat", command=Delete)  # Azure3
            btn_Delete.place(x=35, y=465)

            btn_Save = Button(NoteWindow, text="Save", font=("Arial", 8, 'bold'), fg='white', bg='green', height=1,
                              width=5,
                              relief="flat", command=Save)  # Azure3
            btn_Save.place(x=324, y=465)

            btn_Rename = Button(NoteWindow, text="Re-Name", font=("Arial", 8, 'bold'), fg='white', bg='blue', height=1,
                                relief="flat", command=Rename)  # Azure3
            btn_Rename.place(x=170, y=465)

            NoteWindow.wm_attributes('-alpha', .9)  # Transparency
            NoteWindow.protocol("WM_DELETE_WINDOW",
                                Close_Note_Window)  # controling the function of the close window icon (top right of window)
            NoteWindow.resizable(False, False)  # Cannot change size of the Window(It is locked)
            NoteWindow.title('Notes')  # Add Username to top of WebPage
            NoteWindow.geometry(f'{NoteWindow_app_width}x{NoteWindow_app_height}+{NoteWindow_x}+{NoteWindow_y}')
            NoteWindow.configure(bg='grey15')
            NoteWindow.mainloop()
            #####

    CreateWindow = Toplevel()

    CreateWindow_app_width = 300
    CreateWindow_app_height = 200

    CreateWindow_screen_width = CreateWindow.winfo_screenwidth()
    CreateWindow_screen_height = CreateWindow.winfo_screenheight()

    CreateWindow_x = int((CreateWindow_screen_width / 2) - (CreateWindow_app_width / 2))
    CreateWindow_y = int((CreateWindow_screen_height / 2) - (CreateWindow_app_height / 2))

    lbl_top_Title = Label(CreateWindow, text="Enter Name ", bd=1, fg='light goldenrod', font=("Arial", 14, 'bold'),
                          bg="grey20", width=20)  # open_fld.get()
    lbl_top_Title.place(x=30, y=25)

    lbl_Note_Rename = Label(CreateWindow, text="*Note*\nDo not include\nFile extension.\n Name Only",
                            font=("Calibri", 7, "bold"), bg='grey15', fg="red2")
    lbl_Note_Rename.place(x=220, y=130)

    name_fld = Entry(CreateWindow, bd=1, fg='grey90', font=("Arial", 11, 'bold'), bg="grey20", width=20)
    name_fld.config(insertbackground="light goldenrod")
    name_fld.place(x=65, y=90)

    btn_Create = Button(CreateWindow, text="Create", font=("Arial", 8, 'bold'), fg='white', bg='green', height=1,
                        relief="flat", command = Create_New_Note)  # Azure3
    btn_Create.place(x=115, y=135)

    CreateWindow.wm_attributes('-alpha', 1)  # Transparency
    CreateWindow.protocol("WM_DELETE_WINDOW",
                          Close_Create_Window)  # controling the function of the close window icon (top right of window)
    CreateWindow.resizable(False, False)  # Cannot change size of the Window(It is locked)
    CreateWindow.title('Confirm')  # Add Username to top of WebPage
    CreateWindow.geometry(f'{CreateWindow_app_width}x{CreateWindow_app_height}+{CreateWindow_x}+{CreateWindow_y}') #300x200
    CreateWindow.configure(bg='grey15')
    CreateWindow.mainloop()



def Open_Notes():
    if(File_Exists(open_fld.get()) == True):
        lbl_Header_Notes = Label(MainWindow, text="Error..", font=("Arial", 8, 'bold'), fg='grey15', bg='grey15')
        lbl_Header_Notes.place(x=257, y=310)
        lbl_Header_Notes.after(2500, lambda: lbl_Header_Notes.destroy())
        MainWindow.wm_attributes('-alpha', 0.0)
        def Write_File(File_Path, Text_toFile):
            file_content = open(File_Path, "w")  # Writes text to a given .txt file
            file_content.write(Text_toFile)
            file_content.close()

        def Read_File(File_Path):
            file_content = open(File_Path, "r")
            if (exists(File_Path)):  # opens/reads a file with a given file path....
                return (file_content.read())
            else:
                raise Exception("Error, File not present or empty....")

        def Close_Note_Window():
            open_fld.delete(0, END)
            NoteWindow.destroy()
            MainWindow.wm_attributes('-alpha', .9)
        def Save():
            Write_File("C:\\Notes\\" + open_fld.get(), Note_fld.get(1.0, "end-1c"))
            lbl_top_header = Label(NoteWindow, text="Saved..", bd=1, fg='green2', font=("Arial", 8, 'bold'), bg="grey15", anchor="w")
            lbl_top_header.place(x=300, y=60)
            lbl_top_header.after(2500, lambda: lbl_top_header.destroy())

        def Rename():

            def File_Exists(name):
                exists = os.path.isfile("C:\\Notes\\" + name + ".txt")
                return exists

            def Rename_Official():
                if (File_Exists(rename_fld.get()) == False):
                    Original = "C:\\Notes\\" + open_fld.get()
                    New = "C:\\Notes\\" + rename_fld.get() + ".txt"
                    os.rename(Original, New)
                    Note_fld = scrolledtext.ScrolledText(MainWindow, bd=1, fg='grey90', font=("Arial", 11, 'bold'),
                                                         bg="grey20", width=24,
                                                         height=16)  # bodyfld.get(1.0, "end-1c")   Use this format when grabbing entered text from textbox
                    Note_fld.place(x=35, y=50)
                    Note_fld.insert(1.0, Check_txt_Files())
                    Note_fld.config(state=DISABLED)
                    Note_fld.config(insertbackground="light goldenrod")  # Changes test cursor color
                    NoteWindow.destroy()
                    open_fld.delete(0, END)
                    RenameWindow.destroy()
                    MainWindow.wm_attributes('-alpha', .9)
                    NoteWindow.destroy()

                elif (File_Exists(rename_fld.get()) == True):
                    lbl_Error_Rename = Label(RenameWindow, text="Name already exists",
                                             font=("Calibri", 9, "bold"), bg='grey15', fg="red2")
                    lbl_Error_Rename.place(x=90, y=60)
                    lbl_Error_Rename.after(2500, lambda: lbl_Error_Rename.destroy())

            def Close_Rename_Window():
                RenameWindow.destroy()

            RenameWindow = Tk()

            RenameWindow_app_width = 300
            RenameWindow_app_height = 200

            RenameWindow_screen_width = RenameWindow.winfo_screenwidth()
            RenameWindow_screen_height = RenameWindow.winfo_screenheight()

            RenameWindow_x = int((RenameWindow_screen_width / 2) - (RenameWindow_app_width / 2))
            RenameWindow_y = int((RenameWindow_screen_height / 2) - (RenameWindow_app_height / 2))

            lbl_top_Title = Label(RenameWindow, text="Rename " + open_fld.get(), bd=1, fg='light goldenrod',
                                  font=("Arial", 14, 'bold'), bg="grey20", width=20)  # open_fld.get()
            lbl_top_Title.place(x=30, y=25)

            lbl_Note_Rename = Label(RenameWindow, text="*Note*\nDo not include\nFile extension.\n Name Only",
                                    font=("Calibri", 7, "bold"), bg='grey15', fg="red2")
            lbl_Note_Rename.place(x=220, y=130)

            rename_fld = Entry(RenameWindow, bd=1, fg='grey90', font=("Arial", 11, 'bold'), bg="grey20", width=20)
            rename_fld.config(insertbackground="light goldenrod")
            rename_fld.place(x=65, y=90)

            btn_Rename = Button(RenameWindow, text="Re-Name", font=("Arial", 8, 'bold'), fg='white', bg='blue',
                                height=1, relief="flat", command = Rename_Official)  # Azure3
            btn_Rename.place(x=115, y=135)

            RenameWindow.wm_attributes('-alpha', 1)  # Transparency
            RenameWindow.protocol("WM_DELETE_WINDOW",
                                  Close_Rename_Window)  # controling the function of the close window icon (top right of window)
            RenameWindow.resizable(False, False)  # Cannot change size of the Window(It is locked)
            RenameWindow.title('Confirm')  # Add Username to top of WebPage
            RenameWindow.geometry(f'{RenameWindow_app_width}x{RenameWindow_app_height}+{RenameWindow_x}+{RenameWindow_y}') #300x200
            RenameWindow.configure(bg='grey15')
            RenameWindow.mainloop()


        def Delete():
            def Close_Confirm_Window():
                ConfirmWindow.destroy()

            def Confirm_Delete():
                def Remove_File(File_Name):
                    path = "C:\\Notes\\" + File_Name
                    os.remove(path)
                Remove_File(open_fld.get())
                Note_fld = scrolledtext.ScrolledText(MainWindow, bd=1, fg='grey90', font=("Arial", 11, 'bold'),
                                                     bg="grey20", width=24,
                                                     height=16)  # bodyfld.get(1.0, "end-1c")   Use this format when grabbing entered text from textbox
                Note_fld.place(x=35, y=50)
                Note_fld.insert(1.0, Check_txt_Files())
                Note_fld.config(state=DISABLED)
                Note_fld.config(insertbackground="light goldenrod")  # Changes test cursor color
                ConfirmWindow.destroy()
                NoteWindow.destroy()
                MainWindow.wm_attributes('-alpha', .9)
                open_fld.delete(0, END)


            ConfirmWindow = Tk()

            ConfirmWindow_app_width = 300
            ConfirmWindow_app_height = 200

            ConfirmWindow_screen_width = ConfirmWindow.winfo_screenwidth()
            ConfirmWindow_screen_height = ConfirmWindow.winfo_screenheight()

            ConfirmWindow_x = int((ConfirmWindow_screen_width / 2) - (ConfirmWindow_app_width / 2))
            ConfirmWindow_y = int((ConfirmWindow_screen_height / 2) - (ConfirmWindow_app_height / 2))


            lbl_top_Confirm = Label(ConfirmWindow, text="Are you Sure?", bd=1, fg='light goldenrod',
                                    font=("Arial", 14, 'bold'), bg="grey20", width=20)
            lbl_top_Confirm.place(x=30, y=25)

            btn_No = Button(ConfirmWindow, text="No", font=("Arial", 8, 'bold'), fg='white', bg='red', height=1,
                            width=5, relief="flat", command=Close_Confirm_Window)  # Azure3
            btn_No.place(x=80, y=100)

            btn_Yes = Button(ConfirmWindow, text="Yes", font=("Arial", 8, 'bold'), fg='white', bg='green', height=1,
                             width=5, relief="flat", command=Confirm_Delete)  # Azure3
            btn_Yes.place(x=180, y=100)

            ConfirmWindow.wm_attributes('-alpha', 1)  # Transparency
            ConfirmWindow.protocol("WM_DELETE_WINDOW",
                                   Close_Confirm_Window)  # controling the function of the close window icon (top right of window)
            ConfirmWindow.resizable(False, False)  # Cannot change size of the Window(It is locked)
            ConfirmWindow.title('Confirm')  # Add Username to top of WebPage
            ConfirmWindow.geometry(f'{ConfirmWindow_app_width}x{ConfirmWindow_app_height}+{ConfirmWindow_x}+{ConfirmWindow_y}') #300x200
            ConfirmWindow.configure(bg='grey15')
            ConfirmWindow.mainloop()

        NoteWindow = Toplevel()

        NoteWindow_app_width = 400
        NoteWindow_app_height = 500

        NoteWindow_screen_width = NoteWindow.winfo_screenwidth()
        NoteWindow_screen_height = NoteWindow.winfo_screenheight()

        NoteWindow_x = int((NoteWindow_screen_width / 2) - (NoteWindow_app_width / 2))
        NoteWindow_y = int((NoteWindow_screen_height / 2) - (NoteWindow_app_height / 2))

        Note_fld = scrolledtext.ScrolledText(NoteWindow, bd=1, fg='grey90', font=("Arial", 11, 'bold'), bg="grey20",
                                             width=39,
                                             height=20)  # bodyfld.get(1.0, "end-1c")   Use this format when grabbing entered text from textbox
        Note_fld.place(x=35, y=90)
        Note_fld.insert(1.0, Read_File("C:\\Notes\\" + open_fld.get()))
        Note_fld.config(insertbackground="white")  # Changes test cursor color

        lbl_top_header = Label(NoteWindow, text=open_fld.get(), bd=1, fg='light goldenrod', font=("Arial", 14, 'bold'),
                               bg="grey20", width=27, anchor="w")
        lbl_top_header.place(x=38, y=25)

        btn_Delete = Button(NoteWindow, text="Delete", font=("Arial", 8, 'bold'), fg='white', bg='red', height=1,
                            width=5, relief="flat", command = Delete)  # Azure3
        btn_Delete.place(x=35, y=465)

        btn_Save = Button(NoteWindow, text="Save", font=("Arial", 8, 'bold'), fg='white', bg='green', height=1, width=5,
                          relief="flat", command = Save)  # Azure3
        btn_Save.place(x=324, y=465)

        btn_Rename = Button(NoteWindow, text="Re-Name", font=("Arial", 8, 'bold'), fg='white', bg='blue', height=1,
                            relief="flat", command = Rename)  # Azure3
        btn_Rename.place(x=170, y=465)

        NoteWindow.wm_attributes('-alpha', .9)  # Transparency
        NoteWindow.protocol("WM_DELETE_WINDOW",
                            Close_Note_Window)  # controling the function of the close window icon (top right of window)
        NoteWindow.resizable(False, False)  # Cannot change size of the Window(It is locked)
        NoteWindow.title('Notes')  # Add Username to top of WebPage
        NoteWindow.geometry(f'{NoteWindow_app_width}x{NoteWindow_app_height}+{NoteWindow_x}+{NoteWindow_y}') #400x500
        NoteWindow.configure(bg='grey15')
        NoteWindow.mainloop()


    else:
        lbl_Header_Notes = Label(MainWindow, text="Error..", font=("Arial", 8, 'bold'), fg='red', bg='grey15')
        lbl_Header_Notes.place(x=257, y=310)
        lbl_Header_Notes.after(2500, lambda: lbl_Header_Notes.destroy())

MainWindow = Tk()


MainWindow_app_width = 300
MainWindow_app_height = 400

MainWindow_screen_width = MainWindow.winfo_screenwidth()
MainWindow_screen_height = MainWindow.winfo_screenheight()

MainWindow_x = int((MainWindow_screen_width / 2) - (MainWindow_app_width / 2))
MainWindow_y = int((MainWindow_screen_height / 2) - (MainWindow_app_height / 2))

lbl_Header_Notes = Label(MainWindow, text = "Notes", font = ("Arial" , 14, 'bold'), fg = 'light goldenrod', bg = 'grey15')
lbl_Header_Notes.place(x=120, y=10)

Note_fld = scrolledtext.ScrolledText(MainWindow, bd=1, fg='grey90', font=("Arial", 11, 'bold'), bg="grey20", width=24, height=16)  # bodyfld.get(1.0, "end-1c")   Use this format when grabbing entered text from textbox
Note_fld.place(x=35, y=50)
Note_fld.insert(1.0, Check_txt_Files())
Note_fld.config(state = DISABLED)
Note_fld.config(insertbackground="light goldenrod")  # Changes test cursor color


open_fld = Entry(MainWindow, bd=1, fg = 'grey90', font=("Arial", 11, 'bold'), bg="grey20", width=15)
open_fld.config(insertbackground="white")
open_fld.place(x=35, y = 360)


btn_Notes = Button(MainWindow, text = "open", font = ("Arial" , 8, 'bold'), fg = 'grey15', bg = 'light goldenrod', command = Open_Notes) #Azure3
btn_Notes.place(x=170, y=360)


btn_Notes = Button(MainWindow, text = "+", font = ("Arial" , 11, 'bold'), fg = 'grey15', bg = 'light goldenrod', height = 1, width = 2, command = New_Note) #Azure3
btn_Notes.place(x=255, y=355)

MainWindow.wm_attributes('-alpha', .9)  # Transparency
MainWindow.protocol("WM_DELETE_WINDOW", Close_Main_Window)  # controling the function of the close window icon (top right of window)
MainWindow.resizable(False, False)  # Cannot change size of the Window(It is locked)
MainWindow.title('Main Menu')  # Add Username to top of WebPage
MainWindow.geometry(f'{MainWindow_app_width}x{MainWindow_app_height}+{MainWindow_x}+{MainWindow_y}') #300x400
MainWindow.configure(bg='grey15')
MainWindow.mainloop()



