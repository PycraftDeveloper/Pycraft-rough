if __name__ != "__main__":
    print("Started <Pycraft_Uninstall>")

    class BeginUninstall:
        def __init__(self):
            pass

        def UninstallScreen_0(InstallerImportData, root, PycPath, ChooseBETA, Choice):
            root = InstallerImportData.mod_tkinter_utils__.TkinterInstaller.Createdisplay(
                InstallerImportData,
                root)

            InstallerImportData.mod_Tkinter_tk_.Label(
                root,
                text="Pycraft's Installation Assistant",
                background='white',
                font=(None, 20)).place(x=200, y=0)

            InstallerImportData.mod_Tkinter_tk_.Label(
                root,
                text="Modify Your Install - Uninstall",
                background='white',
                font=(None, 20)).place(x=200, y=35)

            text = InstallerImportData.mod_Tkinter_tk_.Text(
                root,
                wrap=InstallerImportData.mod_Tkinter_tk_.WORD,
                relief=InstallerImportData.mod_Tkinter_tk_.FLAT,
                font=(None, 10))

            UninstallerInstructions = "".join(("You have arrived at Pycraft's uninstall ",
                                               "utility, here you can remove Pycraft from ",
                                               "your system and/or remove the project's ",
                                               "additional files, these will be sent to ",
                                               "your recycle bin so you have the option to ",
                                               "change your mind.\n\nIf you want to feel ",
                                               "free to feedback any bugs, ideas or ",
                                               "suggestions to the developers who's contact ",
                                               "you can find here: ",
                                               "https://github.com/PycraftDeveloper/Pycraft"))

            text.insert(InstallerImportData.mod_Tkinter_tk_.INSERT, UninstallerInstructions)
            text["state"] = InstallerImportData.mod_Tkinter_tk_.DISABLED
            text.place(x=200, y=80)

            def GetConformation():
                global UpdateUtility
                UpdateUtility = False
                if InstallerImportData.mod_Tkinter_messagebox_.askokcancel(
                    "Are you sure with your decision",
                    "".join(("Please now take the time to make sure you have ",
                             "chosen correctly as some options will clear all ",
                             "settings and progress made! \n\nPress OK to ",
                             "continue the uninstall process"))):

                    ans = InstallerImportData.mod_Tkinter_messagebox_.askquestion(
                        "Permissions manager",
                        "Can we have permission to remove and change some files on your PC?")

                    while ans == "no":
                        ans2 = InstallerImportData.mod_Tkinter_messagebox_.askquestion(
                            "Caution",
                            "".join(("We did not receive permission to remove and modify ",
                                     "files on this PC, as a result we cannot uninstall ",
                                     "Pycraft, would you like to amend this decision (yes) ",
                                     "or close the installer (no)?")))

                        if ans2 == "no":
                            quit()
                        else:
                            ans = InstallerImportData.mod_Tkinter_messagebox_.askquestion(
                                "Permissions manager",
                                "Can we have permission to remove and change files on your PC?")

                    if Uninstall_Option.get() == 1:
                        BeginUninstall.Remove_But_Keep_Save(
                            InstallerImportData,
                            root,
                            PycPath,
                            ChooseBETA,
                            Choice)

                    elif Uninstall_Option.get() == 2:
                        BeginUninstall.Remove_But_Leave(
                            InstallerImportData,
                            root,
                            PycPath,
                            ChooseBETA,
                            Choice)

                    else:
                        BeginUninstall.Remove_All(
                            InstallerImportData,
                            root,
                            PycPath,
                            ChooseBETA,
                            Choice)

            InstallerImportData.mod_Tkinter_ttk_.Button(
                root,
                text='Home',
                command=lambda: InstallerImportData.mod_InstallerUtil__.CoreInstallerFunctionality.Home(
                    InstallerImportData,
                    root,
                    PycPath,
                    ChooseBETA, Choice)).place(x=680, y=500)

            InstallerImportData.mod_Tkinter_ttk_.Button(
                root,
                text='Continue',
                command=GetConformation).place(x=760, y=500)

            Uninstall_Option = InstallerImportData.mod_Tkinter_tk_.IntVar()

            InstallerImportData.mod_Tkinter_ttk_.Radiobutton(
                root,
                text="Remove Pycraft and additional files but keep save data",
                variable=Uninstall_Option,
                value=1).place(x=200, y=200)

            InstallerImportData.mod_Tkinter_ttk_.Radiobutton(
                root,
                text="Remove Pycraft but leave additional files",
                variable=Uninstall_Option,
                value=2).place(x=200, y=225)

            InstallerImportData.mod_Tkinter_ttk_.Radiobutton(
                root,
                text="Remove everything",
                variable=Uninstall_Option,
                value=3).place(x=200, y=250)

            Uninstall_Option.set(1)

            root.mainloop()


        def Remove_All(InstallerImportData, root, PycPath, ChooseBETA, Choice):
            root = InstallerImportData.mod_tkinter_utils__.TkinterInstaller.Createdisplay(
                InstallerImportData,
                root)

            InstallerImportData.mod_Tkinter_tk_.Label(
                root,
                text="Pycraft's Installation Assistant",
                background='white',
                font=(None, 20)).place(x=200, y=0)

            InstallerImportData.mod_Tkinter_tk_.Label(
                root,
                text="Uninstalling Pycraft and all additional files",
                background='white',
                font=(None, 15)).place(x=200, y=35)

            OUTPUTtext = "Querying versions"

            InstallerImportData.mod_Installer_TextUtils_.InstallerText.CreateText(
                InstallerImportData,
                root,
                OUTPUTtext)

            import main
            version = main.QueryVersion()
            OUTPUTtext += f"\nPreparing to remove {version} and additional files"

            InstallerImportData.mod_Installer_TextUtils_.InstallerText.CreateText(
                InstallerImportData,
                root,
                OUTPUTtext)

            FileArray = InstallerImportData.mod_InstallerUtil__.FileManipulation.search_files(
                InstallerImportData,
                PycPath)

            import site
            AdditionalFileArray = InstallerImportData.mod_InstallerUtil__.FileManipulation.search_files(
                InstallerImportData,
                (site.getuserbase()+"\\Python310\\site-packages"))

            FileArray = FileArray+AdditionalFileArray
            OUTPUTtext += f"\nIdentified {len(FileArray)} files to remove"

            InstallerImportData.mod_Installer_TextUtils_.InstallerText.CreateText(
                InstallerImportData,
                root,
                OUTPUTtext)

            InstallerImportData.mod_threading__.Thread(
                target=InstallerImportData.mod_InstallerUtil__.FileManipulation.remove_files,
                args=(InstallerImportData,
                        FileArray,)).start()

            OUTPUTtext += f"\nRemoving {version}"

            InstallerImportData.mod_Installer_TextUtils_.InstallerText.CreateText(
                InstallerImportData,
                root,
                OUTPUTtext)

            i = 0
            def Render_Progressbar(i):
                CompletionProgressbar = InstallerImportData.mod_Tkinter_ttk_.Progressbar(
                    root,
                    orient=InstallerImportData.mod_Tkinter_tk_.HORIZONTAL,
                    length=100,
                    mode='indeterminate')

                CompletionProgressbar.place(x=200, y=500)
                CompletionProgressbar['value'] += i
                root.update()

            while "remove_files" in InstallerImportData.mod_threading__.enumerate():
                i += 1
                root.after(
                    50,
                    Render_Progressbar(i))

            OUTPUTtext += f"\nSuccessfully removed {version} and additional files"

            InstallerImportData.mod_Installer_TextUtils_.InstallerText.CreateText(
                InstallerImportData,
                root,
                OUTPUTtext)

            OUTPUTtext += "\nCleaning Up"

            InstallerImportData.mod_Installer_TextUtils_.InstallerText.CreateText(
                InstallerImportData,
                root,
                OUTPUTtext)

            try:
                InstallerImportData.mod_Os__.rmdir(PycPath)
                
            except:
                pass

            OUTPUTtext += "\nDone"
            InstallerImportData.mod_Installer_TextUtils_.InstallerText.CreateText(
                InstallerImportData,
                root,
                OUTPUTtext)

            BeginUninstall.Finish_Uninstall(
                InstallerImportData,
                root)


        def Remove_But_Keep_Save(InstallerImportData, root, PycPath, ChooseBETA, Choice):
            root = InstallerImportData.mod_tkinter_utils__.TkinterInstaller.Createdisplay(
                InstallerImportData,
                root)

            InstallerImportData.mod_Tkinter_tk_.Label(
                root,
                text="Pycraft's Installation Assistant",
                background='white',
                font=(None, 20)).place(x=200, y=0)

            InstallerImportData.mod_Tkinter_tk_.Label(
                root,
                text="Uninstalling Pycraft and all additional files but keeping save data",
                background='white',
                font=(None, 15)).place(x=200, y=35)

            OUTPUTtext = "Querying versions"
            InstallerImportData.mod_Installer_TextUtils_.InstallerText.CreateText(
                InstallerImportData,
                root,
                OUTPUTtext)

            import main
            version = main.QueryVersion()
            OUTPUTtext += f"\nPreparing to remove {version} and additional files"

            InstallerImportData.mod_Installer_TextUtils_.InstallerText.CreateText(
                InstallerImportData,
                root,
                OUTPUTtext)

            FileArray = InstallerImportData.mod_InstallerUtil__.FileManipulation.search_files(
                InstallerImportData,
                PycPath)

            import site
            AdditionalFileArray = InstallerImportData.mod_InstallerUtil__.FileManipulation.search_files(
                InstallerImportData,
                (site.getuserbase()+"\\Python310\\site-packages"))

            FileArray = FileArray+AdditionalFileArray
            OUTPUTtext += f"\nIdentified {len(FileArray)} files to remove"

            InstallerImportData.mod_Installer_TextUtils_.InstallerText.CreateText(
                InstallerImportData,
                root,
                OUTPUTtext)

            InstallerImportData.mod_threading__.Thread(
                target=InstallerImportData.mod_InstallerUtil__.FileManipulation.remove_files,
                args=(InstallerImportData,
                        FileArray,)).start()

            OUTPUTtext += f"\nRemoving {version}"

            InstallerImportData.mod_Installer_TextUtils_.InstallerText.CreateText(
                InstallerImportData,
                root,
                OUTPUTtext)

            i = 0
            def Render_Progressbar(i):
                CompletionProgressbar = InstallerImportData.mod_Tkinter_ttk_.Progressbar(
                    root,
                    orient=InstallerImportData.mod_Tkinter_tk_.HORIZONTAL,
                    length=100,
                    mode='indeterminate')

                CompletionProgressbar.place(x=200, y=500)
                CompletionProgressbar['value'] += i
                root.update()

            while "remove_files" in InstallerImportData.mod_threading__.enumerate():
                i += 1
                root.after(
                    50,
                    Render_Progressbar(i))

            OUTPUTtext += f"\nSuccessfully removed {version} and additional files"

            InstallerImportData.mod_Installer_TextUtils_.InstallerText.CreateText(
                InstallerImportData,
                root,
                OUTPUTtext)

            OUTPUTtext += "\nCleaning Up"

            InstallerImportData.mod_Installer_TextUtils_.InstallerText.CreateText(
                InstallerImportData,
                root,
                OUTPUTtext)

            OUTPUTtext += "\nDone"

            InstallerImportData.mod_Installer_TextUtils_.InstallerText.CreateText(
                InstallerImportData,
                root,
                OUTPUTtext)

            try:
                global UpdateUtility
                if not UpdateUtility:
                    BeginUninstall.Finish_Uninstall(
                        InstallerImportData,
                        root)

            except:
                with open(
                    InstallerImportData.mod_Os__.path.join(
                        InstallerImportData.base_folder,
                        ("data files\\installer_config.json")), 'r') as openFile:

                    SavedData = InstallerImportData.mod_Json__.load(openFile)

                Dir = SavedData["PATH"]

                InstallerImportData.mod_Installer_Install_.BeginInstall.InstallScreen_2(
                    InstallerImportData,
                    root,
                    Choice,
                    Dir)


        def Remove_But_Leave(InstallerImportData, root, PycPath, ChooseBETA, Choice):
            root = InstallerImportData.mod_tkinter_utils__.TkinterInstaller.Createdisplay(
                InstallerImportData,
                root)

            InstallerImportData.mod_Tkinter_tk_.Label(
                root,
                text="Pycraft's Installation Assistant",
                background='white',
                font=(None, 20)).place(x=200, y=0)

            InstallerImportData.mod_Tkinter_tk_.Label(
                root,
                text="Uninstalling Pycraft but keeping additional files",
                background='white',
                font=(None, 15)).place(x=200, y=35)

            OUTPUTtext = "Querying versions"

            InstallerImportData.mod_Installer_TextUtils_.InstallerText.CreateText(
                InstallerImportData,
                root,
                OUTPUTtext)

            import main
            version = main.QueryVersion()
            OUTPUTtext += f"\nPreparing to remove {version}"

            InstallerImportData.mod_Installer_TextUtils_.InstallerText.CreateText(
                InstallerImportData,
                root,
                OUTPUTtext)

            FileArray = InstallerImportData.mod_InstallerUtil__.FileManipulation.search_files(
                InstallerImportData,
                PycPath)

            OUTPUTtext += f"\nIdentified {len(FileArray)} files to remove"

            InstallerImportData.mod_Installer_TextUtils_.InstallerText.CreateText(
                InstallerImportData,
                root,
                OUTPUTtext)

            InstallerImportData.mod_threading__.Thread(
                target=InstallerImportData.mod_InstallerUtil__.FileManipulation.remove_files,
                args=(InstallerImportData,
                        FileArray,)).start()

            OUTPUTtext += f"\nRemoving {version}"

            InstallerImportData.mod_Installer_TextUtils_.InstallerText.CreateText(
                InstallerImportData,
                root,
                OUTPUTtext)

            i = 0
            def Render_Progressbar(i):
                CompletionProgressbar = InstallerImportData.mod_Tkinter_ttk_.Progressbar(
                    root,
                    orient=InstallerImportData.mod_Tkinter_tk_.HORIZONTAL,
                    length=100,
                    mode='indeterminate')

                CompletionProgressbar.place(x=200, y=500)
                CompletionProgressbar['value'] += i
                root.update()

            while "remove_files" in InstallerImportData.mod_threading__.enumerate():
                i += 1
                root.after(
                    50,
                    Render_Progressbar(i))

            OUTPUTtext += f"\nSuccessfully removed {version}"

            InstallerImportData.mod_Installer_TextUtils_.InstallerText.CreateText(
                InstallerImportData,
                root,
                OUTPUTtext)

            OUTPUTtext += "\nCleaning Up"

            InstallerImportData.mod_Installer_TextUtils_.InstallerText.CreateText(
                InstallerImportData,
                root,
                OUTPUTtext)

            try:
                InstallerImportData.mod_Os__.rmdir(PycPath)
                
            except:
                pass

            OUTPUTtext += "\nDone"

            InstallerImportData.mod_Installer_TextUtils_.InstallerText.CreateText(
                InstallerImportData,
                root,
                OUTPUTtext)

            BeginUninstall.Finish_Uninstall(
                InstallerImportData,
                root)


        def Finish_Uninstall(InstallerImportData, root):
            root = InstallerImportData.mod_tkinter_utils__.TkinterInstaller.Createdisplay(
                InstallerImportData,
                root)

            InstallerImportData.mod_Tkinter_tk_.Label(
                root,
                text="Pycraft's Installation Assistant",
                background='white',
                font=(None, 20)).place(x=200, y=0)

            InstallerImportData.mod_Tkinter_tk_.Label(
                root,
                text="Successfully uninstalled Pycraft",
                background='white',
                font=(None, 15)).place(x=200, y=35)

            EnterText = "".join(("Pycraft has been removed from your computer, ",
                                 "you can re-install the project at any time ",
                                 "from GitHub, SourceForge or PyPi. If you ",
                                 "have experienced any bugs or have any ",
                                 "suggestions then feel free to share them ",
                                 "on the project page!"))

            text = InstallerImportData.mod_Tkinter_tk_.Text(
                root,
                wrap=InstallerImportData.mod_Tkinter_tk_.WORD,
                relief=InstallerImportData.mod_Tkinter_tk_.FLAT,
                font=(None, 10))

            text.insert(
                InstallerImportData.mod_Tkinter_tk_.INSERT,
                EnterText)

            text["state"] = InstallerImportData.mod_Tkinter_tk_.DISABLED
            text.place(x=200, y=40)

            InstallerImportData.mod_Tkinter_ttk_.Button(
                root,
                text='Quit',
                command=InstallerImportData.mod_sys__.exit).place(x=760, y=500)

            root.mainloop()

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
