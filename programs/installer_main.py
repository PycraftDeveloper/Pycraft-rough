try:
    from registry_utils import Registry

    import tkinter_utils
    import installer_utils
    import installer_home
    import file_utils
except ModuleNotFoundError as Message:
    from tkinter import messagebox
    error_message = f"{Message} in installer_main"
    messagebox.showerror(
        "Startup Error",
        error_message)
    quit()

class Run(Registry):
    def init():
        tkinter_utils.tkinter_installer.create_display()

        file_utils.fix_installer.get_installer_config()

        file_utils.InstallerText.get_installer_text()
        
        installer_utils.file_manipulation.get_versions()
        
        Registry.initialized = True
        
    def start():
        if not Registry.initialized:
            Run.init()
            
        installer_home.installer_home.start()

        Registry.root.mainloop()

def get_installer_version():
    return "3.2.0"
