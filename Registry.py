if __name__ != "__main__":
    class generate_registry:
        def __init__(self):
            pass

        def registry(self):
            try:
                CurrentTime = self.mod_datetime__.datetime.now()
                
                self.FOV = 70
                self.FPS = 60
                self.FPS_overclock = False
                self.aFPS = 0
                self.aa = True
                self.aa_quality = "2x"
                self.accent_color = (237, 125, 49)
                self.background_color = [30, 30, 30]
                self.camera = None
                self.camera_angle_speed = 3.5
                self.camera_enabled = True
                self.clear_cache = False
                self.clock = self.mod_pygame__.time.Clock()
                self.command = None
                self.connection_permission = None
                self.connection_status = False
                self.crash = False
                self.ctx = 0
                self.current_date = "".join((f"{CurrentTime.day}/",
                                            f"{CurrentTime.month}/",
                                            f"{CurrentTime.year}"))
                
                self.current_memory_usage = 0
                self.current_time = CurrentTime
                self.currently_displaying_message = False
                self.data_CPU_usage = []
                self.data_CPU_usage_Max = 1
                self.data_aFPS = []
                self.data_aFPS_Max = 1
                self.data_eFPS = []
                self.data_eFPS_Max = 1
                self.data_memory_usage = []
                self.data_memory_usage_Max = 1
                self.detailed_captions = False
                self.detailed_error_messages = False
                self.device_connected = False
                self.device_connected_update = False
                self.display = 0
                self.draw_devmode_graph = False
                self.eFPS = 60
                self.error_message = None
                self.error_message_detailed = None
                self.exit_mode = None
                self.extended_developer_options = False
                self.fancy_graphics = True
                self.fancy_particles = True

                self.folder_size = 0

                self.colors = [(224, 175, 160),
                                    (181, 68, 110),
                                    (144, 227, 154),
                                    (125, 131, 255),
                                    (43, 65, 98),
                                    (175, 66, 174),
                                    (77, 157, 224),
                                    (0, 212, 140),
                                    (6, 141, 157),
                                    (109, 157, 197),
                                    (232, 141, 103),
                                    (97, 61, 193),
                                    (155, 197, 61)]
                    
                self.chosen_colors = []

                temporary_colors = self.colors
                for _ in range(9):
                    index = self.mod_random__.randint(0, len(temporary_colors)-1)
                    self.chosen_colors.append(temporary_colors[index])
                    del temporary_colors[index]
                    
                self.file_structure = {"Source code": {"size": 0, "color": self.chosen_colors[0]},
                                            "Data files": {"size": 0, "color": self.chosen_colors[1]},
                                            "Audio": {"size": 0, "color": self.chosen_colors[2]},
                                            "Video": {"size": 0, "color": self.chosen_colors[3]},
                                            "Images": {"size": 0, "color": self.chosen_colors[4]},
                                            "3D objects": {"size": 0, "color": self.chosen_colors[5]},
                                            "Temporary": {"size": 0, "color": self.chosen_colors[6]},
                                            "Fonts": {"size": 0, "color": self.chosen_colors[7]},
                                            "Misc": {"size": 0, "color": self.chosen_colors[8]}}

                if self.platform == "Linux":
                    self.files_to_trash = ["resources//benchmark resources//Crate.obj.bin",
                                    "resources//game engine resources//map//map.obj.bin",
                                    "resources//game engine resources//map//map.obj.json",
                                    "resources//game engine resources//map//map2.obj.bin",
                                    "resources//game engine resources//map//map2.obj.json",
                                    "resources//game engine resources//clouds//Rnd_noise.png",
                                    "resources//general resources//PauseIMG.png"]

                else:
                    self.files_to_trash = ["resources\\benchmark resources\\Crate.obj.bin",
                                    "resources\\game engine resources\\map\\map.obj.bin",
                                    "resources\\game engine resources\\map\\map.obj.json",
                                    "resources\\game engine resources\\map\\map2.obj.bin",
                                    "resources\\game engine resources\\map\\map2.obj.json",
                                    "resources\\game engine resources\\clouds\\Rnd_noise.png",
                                    "resources\\general resources\\PauseIMG.png"]

                for dirpath, _, files in self.mod_OS__.walk(self.mod_OS__.path.join(self.base_folder, "__pycache__")):
                    for name in files:
                        file_path = self.mod_OS__.path.join(dirpath, name)
                        self.files_to_trash.append(file_path)
                
                self.font_color = (255, 255, 255)
                self.FOV = 90
                self.FPS = 60
                self.from_game_GUI = False
                self.from_play = False
                self.fullscreen = False
                self.fullscreen_x = self.mod_pyautogui__.size()[0]
                self.fullscreen_y = self.mod_pyautogui__.size()[1]
                
                self.game_engine_control = [[False, False],
                                            [False, False],
                                            [False, False],
                                            [False, False]]
                
                self.get_outdated = [False, False]
                self.go_to = None
                self.increased_speed = False
                self.input_configuration = None
                self.install_location = None
                self.iteration = 1
                self.joystick_connected = False
                self.joystick_exit = False
                self.joystick_hat_pressed = False
                self.joystick_zoom = None
                self.last_run = "29/09/2021"
                self.load_3D = True
                self.load_music = True
                self.load_time = [0, 1]
                self.logging_dictionary = {"boot-up information": False,
                                                "event updates": False,
                                                "warnings": False,
                                                "errors": False}
                self.mouse_button_down = False
                self.mouse_x = 0
                self.mouse_y = 0
                self.music = True
                self.music_volume = 5
                self.outdated = False
                self.output_log = False
                self.play_time = 0
                self.progress_line = []
                self.progress_message_text = "Initiating"
                self.project_sleeping = False
                self.pygame_device_added_update = False
                self.pygame_device_removed_update = False
                self.real_window_height = 720
                self.real_window_width = 1280
                self.adaptive_FPS = 60
                self.remove_file_permission = None
                self.render_fog = True
                self.reset_pycraft = False
                self.resolution = (1280, 720)
                self.resolution_preset = "default"
                self.run_full_startup = False
                self.run_timer = 0
                self.save_keys = {"theme": False,
                                    "settings_preset": "high",
                                    "adaptive_FPS": 60,
                                    "FPS": 60,
                                    "aFPS": 60,
                                    "iteration": 1,
                                    "FOV": 75,
                                    "camera_angle_speed": 3,
                                    "aa": True,
                                    "render_fog": True,
                                    "fancy_graphics": True,
                                    "fancy_particles": True,
                                    "sound": True,
                                    "sound_volume": 75,
                                    "music": False,
                                    "music_volume": 50,
                                    "x": 0,
                                    "y": 0,
                                    "z": 0,
                                    "last_run": "29/09/2021",
                                    "run_full_startup": True,
                                    "crash": False,
                                    "saved_window_width": 1280,
                                    "saved_window_height": 720,
                                    "fullscreen": True,
                                    "connection_permission": None,
                                    "updated": True,
                                    "load_time": [0, 1],
                                    "show_message": False,
                                    "show_strobe_effects": None,
                                    "extended_developer_options": False,
                                    "draw_devmode_graph": False,
                                    "detailed_error_messages": False,
                                    "logging_dictionary": {"information": False,
                                                                "warnings": False,
                                                                "errors": False},
                                    "save_on_exit": True,
                                    "resolution_preset": "default",
                                    "vsync": True,
                                    "aa_quality": "2x",
                                    "detailed_captions": False,
                                    "output_log": False,
                                    "increased_speed": False,
                                    "skip_time": False,
                                    "remove_file_permission": None,
                                    "input_configuration": {
                                        "keyboard": {
                                            "Jump": "Space",
                                            "Back": "Esc",
                                            "Toggle full-screen": "F11",
                                            "List variables": "Q",
                                            "Walk forwards": "W",
                                            "Walk backwards": "S", 
                                            "Walk left": "A", 
                                            "Walk right": "D",
                                            "Open inventory": "E",
                                            "Open map": "R",
                                            "Unlock mouse": "L",
                                            "Skip time": "K",
                                            "Confirm": "Enter",
                                            "Increase speed": "I"},

                                        "controller": {
                                            "Confirm": 1,
                                            "Back": 3,
                                            "Open inventory": 7,
                                            "Open map": 6,
                                            "Jump": 3
                                        }
                                    }
                                }
                
                self.save_on_exit = True
                self.saved_window_height = 720
                self.saved_window_width = 1280
                self.scan_pycraft = False
                self.secondary_font_color = (100, 100, 100)
                self.selected_input_reconfig = "keyboard"
                self.settings_preset = "Medium"
                self.shape_color = (80, 80, 80)
                self.show_strobe_effects = None
                self.show_message = True
                self.skip_time = False
                self.sound = True
                self.sound_volume = 75
                self.startup_animation = True
                self.theme = False
                self.timer = 0
                self.total_move_x = 0
                self.total_move_y = 0
                self.total_move_z = 0
                self.total_number_of_updates = 0
                self.updated = False
                self.use_mouse_input = True
                self.version = "0.9.6-2.5"
                self.vsync = True
                self.vsync_FPS = 60
                self.window_in_focus = True
                self.wnd = None
                self.x = 0
                self.x_scale_factor = 0
                self.y = 0
                self.y_scale_factor = 0
                self.z = 0
                
            except Exception as Message:
                self.error_message = "".join(("Registry > generate_registry ",
                                             f"> registry: {str(Message)}"))

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
