if __name__ != "__main__":
    class StartupTest:
        def __init__(self):
            pass

        def TestForResource(self, name, path):
            try:
                FoundFile = self.mod_OS__.path.exists(
                    self.mod_OS__.path.join(
                        self.base_folder,
                        path))
                
                if FoundFile is False:
                    StartupTest.ResourceNotFound(
                        self,
                        name,
                        self.mod_OS__.path.join(
                        self.base_folder,
                        path))
                    
            except Exception as Message:
                self.error_message = "".join(("PycraftStartupTest > StartupTest ",
                                              f"> TestForResource: {str(Message)}"))

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

        def ResourceNotFound(self, name, path):
            self.error_message = "".join(("PycraftStartupTest > StartupTest > ",
                                             f"PycraftResourceTest: Unable to locate: {name}"))

            self.error_message_detailed = "".join(("PycraftStartupTest > StartupTest > ",
                                             f"PycraftResourceTest: Unable to locate: {name} ",
                                             f"at location: {path}"))

            self.mod_error_utils__.generate_error_screen.error_screen(self)

        def PycraftSelfTest(self):
            try:
                self.mod_pygame__.display.set_icon(self.window_icon)

                SDLversion = self.mod_pygame__.get_sdl_version()[0]
                RAM = ((self.mod_psutil__.virtual_memory().available)/1000000)
                # expressed in MB
                OpenGLversion = self.mod_ModernGL_window_.conf.settings.WINDOW["gl_version"]

                if OpenGLversion[0] < 2 and OpenGLversion[1] >= 8:
                    root = self.mod_tkinter__tk.Tk()
                    root.withdraw()
                    self.mod_Tkinter_messagebox_.showerror(
                        "Invalid OpenGL version",
                        "".join((f"OpenGL version: {OpenGLversion[0]}.{OpenGLversion[1]} ",
                                 "is not supported; try a version greater than 2.7")))

                    quit()

                if SDLversion < 2:
                    root = self.mod_tkinter__tk.Tk()
                    root.withdraw()
                    self.mod_Tkinter_messagebox_.showerror(
                        "Invalid SDL version",
                        "".join((f"SDL version: {SDLversion} is not supported; try a ",
                                 "version greater than or equal to 2")))

                    quit()

                if RAM < 260:
                    root = self.mod_tkinter__tk.Tk()
                    root.withdraw()
                    self.mod_Tkinter_messagebox_.showerror(
                        "Minimum system requirements not met",
                        "".join(("Your system does not meet the minimum 260mb free ",
                                 "memory specification needed to play this game")))

                    quit()

                if self.mod_sys__.platform == "win32" or self.mod_sys__.platform == "win64":
                    self.mod_OS__.environ["SDL_VIDEO_CENTERED"] = "1"
                    
            except Exception as Message:
                self.error_message = "".join(("PycraftStartupTest > StartupTest > ",
                                             f"PycraftSelfTest: {str(Message)}"))

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)


        def PycraftResourceTest(self, override):
            try:
                if (self.current_date != self.last_run or
                        self.crash or
                        self.run_full_startup or
                        override):

                    if self.platform == "Linux":
                        for trackID in range(6):
                            StartupTest.TestForResource(
                                self,
                                f"footsteps{trackID}.wav",
                                f"resources//game engine resources//GameSounds//footstep//footsteps{trackID}.wav")

                        StartupTest.TestForResource(
                            self,
                            "FieldAmb.ogg",
                            "resources//game engine resources//GameSounds//FieldAmb.ogg")

                        StartupTest.TestForResource(
                            self,
                            "FieldAmb.ogg",
                            "resources//game engine resources//GameSounds//FieldAmb.ogg")

                        for trackID in range(11):
                            StartupTest.TestForResource(
                                self,
                                f"thunder{trackID}.ogg",
                                f"resources//game engine resources//GameSounds//thunder//thunder{trackID}.ogg")

                        StartupTest.TestForResource(
                            self,
                            "selectorICONlight.jpg",
                            "resources//general resources//selectorICONlight.jpg")

                        StartupTest.TestForResource(
                            self,
                            "selectorICONdark.jpg",
                            "resources//general resources//selectorICONdark.jpg")

                        StartupTest.TestForResource(
                            self,
                            "ClearSkyTransition.gif",
                            "resources//game engine resources//skysphere//ClearSkyTransition.gif")

                        StartupTest.TestForResource(
                            self,
                            "GrassTexture.png",
                            "resources//game engine resources//map//GrassTexture.png")

                        StartupTest.TestForResource(
                            self,
                            "RockTexture.png",
                            "resources//game engine resources//map//RockTexture.png")

                        StartupTest.TestForResource(
                            self,
                            "Crate.png",
                            "resources//benchmark resources//Crate.png")

                        StartupTest.TestForResource(
                            self,
                            "InventoryGeneral.ogg",
                            "resources//general resources//InventoryGeneral.ogg")

                        StartupTest.TestForResource(
                            self,
                            "Click.ogg",
                            "resources//general resources//Click.ogg")

                        StartupTest.TestForResource(
                            self,
                            "map.obj",
                            "resources//game engine resources//map//map.obj")

                        StartupTest.TestForResource(
                            self,
                            "map.mtl",
                            "resources//game engine resources//map//map.mtl")

                        StartupTest.TestForResource(
                            self,
                            "Crate.obj",
                            "resources//benchmark resources//Crate.obj")

                        StartupTest.TestForResource(
                            self,
                            "raw_depth.glsl",
                            "programs//raw_depth.glsl")

                        StartupTest.TestForResource(
                            self,
                            "shadowmap.glsl",
                            "programs//shadowmap.glsl")

                        StartupTest.TestForResource(
                            self,
                            "orbital_prog.glsl",
                            "programs//orbital_prog.glsl")

                        StartupTest.TestForResource(
                            self,
                            "skysphere.glsl",
                            "programs//skysphere.glsl")

                        StartupTest.TestForResource(
                            self,
                            "benchmark.glsl",
                            "programs//benchmark.glsl")

                        StartupTest.TestForResource(
                            self,
                            "particles_screen.glsl",
                            "programs//particles_screen.glsl")

                        StartupTest.TestForResource(
                            self,
                            "Full_Map.png",
                            "resources//map resources//Full_Map.png")

                        StartupTest.TestForResource(
                            self,
                            "Marker.png",
                            "resources//map resources//Marker.png")

                    else:
                        for trackID in range(6):
                            StartupTest.TestForResource(
                                self,
                                f"footsteps{trackID}.wav",
                                f"resources\\game engine resources\\GameSounds\\footstep\\footsteps{trackID}.wav")

                        StartupTest.TestForResource(
                            self,
                            "FieldAmb.ogg",
                            "resources\\game engine resources\\GameSounds\\FieldAmb.ogg")

                        StartupTest.TestForResource(
                            self,
                            "FieldAmb.ogg",
                            "resources\\game engine resources\\GameSounds\\FieldAmb.ogg")

                        for trackID in range(11):
                            StartupTest.TestForResource(
                                self,
                                f"thunder{trackID}.ogg",
                                f"resources\\game engine resources\\GameSounds\\thunder\\thunder{trackID}.ogg")

                        StartupTest.TestForResource(
                            self,
                            "selectorICONlight.jpg",
                            "resources\\general resources\\selectorICONlight.jpg")

                        StartupTest.TestForResource(
                            self,
                            "selectorICONdark.jpg",
                            "resources\\general resources\\selectorICONdark.jpg")

                        StartupTest.TestForResource(
                            self,
                            "ClearSkyTransition.gif",
                            "resources\\game engine resources\\skysphere\\ClearSkyTransition.gif")

                        StartupTest.TestForResource(
                            self,
                            "GrassTexture.png",
                            "resources\\game engine resources\\map\\GrassTexture.png")

                        StartupTest.TestForResource(
                            self,
                            "RockTexture.png",
                            "resources\\game engine resources\\map\\RockTexture.png")

                        StartupTest.TestForResource(
                            self,
                            "Crate.png",
                            "resources\\benchmark resources\\Crate.png")

                        StartupTest.TestForResource(
                            self,
                            "InventoryGeneral.ogg",
                            "resources\\general resources\\InventoryGeneral.ogg")

                        StartupTest.TestForResource(
                            self,
                            "Click.ogg",
                            "resources\\general resources\\Click.ogg")

                        StartupTest.TestForResource(
                            self,
                            "map.obj",
                            "resources\\game engine resources\\map\\map.obj")

                        StartupTest.TestForResource(
                            self,
                            "map.mtl",
                            "resources\\game engine resources\\map\\map.mtl")

                        StartupTest.TestForResource(
                            self,
                            "Crate.obj",
                            "resources\\benchmark resources\\Crate.obj")

                        StartupTest.TestForResource(
                            self,
                            "raw_depth.glsl",
                            "programs\\raw_depth.glsl")

                        StartupTest.TestForResource(
                            self,
                            "shadowmap.glsl",
                            "programs\\shadowmap.glsl")

                        StartupTest.TestForResource(
                            self,
                            "orbital_prog.glsl",
                            "programs\\orbital_prog.glsl")

                        StartupTest.TestForResource(
                            self,
                            "skysphere.glsl",
                            "programs\\skysphere.glsl")

                        StartupTest.TestForResource(
                            self,
                            "benchmark.glsl",
                            "programs\\benchmark.glsl")

                        StartupTest.TestForResource(
                            self,
                            "particles_screen.glsl",
                            "programs\\particles_screen.glsl")

                        StartupTest.TestForResource(
                            self,
                            "Full_Map.png",
                            "resources\\map resources\\Full_Map.png")

                        StartupTest.TestForResource(
                            self,
                            "Marker.png",
                            "resources\\map resources\\Marker.png")

            except Exception as Message:
                self.error_message = "".join(("PycraftStartupTest > StartupTest > ",
                                             f"PycraftResourceTest: {str(Message)}"))

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
