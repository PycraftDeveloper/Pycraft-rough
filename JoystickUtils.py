if __name__ != "__main__":
    class establish_joystick_removed:
        def __init__(self):
            pass

        def JoystickRemoved(self):
            while True:
                try:
                    if self.mod_pygame__.init():
                        if (self.mod_pygame__.joystick.get_count() == 0 and
                                self.pygame_device_removed_update is False and
                                self.joystick_connected):

                            self.pygame_device_removed_update = True
                            self.device_connected = False
                            self.device_connected_update = True
                            self.pygame_device_added_update = False

                        elif (self.mod_pygame__.joystick.get_count() >= 1 and
                                self.pygame_device_added_update is False):

                            self.device_connected = True
                            self.device_connected_update = True
                            self.DeviceRemoved_Update = True
                            self.pygame_device_added_update = True
                            self.pygame_device_removed_update = False
                            self.joystick_connected = True
                            
                except Exception as Message:
                    log_message = "JoystickUtils > establish_joystick_connection > JoystickRemoved: " + \
                        str(Message)

                    self.mod_logging_utils__.create_log_message.update_log_warning(
                        self,
                        log_message)

                finally:
                    self.mod_time__.sleep(1)

            self.mod_logging_utils__.create_log_message.update_log_information(
                self,
                "'thread_joystick_removed' has stopped")


    class establish_joystick_connection:
        def __init__(self):
            pass

        def joystick_events(self):
            def print_add(joy):
                pass

            def print_remove(joy):
                pass

            def key_received(key):
                import os
                if ("site-packages" in os.path.dirname(__file__) or
                        "dist-packages" in os.path.dirname(__file__)):
                    try:
                        from pycraft.ShareDataUtils import game_shared_data
                        
                    except:
                        from ShareDataUtils import game_shared_data
                        
                else:
                    from ShareDataUtils import game_shared_data

                try:
                    if self.use_mouse_input is False:
                        if self.command == "Play":
                            if "Button" in str(key) or "Hat" in str(key):
                                if "Button 3" in str(key) and game_shared_data.Jump is False:
                                    game_shared_data.Jump = True
                                    game_shared_data.jump_timer = game_shared_data.shared_data.mod_time__.perf_counter()
                                    game_shared_data.StartYposition = game_shared_data.camera.position.y

                                if "Hat" in str(key):
                                    game_shared_data.shared_data.mod_base__.CameraWindow.close(
                                        game_shared_data)

                                else:
                                    if "Button 7" in str(key):
                                        game_shared_data.shared_data.mod_base__.CameraWindow.key_event(
                                            game_shared_data,
                                            game_shared_data.wnd.keys.E,
                                            game_shared_data.wnd.keys.ACTION_PRESS,
                                            None)

                                    if "Button 6" in str(key):
                                        game_shared_data.shared_data.mod_base__.CameraWindow.key_event(
                                            game_shared_data,
                                            game_shared_data.wnd.keys.R,
                                            game_shared_data.wnd.keys.ACTION_PRESS,
                                            None)

                            if "Axis" in str(key):
                                if "Axis 3" in str(key):
                                    Axis3value = self.mod_pyjoystick__.Key.get_value(key)
                                    game_shared_data.Joystick_Rotation[0] = Axis3value

                                if "Axis 4" in str(key):
                                    Axis4value = self.mod_pyjoystick__.Key.get_value(key)
                                    game_shared_data.Joystick_Rotation[1] = Axis4value

                                if "Axis 1" in str(key):
                                    try:
                                        if self.mod_pyjoystick__.Key.get_value(key) < -0.25:
                                            game_shared_data.shared_data.mod_base__.CameraWindow.key_event(
                                                game_shared_data,
                                                game_shared_data.wnd.keys.W,
                                                game_shared_data.wnd.keys.ACTION_PRESS,
                                                None)

                                        else:
                                            game_shared_data.shared_data.mod_base__.CameraWindow.key_event(
                                                game_shared_data,
                                                game_shared_data.wnd.keys.W,
                                                game_shared_data.wnd.keys.ACTION_RELEASE,
                                                None)

                                        if self.mod_pyjoystick__.Key.get_value(key) > 0.25:
                                            game_shared_data.shared_data.mod_base__.CameraWindow.key_event(
                                                game_shared_data,
                                                game_shared_data.wnd.keys.S,
                                                game_shared_data.wnd.keys.ACTION_PRESS,
                                                None)

                                        else:
                                            game_shared_data.shared_data.mod_base__.CameraWindow.key_event(
                                                game_shared_data,
                                                game_shared_data.wnd.keys.S,
                                                game_shared_data.wnd.keys.ACTION_RELEASE,
                                                None)
                                            
                                    except Exception as Message:
                                        log_message = "JoystickUtils > establish_joystick_connection > joystick_events > key_received: "+str(Message)
                                        
                                        self.mod_logging_utils__.create_log_message.update_log_warning(
                                            self,
                                            log_message)

                                if "Axis 0" in str(key):
                                    try:
                                        if self.mod_pyjoystick__.Key.get_value(key) < -0.25:
                                            game_shared_data.shared_data.mod_base__.CameraWindow.key_event(
                                                game_shared_data,
                                                game_shared_data.wnd.keys.A,
                                                game_shared_data.wnd.keys.ACTION_PRESS,
                                                None)

                                        else:
                                            game_shared_data.shared_data.mod_base__.CameraWindow.key_event(
                                                game_shared_data,
                                                game_shared_data.wnd.keys.A,
                                                game_shared_data.wnd.keys.ACTION_RELEASE,
                                                None)

                                        if self.mod_pyjoystick__.Key.get_value(key) > 0.25:
                                            game_shared_data.shared_data.mod_base__.CameraWindow.key_event(
                                                game_shared_data,
                                                game_shared_data.wnd.keys.D,
                                                game_shared_data.wnd.keys.ACTION_PRESS,
                                                None)

                                        else:
                                            game_shared_data.shared_data.mod_base__.CameraWindow.key_event(
                                                game_shared_data,
                                                game_shared_data.wnd.keys.D,
                                                game_shared_data.wnd.keys.ACTION_RELEASE,
                                                None)
                                            
                                    except Exception as Message:
                                        log_message = "JoystickUtils > establish_joystick_connection > joystick_events > key_received: " + \
                                            str(Message)

                                        self.mod_logging_utils__.create_log_message.update_log_warning(
                                            self,
                                            log_message)
                                        
                except Exception as Message:
                    self.error_message = "".join(("JoystickUtils > establish_joystick_connection ",
                                                 "> joystick_events > ",
                                                 f"key_received: {str(Message)}"))

                    self.error_message_detailed = "".join(
                        self.mod_traceback__.format_exception(
                            None,
                            Message,
                            Message.__traceback__))

                    self.mod_error_utils__.generate_error_screen.error_screen(self)
            try:
                while True:
                    pass
                    #self.mod_pyjoystick_run_event_loop_(print_add, print_remove, key_received)
                    
            except Exception as Message:
                self.error_message = "".join(("JoystickUtils > establish_joystick_connection > ",
                                             f"joystick_events: {str(Message)}"))

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
