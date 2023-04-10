if __name__ != "__main__":
    try:
        from tkinter import messagebox
        import tkinter
        
        from PIL import Image
        from PIL import ImageTk
        
        from registry_utils import Registry
    except ModuleNotFoundError as Message:
        from tkinter import messagebox
        error_message = f"{Message} in image_utils"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()

    class tkinter_installer(Registry):
        def open_img(offset_x=-3, offset_y=-5):
            try:
                load = Image.open(Registry.banner_path)

                render = ImageTk.PhotoImage(
                    load,
                    master=Registry.root)

                img = tkinter.Label(
                    Registry.root,
                    image=render)

                img.image = render
                img.place(
                    x=offset_x,
                    y=offset_y)

            except Exception as Message:
                messagebox.showerror(
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
    print("You need to run this as part of Pycraft's Installer")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft's Installer, please run the 'main.py' file")
    quit()
