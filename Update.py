if __name__ != "__main__":
    print("Started <Pycraft_Update>")

    class BeginUpdate:
        def __init__(self):
            pass

        def UpdateScreen_0(InstallerImportData, root, PycPath, ChooseBETA, choice):
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
                text="Preparing to update Pycraft",
                background='white',
                font=(None, 15)).place(x=200, y=35)

            EnterText = "".join(("Welcome to Pycraft's update utility, here we will ",
                                 "uninstall all of Pycraft's files as well as its ",
                                 "additional data with the exception of your saved ",
                                 "data, then reinstall the latest version.\nThe ",
                                 "update utility will prompt for both accessing and ",
                                 "downloading files from the internet and for the ",
                                 "manipulation and removal of some of your files.",
                                 "\n\nIf an update is available then you can ",
                                 "continue through the update utility, if not ",
                                 "then you can return back to the 'Modify Your ",
                                 "Install' screen.\n\n"))

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
                text='Continue',
                command=lambda: BeginUpdate.UpdateScreen_1(
                    InstallerImportData,
                    root,
                    PycPath,
                    ChooseBETA,
                    choice)).place(x=760, y=500)

            InstallerImportData.mod_Tkinter_ttk_.Button(
                root,
                text='Home',
                command=lambda: InstallerImportData.mod_InstallerUtil__.CoreInstallerFunctionality.Home(
                    InstallerImportData,
                    root,
                    PycPath,
                    ChooseBETA,
                    choice)).place(x=680, y=500)

        def UpdateScreen_1(InstallerImportData, root, PycPath, ChooseBETA, choice):
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
                text="Checking for updates",
                background='white',
                font=(None, 15)).place(x=200, y=35)

            ContinueButtonState = InstallerImportData.mod_Tkinter_tk_.DISABLED
            BackButtonState = InstallerImportData.mod_Tkinter_tk_.DISABLED

            i = 0
            def UpdateOptions(ContinueButtonState, BackButtonState):
                global UpdateUtility
                UpdateUtility = True

                ContinueButton = InstallerImportData.mod_Tkinter_ttk_.Button(
                    root,
                    text='Continue',
                    command=lambda: InstallerImportData.mod_Installer_Uninstall_.BeginUninstall.Remove_But_Keep_Save(
                        InstallerImportData,
                        root,
                        PycPath,
                        ChooseBETA,
                        choice))
                ContinueButton.place(x=760, y=500)
                ContinueButton['state'] = ContinueButtonState

                BackButton = InstallerImportData.mod_Tkinter_ttk_.Button(
                    root,
                    text='Back',
                    command=lambda: BeginUpdate.UpdateScreen_0(
                        InstallerImportData,
                        root,
                        PycPath,
                        ChooseBETA,
                        choice))
                BackButton.place(x=680, y=500)
                BackButton['state'] = BackButtonState

            UpdateOptions(
                ContinueButtonState,
                BackButtonState)

            ans = InstallerImportData.mod_Tkinter_messagebox_.askquestion(
                "Permissions manager",
                "".join(("Can we have permission to download files from the ",
                    "internet and also modify files on this PC during the ",
                    "update process?")))

            retry = True

            while retry:
                if ans == "yes":
                    retry = False
                    break

                else:
                    ans2 = InstallerImportData.mod_Tkinter_messagebox_.askquestion(
                        "Caution",
                        "".join(("We did not receive permission to download files ",
                                 "from the internet and modify files on this PC, as ",
                                 "a result we cannot install Pycraft, would you ",
                                 "like to amend this decision (yes) or quit the ",
                                 "installer (no)?")))

                    if ans2 == "no":
                        InstallerImportData.mod_sys__.exit()

                    else:
                        retry = True
                        ans = InstallerImportData.mod_Tkinter_messagebox_.askquestion(
                            "Permissions manager",
                            "".join(("Can we have permission to download files from the ",
                                "internet and also modify files on this PC at any time ",
                                "using this Installer?")))

            OUTPUTtext = "Querying versions"

            InstallerImportData.mod_Installer_TextUtils_.InstallerText.CreateText(
                InstallerImportData,
                root,
                OUTPUTtext)

            import main
            version = main.QueryVersion()
            OUTPUTtext += f"\nFound current install as {version}"

            InstallerImportData.mod_Installer_TextUtils_.InstallerText.CreateText(
                InstallerImportData,
                root,
                OUTPUTtext)

            OUTPUTtext += "".join(("\nChecking for updates online. ",
                                   "(This might take a bit of time to complete)"))

            InstallerImportData.mod_Installer_TextUtils_.InstallerText.CreateText(
                InstallerImportData,
                root,
                OUTPUTtext)

            global outdated
            outdated = False

            InstallerImportData.mod_threading__.Thread(
                target=InstallerImportData.mod_InstallerUtil__.CoreInstallerFunctionality.outdatedDetector,
                args=(InstallerImportData,)).start()

            def Render_Progressbar(i):
                CompletionProgressbar = InstallerImportData.mod_Tkinter_ttk_.Progressbar(
                    root,
                    orient=InstallerImportData.mod_Tkinter_tk_.HORIZONTAL,
                    length=100,
                    mode='indeterminate')
                CompletionProgressbar.place(x=200, y=500)
                CompletionProgressbar['value'] += i

                root.update()

            while "outdatedDetector" in str(InstallerImportData.mod_threading__.enumerate()):
                i += 1
                root.after(
                    50,
                    Render_Progressbar(i))

            if outdated is False:
                OUTPUTtext += "\nYou already have the latest version of Pycraft"

                InstallerImportData.mod_Installer_TextUtils_.InstallerText.CreateText(
                    InstallerImportData,
                    root,
                    OUTPUTtext)

                ContinueButtonState = InstallerImportData.mod_Tkinter_tk_.DISABLED
                BackButtonState = InstallerImportData.mod_Tkinter_tk_.NORMAL

                UpdateOptions(
                    ContinueButtonState,
                    BackButtonState)

            else:
                OUTPUTtext += "".join(("\nThere are updates available on this PC, ",
                                       "press 'continue' to start the update"))

                InstallerImportData.mod_Installer_TextUtils_.InstallerText.CreateText(
                    InstallerImportData,
                    root,
                    OUTPUTtext)

                ContinueButtonState = InstallerImportData.mod_Tkinter_tk_.NORMAL
                BackButtonState = InstallerImportData.mod_Tkinter_tk_.NORMAL

                UpdateOptions(
                    ContinueButtonState,
                    BackButtonState)

        def FinishedUpdate(InstallerImportData, root):
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
                text="Finished Updating Pycraft",
                background='white',
                font=(None, 20)).place(x=200, y=40)

            text = InstallerImportData.mod_Tkinter_tk_.Text(
                root,
                wrap=InstallerImportData.mod_Tkinter_tk_.WORD,
                relief=InstallerImportData.mod_Tkinter_tk_.FLAT,
                font=(None, 10))

            text.insert(
                InstallerImportData.mod_Tkinter_tk_.INSERT,
                "".join(("Pycraft has successfully updated to the latest version. ",
                         "Running Pycraft now will automatically run the latest ",
                         "version.\n\nThis is a new feature so might cause some ",
                         "saved data to be lost whilst the project features ",
                         "changes to how it stores saved data.\nWe hope you ",
                         "enjoy using the latest update, feel free to leave ",
                         "feedback and view the changes on GitHub!")))

            text["state"] = InstallerImportData.mod_Tkinter_tk_.DISABLED
            text.place(x=200, y=80)

            InstallerImportData.mod_Tkinter_ttk_.Button(
                root,
                text='Finish',
                command=InstallerImportData.mod_sys__.exit).place(x=760, y=500)

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
