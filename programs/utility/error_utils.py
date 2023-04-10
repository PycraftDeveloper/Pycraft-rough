if __name__ != "__main__":
    try:
        from registry_utils import Registry
        
        import logging_utils
    except ModuleNotFoundError as Message:
        from tkinter import messagebox
        error_message = f"{Message} in installer_main"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()
            
    class generate_error_screen(Registry):
        def error_screen(
                error_message,
                error_message_detailed):
            
            from tkinter import messagebox as msgbox

            try:
                if Registry.detailed_error_messages:
                    message = "".join(("Pycraft closed because an error occurred\n\n",
                                            f"More Details:\n{error_message_detailed}"))
                    
                    logging_utils.create_log_message.update_log_error(
                        message)

                    msgbox.showerror(
                        "Pycraft closed because an error occurred",
                        message)

                else:
                    message = "".join(("Pycraft closed because an error occurred\n\n",
                                       f"More Details:\n{error_message}"))

                    logging_utils.create_log_message.update_log_error(
                        message)
                    
                    msgbox.showerror(
                        "Pycraft closed because an error occurred",
                        message)

                quit()
                
            except Exception as Message:
                log_message = "ErrorUtils > generate_error_screen > error_screen: " + str(Message)
                
                logging_utils.create_log_message.update_log_warning(
                    log_message)
                
                msgbox.showerror("Pycraft closed because an error occurred",
                                    "".join(("Pycraft closed because an error occurred\n\n",
                                            f"More Details:\n{error_message}")))

                quit()

else:
    print("You need to run this as part of Pycraft's Installer")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft's Installer, please run the 'main.py' file")

    quit()
