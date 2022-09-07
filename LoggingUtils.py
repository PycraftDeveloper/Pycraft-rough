if __name__ != "__main__":
    class create_log_message:
        def __init__(self):
            pass

        def update_log_information(self, text):
            try:
                if self.logging_dictionary["information"]:
                    text = f"Information: {str(text)}"
                    text += f" @ {self.mod_datetime__.datetime.now()}\n"
                    if self.output_log:
                        print(text)
                        
                    log_file.update_log(self, text)
                    
            except Exception as Message:
                self.error_message = "".join(("LoggingUtils > create_log_message ",
                                              f"> update_log_information: {str(Message)}"))

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

        def update_log_warning(self, text):
            try:
                if self.logging_dictionary["warnings"]:
                    text = f"Warning: {str(text)}"
                    text += f" @ {self.mod_datetime__.datetime.now()}\n"
                    if self.output_log:
                        print(text)

                    log_file.update_log(self, text)
                    
            except Exception as Message:
                self.error_message = "".join(("LoggingUtils > create_log_message ",
                                              f"> update_log_warning: {str(Message)}"))

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

        def update_log_error(self, error_text):
            try:
                if self.logging_dictionary["errors"]:
                    text = "### ### ### ###\n\n"
                    text += f"Error: {str(error_text)}"
                    text += f" @ {self.mod_datetime__.datetime.now()}\n"
                    text += "\n### ### ### ###\n"
                    if self.output_log:
                        print(text)

                    log_file.update_log(self, text)
                    
            except Exception as Message:
                self.error_message = "".join(("LoggingUtils > create_log_message ",
                                              f"> update_log_error: {str(Message)}"))

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

    class log_file:
        def __init__(self):
            pass

        def clear_log(self):
            try:
                if self.platform == "Linux":
                    with open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            "data files//log.txt"), "w"):

                        pass

                else:
                    with open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            "data files\\log.txt"), "w"):

                        pass
                    
            except Exception as Message:
                self.error_message = (
                    f"LoggingUtils > log_file > clear_log: {str(Message)}")

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

        def update_log(self, text):
            try:
                size = (self.mod_OS__.path.getsize(
                    self.mod_OS__.path.join(
                        self.base_folder,
                        "data files//log.txt"))/1000)/1000 #MB

                if size < 1:
                    if self.platform == "Linux":
                        with open(
                            self.mod_OS__.path.join(
                                self.base_folder,
                                "data files//log.txt"), "a") as file:

                            file.write(text)

                    else:
                        with open(
                            self.mod_OS__.path.join(
                                self.base_folder,
                                "data files\\log.txt"), "a") as file:

                            file.write(text)
                            
            except Exception as Message:
                self.error_message = (
                    f"LoggingUtils > log_file > write_info_log: {str(Message)}")

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

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
