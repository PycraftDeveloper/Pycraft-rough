if __name__ != "__main__":
    class generate_error_screen:
        def __init__(self):
            pass

        def error_screen(self):
            
            import tkinter as TKINTER
            import sys
            from tkinter import messagebox as msgbox
            
            try:
                self.mod_pygame__.quit()
                
            except Exception as Message:
                log_message = "ErrorUtils > generate_error_screen > error_screen" + str(Message)

                self.mod_logging_utils__.create_log_message.update_log_warning(
                    self,
                    log_message)

            try:
                BaseWindow = TKINTER.Tk()
                BaseWindow.withdraw()
                if self.detailed_error_messages:
                    message = "".join(("Pycraft closed because an error occurred\n\n",
                                            f"More Details:\n{self.error_message_detailed}"))
                    
                    self.mod_logging_utils__.create_log_message.update_log_error(self, message)

                    msgbox.showerror(
                        "Pycraft closed because an error occurred",
                        message)

                else:
                    message = "".join(("Pycraft closed because an error occurred\n\n",
                                       f"More Details:\n{self.error_message}"))

                    self.mod_logging_utils__.create_log_message.update_log_error(self, message)
                    
                    msgbox.showerror(
                        "Pycraft closed because an error occurred",
                        message)

                sys.exit()
                
            except Exception as Message:
                try:
                    log_message = "ErrorUtils > generate_error_screen > error_screen" + str(Message)
                    
                    self.mod_logging_utils__.create_log_message.update_log_warning(
                        self,
                        log_message)
                except:
                    pass
                
                try:
                    BaseWindow = TKINTER.Tk()
                    BaseWindow.withdraw()
                    print(self.error_message)
                    msgbox.showerror("Pycraft closed because an error occurred",
                                     "".join(("Pycraft closed because an error occurred\n\n",
                                              f"More Details:\n{self.error_message}")))

                    sys.exit()
                    
                except Exception as Message:
                    sys.exit(Message)

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
