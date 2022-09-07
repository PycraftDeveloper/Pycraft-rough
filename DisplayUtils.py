if __name__ != "__main__":
    class display_functionality:
        def __init__(self):
            pass

        def core_display_functions(self, location="Home", checkEvents=True, resize=True, return_events=False, disable_events=False):
            try:
                if self.use_mouse_input is False:
                    self.mod_pygame__.joystick.init()
                    joystick_count = self.mod_pygame__.joystick.get_count()
                    for i in range(joystick_count):
                        joystick = self.mod_pygame__.joystick.Joystick(i)
                        axes = joystick.get_numaxes()
                        
                        for j in range(axes):
                            multiplier = ((60 * 4) / (self.aFPS / self.iteration))
                            axis = round(joystick.get_axis(j), 6) * multiplier
                            
                            print(axis, j)

                            if j == 0:
                                self.mouse_x += axis * self.x_scale_factor
                            if j == 1:
                                self.mouse_y += axis * self.y_scale_factor

                        buttons = joystick.get_numbuttons()

                        for j in range(buttons):
                            button = joystick.get_button(j)

                            if j == 1:
                                if (button == 1 and
                                        self.go_to is None):
                                    self.mouse_button_down = True
                                
                                else:
                                    self.mouse_button_down = False

                            if j == 0:
                                if (button == 1 and self.go_to is None):
                                    self.joystick_exit = True

                                else:
                                    self.joystick_exit = False

                        hats = joystick.get_numhats()
                        
                        for j in range(hats):
                            hat = joystick.get_hat(j)
                            for k in range(len(hat)):
                                if int(hat[k]) == 1:
                                    if self.joystick_hat_pressed is False:
                                        self.joystick_hat_pressed = True

                                if k == 0:
                                    if int(hat[k]) == 1:
                                        self.joystick_zoom = "+"
                                    if int(hat[k]) == -1:
                                        self.joystick_zoom = "-"

                    if self.window_in_focus:
                        self.mod_pygame__.mouse.set_pos(
                            self.mouse_x,
                            self.mouse_y)
                else:
                    self.mouse_x = self.mod_pygame__.mouse.get_pos()[0]
                    self.mouse_y = self.mod_pygame__.mouse.get_pos()[1]

                self.real_window_width = self.mod_pygame__.display.get_window_size()[0]
                self.real_window_height = self.mod_pygame__.display.get_window_size()[1]

                if self.saved_window_width < 1280:
                    self.mod_display_utils__.display_utils.generate_min_display(
                        self,
                        1280,
                        self.saved_window_height)

                if self.saved_window_height < 720:
                    self.mod_display_utils__.display_utils.generate_min_display(
                        self,
                        self.saved_window_width,
                        720)

                if self.saved_window_width == self.fullscreen_x:
                    self.saved_window_width = 1280

                if self.saved_window_height == self.fullscreen_y:
                    self.saved_window_height = 720

                if not (self.real_window_width == self.fullscreen_x or
                        self.real_window_height == self.fullscreen_y):
                    
                    self.saved_window_width = self.mod_pygame__.display.get_window_size()[0]
                    self.saved_window_height = self.mod_pygame__.display.get_window_size()[1]

                if self.iteration > 1000:
                    self.aFPS = (self.aFPS/self.iteration)
                    self.iteration = 1
                    
                self.eFPS = self.clock.get_fps()
                self.aFPS += self.eFPS
                self.iteration += 1

                self.y_scale_factor = self.real_window_height/720
                self.x_scale_factor = self.real_window_width/1280

                if self.use_mouse_input is False:
                    if self.joystick_exit:
                        self.joystick_exit = False
                        if self.sound:
                            self.mod_sound_utils__.play_sound.play_click_sound(self)

                        if location == "exit":
                            self.mod_pygame__.quit()
                            self.mod_sys__.exit()

                        else:
                            self.startup_animation = True
                            self.run_timer = 0
                            self.go_to = location

                if checkEvents:
                    try:
                        displayEvents = self.mod_pygame__.event.get()
                        
                    except Exception as Message:
                        joystick_fix = "<built-in function get> returned a result with an exception set"
                        if str(Message) == joystick_fix:
                            displayEvents = []
                        else:
                            self.mod_logging_utils__.create_log_message.update_log_warning(
                                self,
                                Message)
                            
                    for event in displayEvents:
                        if (((event.type == self.mod_pygame__.QUIT
                                or (event.type == self.mod_pygame__.KEYDOWN
                                    and event.key == self.input_key[self.input_configuration["keyboard"]["Back"]][0])) and
                                self.go_to is None and
                                disable_events is False)):

                            self.joystick_exit = False

                            if self.sound:
                                self.mod_sound_utils__.play_sound.play_click_sound(self)

                            if location == "exit":
                                self.mod_pygame__.quit()
                                self.mod_sys__.exit()
                                
                            else:
                                self.startup_animation = True
                                self.run_timer = 0
                                self.go_to = location

                        if event.type == self.mod_pygame__.WINDOWFOCUSLOST:
                            self.window_in_focus = False
                        elif event.type == self.mod_pygame__.WINDOWFOCUSGAINED:
                            self.window_in_focus = True

                        if self.use_mouse_input:
                            if (event.type == self.mod_pygame__.KEYDOWN and
                                    disable_events is False):
                                
                                if (event.key == self.input_key[self.input_configuration["keyboard"]["List variables"]][0] and
                                        self.extended_developer_options):
                                    
                                    self.mod_tkinter_utils__.TkinterInfo.CreateTkinterWindow(
                                        self)
                                    
                                if (event.key == self.input_key[self.input_configuration["keyboard"]["Toggle full-screen"]][0] and
                                        resize):
                                    
                                    self.mod_display_utils__.display_utils.update_display(self)

                                if event.key == self.input_key[self.input_configuration["keyboard"]["Confirm"]][0]:
                                    self.mouse_button_down = True

                            elif (((event.type == self.mod_pygame__.MOUSEBUTTONDOWN or
                                        self.mod_pygame__.mouse.get_pressed()[0]) and
                                    (not event.type == self.mod_pygame__.MOUSEMOTION)) and
                                        self.go_to is None):

                                self.mouse_button_down = True

                            else:
                                self.mouse_button_down = False

                    if return_events:
                        return displayEvents
                    
            except Exception as Message:
                self.error_message = (
                    f"DisplayUtils > display_functionality > core_display_functions: {str(Message)}")

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)


    class display_utils:
        def __init__(self):
            pass

        def update_display(self):
            try:
                self.data_aFPS = []
                self.data_CPU_usage = []
                self.data_eFPS = []
                self.data_memory_usage = []

                self.timer = 0

                self.data_aFPS_Max = 1
                self.data_CPU_usage_Max = 1
                self.data_eFPS_Max = 1
                self.data_memory_usage_Max = 1

                try:
                    self.fullscreen_x = self.mod_pyautogui__.size()[0]
                    self.fullscreen_y = self.mod_pyautogui__.size()[1]

                    self.mod_pygame__.display.set_icon(self.window_icon)

                    if self.fullscreen is False:
                        self.fullscreen = True
                        if self.vsync:
                            self.display = self.mod_pygame__.display.set_mode(
                                (self.saved_window_width, self.saved_window_height),
                                self.mod_pygame__.RESIZABLE,
                                vsync=1)
                            
                        else:
                            self.display = self.mod_pygame__.display.set_mode(
                                (self.saved_window_width, self.saved_window_height),
                                self.mod_pygame__.RESIZABLE,
                                vsync=0)

                    elif self.fullscreen:
                        self.fullscreen = False
                        if self.vsync:
                            self.display = self.mod_pygame__.display.set_mode(
                                (self.fullscreen_x, self.fullscreen_y),
                                self.mod_pygame__.FULLSCREEN,
                                vsync=1)

                        else:
                            self.display = self.mod_pygame__.display.set_mode(
                                (self.fullscreen_x, self.fullscreen_y),
                                self.mod_pygame__.FULLSCREEN,
                                vsync=0)

                except Exception as Message:
                    log_message = "display_utils > display_utils > update_display: "+ str(Message)
                    
                    self.mod_logging_utils__.create_log_message.update_log_warning(
                        self,
                        log_message)
                    
                    self.fullscreen = True
                    self.saved_window_width = 1280
                    self.saved_window_height = 720
                    self.mod_pygame__.display.quit()
                    self.mod_pygame__.init()
                    self.display = self.mod_pygame__.display.set_mode(
                        (self.saved_window_width, self.saved_window_height))

                self.mod_pygame__.display.set_icon(self.window_icon)
                
            except Exception as Message:
                print(Message)
                self.error_message = "display_utils > display_utils > update_display: "+str(Message)
                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

        def set_display(self, opengl=False):
            try:
                self.data_aFPS = []
                self.data_CPU_usage = []
                self.data_eFPS = []
                self.data_memory_usage = []

                self.timer = 0

                self.data_aFPS_Max = 1
                self.data_CPU_usage_Max = 1
                self.data_eFPS_Max = 1
                self.data_memory_usage_Max = 1

                try:
                    self.fullscreen_x = self.mod_pyautogui__.size()[0]
                    self.fullscreen_y = self.mod_pyautogui__.size()[1]

                    if self.fullscreen:
                        if opengl:
                            if self.vsync:
                                self.display = self.mod_pygame__.display.set_mode(
                                    (self.saved_window_width, self.saved_window_height),
                                    self.mod_pygame__.RESIZABLE | self.mod_pygame__.OPENGL | self.mod_pygame__.DOUBLEBUF,
                                    vsync=1)
                                
                            else:
                                self.display = self.mod_pygame__.display.set_mode(
                                    (self.saved_window_width,
                                    self.saved_window_height),
                                    self.mod_pygame__.RESIZABLE | self.mod_pygame__.OPENGL | self.mod_pygame__.DOUBLEBUF,
                                    vsync=0)
                        else:
                            self.display = self.mod_pygame__.display.set_mode(
                                (self.saved_window_width,
                                    self.saved_window_height),
                                self.mod_pygame__.RESIZABLE)
                            
                    elif self.fullscreen is False:
                        if opengl:
                            if self.vsync:
                                self.display = self.mod_pygame__.display.set_mode(
                                    (self.fullscreen_x, self.fullscreen_y),
                                    self.mod_pygame__.FULLSCREEN | self.mod_pygame__.OPENGL | self.mod_pygame__.DOUBLEBUF,
                                    vsync=0)
                                
                            else:
                                self.display = self.mod_pygame__.display.set_mode(
                                    (self.fullscreen_x, self.fullscreen_y),
                                    self.mod_pygame__.FULLSCREEN | self.mod_pygame__.OPENGL | self.mod_pygame__.DOUBLEBUF,
                                    vsync=1)
                        else:
                            self.display = self.mod_pygame__.display.set_mode(
                                (self.fullscreen_x, self.fullscreen_y),
                                self.mod_pygame__.FULLSCREEN)

                except Exception as Message:
                    log_message = "display_utils > display_utils > set_display:", Message
                    
                    self.mod_logging_utils__.create_log_message.update_log_warning(
                        self,
                        log_message)
                    
                    self.saved_window_width = 1280
                    self.saved_window_height = 720
                    self.mod_pygame__.display.quit()
                    self.mod_pygame__.init()
                    self.display = self.mod_pygame__.display.set_mode(
                        (self.saved_window_width, self.saved_window_height))

                self.mod_pygame__.display.set_icon(self.window_icon)
                
            except Exception as Message:
                self.error_message = "display_utils > display_utils > set_display: "+str(Message)
                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)


        def generate_min_display(self, width, height):
            try:
                if self.vsync:
                    self.display = self.mod_pygame__.display.set_mode(
                        (width, height),
                        self.mod_pygame__.RESIZABLE,
                        vsync=1)
                    
                else:
                    self.display = self.mod_pygame__.display.set_mode(
                        (width, height),
                        self.mod_pygame__.RESIZABLE,
                        vsync=0)

                self.mod_pygame__.display.set_icon(self.window_icon)
                
            except Exception as Message:
                self.error_message = "".join(("display_utils > display_utils > ",
                                             f"generate_min_display: {str(Message)}"))

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)


        def get_display_location(self):
            try:
                hwnd = self.mod_pygame__.display.get_wm_info()["window"]

                prototype = self.mod_ctypes__.WINFUNCTYPE(
                    self.mod_ctypes__.wintypes.BOOL,
                    self.mod_ctypes__.wintypes.HWND,
                    self.mod_ctypes__.POINTER(
                        self.mod_ctypes__.wintypes.RECT))

                paramflags = (1, "hwnd"), (2, "lprect")

                GetWindowRect = prototype(
                    ("GetWindowRect",self.mod_ctypes__.windll.user32),
                    paramflags)

                rect = GetWindowRect(hwnd)
                return rect.left+8, rect.top+31
            
            except Exception as Message:
                print(Message)
                log_message = "".join(("display_utils > display_utils > ",
                                            f"get_display_location: {str(Message)}"))
                
                self.mod_logging_utils__.create_log_message.update_log_warning(
                    self,
                    log_message)


        def get_play_status(self):
            try:
                if self.mod_pygame__.display.get_active():
                    if self.platform == "Windows" and self.vsync:
                        tempFPS = self.vsync_FPS
                        
                    else:
                        tempFPS = self.FPS
                        
                    self.project_sleeping = False
                    if not (self.command == "Play" or
                                self.command == "Benchmark"):
                        
                        if self.music:
                            self.mod_pygame__.mixer.music.unpause()
                            if self.mod_pygame__.mixer.music.get_busy() == 0:
                                self.mod_sound_utils__.play_sound.play_inventory_sound(self)
                else:
                    tempFPS = 5
                    self.project_sleeping = True
                    self.mod_pygame__.mixer.music.fadeout(500)

                if self.FPS_overclock:
                    tempFPS = 2000

                return tempFPS
            
            except Exception as Message:
                self.error_message = "".join(("display_utils > display_utils ",
                                                f"> get_play_status: {str(Message)}"))
                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)


    class display_animations:
        def __init__(self):
            pass


        def fade_in(self, size="full"):
            try:
                if self.startup_animation:
                    if size == "full":
                        HideSurface = self.mod_pygame__.Surface(
                            (self.real_window_width, self.real_window_height))
                    else:
                        HideSurface = self.mod_pygame__.Surface(
                            (self.real_window_width, self.real_window_height-40))

                    SurfaceAlpha = 255-(self.run_timer*1000)
                    HideSurface.set_alpha(SurfaceAlpha)
                    HideSurface.fill(self.background_color)
                    self.display.blit(
                        HideSurface,
                        (0, 100))

                    if SurfaceAlpha <= 0:
                        self.startup_animation = False
                        
            except Exception as Message:
                self.error_message = "display_utils > display_animations > fade_in: "+str(Message)
                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)



        def fade_out(self, size="full"):
            try:
                if self.startup_animation:
                    if size == "full":
                        HideSurface = self.mod_pygame__.Surface(
                            (self.real_window_width, self.real_window_height-100))
                    else:
                        HideSurface = self.mod_pygame__.Surface(
                            (self.real_window_width, self.real_window_height-140))

                    SurfaceAlpha = 255-(self.run_timer*1000)
                    HideSurface.set_alpha(255-SurfaceAlpha)
                    HideSurface.fill(self.background_color)

                    if self.go_to == "Credits":
                        self.display.blit(
                            HideSurface,
                            (0, 0))
                    else:
                        self.display.blit(
                            HideSurface,
                            (0, 100))

                    if SurfaceAlpha <= 0:
                        self.startup_animation = False
                        
            except Exception as Message:
                self.error_message = "display_utils > display_animations > fade_out: "+str(Message)
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
