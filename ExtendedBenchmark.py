if __name__ != "__main__":
    class LoadBenchmark:
        def __init__(self):
            pass

        def ExitBenchmark(self):
            try:
                self.mod_pygame__.display.quit()
                self.mod_pygame__.display.init()
                self.command = "Undefined"
                self.mod_display_utils__.display_utils.set_display(self)
                self.mod_main__.Initialize.menu_selector(self)
                
            except Exception as Message:
                self.error_message = "".join(("ExtendedBenchmark > LoadBenchmark ",
                                              f"> ExitBenchmark: {str(Message)}"))
                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

        def run(self):
            try:
                FPSlistX = []
                FPSlistY = []

                FPSlistX2 = []
                FPSlistY2 = []

                FPSlistX3 = []
                FPSlistY3 = []

                SetFPS = [15,
                          30,
                          45,
                          60,
                          75,
                          90,
                          105,
                          120,
                          135,
                          150,
                          200,
                          250,
                          300,
                          350,
                          500]

                SetFPSlength = len(SetFPS)

                self.display = self.mod_pygame__.display.set_mode((1280, 720))

                iteration = 0
                self.FPScounter = 0
                Maxiteration = 500

                while iteration < (500*SetFPSlength):
                    self.mod_pygame__.display.set_caption(
                        "".join((f"Pycraft: v{self.version}: Benchmark | ",
                                 f"Running Blank Window Benchmark @ {SetFPS[self.FPScounter]} FPS")))

                    while iteration != Maxiteration:
                        if not self.clock.get_fps() == 0:
                            FPSlistX.append(iteration)
                            FPSlistY.append(self.clock.get_fps())

                        self.display.fill(self.background_color)

                        for event in self.mod_pygame__.event.get():
                            if (event.type == self.mod_pygame__.QUIT or
                                (event.type == self.mod_pygame__.KEYDOWN and
                                 (not event.key == self.mod_pygame__.K_SPACE))):

                                LoadBenchmark.ExitBenchmark(self)

                        self.mod_pygame__.display.flip()
                        iteration += 1
                        self.clock.tick(SetFPS[self.FPScounter])
                    self.FPScounter += 1
                    Maxiteration += 500

                self.mod_pygame__.display.set_caption(
                    "".join((f"Pycraft: v{self.version}: ",
                             "Benchmark | Preparing Animated Benchmark")))

                iteration = 0
                self.FPScounter = 0
                Maxiteration = 500

                while iteration != 60:
                    self.display.fill(self.background_color)

                    for event in self.mod_pygame__.event.get():
                        if (event.type == self.mod_pygame__.QUIT or
                            (event.type == self.mod_pygame__.KEYDOWN and
                             (not event.key == self.mod_pygame__.K_SPACE))):

                            LoadBenchmark.ExitBenchmark(self)

                    self.mod_pygame__.display.flip()
                    iteration += 1
                    self.clock.tick(60)


                iteration = 0
                self.FPScounter = 0
                Maxiteration = 500

                while iteration < (500*SetFPSlength):
                    self.mod_pygame__.display.set_caption(
                        "".join((f"Pycraft: v{self.version}: Benchmark | ",
                                 f"Running Animated Window Benchmark @ {SetFPS[self.FPScounter]} FPS")))

                    while not iteration == Maxiteration:
                        if not self.clock.get_fps() == 0:
                            FPSlistX2.append(iteration)
                            FPSlistY2.append(self.clock.get_fps())

                        self.display.fill(self.background_color)

                        self.mod_drawing_utils__.draw_rose.create_rose(
                            self,
                            False)

                        self.mod_drawing_utils__.draw_rose.create_rose(
                            self,
                            False)

                        self.mod_drawing_utils__.draw_rose.create_rose(
                            self,
                            False)

                        self.mod_drawing_utils__.draw_rose.create_rose(
                            self,
                            False)

                        self.mod_drawing_utils__.draw_rose.create_rose(
                            self,
                            False)

                        self.mod_drawing_utils__.draw_rose.create_rose(
                            self,
                            False)

                        self.mod_drawing_utils__.draw_rose.create_rose(
                            self,
                            False)

                        self.mod_drawing_utils__.draw_rose.create_rose(
                            self,
                            False)

                        for event in self.mod_pygame__.event.get():
                            if (event.type == self.mod_pygame__.QUIT or
                                (event.type == self.mod_pygame__.KEYDOWN and
                                 (not event.key == self.mod_pygame__.K_SPACE))):

                                LoadBenchmark.ExitBenchmark(self)

                        self.mod_pygame__.display.flip()
                        iteration += 1
                        self.clock.tick(SetFPS[self.FPScounter])
                    self.FPScounter += 1
                    Maxiteration += 500

                self.mod_pygame__.display.set_caption(
                    "".join((f"Pycraft: v{self.version}: Benchmark | ",
                             "Preparing OpenGL Benchmark")))

                iteration = 0
                self.FPScounter = 0
                Maxiteration = 500

                while iteration != 60:
                    self.display.fill(self.background_color)
                    for event in self.mod_pygame__.event.get():
                        if (event.type == self.mod_pygame__.QUIT or
                            (event.type == self.mod_pygame__.KEYDOWN and
                             (not event.key == self.mod_pygame__.K_SPACE))):

                            LoadBenchmark.ExitBenchmark(self)

                    self.mod_pygame__.display.flip()
                    iteration += 1
                    self.clock.tick(60)

                self.mod_pygame__.display.quit()
                self.mod_pygame__.display.init()

                shared_data = self

                class Create3Dbenchmark(self.mod_base__.BenchmarkWindow):
                    self.mod_base__.title = "Crate"
                    self.mod_base__.vsync = False
                    self.mod_base__.window_size = 1280, 720

                    def __init__(self, **kwargs):
                        self.shared_data = shared_data

                        super().__init__(**kwargs)

                        if shared_data.platform == "Linux":
                            self.prog = self.load_program(
                                shared_data.mod_OS__.path.join(
                                    shared_data.base_folder,
                                    ("programs//benchmark.glsl")))

                            self.scene = self.load_scene(
                                shared_data.mod_OS__.path.join(
                                    shared_data.base_folder,
                                    ("resources//benchmark resources//Crate.obj")))

                            self.texture = self.load_texture_2d(
                                shared_data.mod_OS__.path.join(
                                    shared_data.base_folder,
                                    ("resources//benchmark resources//Crate.png")))

                        else:
                            self.prog = self.load_program(
                                shared_data.mod_OS__.path.join(
                                    shared_data.base_folder,
                                    ("programs\\benchmark.glsl")))

                            self.scene = self.load_scene(
                                shared_data.mod_OS__.path.join(
                                    shared_data.base_folder,
                                    ("resources\\benchmark resources\\Crate.obj")))

                            self.texture = self.load_texture_2d(
                                shared_data.mod_OS__.path.join(
                                    shared_data.base_folder,
                                    ("resources\\benchmark resources\\Crate.png")))

                        self.mvp = self.prog["Mvp"]
                        self.light = self.prog["Light"]

                        self.vao = self.scene.root_nodes[0].mesh.vao.instance(self.prog)

                        self.SetFPS = SetFPS
                        self.SetFPSlength = SetFPSlength

                        self.FPSlistX3 = FPSlistX3
                        self.FPSlistY3 = FPSlistY3

                        self.iteration = 0
                        self.Maxiteration = 500

                        self.wnd.title = "".join((f"Pycraft: v{self.shared_data.version}: Benchmark | ",
                                                  "Running OpenGL Benchmark ",
                                                  f"@ {self.SetFPS[self.shared_data.FPScounter]} FPS"))

                        self.PreviousFPS = 15

                        self.aFPS = 15

                        self.time = 0

                        while self.iteration < 500*self.SetFPSlength:
                            RunTime = self.shared_data.mod_time__.perf_counter()
                            try:
                                if self.iteration == self.Maxiteration:
                                    self.shared_data.FPScounter += 1
                                    self.Maxiteration += 500
                                    if self.shared_data.FPScounter <= self.SetFPSlength:
                                        self.wnd.title = "".join((f"Pycraft: v{self.shared_data.version}: ",
                                            "Benchmark | Running OpenGL Benchmark ",
                                            f"@ {self.SetFPS[self.shared_data.FPScounter]} FPS"))

                                angle = self.time
                                self.ctx.clear(
                                    0.0,
                                    0.0,
                                    0.0)

                                self.ctx.enable(self.shared_data.mod_ModernGL__.DEPTH_TEST)

                                camera_pos = (
                                    self.shared_data.mod_numpy__.cos(angle) * 3.0,
                                    self.shared_data.mod_numpy__.sin(angle) * 3.0,
                                    2.0)

                                proj = self.shared_data.mod_pyrr_Matrix44_.perspective_projection(
                                    45.0,
                                    self.aspect_ratio,
                                    0.1,
                                    100.0)

                                lookat = self.shared_data.mod_pyrr_Matrix44_.look_at(
                                    camera_pos,
                                    (0.0, 0.0, 0.5),
                                    (0.0, 0.0, 1.0),
                                )

                                self.mvp.write((proj * lookat).astype("f4"))
                                self.light.value = camera_pos
                                self.texture.use()
                                self.vao.render()
                                self.shared_data.mod_time__.sleep(1/(self.SetFPS[self.shared_data.FPScounter]))

                                eFPS = 1/(self.shared_data.mod_time__.perf_counter()-RunTime)
                                self.aFPS = (eFPS+self.PreviousFPS)/2
                                self.PreviousFPS = eFPS

                                if not eFPS == 0 and len(self.FPSlistX3) < 7500:
                                    self.FPSlistX3.append(self.iteration)
                                    self.FPSlistY3.append(self.aFPS)

                                self.iteration += 1
                                self.time += shared_data.mod_time__.perf_counter()-RunTime
                                self.wnd.swap_buffers()

                            except Exception as Message:
                                try:
                                    self.wnd.close()
                                    self.wnd.destroy()
                                    
                                except:
                                    pass

                                if str(Message) != "'NoneType' object has no attribute 'flip'":
                                    shared_data.error_message = "".join(("ExtendedBenchmark > ",
                                                                f"Create3Dbenchmark > {str(Message)}"))

                                    shared_data.error_message_detailed = "".join(
                                        shared_data.mod_traceback__.format_exception(
                                            None,
                                            Message,
                                            Message.__traceback__))

                                    self.shared_data.mod_error_utils__.generate_error_screen.error_screen(
                                        shared_data)

                                self.shared_data.command = "Undefined"
                                self.shared_data.mod_pygame__.display.quit()
                                self.shared_data.mod_pygame__.init()
                                self.shared_data.mod_display_utils__.display_utils.set_display(self.shared_data)
                                self.shared_data.mod_Main__.Initialize.menu_selector(self.shared_data)

                        else:
                            self.wnd.close()
                            self.wnd.destroy()

                self.mod_ModernGL_window_.run_window_config(Create3Dbenchmark)
                self.mod_display_utils__.display_utils.set_display(self)
                
            except Exception as Message:
                if not (str(Message) == "WindowConfig.render not implemented" or
                        str(Message) == "'NoneType' object has no attribute 'flip'"):

                    self.error_message = "ExtendedBenchmark > LoadBenchmark > run: "+str(Message)
                    self.error_message_detailed = "".join(
                        self.mod_traceback__.format_exception(
                            None,
                            Message,
                            Message.__traceback__))

                    self.mod_error_utils__.generate_error_screen.error_screen(self)

                else:
                    return FPSlistX, FPSlistY, FPSlistX2, FPSlistY2, FPSlistX3, FPSlistY3
            else:
                return FPSlistX, FPSlistY, FPSlistX2, FPSlistY2, FPSlistX3, FPSlistY3

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
