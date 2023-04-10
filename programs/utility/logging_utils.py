if __name__ != "__main__":
    try:
        import datetime
        import os
        
        from registry_utils import Registry
    except ModuleNotFoundError as Message:
        from tkinter import messagebox
        error_message = f"{Message} in logging_utils"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()
        
    class create_log_message(Registry):
        def update_log_information(text):
            if Registry.logging_dictionary["information"]:
                text = f"Information: {str(text)}"
                text += f" @ {datetime.datetime.now()}"
                if Registry.output_log:
                    print(text)

                log_file.update_log(text)
                
        def update_log_warning(text):
            if Registry.logging_dictionary["warnings"]:
                text = f"Warning: {str(text)}"
                text += f" @ {datetime.datetime.now()}"
                if Registry.output_log:
                    print(text)

                log_file.update_log(text)

        def update_log_error(error_text):
            if Registry.logging_dictionary["errors"]:
                text = "### ### ### ###\n\n"
                text += f"Error: {str(error_text)}"
                text += f" @ {datetime.datetime.now()}\n"
                text += "\n### ### ### ###\n"
                if Registry.output_log:
                    print(text)

                log_file.update_log(text)

    class log_file(Registry):
        def clear_log():
            log_path = Registry.base_folder / "data files" / "log.txt"
            with open(
                    log_path,
                    "w"):

                pass

        def update_log(text):
            log_path = Registry.base_folder / "data files" / "log.txt"
            size = (os.path.getsize(log_path)/1000)/1000 #MB

            if size < 1:
                with open(
                        log_path,
                        "a") as file:

                    file.write(text)

else:
    print("You need to run this as part of Pycraft's Installer")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft's Installer, please run the 'main.py' file")
    quit()
