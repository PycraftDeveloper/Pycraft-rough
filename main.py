DEVELOPER_BUILD = True
if __name__ == "__main__":
    try:
        import traceback
        import __init__
        
        from registry_utils import Registry
        
        import logging_utils
    except ModuleNotFoundError as Message:
        from tkinter import messagebox
        error_message = f"{Message} in main"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()
        
    try:
        if DEVELOPER_BUILD:
            Registry.output_log = True
        logging_utils.log_file.clear_log()
        __init__.installer_main.Run.start()
    except Exception as message:
        from tkinter import messagebox
        if DEVELOPER_BUILD:
            message = "".join((traceback.format_exception(
                None,
                message,
                message.__traceback__)))
            
        logging_utils.create_log_message.update_log_error(
            message)
            
        messagebox.showerror(
            "Pycraft closed because an error occurred",
            str(message))
        
        quit()