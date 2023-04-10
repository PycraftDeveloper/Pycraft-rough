if __name__ != "__main__":
    try:
        import tkinter
        from tkinter import messagebox
        import tkinter.ttk as tkinter_ttk
        import threading
        import sys
        
        from registry_utils import Registry

        import uninstall

        import tkinter_utils
        import installer_utils
        import text_utils
    except ModuleNotFoundError as Message:
        from tkinter import messagebox
        error_message = f"{Message} in update"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()

    class Update:
        def update_screen_one():
            tkinter_utils.tkinter_installer.create_display()

            tkinter.Label(
                root,
                text="Pycraft's Installation Assistant",
                background='white',
                font=(None, 20)).place(x=200, y=0)

            tkinter.Label(
                root,
                text="Preparing to update Pycraft",
                background='white',
                font=(None, 15)).place(x=200, y=35)

            EnterText = Registry.installer_text["update"][0]

            text = tkinter.Text(
                root,
                wrap=tkinter.WORD,
                relief=tkinter.FLAT,
                font=(None, 10))

            text.insert(
                tkinter.INSERT,
                EnterText)

            text["state"] = tkinter.DISABLED
            text.place(x=200, y=40)

            tkinter_ttk.Button(
                root,
                text='Continue',
                command=lambda: Update.update_screen_two(
                    self,
                    root,
                    pycraft_install_path,
                    install_custom_version,
                    choice)).place(x=760, y=500)

            tkinter_ttk.Button(
                root,
                text='home',
                command=lambda: installer_utils.core_installer_functionality.home(
                    self,
                    root,
                    pycraft_install_path,
                    install_custom_version,
                    choice)).place(x=680, y=500)

        def update_screen_two(self, root, pycraft_install_path, install_custom_version, choice):
            root = tkinter_utils.tkinter_installer.create_display(
                self,
                root)

            tkinter.Label(
                root,
                text="Pycraft's Installation Assistant",
                background='white',
                font=(None, 20)).place(x=200, y=0)

            tkinter.Label(
                root,
                text="Checking for updates",
                background='white',
                font=(None, 15)).place(x=200, y=35)

            ContinueButtonState = tkinter.DISABLED
            BackButtonState = tkinter.DISABLED

            i = 0
            def update_options(ContinueButtonState, BackButtonState):
                global UpdateUtility
                UpdateUtility = True

                ContinueButton = tkinter_ttk.Button(
                    root,
                    text='Continue',
                    command=lambda: uninstall.begin_uninstall.remove_but_keep_save(
                        self,
                        root,
                        pycraft_install_path,
                        install_custom_version,
                        choice))
                ContinueButton.place(x=760, y=500)
                ContinueButton['state'] = ContinueButtonState

                BackButton = tkinter_ttk.Button(
                    root,
                    text='Back',
                    command=lambda: Update.update_screen_one(
                        self,
                        root,
                        pycraft_install_path,
                        install_custom_version,
                        choice))
                BackButton.place(x=680, y=500)
                BackButton['state'] = BackButtonState

            update_options(
                ContinueButtonState,
                BackButtonState)

            ans = messagebox.askquestion(
                "Permissions manager",
                Registry.installer_text["update"][1])

            retry = True

            while retry:
                if ans == "yes":
                    retry = False
                    break

                else:
                    ans2 = messagebox.askquestion(
                        "Caution",
                        Registry.installer_text["update"][2])

                    if ans2 == "no":
                        sys.exit()

                    else:
                        retry = True
                        ans = messagebox.askquestion(
                            "Permissions manager",
                            Registry.installer_text["update"][3])

            OUTPUTtext = "Querying versions"

            text_utils.installer_text.create_text(
                root,
                OUTPUTtext)

            import pycraft_main
            version = pycraft_main.QueryVersion()
            OUTPUTtext += f"\nFound current install as {version}"

            text_utils.installer_text.create_text(
                root,
                OUTPUTtext)

            OUTPUTtext += Registry.installer_text["update"][4]

            text_utils.installer_text.create_text(
                root,
                OUTPUTtext)

            global outdated
            outdated = False

            threading.Thread(
                target=installer_utils.core_installer_functionality.outdated_detector,
                args=(self,)).start()

            def render_progress_bar(i):
                CompletionProgressbar = tkinter_ttk.Progressbar(
                    root,
                    orient=tkinter.HORIZONTAL,
                    length=100,
                    mode='indeterminate')
                CompletionProgressbar.place(x=200, y=500)
                CompletionProgressbar['value'] += i

                root.update()

            while "outdated_detector" in str(threading.enumerate()):
                i += 1
                root.after(
                    50,
                    render_progress_bar(i))

            if outdated is False:
                OUTPUTtext += "\nYou already have the latest version of Pycraft"

                text_utils.installer_text.create_text(
                    root,
                    OUTPUTtext)

                ContinueButtonState = tkinter.DISABLED
                BackButtonState = tkinter.NORMAL

                update_options(
                    ContinueButtonState,
                    BackButtonState)

            else:
                OUTPUTtext += Registry.installer_text["update"][5]

                text_utils.installer_text.create_text(
                    root,
                    OUTPUTtext)

                ContinueButtonState = tkinter.NORMAL
                BackButtonState = tkinter.NORMAL

                update_options(
                    ContinueButtonState,
                    BackButtonState)

        def finished_update(self, root):
            root = tkinter_utils.tkinter_installer.create_display(
                self,
                root)

            tkinter.Label(
                root,
                text="Pycraft's Installation Assistant",
                background='white',
                font=(None, 20)).place(x=200, y=0)

            tkinter.Label(
                root,
                text="Finished Updating Pycraft",
                background='white',
                font=(None, 20)).place(x=200, y=40)

            text = tkinter.Text(
                root,
                wrap=tkinter.WORD,
                relief=tkinter.FLAT,
                font=(None, 10))

            text.insert(
                tkinter.INSERT,
                Registry.installer_text["update"][6])

            text["state"] = tkinter.DISABLED
            text.place(x=200, y=80)

            tkinter_ttk.Button(
                root,
                text='Finish',
                command=sys.exit).place(x=760, y=500)

else:
    print("You need to run this as part of Pycraft's Installer")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft's Installer, please run the 'main.py' file")

    quit()
