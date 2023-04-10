if __name__ != "__main__":
    try:
        import threading
        import time
        import json
        import site
        import os
        import tkinter
        import tkinter.ttk as tkinter_ttk
        from tkinter import messagebox
        import pathlib

        from registry_utils import Registry

        import update

        import tkinter_utils
        import installer_utils
        import text_utils
        import install_utils
        import file_utils
        from install_utils import install_data
    except ModuleNotFoundError as Message:
        from tkinter import messagebox
        error_message = f"{Message} in installer_main"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()
        
    class begin_install:
        def install_screen_one():
            tkinter_utils.tkinter_installer.create_display()
            
            install_data.var1 = tkinter.IntVar()

            tkinter.Label(
                Registry.root,
                text="Pycraft's Installation Assistant",
                background="white",
                font=(None, 20)).place(x=200, y=0)

            tkinter.Label(
                Registry.root,
                text="Important Information",
                background="white",
                font=(None, 20)).place(x=200, y=35)

            text = tkinter.Text(
                Registry.root,
                wrap=tkinter.WORD,
                relief=tkinter.FLAT,
                font=(None, 10))

            text.insert(
                tkinter.INSERT,
                Registry.installer_text["install"][0])

            text["state"] = tkinter.DISABLED
            text.place(x=200, y=80)

            install_data.var1 = tkinter.IntVar()

            install_utils.install_screen_one.button_check()

            tkinter_utils.tkinter_installer.style("TRadiobutton")
            tkinter_ttk.Radiobutton(
                Registry.root,
                text="I have not read the above text",
                variable=install_data.var1,
                value=0,
                command=lambda: install_utils.install_screen_one.button_check()).place(x=200, y=475)
            
            tkinter_utils.tkinter_installer.style("TRadiobutton")
            tkinter_ttk.Radiobutton(
                Registry.root,
                text="I have read the above text",
                variable=install_data.var1,
                value=1,
                command=lambda: install_utils.install_screen_one.button_check()).place(x=200, y=500)

            tkinter_ttk.Button(
                Registry.root,
                text="home",
                command=lambda: installer_utils.core_installer_functionality.home()).place(x=680, y=500)

        def install_screen_two():
            tkinter_utils.tkinter_installer.create_display()

            tkinter.Label(
                Registry.root,
                text="Pycraft's Installation Assistant",
                background="white",
                font=(None, 20)).place(x=200, y=0)

            tkinter.Label(
                Registry.root,
                text="Set Install Location",
                background="white",
                font=(None, 20)).place(x=200, y=40)

            OUTPUTtext = Registry.installer_text["install"][1]

            text = tkinter.Text(
                Registry.root,
                wrap=tkinter.WORD,
                relief=tkinter.FLAT,
                font=(None, 10))

            text.insert(
                tkinter.INSERT,
                OUTPUTtext)

            text["state"] = tkinter.DISABLED
            text.place(x=200, y=80)

            tkinter_ttk.Button(
                Registry.root,
                text="Choose file location",
                command= install_utils.install_screen_two.get_dir).place(x=200, y=150)

            global UpdateUtility
            UpdateUtility = True

            ComputePath = str(Registry.base_folder)[len(
                str(Registry.base_folder))-90:]

            install_data.CurrentLocat = tkinter.Label(
                Registry.root,
                text=("  "+ComputePath+"  "),
                background="white",
                relief=tkinter.RIDGE)

            install_data.CurrentLocat.place(x=313, y=152.5)

            tkinter_ttk.Button(
                Registry.root,
                text="Continue",
                command=lambda: begin_install.install_screen_three()).place(x=760, y=500)

            tkinter_ttk.Button(
                Registry.root,
                text="Back",
                command=lambda: begin_install.install_screen_one()).place(x=680, y=500)

            Registry.root.update_idletasks()

        def install_screen_three():
            tkinter_utils.tkinter_installer.create_display()

            tkinter.Label(
                Registry.root,
                text="Pycraft's Installation Assistant",
                background="white",
                font=(None, 20)).place(x=200, y=0)

            tkinter.Label(
                Registry.root,
                text="Downloading and installing Pycraft",
                background="white",
                font=(None, 20)).place(x=200, y=40)

            ans = messagebox.askquestion(
                "Permissions manager",
                Registry.installer_text["install"][2])

            retry = True
            i = 0
            while retry:
                if ans == "yes":
                    retry = False

                    global current_location

                    current_location = None
                    infoVers = None

                    if Registry.install_custom_version is False:
                        OUTPUTtext = f"Found latest version as: Pycraft {list(Registry.pycraft_versions.keys())[0]}"

                        text_utils.installer_text.create_text(
                            OUTPUTtext)

                        infoVers = f"Pycraft {list(Registry.pycraft_versions.keys())[0]}"
                    else:
                        OUTPUTtext = f"Found requested version as: {Registry.choice}"

                        text_utils.installer_text.create_text(
                            OUTPUTtext)

                        infoVers = Registry.choice

                    OUTPUTtext += Registry.installer_text["install"][3].format(
                        infoVers)

                    text_utils.installer_text.create_text(
                        OUTPUTtext)

                    threading.Thread(
                        target=installer_utils.file_manipulation.download,
                        args=(
                            Registry.base_folder,
                            pathlib.Path(install_data.Dir),
                            Registry.choice)).start()

                    start = time.perf_counter()

                    while threading.active_count() == 2:
                        i += 1
                        Registry.root.after(
                            50,
                            install_utils.install_screen_three.render_progress_bar(i))

                    installtime = time.perf_counter()-start
                    
                    file_utils.fix_installer.get_installer_config()
                    
                    OUTPUTtext += f"Installing {infoVers}'s required dependencies."

                    text_utils.installer_text.create_text(
                        OUTPUTtext)

                    threading.Thread(
                        target=installer_utils.file_manipulation.install_dependencies,
                        args=(
                            Registry.pycraft_install_path,)).start()

                    start = time.perf_counter()

                    while threading.active_count() == 2:
                        i += 1
                        Registry.root.after(
                            50,
                            install_utils.install_screen_three.render_progress_bar(i))

                    installtime = time.perf_counter()-start

                    OUTPUTtext += f" - done in {round(installtime, 4)} seconds"
                    text_utils.installer_text.create_text(
                        OUTPUTtext)

                    OUTPUTtext += "\nSuccessfully installed Pycraft"

                    OUTPUTtext += " - done"
                    text_utils.installer_text.create_text(
                        OUTPUTtext)

                    OUTPUTtext += "\nSuccessfully Installed Pycraft"
                    text_utils.installer_text.create_text(
                        OUTPUTtext)

                    try:
                        global UpdateUtility
                        if UpdateUtility:
                            tkinter_ttk.Button(
                                Registry.root,
                                text="Continue",
                                command=lambda: begin_install.install_screen_four()).place(x=760, y=500)

                    except:
                        update.Update.finished_update(
                            Registry.root)

                    Registry.root.update_idletasks()
                else:
                    ans2 = messagebox.askquestion(
                        "Caution",
                        Registry.installer_text["install"][4])

                    if ans2 == "no":
                        quit()

                    else:
                        retry = True
                        ans = messagebox.askquestion(
                            "Permissions manager",
                            Registry.installer_text["install"][2])

        def install_screen_four():
            tkinter_utils.tkinter_installer.create_display()

            tkinter.Label(
                Registry.root,
                text="Pycraft's Installation Assistant",
                background="white",
                font=(None, 20)).place(x=200, y=0)

            tkinter.Label(
                Registry.root,
                text="Successfully Installed Pycraft",
                background="white",
                font=(None, 20)).place(x=200, y=40)

            text = tkinter.Text(
                Registry.root,
                wrap=tkinter.WORD,
                relief=tkinter.FLAT,
                font=(None, 10))

            text.insert(
                tkinter.INSERT,
                Registry.installer_text["install"][6])

            text["state"] = tkinter.DISABLED
            text.place(x=200, y=80)

            choose_create_shortcut = tkinter.BooleanVar(value=True)
            choose_create_desktop_shortcut = tkinter.BooleanVar(value=False)
            choose_release_notes = tkinter.BooleanVar(value=True)

            Config = {"installer_install_path": str(Registry.base_folder)}
            pycraft_installer_config_path = Registry.installer_config_path# LINK TO INSTALLED PYCRAFT
            with open(pycraft_installer_config_path, "w") as file:
                json.dump(Config, file)

            Config = {"pycraft_install_path": str(install_data.Dir)}
            with open(Registry.installer_config_path, "w") as file:
                json.dump(Config, file)

            tkinter_utils.tkinter_installer.style("TCheckbutton")
            tkinter_ttk.Checkbutton(
                Registry.root,
                text="Create desktop shortcut on exit",
                variable=choose_create_shortcut,
                onvalue=True,
                offvalue=False,
                command= lambda:install_utils.install_screen_four.desktop_is_checked(
                    choose_create_shortcut)).place(x=200, y=250)

            tkinter_ttk.Checkbutton(
                Registry.root,
                text="Create start-menu shortcut on exit",
                variable=choose_create_desktop_shortcut,
                onvalue=True,
                offvalue=False,
                command= lambda:install_utils.install_screen_four.start_is_checked(
                    choose_create_desktop_shortcut)).place(x=200, y=275)

            tkinter_ttk.Checkbutton(
                Registry.root,
                text="View more details about Pycraft online (on GitHub)",
                variable=choose_release_notes,
                onvalue=True,
                offvalue=False,
                command= lambda:install_utils.install_screen_four.toggle_release_notes(
                    choose_release_notes)).place(x=200, y=300)

            tkinter_ttk.Button(
                Registry.root,
                text="Finish",
                command= install_utils.install_screen_four.on_exit).place(x=760, y=500)

            Registry.root.update_idletasks()

else:
    print("You need to run this as part of Pycraft's Installer")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft's Installer, please run the 'main.py' file")

    quit()
