if __name__ != "__main__":
    class initialize_modules:
        def __init__(self):
            pass

        def initialize_external_modules(self):
            try:
                # [self]
                # mod
                # (module)
                # (module name)
                # (subsection of module)
                # (name references)
                from PIL import Image
                self.mod_PIL_Image_ = Image
                self.mod_logging_utils__.create_log_message.update_log_information(
                    self,
                    "Imported PIL > Image")

                from PIL import ImageFilter
                self.mod_PIL_ImageFilter_ = ImageFilter
                self.mod_logging_utils__.create_log_message.update_log_information(
                    self,
                    "Imported PIL > ImageFilter")

                from moderngl_window.scene.camera import KeyboardCamera
                self.mod_ModernGL_window_keyboard_camera = KeyboardCamera
                self.mod_logging_utils__.create_log_message.update_log_information(
                    self,
                    "Imported moderngl_window.scene.camera > KeyboardCamera")

                from matplotlib import cm
                self.mod_matplotlib_cm_ = cm
                self.mod_logging_utils__.create_log_message.update_log_information(
                    self,
                    "Imported matplotlib > cm")

                from pyjoystick.sdl2 import run_event_loop
                self.mod_pyjoystick_run_event_loop_ = run_event_loop
                self.mod_logging_utils__.create_log_message.update_log_information(
                    self,
                    "Imported pyjoystick.sdl2 > run_event_loop")

                from pyrr import Matrix44, Vector3, matrix44
                self.mod_pyrr_Matrix44_ = Matrix44
                self.mod_logging_utils__.create_log_message.update_log_information(
                    self,
                    "Imported pyrr > Matrix44")
                self.mod_pyrr_Vector3_ = Vector3
                self.mod_logging_utils__.create_log_message.update_log_information(
                    self,
                    "Imported pyrr > Vector3")
                self.mod_pyrr_matrix44_ = matrix44
                self.mod_logging_utils__.create_log_message.update_log_information(
                    self,
                    "Imported pyrr > matrix44")

                from tkinter import messagebox
                self.mod_tkinter_messagebox_ = messagebox
                self.mod_logging_utils__.create_log_message.update_log_information(
                    self,
                    "Imported tkinter > messagebox")

                from typing import Final
                self.mod_typing_Final = Final
                self.mod_logging_utils__.create_log_message.update_log_information(
                    self,
                    "Imported typing > Final")

                import GPUtil
                self.mod_GPUtil__ = GPUtil
                self.mod_logging_utils__.create_log_message.update_log_information(
                    self,
                    "Imported GPUtil")

                import cpuinfo
                self.mod_cpuinfo__ = cpuinfo
                self.mod_logging_utils__.create_log_message.update_log_information(
                    self,
                    "Imported cpuinfo")

                import ctypes
                self.mod_ctypes__ = ctypes
                self.mod_logging_utils__.create_log_message.update_log_information(
                    self,
                    "Imported ctypes")

                import math
                self.mod_math__ = math
                self.mod_logging_utils__.create_log_message.update_log_information(
                    self,
                    "Imported math")

                import moderngl
                self.mod_ModernGL__ = moderngl
                self.mod_logging_utils__.create_log_message.update_log_information(
                    self,
                    "Imported moderngl")

                import moderngl_window
                self.mod_ModernGL_window_ = moderngl_window
                self.mod_logging_utils__.create_log_message.update_log_information(
                    self,
                    "Imported moderngl_window")

                import moderngl_window.geometry as geometry
                self.mod_ModernGL_window_geometry = geometry
                self.mod_logging_utils__.create_log_message.update_log_information(
                    self,
                    "Imported moderngl_window.geometry as geometry")

                import moderngl_window.screenshot as screenshot
                self.mod_ModernGL_window_screenshot = screenshot
                self.mod_logging_utils__.create_log_message.update_log_information(
                    self,
                    "Imported moderngl_window.screenshot as screenshot")

                import numpy
                self.mod_numpy__ = numpy
                self.mod_logging_utils__.create_log_message.update_log_information(
                    self,
                    "Imported numpy")

                import pickle
                self.mod_pickle__ = pickle
                self.mod_logging_utils__.create_log_message.update_log_information(
                    self,
                    "Imported pickle")

                import psutil
                self.mod_psutil__ = psutil
                self.mod_logging_utils__.create_log_message.update_log_information(
                    self,
                    "Imported psutil")

                import pyjoystick
                self.mod_pyjoystick__ = pyjoystick
                self.mod_logging_utils__.create_log_message.update_log_information(
                    self,
                    "Imported pyjoystick")

                import subprocess
                self.mod_subprocess__ = subprocess
                self.mod_logging_utils__.create_log_message.update_log_information(
                    self,
                    "Imported subprocess")

                import sys
                self.mod_sys__ = sys
                self.mod_logging_utils__.create_log_message.update_log_information(
                    self,
                    "Imported sys")

                import threading
                self.mod_threading__ = threading
                self.mod_logging_utils__.create_log_message.update_log_information(
                    self,
                    "Imported threading")

                import time
                self.mod_time__ = time
                self.mod_logging_utils__.create_log_message.update_log_information(
                    self,
                    "Imported time")

                import timeit
                self.mod_timeit__ = timeit
                self.mod_logging_utils__.create_log_message.update_log_information(
                    self,
                    "Imported timeit")

                import tkinter as tk
                self.mod_tkinter__tk = tk
                self.mod_logging_utils__.create_log_message.update_log_information(
                    self,
                    "Imported tkinter as tk")

                import typing
                self.mod_typing__ = typing
                self.mod_logging_utils__.create_log_message.update_log_information(
                    self,
                    "Imported typing")

                import send2trash
                self.mod_send2trash__ = send2trash
                self.mod_logging_utils__.create_log_message.update_log_information(
                    self,
                    "Imported send2trash")
                
            except Exception as Message:
                self.error_message = "".join(("ModuleUtils > initialize_modules ",
                                              f"> initialize_external_modules: {str(Message)}"))

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

        def initialize_internal_modules(self):
            try:
                ImportPackagesAsUsual = True

                if ("site-packages" in self.base_folder or
                        "dist-packages" in self.base_folder):
                    ImportPackagesAsUsual = False

                if ImportPackagesAsUsual:
                    import Achievements
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported Achievements")
                    
                    import Benchmark
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported Benchmark")
                    
                    import CaptionUtils
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported CaptionUtils")
                    
                    import CharacterDesigner
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported CharacterDesigner")
                    
                    import Credits
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported Credits")
                    
                    import DisplayUtils
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported DisplayUtils")
                    
                    import DrawingUtils
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported DrawingUtils")
                    
                    import ExtendedBenchmark
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported ExtendedBenchmark")

                    import pygame_game
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported GameEngine")
                    
                    import GameEngineUtils
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported GameEngineUtils")
                    
                    import GLWindowUtils
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported GLWindowUtils")
                    
                    import HomeScreen
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported HomeScreen")
                    
                    import ImageUtils
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported ImageUtils")
                    
                    import Installer_main
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported Installer_main")
                    
                    import IntegratedInstaller
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported IntegratedInstaller")
                    
                    import Inventory
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported Inventory")
                    
                    import JoystickUtils
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported JoystickUtils")
                    
                    import main
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported main")
                    
                    import MapGUI
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported MapGUI")

                    import DataTransferUtils
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported DataTransferUtils")
                    
                    import PycraftStartupTest
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported PycraftStartupTest")
                    
                    import Settings
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported Settings")
                    
                    import ShareDataUtils
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported ShareDataUtils")
                    
                    import SoundUtils
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported SoundUtils")
                    
                    import StartupAnimation
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported StartupAnimation")
                    
                    import TextUtils
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported TextUtils")
                    
                    import ThemeUtils
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported ThemeUtils")
                    
                    import ThreadingUtils
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported ThreadingUtils")
                    
                    import TkinterUtils
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported TkinterUtils")

                else:
                    from pycraft import Achievements
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported Achievements")
                    
                    from pycraft import Benchmark
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported Benchmark")
                    
                    from pycraft import CaptionUtils
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported CaptionUtils")
                    
                    from pycraft import CharacterDesigner
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported CharacterDesigner")
                    
                    from pycraft import Credits
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported Credits")
                    
                    from pycraft import DisplayUtils
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported DisplayUtils")
                    
                    from pycraft import DrawingUtils
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported DrawingUtils")
                    
                    from pycraft import ExtendedBenchmark
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported ExtendedBenchmark")

                    from pycraft import pygame_game
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported GameEngine")
                    
                    from pycraft import GameEngineUtils
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported GameEngineUtils")
                    
                    from pycraft import GLWindowUtils
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported GLWindowUtils")
                    
                    from pycraft import HomeScreen
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported HomeScreen")
                    
                    from pycraft import ImageUtils
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported ImageUtils")
                    
                    from pycraft import Installer_main
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported Installer_main")
                    
                    from pycraft import IntegratedInstaller
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported IntegratedInstaller")
                    
                    from pycraft import Inventory
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported Inventory")
                    
                    from pycraft import JoystickUtils
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported JoystickUtils")
                    
                    from pycraft import main
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported main")
                    
                    from pycraft import MapGUI
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported MapGUI")

                    from pycraft import DataTransferUtils
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported DataTransferUtils")
                    
                    from pycraft import PycraftStartupTest
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported PycraftStartupTest")
                    
                    from pycraft import Settings
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported Settings")
                    
                    from pycraft import ShareDataUtils
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported ShareDataUtils")
                    
                    from pycraft import SoundUtils
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported SoundUtils")
                    
                    from pycraft import StartupAnimation
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported StartupAnimation")
                    
                    from pycraft import TextUtils
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported TextUtils")
                    
                    from pycraft import ThemeUtils
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported ThemeUtils")
                    
                    from pycraft import ThreadingUtils
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported ThreadingUtils")
                    
                    from pycraft import TkinterUtils
                    self.mod_logging_utils__.create_log_message.update_log_information(
                        self,
                        "Imported TkinterUtils")

                self.mod_achievements__ = Achievements
                self.mod_base__ = GLWindowUtils
                self.mod_benchmark__ = Benchmark
                self.mod_caption_utils__ = CaptionUtils
                self.mod_character_designer__ = CharacterDesigner
                self.mod_credits__ = Credits
                self.mod_data_transfer_utils__ = DataTransferUtils
                self.mod_display_utils__ = DisplayUtils
                self.mod_drawing_utils__ = DrawingUtils
                self.mod_extended_benchmark__ = ExtendedBenchmark
                self.mod_game_engine__ = pygame_game
                self.mod_game_engine_utils__ = GameEngineUtils
                self.mod_globals__ = ShareDataUtils
                self.mod_home_screen__ = HomeScreen
                self.mod_image_utils__ = ImageUtils
                self.mod_installer__ = Installer_main
                self.mod_integrated_installer__ = IntegratedInstaller
                self.mod_inventory__ = Inventory
                self.mod_joystick_utils__ = JoystickUtils
                self.mod_main__ = main
                self.mod_map_GUI__ = MapGUI
                self.mod_pycraft_startup_test__ = PycraftStartupTest
                self.mod_settings__ = Settings
                self.mod_sound_utils__ = SoundUtils
                self.mod_startup_animation__ = StartupAnimation
                self.mod_text_utils__ = TextUtils
                self.mod_theme_utils__ = ThemeUtils
                self.mod_threading_utils__ = ThreadingUtils
                self.mod_tkinter_utils__ = TkinterUtils
                
            except Exception as Message:
                self.error_message = "".join(("ModuleUtils > initialize_modules ",
                                              f"> initialize_internal_modules: {str(Message)}"))

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
