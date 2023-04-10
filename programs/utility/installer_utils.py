if __name__ != "__main__":
    try:
        import os
        import json
        import sys
        import subprocess
        from zipfile import ZipFile
        import pathlib
        import requests
        from requests.adapters import TimeoutSauce
        import re
        from tkinter import messagebox
        
        from registry_utils import Registry

        import installer_home
        
        import file_utils
    except ModuleNotFoundError as Message:
        from tkinter import messagebox
        error_message = f"{Message} in installer_utils"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()
    
    class MyTimeout(TimeoutSauce):
        def __init__(self, *args, **kwargs):
            if kwargs['connect'] is None:
                kwargs['connect'] = 5
            if kwargs['read'] is None:
                kwargs['read'] = 5
            super(MyTimeout, self).__init__(*args, **kwargs)

    requests.adapters.TimeoutSauce = MyTimeout

    class core_installer_functionality(Registry):
        def close():
            if messagebox.askokcancel(
                "Pycraft Setup Wizard",
                "Are you sure you want to quit?"):

                Registry.root.destroy()
                sys.exit()


        def home():
            installer_home.installer_home.start()

        def outdated_detector(InstallerImportData):
            try:
                import urllib.request as urlOpener

                urlOpener.urlopen(
                    "https://www.google.com",
                    timeout=1)

                List = subprocess.check_output(
                        [sys.executable, "-m", "pip", "list", "--outdated"],
                        False)

                global outdated

                if b"Python-Pycraft" in List:
                    outdated =  True
                    
            except Exception as Message:
                messagebox.showerror(
                    "An error has occurred",
                    "".join(("We were unable to check for updates to Pycraft, ",
                             "the most likely reason for this is a faulty ",
                             "internet connection.\n\nFull Error ",
                             f"Message:\n{Message}")))

                sys.exit()

    class file_manipulation(Registry):
        def get_versions():
            version_IDs = {}
            r = requests.get(
                'https://api.github.com/repos/PycraftDeveloper/Pycraft/tags',
                timeout=30)
            raw = r.text
            array = raw.split("},{")
            for element in array:
                name = re.sub('["\[\]{}]', "", element[1:-1]).split(",")
                name = name[0].split(":")
                version_code = ""
                broken_down = re.split("[.dev]", name[1])
                if broken_down[1] != "0":
                    for element in broken_down:
                        if len(element) > 0:
                            version_code += ("0"*(3-len(element))+element)

                    version_IDs[name[1]] = version_code

            Registry.pycraft_versions = version_IDs
            
        def install_dependencies(pycraft_install_path):
            requirements_file_path = pathlib.Path(pycraft_install_path) / "requirements.txt"
            quit() # Remove this
            subprocess.check_output(
                f"{sys.executable} -m pip install -r {str(requirements_file_path)}")

        def download(base_folder, install_path, choice):
            try:
                if " (latest)" in choice or choice == "Latest":
                    version = list(Registry.pycraft_versions.keys())[0]
                    url = f"https://github.com/PycraftDeveloper/Pycraft/archive/refs/tags/{version}.zip"
                else:
                    url = f"https://github.com/PycraftDeveloper/Pycraft/archive/refs/tags/{choice.split(' ')[1]}.zip"
                
                path = install_path / "TEMP.zip"

                session = requests.Session()
                online_download = session.get(url)

                online_download.raise_for_status()
                
                with open(path, "wb") as file:
                    file.write(online_download.content)
                
                with ZipFile(path, "r") as zip_file:
                    file_names = zip_file.namelist()
                    zip_file.extractall(path=path.parent)
                    
                extracted_file_path = path.parent / file_names[0]
                
                new_data = {"pycraft_install_path": str(extracted_file_path)}
                file_utils.fix_installer.update_install_config(new_data)
                
                os.remove(str(path))
            except Exception as message:
                print(message)
                messagebox.showerror(
                    "An error ocurred",
                    "".join(("We were unable to install the additional ",
                             "files Pycraft needs in-order to install.\n\n",
                             f"Full Error Message: {message}")))

                quit()


        def search_files(InstallerImportData, directory):
            arr = []
            print(f"Scanning {directory}")
            for dirpath, dirnames, files in os.walk(directory):
                for name in files:
                    arr.append(f"{dirpath}\{name}")
                    
            return arr


        def remove_files(InstallerImportData, FileArray, keep_save=False):
            try:
                for i in range(len(FileArray)):
                    try:
                        if keep_save:
                            if not ("Data Files" in FileArray[i] or
                                    "distutils" in FileArray[i] or
                                    "pip" in FileArray[i] or
                                    "setuptools" in FileArray[i] or
                                    "pkg_resources" in FileArray[i] or
                                    "README" in FileArray[i] or
                                    "win32" in FileArray[i] or
                                    "wheel" in FileArray[i]):

                                os.remove(FileArray[i])

                        else:
                            if not ("distutils" in FileArray[i] or
                                    "pip" in FileArray[i] or
                                    "setuptools" in FileArray[i] or
                                    "pkg_resources" in FileArray[i] or
                                    "README" in FileArray[i] or
                                    "win32" in FileArray[i] or
                                    "wheel" in FileArray[i]):

                                os.remove(FileArray[i])

                    except Exception as Message:
                        print(Message)
                        
            except Exception as Message:
                messagebox.showerror(
                    "An error ocurred",
                    "".join(("We were unable to remove some files for ",
                             f"Pycraft from your PC.\n\nFull Error Message: {Message}")))

                quit()

else:
    print("You need to run this as part of Pycraft's Installer")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft's Installer, please run the 'main.py' file")

    quit()
