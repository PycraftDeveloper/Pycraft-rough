if __name__ != "__main__":
    print("Started <Pycraft_TkinterUtils>")
    
    class TkinterInfo:
        def __init__(self):
            pass

        def GetPermissions(self, permission_message):
            try:
                root = self.mod_tkinter__tk.Tk()
                root.withdraw()

                answer = self.mod_tkinter_messagebox_.askquestion(
                    "Check Permission",
                    permission_message)

                if answer == "yes":
                    return True

                else:
                    return False

            except Exception as Message:
                self.error_message = "TkinterUtils > TkinterInfo > GetPermissions: "+str(Message)

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

        def CreateTkinterWindow(self):
            try:
                DataWindow = self.mod_tkinter__tk.Tk()
                DataWindow.title("Player Information")
                DataWindow.configure(width=500, height=300)
                DataWindow.configure(bg="darkgrey")

                text = self.mod_tkinter__tk.Text(
                    DataWindow,
                    wrap=self.mod_tkinter__tk.WORD,
                    relief=self.mod_tkinter__tk.FLAT)

                text.insert(
                    self.mod_tkinter__tk.INSERT,
                    f"Pycraft: v{self.version}\n")

                VariableData = vars(self)

                VariableInformation = []
                for key in VariableData:
                    VariableInformation.append(f"{key} = {str(VariableData[key])}\n")

                VariableInformation = sorted(VariableInformation, key=len)

                for i in range(len(VariableInformation)):
                    text.insert(self.mod_tkinter__tk.INSERT, VariableInformation[i])

                text["state"] = self.mod_tkinter__tk.DISABLED

                text["bg"] = "#%02x%02x%02x" % (self.background_color[0],
                                                    self.background_color[1],
                                                    self.background_color[2])

                text["fg"] = "#%02x%02x%02x" % (self.font_color[0],
                                                    self.font_color[1],
                                                    self.font_color[2])

                text.place(
                    x=0,
                    y=0,
                    relwidth=1,
                    relheight=1)

                DataWindow.mainloop()
                DataWindow.quit()
                
            except Exception as Message:
                self.error_message = "".join(("TkinterUtils > TkinterInfo > ",
                                             f"CreateTkinterWindow: {str(Message)}"))

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

    class TkinterInstaller:
        def __init__():
            pass

        def Createdisplay(InstallerImportData, root):
            try:
                geometry = root.winfo_geometry().split("+")
                Xpos = geometry[1]
                Ypos = geometry[2]
                root.destroy()
                
            except:
                Xpos, Ypos = 0, 0

            root = InstallerImportData.mod_Tkinter_tk_.Tk()

            root.title("Pycraft Setup Wizard")

            root.resizable(
                False,
                False)

            root.configure(bg="white")
            root.geometry(f"850x537+{int(Xpos)}+{int(Ypos)}")

            if InstallerImportData.platform == "Linux":
                ImageFileLocation = InstallerImportData.mod_Os__.path.join(
                    InstallerImportData.base_folder,
                    ("resources//installer resources//Banner.png"))

            else:
                ImageFileLocation = InstallerImportData.mod_Os__.path.join(
                    InstallerImportData.base_folder,
                    ("resources\\installer resources\\Banner.png"))

            InstallerImportData.mod_image_utils__.TkinterInstaller.open_img(
                InstallerImportData,
                root,
                ImageFileLocation)
            return root

else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror(
        "Startup Fail",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
