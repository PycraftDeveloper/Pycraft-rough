if __name__ != "__main__":
    try:
        import tkinter

        from registry_utils import Registry
    except ModuleNotFoundError as Message:
        from tkinter import messagebox
        error_message = f"{Message} in text_utils"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()
            
    class installer_text(Registry):
        def create_text(OUTPUTtext):
            text = tkinter.Text(
                Registry.root,
                wrap=tkinter.WORD,
                relief=tkinter.FLAT,
                font=(None, 10))

            text.insert(
                tkinter.INSERT,
                OUTPUTtext)

            text["state"] = tkinter.DISABLED
            text.place(x=200, y=80)
            Registry.root.update_idletasks()
            
else:
    print("You need to run this as part of Pycraft's Installer")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft's Installer, please run the 'main.py' file")

    quit()
