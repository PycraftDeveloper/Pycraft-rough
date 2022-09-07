if __name__ != "__main__":
    class create_game_engine:
        def __init__(self):
            import os
            if ("site-packages" in os.path.dirname(__file__) or
                    "dist-packages" in os.path.dirname(__file__)):
                try:
                    from pycraft import DataTransferUtils

                except:
                    import DataTransferUtils

            else:
                import DataTransferUtils

            self = DataTransferUtils.data_transfer.loadData()

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

            self.mod_logging_utils__.create_log_message.update_log_information(
                self, "Imported os")
            self.mod_logging_utils__.create_log_message.update_log_information(
                self, "Imported traceback")
            self.mod_logging_utils__.create_log_message.update_log_information(
                self, "Imported datetime")
            self.mod_logging_utils__.create_log_message.update_log_information(
                self, "Imported platform")
            self.mod_logging_utils__.create_log_message.update_log_information(
                self, "Imported json")
            self.mod_logging_utils__.create_log_message.update_log_information(
                self, "Imported pygame")
            self.mod_logging_utils__.create_log_message.update_log_information(
                self, "Imported pyautogui")
            self.mod_logging_utils__.create_log_message.update_log_information(
                self, "Imported random")

            self.mod_logging_utils__.create_log_message.update_log_information(
                self, "Imported ModuleUtils")
            self.mod_logging_utils__.create_log_message.update_log_information(
                self, "Imported LoggingUtils")
            self.mod_logging_utils__.create_log_message.update_log_information(
                self, "Imported ErrorUtils")
            self.mod_logging_utils__.create_log_message.update_log_information(
                self, "Imported FileUtils")
            self.mod_logging_utils__.create_log_message.update_log_information(
                self, "Imported Registry")

            self.mod_module_utils__.initialize_modules.initialize_external_modules(
                self)
            self.mod_module_utils__.initialize_modules.initialize_internal_modules(
                self)

            self.clock = self.mod_pygame__.time.Clock()
            self.fullscreen_x = self.mod_pyautogui__.size()[
                0]
            self.fullscreen_y = self.mod_pyautogui__.size()[
                1]
            self.mod_pygame__.init()

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

            self.mod_game_engine__.create_game_engine.main_game_engine(self)

        def main_game_engine(self):
            class GameEngine(self.mod_base__.CameraWindow):
                self.mod_base__.CameraWindow.title = f"Pycraft: v{self.version}: Playing"
                self.mod_base__.CameraWindow.resource_dir = self.base_folder
                self.mod_base__.CameraWindow.vsync = self.vsync
                self.mod_base__.CameraWindow.resizable = True
                self.mod_base__.CameraWindow.window_size = (
                    self.real_window_width,
                    self.real_window_height)

                if self.aa:
                    self.mod_base__.CameraWindow.samples = int(
                        str(self.aa_quality).split("x")[0])

                def __init__(self, **kwargs):
                    print("here")