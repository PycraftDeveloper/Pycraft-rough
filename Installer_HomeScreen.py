if __name__ != "__main__":
    print("Started <Pycraft_Installer_HomeScreen>")

    class Installer_Home:
        def Start(InstallerImportData, root, PycPath, ChooseBETA, Choice):
            root = InstallerImportData.mod_tkinter_utils__.TkinterInstaller.Createdisplay(
                InstallerImportData,
                root)

            InstallerImportData.mod_Tkinter_tk_.Label(
                root,
                text="Pycraft's Installation Assistant",
                background="white",
                font=(None, 20)).place(x=200, y=0)

            if InstallerImportData.platform == "Windows":
                if PycPath is not None:
                    ButtonPos = (760, 500)

                    InstallerImportData.mod_Tkinter_tk_.Label(
                        root,
                        text="Modify Your Install",
                        background="white",
                        font=(None, 20)).place(x=200, y=35)

                    EnterText = "".join(("Welcome back to Pycraft's Setup Wizard, we ",
                                         "have detected you already have an install of ",
                                         "Pycraft on your system, this gives you 3 ",
                                         "available options.\n\nWould you like to update, ",
                                         "modify or uninstall your version of Pycraft?",
                                         "\n\nThis will modify the installation of ",
                                         f"Pycraft at: {PycPath}"))

                    InstallerImportData.mod_Tkinter_ttk_.Button(
                        root,
                        text="Update",
                        command=lambda: InstallerImportData.mod_Installer_Update_.BeginUpdate.UpdateScreen_0(
                            InstallerImportData,
                            root,
                            PycPath,
                            ChooseBETA,
                            Choice)).place(x=680, y=500)

                    RepairButton = InstallerImportData.mod_Tkinter_ttk_.Button(
                        root,
                        text="Repair")
                    RepairButton["state"] = InstallerImportData.mod_Tkinter_tk_.DISABLED
                    RepairButton.place(x=600, y=500)

                    InstallerImportData.mod_Tkinter_ttk_.Button(
                        root,
                        text="Uninstall",
                        command=lambda: InstallerImportData.mod_Installer_Uninstall_.BeginUninstall.UninstallScreen_0(
                            InstallerImportData,
                            root,
                            PycPath,
                            ChooseBETA,
                            Choice)).place(x=520, y=500)

                    IfCompat = InstallerImportData.mod_Tkinter_tk_.NORMAL
                else:
                    try:
                        EnterText = "".join(("Welcome to Pycraft's Setup Wizard, ",
                                             "here we will guide you through your install ",
                                             "and setup of the latest stable version of ",
                                             "Pycraft, if you wish to install the BETA ",
                                             "versions of the game, please tick the box ",
                                             "below and then once you are satisfied with ",
                                             "your choice, please press the continue ",
                                             "button, you can press the back button to ",
                                             "navigate to the previous menu or choose ",
                                             "to exit Pycraft's Setup Wizard by closing ",
                                             "the GUI.\n\nThere are a few steps to this ",
                                             "install but this shouldn't take long."))

                        IfCompat = InstallerImportData.mod_Tkinter_tk_.NORMAL

                        ButtonPos = (680, 500)

                        BETAchoice = InstallerImportData.mod_Tkinter_tk_.BooleanVar(
                            value=ChooseBETA)

                        versions = [
                            "Latest",
                            "Latest",
                            "Pycraft-v0.9.1",
                            "Pycraft-v0.9.2",
                            "Pycraft-v0.9.3",
                            "Pycraft-v0.9.4",
                            "Pycraft-v0.9.5 (latest)"]

                        VersionChoice = InstallerImportData.mod_Tkinter_tk_.StringVar()
                        VersionChoice.set(versions[0])

                        DropDown = InstallerImportData.mod_Tkinter_ttk_.OptionMenu(
                            root,
                            VersionChoice,
                            *versions)

                        def GetVersion(BETAchoice):
                            if BETAchoice.get():
                                DropDown["state"] = InstallerImportData.mod_Tkinter_tk_.NORMAL

                            else:
                                DropDown["state"] = InstallerImportData.mod_Tkinter_tk_.DISABLED

                            DropDown.place(x=450, y=500)

                        GetVersion(BETAchoice)

                        InstallerImportData.mod_Tkinter_ttk_.Checkbutton(
                            root,
                            text="I want to install a BETA version of Pycraft",
                            variable=BETAchoice,
                            onvalue=True,
                            offvalue=False,
                            command=lambda: GetVersion(BETAchoice)).place(x=200, y=500)

                        ContinueButton = InstallerImportData.mod_Tkinter_ttk_.Button(
                            root,
                            text="Continue",
                            command=lambda: InstallerImportData.mod_Installer_Install_.BeginInstall.InstallScreen_0(
                                InstallerImportData,
                                root,
                                PycPath,
                                BETAchoice.get(),
                                VersionChoice.get()))

                        ContinueButton.place(x=760, y=500)
                        ContinueButton["state"] = IfCompat

                    except:
                        IfCompat = InstallerImportData.mod_Tkinter_tk_.DISABLED

                        EnterText = "".join(("Welcome to Pycraft's Setup Wizard, ",
                                             "here we will guide you through your ",
                                             "install and setup of the latest stable ",
                                             "version of Pycraft, if you wish to ",
                                             "install the BETA versions of the game, ",
                                             "please tick the box below and then once ",
                                             "you are satisfied with your choice, ",
                                             "please press the continue button, you ",
                                             "can press the back button to navigate ",
                                             "to the previous menu or choose to exit ",
                                             "Pycraft's Setup Wizard by closing the GUI.",
                                             "\n\nThere are a few steps to this install ",
                                             "but this shouldn't take long.\n\nIn order ",
                                             "to install Pycraft you will need to have a ",
                                             "suitable version of Python installed on ",
                                             "your system, ideally this needs to be 3.7 ",
                                             "or greater -with version checking coming ",
                                             "in a later version-. If you want to ",
                                             "install Pycraft stand-alone then on the ",
                                             "releases page of the project (here: ",
                                             "https://github.com/PycraftDeveloper/Pycraft/releases) ",
                                             "please download the (.exe) version."))

            else:
                IfCompat = InstallerImportData.mod_Tkinter_tk_.DISABLED

                ButtonPos = (680, 500)

                EnterText = ("Welcome to Pycraft's Setup Wizard, here we will ",
                             "guide you through your install and setup of the ",
                             "latest stable version of Pycraft, if you wish to ",
                             "install the BETA versions of the game, please tick ",
                             "the box below and then once you are satisfied with ",
                             "your choice, please press the continue button, you ",
                             "can press the back button to navigate to the previous ",
                             "menu or choose to exit Pycraft's Setup Wizard by ",
                             "closing the GUI.\n\nThere are a few steps to this ",
                             "install but this shouldn't take long.\n\nCurrently ",
                             "this installer is Windows only, but more OS's will ",
                             "be supported in later editions")

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
                text="Quit",
                command=lambda: InstallerImportData.mod_InstallerUtil__.CoreInstallerFunctionality.Close(
                    InstallerImportData)).place(
                        x=ButtonPos[0],
                        y=ButtonPos[1])

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
