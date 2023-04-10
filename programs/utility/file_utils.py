if __name__ != "__main__":
    try:
        import json
        from tkinter import messagebox
        import pathlib

        from registry_utils import Registry
    except ModuleNotFoundError as Message:
        from tkinter import messagebox
        error_message = f"{Message} in file_utils"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()
            
    class InstallerText(Registry):
        def get_installer_text():
            with open(
                    Registry.installer_text_path,
                    "r") as file:
                
                Registry.installer_text = json.load(file)
            
    class fix_installer(Registry):
        def get_installer_config():
            try:
                with open(
                        Registry.installer_config_path,
                        "r") as file:

                    data = json.load(file)
            except json.JSONDecodeError:
                with open(
                        Registry.installer_config_path,
                        "w") as file:
                    
                    file.truncate()
                    
                for key in Registry.save_keys:
                    setattr(Registry, key, Registry.save_keys[key])
                    
                
                fix_installer.set_installer_config()
                        
                data = Registry.save_keys
                
            for key in Registry.save_keys:
                try:
                    setattr(Registry, key, data[key])
                except KeyError:
                    setattr(Registry, key, Registry.save_keys[key])
                    
        def set_installer_config():
            save_data = {}
            
            for key in Registry.save_keys:
                save_data[key] = Registry.__dict__[key]
                
            with open(Registry.installer_config_path, "w") as file:
                json.dump(save_data, file)
        
        def update_install_config(new_data):
            with open(Registry.installer_config_path, "r") as file:
                data = json.load(file)
            
            for key in new_data:
                data[key] = new_data[key]
                
            with open(Registry.installer_config_path, "w") as file:
                json.dump(data, file)
        
        def link_pycraft_to_installer():
            link_path = pathlib.Path(Registry.pycraft_install_path) / "pycraft" / 
            with open()
                
else:
    print("You need to run this as part of Pycraft's Installer")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft's Installer, please run the 'main.py' file")

    quit()
