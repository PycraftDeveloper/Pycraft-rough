if __name__ != "__main__":
    class GenerateMapGUI:
        def __init__(self):
            pass

        def GetMapPos(self):
            try:
                x = 0
                z = 0
                if self.x == 0:
                    x = 640
                if self.z == 0:
                    z = 360
                x -= 6
                z -= 19
                return (x,z)
            
            except Exception as Message:
                self.error_message = "".join(("MapGUI > GenerateMapGUI ",
                                            f"> GetMapPos: {str(Message)}"))

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)


        def MapGUI(self):
            try:
                Message = self.mod_display_utils__.display_utils.set_display(self)
                self.display.fill(self.background_color)
                self.mod_pygame__.display.update()

                if self.platform == "Linux":
                    MapPIL =  self.mod_PIL_Image_.open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("resources//map resources//Full_Map.png")))

                else:
                    MapPIL =  self.mod_PIL_Image_.open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("resources\\map resources\\Full_Map.png")))

                Map0 = self.mod_pygame__.image.fromstring(
                    MapPIL.tobytes(),
                    MapPIL.size,
                    MapPIL.mode).convert()

                if self.platform == "Linux":
                    MapIcon = self.mod_pygame__.image.load(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("resources//map resources//Marker.png"))).convert_alpha()

                else:
                    MapIcon = self.mod_pygame__.image.load(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("resources\\map resources\\Marker.png"))).convert_alpha()

                zoom = 0

                X,Y = 0, 0
                key = ""

                if self.platform == "Linux":
                    MapPIL0 =  self.mod_PIL_Image_.open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("resources//map resources//Full_Map.png"))).resize(
                                (self.real_window_width,
                                 self.real_window_height),
                                self.mod_PIL_Image_.ANTIALIAS)

                else:
                    MapPIL0 =  self.mod_PIL_Image_.open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("resources\\map resources\\Full_Map.png"))).resize(
                                (self.real_window_width,
                                 self.real_window_height),
                                self.mod_PIL_Image_.ANTIALIAS)

                Map0 = self.mod_pygame__.image.fromstring(
                    MapPIL0.tobytes(),
                    MapPIL0.size,
                    MapPIL0.mode).convert()

                if self.platform == "Linux":
                    MapPIL1 =  self.mod_PIL_Image_.open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("resources//map resources//Full_Map.png"))).resize(
                                (int(self.real_window_width*1.75),
                                 int(self.real_window_height*1.75)),
                                self.mod_PIL_Image_.ANTIALIAS)

                else:
                    MapPIL1 =  self.mod_PIL_Image_.open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("resources\\map resources\\Full_Map.png"))).resize(
                                (int(self.real_window_width*1.75),
                                 int(self.real_window_height*1.75)),
                                self.mod_PIL_Image_.ANTIALIAS)

                Map1 = self.mod_pygame__.image.fromstring(
                    MapPIL1.tobytes(),
                    MapPIL1.size,
                    MapPIL1.mode).convert()

                if self.platform == "Linux":
                    MapPIL2 =  self.mod_PIL_Image_.open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("resources//map resources//Full_Map.png"))).resize(
                                (int(self.real_window_width*2),
                                 int(self.real_window_height*2)),
                                self.mod_PIL_Image_.ANTIALIAS)

                else:
                    MapPIL2 =  self.mod_PIL_Image_.open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("resources\\map resources\\Full_Map.png"))).resize(
                                (int(self.real_window_width*2),
                                 int(self.real_window_height*2)),
                                self.mod_PIL_Image_.ANTIALIAS)

                Map2 = self.mod_pygame__.image.fromstring(
                    MapPIL2.tobytes(),
                    MapPIL2.size,
                    MapPIL2.mode).convert()

                while True:
                    self.mod_caption_utils__.generate_captions.get_normal_caption(
                        self,
                        "Map")

                    self.display.fill(self.background_color)

                    self.mod_display_utils__.display_functionality.core_display_functions(
                        self, checkEvents=False)

                    for event in self.mod_pygame__.event.get():
                        if (event.type == self.mod_pygame__.QUIT or
                                (event.type == self.mod_pygame__.KEYDOWN and
                                    event.key == self.mod_pygame__.K_ESCAPE) or
                                (event.type == self.mod_pygame__.KEYDOWN and
                                    event.key == self.mod_pygame__.K_r)):

                            self.load_3D = False

                            if self.sound:
                                self.mod_sound_utils__.play_sound.play_click_sound(self)

                            self.mod_pygame__.display.quit()
                            return

                        if event.type == self.mod_pygame__.WINDOWSIZECHANGED:
                            if self.platform == "Linux":
                                MapPIL0 =  self.mod_PIL_Image_.open(
                                    self.mod_OS__.path.join(
                                        self.base_folder,
                                        ("resources//map resources//Full_Map.png"))).resize(
                                            (self.real_window_width,
                                             self.real_window_height),
                                            self.mod_PIL_Image_.ANTIALIAS)

                            else:
                                MapPIL0 =  self.mod_PIL_Image_.open(
                                    self.mod_OS__.path.join(
                                        self.base_folder,
                                        ("resources\\map resources\\Full_Map.png"))).resize(
                                            (self.real_window_width,
                                             self.real_window_height),
                                            self.mod_PIL_Image_.ANTIALIAS)

                            Map0 = self.mod_pygame__.image.fromstring(
                                MapPIL0.tobytes(),
                                MapPIL0.size,
                                MapPIL0.mode).convert()

                            if self.platform == "Linux":
                                MapPIL1 =  self.mod_PIL_Image_.open(
                                    self.mod_OS__.path.join(
                                        self.base_folder,
                                        ("resources//map resources//Full_Map.png"))).resize(
                                            (int(self.real_window_width*1.75),
                                             int(self.real_window_height*1.75)),
                                            self.mod_PIL_Image_.ANTIALIAS)

                            else:
                                MapPIL1 =  self.mod_PIL_Image_.open(
                                    self.mod_OS__.path.join(
                                        self.base_folder,
                                        ("resources\\map resources\\Full_Map.png"))).resize(
                                            (int(self.real_window_width*1.75),
                                             int(self.real_window_height*1.75)),
                                            self.mod_PIL_Image_.ANTIALIAS)

                            Map1 = self.mod_pygame__.image.fromstring(
                                MapPIL1.tobytes(),
                                MapPIL1.size,
                                MapPIL1.mode).convert()

                            if self.platform == "Linux":
                                MapPIL2 =  self.mod_PIL_Image_.open(
                                    self.mod_OS__.path.join(
                                        self.base_folder,
                                        ("resources//map resources//Full_Map.png"))).resize(
                                            (int(self.real_window_width*2),
                                             int(self.real_window_height*2)),
                                            self.mod_PIL_Image_.ANTIALIAS)

                            else:
                                MapPIL2 =  self.mod_PIL_Image_.open(
                                    self.mod_OS__.path.join(
                                        self.base_folder,
                                        ("resources\\map resources\\Full_Map.png"))).resize(
                                            (int(self.real_window_width*2),
                                             int(self.real_window_height*2)),
                                            self.mod_PIL_Image_.ANTIALIAS)

                            Map2 = self.mod_pygame__.image.fromstring(
                                MapPIL2.tobytes(),
                                MapPIL2.size,
                                MapPIL2.mode).convert()

                        if event.type == self.mod_pygame__.KEYDOWN:
                            if event.key == self.mod_pygame__.K_SPACE:
                                zoom = 0

                            if event.key == self.mod_pygame__.K_w:
                                key = "w"

                            if event.key == self.mod_pygame__.K_s:
                                key = "s"

                            if event.key == self.mod_pygame__.K_d:
                                key = "d"

                            if event.key == self.mod_pygame__.K_a:
                                key = "a"

                            if event.key == self.mod_pygame__.K_F11:
                                self.mod_display_utils__.display_utils.update_display(self)

                        if event.type == self.mod_pygame__.KEYUP:
                            key = ""

                        if event.type == self.mod_pygame__.MOUSEWHEEL:
                            if str(event.y)[0] == "-":
                                zoom -= 1
                            else:
                                zoom += 1

                    if self.use_mouse_input is False:
                        if self.joystick_zoom == "-":
                            zoom -= 1
                            self.joystick_zoom = None

                        elif self.joystick_zoom == "+":
                            zoom += 1
                            self.joystick_zoom = None

                        joystick_mouse = self.mod_pygame__.mouse.get_rel()

                        if joystick_mouse[0] > 0:
                            key = "a"

                        elif joystick_mouse[0] < 0:
                            key = "d"

                        elif joystick_mouse[1] > 0:
                            key = "w"

                        elif joystick_mouse[1] < 0:
                            key = "s"

                        else:
                            key = ""

                        if self.joystick_exit:
                            self.joystick_exit = False

                            if self.sound:
                                self.mod_sound_utils__.play_sound.play_click_sound(self)
                            return

                    if zoom >= 2:
                        zoom = 2
                    if zoom <= 0:
                        zoom = 0

                    if key == "w":
                        if zoom == 1:
                            Y -= 5
                        elif zoom == 2:
                            Y -= 10
                    if key == "s":
                        if zoom == 1:
                            Y += 5
                        elif zoom == 2:
                            Y += 10
                    if key == "d":
                        if zoom == 1:
                            X += 5
                        elif zoom == 2:
                            X += 10
                    if key == "a":
                        if zoom == 1:
                            X -= 5
                        elif zoom == 2:
                            X -= 10

                    if zoom == 1:
                        self.display.blit(
                            Map1,
                            (X,Y))

                        self.display.blit(
                            MapIcon,
                            GenerateMapGUI.GetMapPos(self))

                        if X <= -955:
                            X = -955
                        if Y <= -535:
                            Y = -535
                        if X >= -5:
                            X = -5
                        if Y >= -5:
                            Y = -5
                    elif zoom == 2:
                        self.display.blit(
                            Map2,
                            (X,Y))

                        self.display.blit(
                            MapIcon,
                            GenerateMapGUI.GetMapPos(self))

                        if X <= -1590:
                            X = -1590
                        if Y <= -890:
                            Y = -890
                        if X >= -10:
                            X = -10
                        if Y >= -10:
                            Y = -10
                    else:
                        self.display.blit(
                            Map0,
                            (0, 0))

                        self.display.blit(
                            MapIcon,
                            GenerateMapGUI.GetMapPos(self))

                    self.mod_pygame__.display.update()
                    self.clock.tick(
                        self.mod_display_utils__.display_utils.get_play_status(self))
                    
            except Exception as Message:
                self.error_message = "MapGUI > GenerateMapGUI > MapGUI: "+str(Message)

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
