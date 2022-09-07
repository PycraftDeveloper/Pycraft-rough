if __name__ != "__main__":
    class delete_files:
        def __init__(self):
            pass

        def clear_temporary_files(self):
            try:
                for i in range(len(self.files_to_trash)):
                    try:
                        self.mod_send2trash__.send2trash(self.mod_OS__.path.join(self.base_folder, self.files_to_trash[i]))
                        
                    except Exception as Message:
                        log_message = "".join(("FileUtils > delete_files > ",
                                            "clear_temporary_files: Unable ",
                                            "to remove file as it likely ",
                                            "doesn't exist. More details:\n",
                                            f"{str(Message)}"))

                        self.mod_logging_utils__.create_log_message.update_log_warning(
                            self,
                            log_message)

                    else:
                        self.mod_logging_utils__.create_log_message.update_log_information(
                            self,
                            f"Cleared: {self.mod_OS__.path.join(self.base_folder, self.files_to_trash[i])} \nwhich is considered a temporary file")
                
            except Exception as Message:
                self.error_message = "".join(("FileUtils > delete_files ",
                                              f"> clear_temporary_files: {str(Message)}"))
                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)
                
    class scan_folder:
        def __init__(self):
            pass

        def search_files(self, directory):
            try:
                self.mod_logging_utils__.create_log_message.update_log_information(
                    self,
                    f"Scanning {directory}")

                for key in self.file_structure:
                    self.file_structure[key]["size"] = 0

                self.folder_size = 0
                trash_files_array = []
                for i in range(len(self.files_to_trash)):
                    trash_files_array.append(self.mod_OS__.path.join(
                        self.base_folder, self.files_to_trash[i]))
                    
                files_array = []
                for dirpath, _, files in self.mod_OS__.walk(directory):
                    for name in files:
                        file_path = self.mod_OS__.path.join(dirpath, name)
                        files_array.append(file_path)
                        self.folder_size += self.mod_OS__.path.getsize(file_path)

                for i in range(len(files_array)):
                    trash = False
                    for j in range(len(trash_files_array)):
                        if files_array[i] == trash_files_array[j]:
                            trash = True
                            self.file_structure["Temporary"]["size"] += self.mod_OS__.path.getsize(
                                files_array[i])

                    if trash is False:
                        if (".ogg" in files_array[i] or
                                ".wav" in files_array[i] or
                                ".mp3" in files_array[i]):
                            
                            self.file_structure["Audio"]["size"] += self.mod_OS__.path.getsize(
                                files_array[i])

                        elif ".ttf" in files_array[i]:
                            self.file_structure["Fonts"]["size"] += self.mod_OS__.path.getsize(
                                files_array[i])

                        elif (".txt" in files_array[i] or
                                ".json" in files_array[i] or
                                ".md" in files_array[i]):
                            
                            self.file_structure["Data files"]["size"] += self.mod_OS__.path.getsize(
                                files_array[i])

                        elif (".py" in files_array[i] or
                                ".glsl" in files_array[i]):
                            
                            self.file_structure["Source code"]["size"] += self.mod_OS__.path.getsize(
                                files_array[i])

                        elif (".obj" in files_array[i] or
                                ".mtl" in files_array[i]):
                            
                            self.file_structure["3D objects"]["size"] += self.mod_OS__.path.getsize(
                                files_array[i])

                        elif (".png" in files_array[i] or
                                ".jpg" in files_array[i] or
                                ".ico" in files_array[i] or
                                ".gif" in files_array[i]):
                            
                            self.file_structure["Images"]["size"] += self.mod_OS__.path.getsize(
                                files_array[i])

                        else:
                            self.mod_logging_utils__.create_log_message.update_log_information(
                                self,
                                f"Not currently categorised: {files_array[i]}")

                            self.file_structure["Misc"]["size"] += self.mod_OS__.path.getsize(
                                files_array[i])
                            
            except Exception as Message:
                self.error_message = "".join(("FileUtils > scan_folder ",
                                             f"> search_files: {str(Message)}"))

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)
                        
    class FixInstaller:
        def __init__(self):
            pass

        def Setinstall_location(self):
            try:
                Repair = {"PATH":self.base_folder}

                if self.platform == "Linux":
                    with open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("data files//installer_config.json")), "w") as openFile:

                        self.mod_json__.dump(
                            Repair,
                            openFile)

                else:
                    with open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("data files\\installer_config.json")), "w") as openFile:

                        self.mod_json__.dump(
                            Repair,
                            openFile)

            except Exception as Message:
                self.error_message = "".join(("FileUtils > FixInstaller ",
                                             f"> Setinstall_location: {str(Message)}"))

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

        def Getinstall_location(self):
            try:
                if self.platform == "Linux":
                    with open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("data files//installer_config.json")), "r") as openFile:

                        StoredData = self.mod_json__.load(openFile)

                else:
                    with open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("data files\\installer_config.json")), "r") as openFile:

                        StoredData = self.mod_json__.load(openFile)

                self.install_location = StoredData["PATH"]
                
            except Exception as Message:
                log_message = "FileUtils > FixInstaller > Getinstall_location: "+str(Message)
                
                self.mod_logging_utils__.create_log_message.update_log_warning(
                    self,
                    log_message)

                self.install_location = None

    class pycraft_config_utils:
        def __init__(self):
            pass

        def read_input_key(self):
            try:
                if self.platform == "Linux":
                    with open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("data files//input_key.json")), "r") as openFile:

                        self.input_key = self.mod_json__.load(openFile)

                else:
                    with open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("data files\\input_key.json")), "r") as openFile:

                        self.input_key = self.mod_json__.load(openFile)

            except Exception as Message:
                self.error_message = "".join(("FileUtils > pycraft_config_utils ",
                                                f"> read_input_key: {str(Message)}"))

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(
                    self)

        def ReadMainSave(self):
            try:
                if self.platform == "Linux":
                    with open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("data files//pycraft_config.json")), "r") as openFile:

                        save = self.mod_json__.load(openFile)

                else:
                    with open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("data files\\pycraft_config.json")), "r") as openFile:

                        save = self.mod_json__.load(openFile)

                error_array = []
                for key in self.save_keys:
                    try:
                        setattr(self, key, save[key])
                        
                    except Exception as message_for_array:
                        setattr(self, key, self.save_keys[key])
                        error_array.append(str(message_for_array))
                        

                if len(error_array) > 0:
                    Message = ""

                    for error in error_array:
                        Message += error+"\n"
                        
                    error_message = "".join(("FileUtils > pycraft_config_utils ",
                                                "> ReadMainSave: ",
                                                "Your some of your saved file ",
                                                "was missing, we have attempted ",
                                                "to recover missing data."))

                    error_message_detailed = "".join(("FileUtils > pycraft_config_utils ",
                                                        "> ReamMainSave: ",
                                                        "Your some of your saved file ",
                                                        "was missing, we have attempted ",
                                                        "to recover missing data.\n",
                                                        "The following entries were ",
                                                        "missing and have been ",
                                                        f"reset:\n{Message}"))

                    if self.detailed_error_messages:
                        self.mod_logging_utils__.create_log_message.update_log_warning(
                            self,
                            error_message_detailed)
                        
                        self.mod_tkinter_messagebox_.showerror("Some saved data was missing",
                                                            error_message_detailed)
                        
                    else:
                        self.mod_logging_utils__.create_log_message.update_log_warning(
                            self,
                            error_message)
                        
                        self.mod_tkinter_messagebox_.showerror("Some saved data was missing",
                                                            error_message)

                if self.aFPS == float("inf"):
                    self.mod_logging_utils__.create_log_message.update_log_warning(
                        self,
                        "Reset aFPS from infinity")
                    
                    self.aFPS = 1
                    self.iteration = 1
                    
            except Exception as Message:
                if not "object has no attribute" in str(Message):
                    self.error_message = "".join(("FileUtils > pycraft_config_utils ",
                                                f"> ReadMainSave: {str(Message)}"))
                    
                    self.error_message_detailed = "".join(
                        self.mod_traceback__.format_exception(
                            None,
                            Message,
                            Message.__traceback__))

                    self.mod_error_utils__.generate_error_screen.error_screen(self)

        def RepairLostSave(self):
            try:
                if self.platform == "Linux":
                    with open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("data files//pycraft_config.json")), "w") as openFile:

                        self.mod_json__.dump(
                            self.save_keys,
                            openFile,
                            indent=1)

                else:
                    with open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("data files\\pycraft_config.json")), "w") as openFile:

                        self.mod_json__.dump(
                            self.save_keys,
                            openFile,
                            indent=1)

            except Exception as Message:
                self.error_message = "FileUtils > pycraft_config_utils > RepairLostSave: "+str(Message)
                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

        def save_pycraft_config(self):
            try:
                current_time = self.mod_datetime__.datetime.now()
                current_date = f"{current_time.day}/{current_time.month}/{current_time.year}"

                if self.updated:
                    self.updated = False

                SavedData = {"theme": self.theme,
                                "settings_preset": self.settings_preset,
                                "adaptive_FPS": self.adaptive_FPS,
                                "FPS": self.FPS,
                                "aFPS": round(self.aFPS, 3),
                                "iteration": self.iteration,
                                "FOV": self.FOV,
                                "camera_angle_speed": self.camera_angle_speed,
                                "aa": self.aa,
                                "render_fog": self.render_fog,
                                "fancy_graphics": self.fancy_graphics,
                                "fancy_particles": self.fancy_particles,
                                "sound": self.sound,
                                "sound_volume": self.sound_volume,
                                "music": self.music,
                                "music_volume": self.music_volume,
                                "x": round(self.x, 4),
                                "y": round(self.y, 4),
                                "z": round(self.z, 4),
                                "last_run": current_date,
                                "run_full_startup": self.run_full_startup,
                                "crash": False,
                                "saved_window_width": self.saved_window_width,
                                "saved_window_height": self.saved_window_height,
                                "fullscreen": self.fullscreen,
                                "connection_permission": self.connection_permission,
                                "updated": self.updated,
                                "load_time": [
                                    round(self.load_time[0], 3),
                                    round(self.load_time[1], 3)],
                                
                                "show_message": self.show_message,
                                "show_strobe_effects": self.show_strobe_effects,
                                "extended_developer_options": self.extended_developer_options,
                                "draw_devmode_graph": self.draw_devmode_graph,
                                "detailed_error_messages": self.detailed_error_messages,
                                "logging_dictionary": self.logging_dictionary,
                                "save_on_exit": self.save_on_exit,
                                "resolution_preset": self.resolution_preset,
                                "vsync": self.vsync,
                                "aa_quality": self.aa_quality,
                                "detailed_captions": self.detailed_captions,
                                "output_log": self.output_log,
                                "increased_speed": self.increased_speed,
                                "skip_time": self.skip_time,
                                "remove_file_permission": self.remove_file_permission,
                                "input_configuration": self.input_configuration}

                if self.platform == "Linux":
                    with open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("data files//pycraft_config.json")), "w") as openFile:

                        self.mod_json__.dump(
                            SavedData,
                            openFile,
                            indent=1)

                else:
                    with open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("data files\\pycraft_config.json")), "w") as openFile:

                        self.mod_json__.dump(
                            SavedData,
                            openFile,
                            indent=1)
                        
            except Exception as Message:
                self.error_message = "FileUtils > pycraft_config_utils > SaveTOpycraft_configFILE: "+str(Message)

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
