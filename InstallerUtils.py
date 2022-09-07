if __name__ != "__main__":
    print("Started <Pycraft_InstallerUtil>")

    class GetInstallerData:
        def __init__(self):
            pass

        def GetData(InstallerImportData):
            try:
                if InstallerImportData.platform == "Linux":
                    with open(
                        InstallerImportData.mod_Os__.path.join(
                            InstallerImportData.base_folder,
                            ("data files//installer_config.json")), "r") as openFile:

                        SavedData = InstallerImportData.mod_Json__.load(openFile)
                else:
                    with open(
                         InstallerImportData.mod_Os__.path.join(
                             InstallerImportData.base_folder,
                             ("data files\\installer_config.json")), "r") as openFile:

                        SavedData = InstallerImportData.mod_Json__.load(openFile)

            except:
                PycPath = None
                Repair = {"PATH":None}

                if InstallerImportData.platform == "Linux":
                    with open(
                        InstallerImportData.mod_Os__.path.join(
                            InstallerImportData.base_folder,
                            ("data files//installer_config.json")), "w") as openFile:

                        InstallerImportData.mod_Json__.dump(
                            Repair,
                            openFile)
                else:
                    with open(
                        InstallerImportData.mod_Os__.path.join(
                            InstallerImportData.base_folder,
                            ("data files\\installer_config.json")), "w") as openFile:

                        InstallerImportData.mod_Json__.dump(
                            Repair,
                            openFile)

            else:
                PycPath = SavedData["PATH"]

            return PycPath


    class CoreInstallerFunctionality:
        def __init__(self):
            pass


        def Close(InstallerImportData):
            if InstallerImportData.mod_Tkinter_messagebox_.askokcancel(
                "Pycraft Setup Wizard",
                "Are you sure you want to cancel the install?"):

                InstallerImportData.mod_sys__.exit()


        def Home(InstallerImportData, root, PycPath, ChooseBETA, Choice):
            InstallerImportData.mod_Installer_HomeScreen_.Installer_Home.Start(
                InstallerImportData,
                root,
                PycPath,
                ChooseBETA,
                Choice)


        def outdatedDetector(InstallerImportData):
            try:
                import urllib.request as urlOpener

                urlOpener.urlopen(
                    "https://www.google.com",
                    timeout=1)

                List = InstallerImportData.mod_subprocess__.check_output(
                    [InstallerImportData.mod_sys__.executable,
                     "-m",
                     "pip",
                     "list",
                     "--outdated"],
                    False)

                global outdated

                if b"Python-Pycraft" in List:
                    outdated =  True
                    
            except Exception as Message:
                InstallerImportData.mod_Tkinter_messagebox_.showerror(
                    "An error has occurred",
                    "".join(("We were unable to check for updates to Pycraft, ",
                             "the most likely reason for this is a faulty ",
                             "internet connection.\n\nFull Error ",
                             f"Message:\n{Message}")))

                InstallerImportData.mod_sys__.exit()

    class FileManipulation:
        def __init__(self):
            pass


        def MoveFiles(InstallerImportData, Dir):
            global CurrentLocation
            try:
                temp = str(CurrentLocation.decode("UTF-8"))[:-1]
                
            except:
                temp = InstallerImportData.mod_Site__.getusersitepackages()

            try:
                InstallerImportData.mod_shutil__.copytree(
                    fr"{temp}\\pycraft",
                    fr"{Dir}\\pycraft")

            except Exception as Message:
                InstallerImportData.mod_Tkinter_messagebox_.showerror(
                    "An error has occurred",
                    "".join(("We were unable to move Pycraft to the ",
                             "requested install location.\n\nFull Error ",
                             f"Message:\n{Message}")))

                InstallerImportData.mod_sys__.exit()


        def DownloadandInstall(InstallerImportData, choice):
            try:
                if choice == "Latest":
                    InstallerImportData.mod_subprocess__.check_call(
                        [InstallerImportData.mod_sys__.executable,
                         "-m",
                         "pip",
                         "install",
                         "python-pycraft"],
                        False)

                else:
                    #["none", "Pycraft-v0.9.1", "Pycraft-v0.9.2", "Pycraft-v0.9.3"]
                    if choice == "Pycraft-v0.9.1":
                        InstallerImportData.mod_subprocess__.check_call(
                            [InstallerImportData.mod_sys__.executable,
                             "-m",
                             "pip",
                             "install",
                             "python-pycraft==0.9.1"],
                            False)

                    elif choice == "Pycraft-v0.9.2":
                        InstallerImportData.mod_subprocess__.check_call(
                            [InstallerImportData.mod_sys__.executable,
                             "-m",
                             "pip",
                             "install",
                             "python-pycraft==0.9.2"],
                            False)

                    elif choice == "Pycraft-v0.9.3":
                        InstallerImportData.mod_subprocess__.check_call(
                            [InstallerImportData.mod_sys__.executable,
                             "-m",
                             "pip",
                             "install",
                             "python-pycraft==0.9.3"],
                            False)

                    elif choice == "Pycraft-v0.9.4":
                        InstallerImportData.mod_subprocess__.check_call(
                            [InstallerImportData.mod_sys__.executable,
                             "-m",
                             "pip",
                             "install",
                             "python-pycraft==0.9.4"],
                            False)

                    else:
                        InstallerImportData.mod_subprocess__.check_call(
                            [InstallerImportData.mod_sys__.executable,
                             "-m",
                             "pip",
                             "install",
                             "python-pycraft"],
                            False)
                        
            except Exception as Message:
                InstallerImportData.mod_Tkinter_messagebox_.showerror(
                    "An error ocurred",
                    "".join(("We were unable to install the additional ",
                             "files Pycraft needs in-order to install.\n\n",
                             f"Full Error Message: {Message}")))

                InstallerImportData.mod_sys__.exit()


        def search_files(InstallerImportData, directory):
            arr = []
            print(f"Scanning {directory}")
            for dirpath, dirnames, files in InstallerImportData.mod_Os__.walk(directory):
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

                                InstallerImportData.mod_Os__.remove(FileArray[i])

                        else:
                            if not ("distutils" in FileArray[i] or
                                    "pip" in FileArray[i] or
                                    "setuptools" in FileArray[i] or
                                    "pkg_resources" in FileArray[i] or
                                    "README" in FileArray[i] or
                                    "win32" in FileArray[i] or
                                    "wheel" in FileArray[i]):

                                InstallerImportData.mod_Os__.remove(FileArray[i])

                    except Exception as Message:
                        print(Message)
                        
            except Exception as Message:
                InstallerImportData.mod_Tkinter_messagebox_.showerror(
                    "An error ocurred",
                    "".join(("We were unable to remove some files for ",
                             f"Pycraft from your PC.\n\nFull Error Message: {Message}")))

                InstallerImportData.mod_sys__.exit()

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
