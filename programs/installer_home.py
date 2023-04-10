if __name__ != "__main__":
    try:
        import tkinter
        import tkinter.ttk as tkinter_ttk
        
        from registry_utils import Registry

        import update
        import uninstall
        import install
        
        import tkinter_utils
        import installer_utils
    except ModuleNotFoundError as Message:
        from tkinter import messagebox
        error_message = f"{Message} in installer_home"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()

    class installer_home(Registry):
        def start():
            tkinter_utils.tkinter_installer.create_display()
            
            tkinter.Label(
                Registry.root,
                text="Pycraft's installation Assistant",
                background="white",
                font=(None, 20)).place(x=200, y=0)

            if Registry.platform == "Windows":
                if Registry.pycraft_install_path is not None:
                    ButtonPos = (760, 500)

                    tkinter.Label(
                        Registry.root,
                        text="Modify Your install",
                        background="white",
                        font=(None, 20)).place(x=200, y=35)

                    EnterText = Registry.installer_text["installer home"][0].format(Registry.pycraft_install_path)

                    tkinter_ttk.Button(
                        Registry.root,
                        text="Update",
                        command=update.Update.update_screen_one).place(x=680, y=500)

                    RepairButton = tkinter_ttk.Button(
                        Registry.root,
                        text="Repair")
                    RepairButton["state"] = tkinter.DISABLED
                    RepairButton.place(x=600, y=500)

                    tkinter_ttk.Button(
                        Registry.root,
                        text="Uninstall",
                        command=uninstall.Uninstall.uninstall_screen_one).place(x=520, y=500)

                    IfCompat = tkinter.NORMAL
                else:
                    try:
                        EnterText = Registry.installer_text["installer home"][2]

                        IfCompat = tkinter.NORMAL

                        ButtonPos = (680, 500)

                        BETAchoice = tkinter.BooleanVar(
                            value=Registry.install_custom_version)

                        versions = [
                            "Latest"]
                        
                        for key in Registry.pycraft_versions:
                            string = f"Pycraft {key}"
                            if list(Registry.pycraft_versions.keys()).index(key) == 0:
                                string += " (latest)"
                                
                            versions.append(string)

                        VersionChoice = tkinter.StringVar()
                        VersionChoice.set(versions[0])
                        
                        tkinter_utils.tkinter_installer.style("TMenubutton")

                        DropDown = tkinter_ttk.OptionMenu(
                            Registry.root,
                            VersionChoice,
                            *versions)
                        
                        DropDown["menu"].config(bg="white")

                        def get_version(BETAchoice):
                            if BETAchoice.get():
                                DropDown["state"] = tkinter.NORMAL

                            else:
                                DropDown["state"] = tkinter.DISABLED

                            DropDown.place(x=450, y=500)

                        get_version(BETAchoice)
                        
                        tkinter_utils.tkinter_installer.style("TCheckbutton")

                        check_button = tkinter_ttk.Checkbutton(
                            Registry.root,
                            text="I want to install a BETA version of Pycraft",
                            variable=BETAchoice,
                            onvalue=True,
                            offvalue=False,
                            command=lambda: get_version(BETAchoice))
                        
                        check_button.place(x=200, y=500)
                        
                        def continue_button_command(
                                BETAchoice,
                                VersionChoice):
                            
                            Registry.choice = VersionChoice.get()
                            Registry.install_custom_version = BETAchoice.get()
                            install.begin_install.install_screen_one()
                            
                        ContinueButton = tkinter_ttk.Button(
                            Registry.root,
                            text="Continue",
                            command=lambda: continue_button_command(
                                BETAchoice,
                                VersionChoice))
                        
                        ContinueButton.place(x=760, y=500)
                        ContinueButton["state"] = IfCompat
                    except:
                        IfCompat = tkinter.DISABLED

                        EnterText = Registry.installer_text["installer home"][3]

            else:
                IfCompat = tkinter.DISABLED

                ButtonPos = (680, 500)

                EnterText = Registry.installer_text["installer home"][4]

            text = tkinter.Text(
                Registry.root,
                wrap=tkinter.WORD,
                relief=tkinter.FLAT,
                font=(None, 10))

            text.insert(
                tkinter.INSERT,
                EnterText)

            text["state"] = tkinter.DISABLED
            text.place(x=200, y=40)

            tkinter_ttk.Button(
                Registry.root,
                text="Quit",
                command=installer_utils.core_installer_functionality.close).place(
                        x=ButtonPos[0],
                        y=ButtonPos[1])

else:
    print("You need to run this as part of Pycraft's Installer")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft's Installer, please run the 'main.py' file")

    quit()
