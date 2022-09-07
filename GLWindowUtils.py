if __name__ != "__main__":
    import moderngl_window as mglw

    class BenchmarkWindow(mglw.WindowConfig):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.camera = self.mod_ModernGL_window_keyboard_camera(
                self.wnd.keys,
                aspect_ratio=self.wnd.aspect_ratio)

            self.camera_enabled = True

        def key_event(self, key, action, modifiers):
            try:
                keys = self.wnd.keys


                if action == keys.ACTION_PRESS:
                    self.wnd.close()
                    self.wnd.destroy()
                    
            except Exception as Message:
                try:
                    import traceback
                    if ("site-packages" in self.base_folder or
                            "dist-packages" in self.base_folder):

                        import ErrorUtils

                    else:
                        from pycraft import ErrorUtils

                except Exception as Message_2:
                    print(Message)
                    print(Message_2)
                    
                self.wnd.close()
                self.error_message = "".join(("GLWindowUtils > BenchmarkWindow ",
                                                        f"> key_event: {str(Message)}"))

                self.error_message_detailed = "".join(
                    traceback.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                ErrorUtils.generate_error_screen.error_screen(
                    self)

        def close(self):
            try:
                self.command = "Undefined"
                self.iteration = 7500
                
            except Exception as Message:
                try:
                    import traceback
                    if ("site-packages" in self.base_folder or
                            "dist-packages" in self.base_folder):

                        import ErrorUtils

                    else:
                        from pycraft import ErrorUtils

                except Exception as Message_2:
                    print(Message_2)
                    print(Message)
                    
                self.error_message = "GLWindowUtils > BenchmarkWindow > close: " + \
                    str(Message)

                self.error_message_detailed = "".join(
                    traceback.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                ErrorUtils.generate_error_screen.error_screen(
                    self)

    class CameraWindow(mglw.WindowConfig):
        def __init__(self, **kwargs):
            import os
            self.mod_OS__ = os
            
            self.base_folder = self.mod_OS__.path.dirname(__file__)
            
            if ("site-packages" in self.base_folder or
                    "dist-packages" in self.base_folder):

                import GameEngineUtils

            else:

                from pycraft import GameEngineUtils

            GameEngineUtils.create_game_engine_context.load_data_and_initialize(
                self)
            
            super().__init__(**kwargs)
            
            self.camera = self.mod_ModernGL_window_keyboard_camera(
                self.wnd.keys,
                aspect_ratio=self.wnd.aspect_ratio)

            self.camera_enabled = True

        def key_event(self, key, action, modifiers):
            try:
                keys = self.wnd.keys

                if self.camera_enabled:
                    CurrentRunTime = self.mod_time__.perf_counter()
                                        
                    if key == self.input_key[self.input_configuration["keyboard"]["Walk right"]][1]:
                        if action == keys.ACTION_PRESS:
                            self.camera.key_input(
                                keys.D,
                                keys.ACTION_PRESS,
                                modifiers)

                            self.Dkeydowntimer_start = CurrentRunTime
                            self.Dkeydown = True

                        elif action == keys.ACTION_RELEASE:
                            self.camera.key_input(
                                keys.D,
                                keys.ACTION_RELEASE,
                                modifiers)

                            self.Dkeydown = False

                    if key == self.input_key[self.input_configuration["keyboard"]["Walk left"]][1]:
                        if action == keys.ACTION_PRESS:
                            self.camera.key_input(
                                keys.A,
                                keys.ACTION_PRESS,
                                modifiers)

                            self.Akeydowntimer_start = CurrentRunTime
                            self.Akeydown = True

                        elif action == keys.ACTION_RELEASE:
                            self.camera.key_input(
                                keys.A,
                                keys.ACTION_RELEASE,
                                modifiers)

                            self.Akeydown = False

                    if key == self.input_key[self.input_configuration["keyboard"]["Walk forwards"]][1]:
                        if action == keys.ACTION_PRESS:
                            self.camera.key_input(
                                keys.W,
                                keys.ACTION_PRESS,
                                modifiers)

                            self.RunForwardtimer = True
                            self.Wkeydown = True

                            self.RunForwardtimer_start = CurrentRunTime
                            self.RunForwardtimer_start_sound = CurrentRunTime

                        elif action == keys.ACTION_RELEASE:
                            self.camera.key_input(
                                keys.W,
                                keys.ACTION_RELEASE,
                                modifiers)

                            self.RunForwardtimer = False
                            self.Wkeydown = False

                    if key == self.input_key[self.input_configuration["keyboard"]["Walk backwards"]][1]:
                        if action == keys.ACTION_PRESS:
                            self.camera.key_input(
                                keys.S,
                                keys.ACTION_PRESS,
                                modifiers)

                            self.Skeydown = True
                            self.Skeydowntimer_start = CurrentRunTime

                        elif action == keys.ACTION_RELEASE:
                            self.camera.key_input(
                                keys.S,
                                keys.ACTION_RELEASE,
                                modifiers)

                            self.Skeydown = False

                if action == keys.ACTION_PRESS:
                    if key == self.input_key[self.input_configuration["keyboard"]["Unlock mouse"]][1]:
                        self.camera_enabled = not self.camera_enabled
                        self.wnd.mouse_exclusivity = self.camera_enabled
                        self.wnd.cursor = not self.camera_enabled
                    
                    elif key == self.input_key[self.input_configuration["keyboard"]["Jump"]][1] and self.Jump is False:
                        self.space_key_pressed = True

                    elif key == self.input_key[self.input_configuration["keyboard"]["Skip time"]][1] and self.skip_time:
                        self.time += 30
                        self.GameTime += 30
                        self.WeatherTime += 30

                    elif key == self.input_key[self.input_configuration["keyboard"]["Increase speed"]][1] and self.increased_speed:
                        self.IKeyPressed = True

                    elif key == self.input_key[self.input_configuration["keyboard"]["List variables"]][1] and self.extended_developer_options:
                        self.mod_tkinter_utils__.TkinterInfo.CreateTkinterWindow(
                            self)

                    elif key == self.input_key[self.input_configuration["keyboard"]["Open inventory"]][1]:
                        self.Inventory = True

                    elif key == self.input_key[self.input_configuration["keyboard"]["Open map"]][1]:
                        self.Map = True

                elif action == keys.ACTION_RELEASE:
                    self.IKeyPressed = False
                    self.space_key_pressed = False
                    
            except Exception as Message:
                try:
                    import traceback
                    if ("site-packages" in self.base_folder or
                            "dist-packages" in self.base_folder):

                        import ErrorUtils

                    else:
                        from pycraft import ErrorUtils

                except Exception as Message_2:
                    print(Message_2)
                    print(Message)
                    
                self.wnd.close()
                self.error_message = "".join(("GLWindowUtils > CameraWindow ",
                                                        f"> key_event: {str(Message)}"))

                self.error_message_detailed = "".join(
                    traceback.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                ErrorUtils.generate_error_screen.error_screen(
                    self)

        def mouse_position_event(self, x: int, y: int, dx, dy):
            try:
                if self.camera_enabled:
                    self.camera.rot_state(
                        -dx,
                        -dy)
                    
            except Exception as Message:
                try:
                    import traceback
                    if ("site-packages" in self.base_folder or
                            "dist-packages" in self.base_folder):

                        import ErrorUtils

                    else:
                        from pycraft import ErrorUtils

                except Exception as Message_2:
                    print(Message_2)
                    print(Message)
                    
                self.error_message = "".join(("GLWindowUtils > CameraWindow > ",
                                                        f"mouse_position_event: {str(Message)}"))

                self.error_message_detailed = "".join(
                    traceback.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                ErrorUtils.generate_error_screen.error_screen(self)

        def mouse_scroll_event(self, x_offset: float, y_offset: float):
            try:
                if self.skip_time:
                    self.time += y_offset*2
                    self.GameTime += y_offset*2
                    #if self.weather != "rain.heavy.thundery":
                    self.WeatherTime += y_offset*2
                    #if self.weather == "rain.heavy.thundery":
                    #self.Thundertimer += y_offset*2
                    
            except Exception as Message:
                try:
                    import traceback
                    if ("site-packages" in self.base_folder or
                            "dist-packages" in self.base_folder):

                        import ErrorUtils

                    else:
                        from pycraft import ErrorUtils

                except Exception as Message_2:
                    print(Message_2)
                    print(Message)
                    
                self.error_message = "".join(("GLWindowUtils > CameraWindow ",
                                              f"> mouse_scroll_event: {str(Message)}"))

                self.error_message_detailed = "".join(
                    traceback.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                ErrorUtils.generate_error_screen.error_screen(self)

        def resize(self, width: int, height: int):
            try:
                self.fullscreen = not self.wnd.fullscreen
                self.real_window_width, self.real_window_height = self.window_size
                self.camera.projection.update(aspect_ratio=self.wnd.aspect_ratio)
                
            except Exception as Message:
                try:
                    import traceback
                    if ("site-packages" in self.base_folder or
                            "dist-packages" in self.base_folder):

                        import ErrorUtils

                    else:
                        from pycraft import ErrorUtils

                except Exception as Message_2:
                    print(Message_2)
                    print(Message)
                    
                self.error_message = "".join(("GLWindowUtils > CameraWindow > ",
                                                        f"resize: {str(Message)}"))

                self.error_message_detailed = "".join(
                    traceback.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                ErrorUtils.generate_error_screen.error_screen(self)

        def close(self):
            try:
                self.command = "Undefined"
                self.Running = False

                import os
                if ("site-packages" in os.path.dirname(__file__) or
                        "dist-packages" in os.path.dirname(__file__)):

                    import DataTransferUtils

                else:
                    from pycraft import DataTransferUtils

                DataTransferUtils.data_transfer.store_data(self)

                super().close()
                
            except Exception as Message:
                print(Message)
                try:
                    import traceback
                    if ("site-packages" in self.base_folder or
                            "dist-packages" in self.base_folder):

                        import ErrorUtils

                    else:
                        from pycraft import ErrorUtils

                except Exception as Message_2:
                    print(Message_2)
                    print(Message)
                    
                self.error_message = "GLWindowUtils > CameraWindow > close: "+str(Message)

                self.error_message_detailed = "".join(
                    traceback.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                ErrorUtils.generate_error_screen.error_screen(self)

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
