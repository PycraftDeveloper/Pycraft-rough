if __name__ != "__main__":
    print("Started <Pycraft_Install>")
    
    class BeginInstall:
        def __init__(self):
            pass


        def InstallScreen_0(InstallerImportData, root, PycPath, ChooseBETA, choice):
            root = InstallerImportData.mod_tkinter_utils__.TkinterInstaller.Createdisplay(
                InstallerImportData,
                root)

            InstallerImportData.mod_Tkinter_tk_.Label(
                root,
                text="Pycraft's Installation Assistant",
                background="white",
                font=(None, 20)).place(x=200,y=0)

            InstallerImportData.mod_Tkinter_tk_.Label(
                root,
                text="Important Information",
                background="white",
                font=(None, 20)).place(x=200, y=35)

            text = InstallerImportData.mod_Tkinter_tk_.Text(
                root,
                wrap=InstallerImportData.mod_Tkinter_tk_.WORD,
                relief=InstallerImportData.mod_Tkinter_tk_.FLAT,
                font=(None, 10))

            text.insert(
                InstallerImportData.mod_Tkinter_tk_.INSERT,
                "".join(("Please read the below information, once you have ",
                         "familiarised yourself with the information, please ",
                         "tick the box to say that you have and then press ",
                         "continue to start the installation. Use the scroll ",
                         "wheel to scroll the text.\n\nYou can find Pycraft's ",
                         "GitHub repository here for more information: ",
                         "https://github.com/PycraftDeveloper/Pycraft\n\n",
                         "The program will be updated frequently and I shall ",
                         "do my best to keep this up to date too. I also want ",
                         "to add that you are welcome to view and change the ",
                         "program and share it with your friends. If you find ",
                         "any bugs or errors, please feel free to comment in ",
                         "the comments section any feedback so we can improve ",
                         "our program, it will all be much appreciated and give ",
                         "as much detail as you wish to give out. \n\n\nLicence\nMIT ",
                         "License\n\nCopyright (c) 2021 Thomas Jebbo\n\nPermission ",
                         "is hereby granted, free of charge, to any person obtaining ",
                         "a copy of this software and associated documentation files ",
                         "(the \"Software\"), to deal in the Software without ",
                         "restriction, including without limitation the rights to ",
                         "use, copy, modify, merge, publish, distribute, sublicense, ",
                         "and/or sell copies of the Software, and to permit persons to ",
                         "whom the Software is furnished to do so, subject to the ",
                         "following conditions:\n\nThe above copyright notice and ",
                         "this permission notice shall be included in all copies or ",
                         "substantial portions of the Software.\n\nTHE SOFTWARE IS ",
                         "PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS ",
                         "OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF ",
                         "MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND ",
                         "NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR ",
                         "COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR ",
                         "OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR ",
                         "OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE ",
                         "SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.")))

            text["state"] = InstallerImportData.mod_Tkinter_tk_.DISABLED
            text.place(x=200, y=80)

            var1 = InstallerImportData.mod_Tkinter_tk_.IntVar()

            def ButtonCheck(InstallerImportData, root, PycPath, ChooseBETA, choice, var1):
                data = var1.get()
                if data is None or data == 0:
                    continueButton = InstallerImportData.mod_Tkinter_ttk_.Button(
                        root,
                        text="Continue")

                    continueButton.place(x=760, y=500)
                    continueButton["state"] = InstallerImportData.mod_Tkinter_tk_.DISABLED

                else:
                    continueButton = InstallerImportData.mod_Tkinter_ttk_.Button(
                        root,
                        text="Continue",
                        command=lambda: BeginInstall.InstallScreen_1(
                            InstallerImportData,
                            root,
                            PycPath,
                            ChooseBETA,
                            choice))

                    continueButton.place(x=760, y=500)
                    continueButton["state"] = InstallerImportData.mod_Tkinter_tk_.NORMAL
                    root.update_idletasks()


            ButtonCheck(InstallerImportData, root, PycPath, ChooseBETA, choice, var1)

            InstallerImportData.mod_Tkinter_ttk_.Radiobutton(
                root, text="I have not read the above text",
                variable=var1,
                value=0,
                command=lambda: ButtonCheck(
                    InstallerImportData,
                    root,
                    PycPath,
                    ChooseBETA,
                    choice,
                    var1)).place(x=200, y=475)

            InstallerImportData.mod_Tkinter_ttk_.Radiobutton(
                root,
                text="I have read the above text",
                variable=var1,
                value=1,
                command=lambda: ButtonCheck(
                    InstallerImportData,
                    root,
                    PycPath,
                    ChooseBETA,
                    choice,
                    var1)).place(x=200, y=500)

            InstallerImportData.mod_Tkinter_ttk_.Button(
                root,
                text="Home",
                command=lambda: InstallerImportData.mod_InstallerUtil__.CoreInstallerFunctionality.Home(
                    InstallerImportData,
                    root,
                    PycPath,
                    ChooseBETA,
                    choice)).place(x=680, y=500)


        def InstallScreen_1(InstallerImportData, root, PycPath, ChooseBETA, choice):
            root = InstallerImportData.mod_tkinter_utils__.TkinterInstaller.Createdisplay(
                InstallerImportData,
                root)

            InstallerImportData.mod_Tkinter_tk_.Label(
                root,
                text="Pycraft's Installation Assistant",
                background="white",
                font=(None, 20)).place(x=200, y=0)

            InstallerImportData.mod_Tkinter_tk_.Label(
                root,
                text="Set Install Location",
                background="white",
                font=(None, 20)).place(x=200, y=40)

            OUTPUTtext = "".join(("Now we need to ask one final thing before ",
                                  "we start the install, where would you like ",
                                  "to store Pycraft?"))

            text = InstallerImportData.mod_Tkinter_tk_.Text(
                root,
                wrap=InstallerImportData.mod_Tkinter_tk_.WORD,
                relief=InstallerImportData.mod_Tkinter_tk_.FLAT,
                font=(None, 10))

            text.insert(
                InstallerImportData.mod_Tkinter_tk_.INSERT,
                OUTPUTtext)

            text["state"] = InstallerImportData.mod_Tkinter_tk_.DISABLED
            text.place(x=200, y=80)

            global Dir
            Dir = InstallerImportData.base_folder

            def GetDir():
                global Dir
                Dir = InstallerImportData.mod_Tkinter_filedialog_.askdirectory()
                if len(Dir) >= 80:
                    Dir2 = Dir[:80]+"..."
                else:
                    Dir2 = Dir

                global CurrentLocat

                CurrentLocat.destroy()
                CurrentLocat = InstallerImportData.mod_Tkinter_tk_.Label(
                    root,
                    text=("  "+Dir2+"  "),
                    background="white",
                    relief=InstallerImportData.mod_Tkinter_tk_.RIDGE)

                CurrentLocat.place(x=313, y=152.5)

                root.update_idletasks()

            InstallerImportData.mod_Tkinter_ttk_.Button(
                root,
                text="Choose file location",
                command=GetDir).place(x=200, y=150)

            global CurrentLocat, UpdateUtility
            UpdateUtility = True

            ComputePath = InstallerImportData.base_folder[len(InstallerImportData.base_folder)-90:]

            CurrentLocat = InstallerImportData.mod_Tkinter_tk_.Label(
                root,
                text=("  "+ComputePath+"  "),
                background="white",
                relief=InstallerImportData.mod_Tkinter_tk_.RIDGE)

            CurrentLocat.place(x=313, y=152.5)

            InstallerImportData.mod_Tkinter_ttk_.Button(
                root,
                text="Continue",
                command=lambda: BeginInstall.InstallScreen_2(
                    InstallerImportData,
                    root,
                    choice,
                    Dir)).place(x=760, y=500)

            InstallerImportData.mod_Tkinter_ttk_.Button(
                root,
                text="Back",
                command=lambda: BeginInstall.InstallScreen_0(
                    InstallerImportData,
                    root,
                    PycPath,
                    ChooseBETA,
                    choice)).place(x=680, y=500)

            root.update_idletasks()


        def InstallScreen_2(InstallerImportData, root, choice, Dir):
            root = InstallerImportData.mod_tkinter_utils__.TkinterInstaller.Createdisplay(
                InstallerImportData,
                root)

            InstallerImportData.mod_Tkinter_tk_.Label(
                root,
                text="Pycraft's Installation Assistant",
                background="white",
                font=(None, 20)).place(x=200, y=0)

            InstallerImportData.mod_Tkinter_tk_.Label(
                root,
                text="Downloading and installing Pycraft",
                background="white",
                font=(None, 20)).place(x=200, y=40)

            ans = InstallerImportData.mod_Tkinter_messagebox_.askquestion(
                "Permissions manager",
                "".join(("Can we have permission to download files from the internet ",
                         "and also modify files on this PC at any time using this Installer?")))

            retry = True
            i = 0
            while retry:
                if ans == "yes":
                    retry = False

                    global CurrentLocation

                    CurrentLocation = None
                    infoVers = None

                    if choice == "Latest":
                        OUTPUTtext = "Found latest version as: Pycraft v0.9.5"

                        InstallerImportData.mod_Installer_TextUtils_.InstallerText.CreateText(
                            InstallerImportData,
                            root,
                            OUTPUTtext)

                        infoVers = "Pycraft v0.9.5"
                    else:
                        OUTPUTtext = f"Found requested version as: {choice}"

                        InstallerImportData.mod_Installer_TextUtils_.InstallerText.CreateText(
                            InstallerImportData,
                            root,
                            OUTPUTtext)

                        infoVers = choice

                    OUTPUTtext += "".join((f"\nDownloading and installing {infoVers} ",
                                           "and the latest versions of it's dependencies ",
                                           "(This will take a moment)"))

                    InstallerImportData.mod_Installer_TextUtils_.InstallerText.CreateText(
                        InstallerImportData,
                        root,
                        OUTPUTtext)

                    InstallerImportData.mod_threading__.Thread(
                        target=InstallerImportData.mod_InstallerUtil__.FileManipulation.DownloadandInstall,
                        args=(InstallerImportData, choice,)).start()

                    start = InstallerImportData.mod_time__.perf_counter()

                    def Render_Progressbar(i):
                        CompletionProgressbar = InstallerImportData.mod_Tkinter_ttk_.Progressbar(
                            root,
                            orient=InstallerImportData.mod_Tkinter_tk_.HORIZONTAL,
                            length=100,
                            mode="indeterminate")

                        CompletionProgressbar.place(x=200, y=500)

                        CompletionProgressbar["value"] += i
                        root.update()

                    while InstallerImportData.mod_threading__.active_count() == 2:
                        i += 1
                        root.after(
                            50,
                            Render_Progressbar(i))

                    installtime = InstallerImportData.mod_time__.perf_counter()-start

                    OUTPUTtext += f" - done in {round(installtime, 4)} seconds"
                    InstallerImportData.mod_Installer_TextUtils_.InstallerText.CreateText(
                        InstallerImportData,
                        root,
                        OUTPUTtext)

                    OUTPUTtext += "\nSuccessfully installed Pycraft"

                    OUTPUTtext += "\nMoving Pycraft to selected install location"
                    InstallerImportData.mod_Installer_TextUtils_.InstallerText.CreateText(
                        InstallerImportData,
                        root,
                        OUTPUTtext)

                    CurrentLocation = InstallerImportData.mod_Site__.getusersitepackages()

                    InstallerImportData.mod_threading__.Thread(
                        target=InstallerImportData.mod_InstallerUtil__.FileManipulation.MoveFiles,
                        args=(InstallerImportData, Dir,)).start()

                    while InstallerImportData.mod_threading__.active_count() == 2:
                        i += 1
                        root.after(
                            50,
                            Render_Progressbar(i))

                    OUTPUTtext += " - done"
                    InstallerImportData.mod_Installer_TextUtils_.InstallerText.CreateText(
                        InstallerImportData,
                        root,
                        OUTPUTtext)

                    OUTPUTtext += "\nSuccessfully Installed Pycraft"
                    InstallerImportData.mod_Installer_TextUtils_.InstallerText.CreateText(
                        InstallerImportData,
                        root,
                        OUTPUTtext)

                    try:
                        global UpdateUtility
                        if UpdateUtility:
                            InstallerImportData.mod_Tkinter_ttk_.Button(
                                root,
                                text="Continue",
                                command=lambda: BeginInstall.InstallScreen_3(
                                    InstallerImportData,
                                    root,
                                    choice,
                                    Dir)).place(x=760, y=500)

                    except:
                        InstallerImportData.mod_Installer_Update_.BeginUpdate.FinishedUpdate(
                            InstallerImportData,
                            root)

                    root.update_idletasks()
                else:
                    ans2 = InstallerImportData.mod_Tkinter_messagebox_.askquestion(
                        "Caution",
                        "".join(("We did not receive permission to download files from the ",
                                 "internet and modify files on this PC, as a result we ",
                                 "cannot install Pycraft, would you like to amend this ",
                                 "decision (yes) or close the installer (no)?")))

                    if ans2 == "no":
                        quit()

                    else:
                        retry = True
                        ans = InstallerImportData.mod_Tkinter_messagebox_.askquestion(
                            "Permissions manager",
                            "".join(("Can we have permission to download files from ",
                                     "the internet and also modify files on this PC ",
                                     "at any time using this Installer?")))


        def InstallScreen_3(InstallerImportData, root, choice, Dir):
            root = InstallerImportData.mod_tkinter_utils__.TkinterInstaller.Createdisplay(
                InstallerImportData,
                root)

            InstallerImportData.mod_Tkinter_tk_.Label(
                root,
                text="Pycraft's Installation Assistant",
                background="white",
                font=(None, 20)).place(x=200, y=0)

            InstallerImportData.mod_Tkinter_tk_.Label(
                root,
                text="Successfully Installed Pycraft",
                background="white",
                font=(None, 20)).place(x=200, y=40)

            text = InstallerImportData.mod_Tkinter_tk_.Text(
                root,
                wrap=InstallerImportData.mod_Tkinter_tk_.WORD,
                relief=InstallerImportData.mod_Tkinter_tk_.FLAT,
                font=(None, 10))

            text.insert(
                InstallerImportData.mod_Tkinter_tk_.INSERT,
                "".join((f"Successfully installed {choice} we hope that you enjoy using ",
                         "this project. This installer can be opened from Pycraft by ",
                         "clicking on the 'Installer' option on the main menu. The ",
                         "installer will appear differently when you open it from ",
                         "Pycraft, from there you will be able to change these settings ",
                         "again under the 'Modify' section, but you also have the option ",
                         "to 'Repair', 'Uninstall' and 'Update' Pycraft. For now though ",
                         "we have finished the install but we have some final options ",
                         "which will be applied when the GUI closes:\nDo you want to add ",
                         "Pycraft to the desktop?\nAdditionally do you want to add Pycraft ",
                         "to the start (recommended)?\nYou also have the option to view ",
                         "the release notes for this install as well.\nThanks for ",
                         "installing Pycraft!")))

            text["state"] = InstallerImportData.mod_Tkinter_tk_.DISABLED
            text.place(x=200, y=80)

            CS = InstallerImportData.mod_Tkinter_tk_.BooleanVar(value=True)
            CSS = InstallerImportData.mod_Tkinter_tk_.BooleanVar(value=False)
            RelNot = InstallerImportData.mod_Tkinter_tk_.BooleanVar(value=True)

            global CreateDSKShortcut, CreateSTRTShortcut, ReleaseNotes

            CreateDSKShortcut = True
            CreateSTRTShortcut = False
            ReleaseNotes = True

            Config = {"PATH":Dir}
            with open(
                InstallerImportData.mod_Os__.path.join(
                    InstallerImportData.base_folder,
                    ("data files\\installer_config.json")), 'w') as openFile:

                InstallerImportData.mod_Json__.dump(Config, openFile)

            with open(
                (Dir+r"\\data files\\installer_config.json"), 'w') as openFile:

                InstallerImportData.mod_Json__.dump(Config, openFile)


            def DesktopisChecked():
                global CreateDSKShortcut
                CreateDSKShortcut = CS.get()


            def StartisChecked():
                global CreateSTRTShortcut
                CreateSTRTShortcut = CSS.get()


            def ToggleRelNot():
                global ReleaseNotes
                ReleaseNotes = RelNot.get()


            def OnExit():
                try:
                    if CreateDSKShortcut:
                        desktop = InstallerImportData.mod_Os__.path.join(
                            InstallerImportData.mod_Os__.path.join(
                                InstallerImportData.mod_Os__.environ["USERPROFILE"]),
                            "Desktop")

                        shell = InstallerImportData.mod_win32com_client_.Dispatch("WScript.Shell")

                        shortcut = shell.CreateShortCut(
                            InstallerImportData.mod_Os__.path.join(
                                desktop,
                                'Pycraft.lnk'))

                        FolderDirectory = "/pycraft/resources/folder resources/FolderIcon.ico"
                        shortcut.Targetpath = Dir+"/Pycraft/main.py"
                        shortcut.IconLocation = Dir+FolderDirectory
                        shortcut.save()

                    if CreateSTRTShortcut:
                        try:
                            start = InstallerImportData.mod_shutil_shell_.SHGetSpecialFolderPath(
                                0,
                                InstallerImportData.mod_shutil_shellcon_.CSIDL_COMMON_STARTMENU)

                            shell = InstallerImportData.mod_win32com_client_.Dispatch(
                                "WScript.Shell")

                            shortcut = shell.CreateShortCut(
                                InstallerImportData.mod_Os__.path.join(
                                    start,
                                    "Programs\\Pycraft.lnk"))

                            FolderDirectory = "/pycraft/resources/folder resources/FolderIcon.ico"

                            shortcut.Targetpath = Dir+"/pycraft/main.py"
                            shortcut.IconLocation = Dir+FolderDirectory
                            shortcut.save()
                            
                        except Exception as Message:
                            print(Message)
                            InstallerImportData.mod_Tkinter_messagebox_.showwarning(
                                "Permission Denied",
                                "".join(("You need to run this program as an administrator ",
                                         "to be able to use this function")))

                    if ReleaseNotes:
                        import webbrowser
                        webbrowser.open("https://github.com/PycraftDeveloper/Pycraft")
                        
                except Exception as Message:
                    InstallerImportData.mod_Tkinter_messagebox_.showerror(
                        "An error occurred",
                        "".join(("Pycraft has successfully installed but some of your final ",
                                 "configurations have not been made, this will change in later ",
                                 "versions of Pycraft but a quick fix is trying to restart the ",
                                 "installer, files downloaded already will be automatically ",
                                 "skipped in the download and install. Also this is an early ",
                                 "version of the installer, small issues like this will be ",
                                 "fixed in later versions of Pycraft that are build around ",
                                 f"the installer.\n\nFull error message: {Message}")))

                quit()


            InstallerImportData.mod_Tkinter_ttk_.Checkbutton(
                root,
                text="Create desktop shortcut on exit",
                variable=CS,
                onvalue=True,
                offvalue=False,
                command=DesktopisChecked).place(x=200, y=250)

            InstallerImportData.mod_Tkinter_ttk_.Checkbutton(
                root,
                text="Create shortcut to start on exit",
                variable=CSS,
                onvalue=True,
                offvalue=False,
                command=StartisChecked).place(x=200, y=275)

            InstallerImportData.mod_Tkinter_ttk_.Checkbutton(
                root,
                text="View more details about Pycraft online (on GitHub)",
                variable=RelNot,
                onvalue=True,
                offvalue=False,
                command=ToggleRelNot).place(x=200, y=300)

            InstallerImportData.mod_Tkinter_ttk_.Button(
                root,
                text="Finish",
                command=OnExit).place(x=760, y=500)

            root.update_idletasks()

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
