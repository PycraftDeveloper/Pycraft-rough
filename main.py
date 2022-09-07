class Startup:
    def __init__(self):
        try:
            import os
            self.mod_OS__ = os

            import traceback
            self.mod_traceback__ = traceback

            import datetime
            self.mod_datetime__ = datetime

            import platform
            self.mod_platform__ = platform

            import json
            self.mod_json__ = json

            import pygame
            self.mod_pygame__ = pygame

            import pyautogui
            self.mod_pyautogui__ = pyautogui

            import random
            self.mod_random__ = random

            self.base_folder = self.mod_OS__.path.dirname(__file__)

            if ("site-packages" in self.base_folder or
                    "dist-packages" in self.base_folder):

                import ModuleUtils
                import LoggingUtils
                import ErrorUtils
                import FileUtils
                import Registry

            else:
                from pycraft import ModuleUtils
                from pycraft import LoggingUtils
                from pycraft import ErrorUtils
                from pycraft import FileUtils
                from pycraft import Registry
            
            self.mod_module_utils__ = ModuleUtils
            self.mod_logging_utils__ = LoggingUtils
            self.mod_error_utils__ = ErrorUtils
            self.mod_file_utils__ = FileUtils
            self.mod_registry__ = Registry

            self.platform = self.mod_platform__.system()

            self.mod_registry__.generate_registry.registry(self)

            try:

                self.mod_file_utils__.pycraft_config_utils.read_input_key(
                    self)

            except Exception as Message:
                self.mod_file_utils__.pycraft_config_utils.RepairLostSave(
                    self)
                ErrorString = "".join(("Unable to access saved data, we have attempted ",
                                            f"to repair the missing data, please try again\n\n{Message}"))
                self.error_message = f"main: {ErrorString}"
                self.mod_error_utils__.generate_error_screen.error_screen(
                    self)

            try:
                
                self.mod_file_utils__.pycraft_config_utils.ReadMainSave(
                    self)
                
            except Exception as Message:
                self.mod_file_utils__.pycraft_config_utils.RepairLostSave(
                    self)
                ErrorString = "".join(("Unable to access saved data, we have attempted ",
                                            f"to repair the missing data, please try again\n\n{Message}"))
                self.error_message = f"main: {ErrorString}"
                self.mod_error_utils__.generate_error_screen.error_screen(
                    self)

            self.mod_logging_utils__.log_file.clear_log(self)

            self.mod_logging_utils__.create_log_message.update_log_information(self, "Loaded <Pycraft_main>")
            self.mod_logging_utils__.create_log_message.update_log_information(self, "Started <Pycraft_main>")
            
            self.mod_logging_utils__.create_log_message.update_log_information(self, "Imported os")
            self.mod_logging_utils__.create_log_message.update_log_information(self, "Imported traceback")
            self.mod_logging_utils__.create_log_message.update_log_information(self, "Imported datetime")
            self.mod_logging_utils__.create_log_message.update_log_information(self, "Imported platform")
            self.mod_logging_utils__.create_log_message.update_log_information(self, "Imported json")
            self.mod_logging_utils__.create_log_message.update_log_information(self, "Imported pygame")
            self.mod_logging_utils__.create_log_message.update_log_information(self, "Imported pyautogui")
            self.mod_logging_utils__.create_log_message.update_log_information(self, "Imported random")
            
            self.mod_logging_utils__.create_log_message.update_log_information(self, "Imported ModuleUtils")
            self.mod_logging_utils__.create_log_message.update_log_information(self, "Imported LoggingUtils")
            self.mod_logging_utils__.create_log_message.update_log_information(self, "Imported ErrorUtils")
            self.mod_logging_utils__.create_log_message.update_log_information(self, "Imported FileUtils")
            self.mod_logging_utils__.create_log_message.update_log_information(self, "Imported Registry")

            self.mod_module_utils__.initialize_modules.initialize_external_modules(self)

            self.mod_urllib_request_ = None

            self.mod_ModernGL__.create_standalone_context()

            self.mod_OS__.environ["SDL_VIDEO_CENTERED"] = "1"

            self.mod_pygame__.init()

            self.mod_module_utils__.initialize_modules.initialize_internal_modules(self)

            if self.platform == "Linux":
                self.title_font = self.mod_pygame__.font.Font(
                    self.mod_OS__.path.join(
                        self.base_folder,
                        ("fonts//Book Antiqua.ttf")), 60)

                self.window_icon = self.mod_pygame__.image.load(
                    self.mod_OS__.path.join(
                        self.base_folder,
                        ("resources//general resources//Icon.png")))

            else:
                self.window_icon = self.mod_pygame__.image.load(
                    self.mod_OS__.path.join(
                        self.base_folder,
                        ("resources\\general resources\\Icon.png")))

                self.title_font = self.mod_pygame__.font.Font(
                    self.mod_OS__.path.join(
                        self.base_folder,
                        ("fonts\\Book Antiqua.ttf")), 60)

            # Will remove all FPS limits in game, no way to set to 'True' in game for now.
            # False by default!

            if self.FPS_overclock:
                input("".join(("You are entering an unlimited FPS mode; ",
                               "press enter to continue at your own risk.")))

            general_thread = self.mod_threading_utils__.ThreadingUtils.general_threading_utility
            self.thread_pycraft_general = self.mod_threading__.Thread(
                target=general_thread,
                args=(self,))
            self.thread_pycraft_general.daemon = True
            self.thread_pycraft_general.start()
            self.thread_pycraft_general.name = "thread_pycraft_general"

            JoystickEventTarget = self.mod_joystick_utils__.establish_joystick_connection.joystick_events
            self.thread_joystick_events = self.mod_threading__.Thread(
                target=JoystickEventTarget,
                args=(self,))
            self.thread_joystick_events.daemon = True
            self.thread_joystick_events.start()
            self.thread_joystick_events.name = "thread_joystick_events"

            JoystickIOtarget = self.mod_joystick_utils__.establish_joystick_removed.JoystickRemoved
            self.thread_joystick_removed = self.mod_threading__.Thread(
                target=JoystickIOtarget,
                args=(self,))
            self.thread_joystick_removed.daemon = True
            self.thread_joystick_removed.start()
            self.thread_joystick_removed.name = "thread_joystick_removed"

            self.mod_data_transfer_utils__.data_transfer.store_data(self)
            
        except Exception as Message:
            try:
                import sys
                import tkinter as tk
                from tkinter import messagebox
                root = tk.Tk()
                root.withdraw()
                messagebox.showerror(
                    "Startup Fail",
                    str(Message))
                sys.exit()
                
            except Exception as Message:
                print(Message)
                sys.exit()


class Initialize:
    def menu_selector(self):
        try:
            while True:
                if self.mod_pygame__.mixer.Channel(1).get_busy() == 1:
                    self.mod_pygame__.mixer.Channel(1).stop()
                if self.mod_pygame__.mixer.Channel(2).get_busy() == 1:
                    self.mod_pygame__.mixer.Channel(2).stop()
                if self.mod_pygame__.mixer.Channel(3).get_busy() == 1:
                    self.mod_pygame__.mixer.Channel(3).stop()
                if self.mod_pygame__.mixer.Channel(4).get_busy() == 1:
                    self.mod_pygame__.mixer.Channel(4).stop()
                if self.mod_pygame__.mixer.music.get_busy() == 0:
                    self.mod_pygame__.mixer.music.unpause()

                self.mouse_x = self.real_window_width/2
                self.mouse_y = self.real_window_height/2
                self.startup_animation = True
                self.run_timer = 0
                self.go_to = None
                self.mouse_button_down = False

                if self.command == "saveANDexit":
                    self.mod_file_utils__.pycraft_config_utils.save_pycraft_config(
                        self)
                    if self.error_message is not None:
                        self.mod_error_utils__.generate_error_screen.error_screen(
                            self)

                    self.mod_pygame__.quit()
                    self.mod_sys__.exit()

                    continue

                elif self.command == "Credits":
                    self.mod_credits__.GenerateCredits.Credits(
                        self)
                    self.command = "Undefined"
                    continue

                elif self.command == "Achievements":
                    self.mod_achievements__.generate_achievements.Achievements(
                        self)
                    self.command = "Undefined"

                elif self.command == "CharacterDesigner":
                    self.mod_character_designer__.GenerateCharacterDesigner.CharacterDesigner(
                        self)
                    self.command = "Undefined"
                    continue

                elif self.command == "Settings":
                    self.mod_settings__.generate_settings.Settings(
                        self)
                    self.command = "Undefined"
                    continue

                elif self.command == "Benchmark":
                    self.mod_benchmark__.generate_benchmark.Benchmark(
                        self)
                    self.command = "Undefined"
                    continue
 
                elif self.command == "Play":
                    #from line_profiler import LineProfiler
                    self.mod_game_engine__.create_game_engine.game_engine(self)
                    #lp = LineProfiler()
                    #lp_wrapper = lp(self.mod_game_engine__.create_game_engine.game_engine)
                    #lp_wrapper(self)
                    #lp.print_stats()
                    self.command = "Undefined"
                    self.mod_display_utils__.display_utils.set_display(
                        self)
                    continue

                elif self.command == "Inventory":
                    self.mod_inventory__.GenerateInventory.Inventory(
                        self)
                    self.command = "Play"
                    continue

                elif self.command == "MapGUI":
                    self.mod_map_GUI__.GenerateMapGUI.MapGUI(
                        self)
                    self.command = "Play"
                    continue

                elif self.command == "Installer":
                    self.mod_pygame__.quit()
                    self.mod_installer__.RunInstaller.Initialize()
                    self.mod_sys__.exit()

                elif self.error_message is not None:
                    self.mod_error_utils__.generate_error_screen.error_screen(
                        self)
                    continue

                else:
                    self.command = "Undefined"
                    self.command = self.mod_home_screen__.GenerateHomeScreen.Home_Screen(
                        self)
                    continue
                
        except Exception as Message:
            print(Message)
            self.error_message = "".join(("main > Initialize > ",
                                         f"menu_selector: {str(Message)}"))

            self.error_message_detailed = "".join(
                self.mod_traceback__.format_exception(
                    None,
                    Message,
                    Message.__traceback__))

            self.mod_error_utils__.generate_error_screen.error_screen(
                self)

    def Start():
        try:
            global self
            self = Startup()

            self.mod_file_utils__.FixInstaller.Getinstall_location(
                self)
            if self.install_location is None:
                self.mod_file_utils__.FixInstaller.Setinstall_location(
                    self)

            AdaptiveTarget = self.mod_threading_utils__.ThreadingUtils.AdaptiveMode
            self.thread_adaptive_mode = self.mod_threading__.Thread(
                target=AdaptiveTarget,
                args=(self,))
            self.thread_adaptive_mode.daemon = True
            self.thread_adaptive_mode.start()
            self.thread_adaptive_mode.name = "thread_adaptive_mode"

            if self.connection_permission is None:
                permission_message = "Can we have your permission to check the internet for updates to Pycraft?"
                self.connection_permission = self.mod_tkinter_utils__.TkinterInfo.GetPermissions(
                    self,
                    permission_message)

            if self.remove_file_permission is None:
                permission_message = "Can we have your permission to send files from the Pycraft directory to the recycle bin?"
                self.remove_file_permission = self.mod_tkinter_utils__.TkinterInfo.GetPermissions(
                    self,
                    permission_message)

            if self.show_strobe_effects is None:
                self.show_strobe_effects = self.mod_tkinter_messagebox_.askquestion(
                    "Check Permission",
                    "".join(("Strobe effects and bright flashes of light can ",
                                "cause discomfort, (for example lightning), you can choose here ",
                                "whether to enable or disable those ",
                                "strobe effects in Pycraft.\n\n",
                                "Click 'yes' to allow for strobe effects, or 'no' ",
                                "to turn them off. You can always adjust this in ",
                                "Pycraft's settings, under 'Storage and permissions'.")))

                if self.show_strobe_effects == "yes":
                    self.show_strobe_effects = True

                else:
                    self.show_strobe_effects = False

            if (self.current_date != self.last_run or
                    self.crash):
                self.get_outdated = [False, True]
                
                if self.connection_permission:
                    import urllib.request
                    self.mod_urllib_request_ = urllib.request
                    self.connection_status = self.mod_integrated_installer__.CheckConnection.test(
                        self)

                    if self.connection_status:
                        self.Thread_Get_outdated = self.mod_threading__.Thread(
                            target=self.mod_integrated_installer__.IntegInstaller.CheckVersions,
                            args=(self,))

                        self.Thread_Get_outdated.daemon = True
                        self.Thread_Get_outdated.start()
                        self.Thread_Get_outdated.name = "Thread_Get_outdated"

            self.mod_display_utils__.display_utils.set_display(
                self)
            
            if self.error_message is not None:
                self.mod_error_utils__.generate_error_screen.error_screen(
                    self)

            if self.platform == "Windows":
                import win32api

                settings = win32api.EnumDisplaySettings(
                    win32api.EnumDisplayDevices().DeviceName,
                    -1)
                
                self.vsync_FPS = getattr(
                    settings,
                    'DisplayFrequency')
                
            else:
                self.vsync_FPS = 60

            self.mod_pycraft_startup_test__.StartupTest.PycraftSelfTest(
                self)
            
            if self.error_message is not None:
                self.mod_error_utils__.generate_error_screen.error_screen(
                    self)

            self.mod_pygame__.mouse.set_visible(False)
            self.mod_startup_animation__.GenerateStartupScreen.Start(
                self)
            self.mod_pygame__.mouse.set_visible(True)

            if self.error_message is not None:
                self.mod_error_utils__.generate_error_screen.error_screen(
                    self)

            if self.theme is False:
                self.mod_theme_utils__.determine_theme_colours.get_theme_GUI(
                    self)
                
                if self.error_message is not None:
                    self.mod_error_utils__.generate_error_screen.error_screen(
                        self)

            self.mod_theme_utils__.determine_theme_colours.get_colors(
                self)
            if self.error_message is not None:
                self.mod_error_utils__.generate_error_screen.error_screen(
                    self)

            Initialize.menu_selector(self)
            
        except Exception as Message:
            self.error_message = "".join(("main > Initialize ",
                                            f"> Start: {str(Message)}"))

            self.error_message_detailed = "".join(
                self.mod_traceback__.format_exception(
                    None,
                    Message,
                    Message.__traceback__))

            self.mod_error_utils__.generate_error_screen.error_screen(self)


if __name__ == "__main__":
    import sys
    try:
        import psutil
        
    except Exception as Message:
        import tkinter as tk
        from tkinter import messagebox
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror(
            "Startup Fail",
            str(Message))

        sys.exit()
    else:
        try:
            counter = 0
            for proc in psutil.process_iter(["pid", "name", "username"]):
                if "pycraft.exe" in str(proc.info["name"]).lower():
                    counter += 1

            if counter >= 2:
                sys.exit()

            Initialize.Start()
            
        except Exception as Message:
            import tkinter as tk
            from tkinter import messagebox
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror(
                "Startup Fail",
                str(Message))

            sys.exit()

def QueryVersion():
    return "pycraft v0.9.6-2.5"


def start():
    Initialize.Start()
