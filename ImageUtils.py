if __name__ != "__main__":
    print("Started <Pycraft_ImageUtils>")
    
    class ConvertImage:
        def __init__(self):
            pass

        def pilImageToSurface(self, pilImage):
            try:
                return self.mod_pygame__.image.fromstring(
                    pilImage.tobytes(),
                    pilImage.size,
                    pilImage.mode).convert()

            except Exception as Message:
                self.error_message = "ImageUtils > ConvertImage > pilImageToSurface: "+str(Message)
                
                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

    class TkinterInstaller:
        def __init__(self):
            pass

        def open_img(InstallerImportData, root, file):
            try:
                global render, load
                try:
                    load = InstallerImportData.mod_PIL_Image_.open(file)
                    
                except Exception as Message:
                    print(Message)

                render = InstallerImportData.mod_PIL_ImageTk_.PhotoImage(load)

                img = InstallerImportData.mod_Tkinter_tk_.Label(
                    root,
                    image=render)

                img.image = render
                img.place(
                    x=-3,
                    y=-5)

            except Exception as Message:
                InstallerImportData.mod_Tkinter_messagebox_.showerror(
                    "Module Not Found",
                    "".join(("This installer requires the module Pillow, ",
                             "this should have been installed automatically ",
                             "if you got this installer from PyPi, or are ",
                             "running this as a (.exe) file.\nIf you have ",
                             "grabbed this installer from GitHub then I ",
                             "advice you to install PIL with the command:",
                             "\n\npip install pillow\n\nShould any further ",
                             "problems occur then feel free to contact the ",
                             "developer with the links available at: ",
                             "https://github.com/PycraftDeveloper/Pycraft",
                             f"\n\nFull Error Message:\n{Message}")))
                quit()

else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Startup Fail",
                         "You need to run this as part of Pycraft, please run the 'main.py' file")
    quit()
