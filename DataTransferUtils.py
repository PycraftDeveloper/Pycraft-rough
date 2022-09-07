if __name__ != "__main__":
    class data_transfer:
        def __init__(self):
            pass

        def store_data(self):
            try:
                # database
                dictionary = self.__dict__
                pickle_dictionary = {}
                for key, value in dictionary.items():
                    if not ("mod_" in str(key) or ("<" in str(value) and ">" in str(value))):
                        pickle_dictionary.update({key: value})

                # Its important to use binary mode
                dbfile = open('transfer', 'wb')

                # source, destination
                self.mod_pickle__.dump(pickle_dictionary, dbfile)
                dbfile.close()
                
            except Exception as Message:
                self.error_message = "".join(("DataTransferUtils > data_transfer ",
                                              f"> store_data: {str(Message)}"))

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

        def loadData():
            import pickle
            # for reading also binary mode is important
            class create_pycraft_context:
                def __init__(self):
                    dbfile = open('transfer', 'rb')
                    db = pickle.load(dbfile)
                    for key in db:
                        setattr(self, key, db[key])
                        
                    dbfile.close()

            self = create_pycraft_context()
            return self

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
