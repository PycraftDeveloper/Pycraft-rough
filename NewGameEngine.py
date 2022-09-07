if __name__ != "__main__":
    class create_game_engine:
        def __init__():
            create_game_engine.main_game_engine()

        def RenderLoaddisplay(self):
            try:
                self.mod_pygame__.display.init()

                self.mod_caption_utils__.generate_captions.get_normal_caption(
                    self,
                    "Loading Pycraft")

                self.mod_display_utils__.display_utils.set_display(
                    self)

                global GameEngine_Initialisation
                global GameLoadProgressPercent
                global display_position
                global got_display_position

                display_position = self.mod_display_utils__.display_utils.get_display_location(
                    self)

                got_display_position = True

                if self.platform == "Linux":
                    SecondaryFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 35)

                    LoadingFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 15)

                    LoadingTextFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 15)

                else:
                    SecondaryFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 35)

                    LoadingFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 15)

                    LoadingTextFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 15)

                time = 0

                self.clock = self.mod_pygame__.time.Clock()

                self.skysphere_progress_message_text = self.mod_text_utils__.GenerateText.LoadQuickText(
                    self)

                Completion_Percentage = 0

                Averageload_time = self.load_time[0]/self.load_time[1]
                
                while GameEngine_Initialisation:
                    eFPS = self.clock.get_fps()
                    if self.load_time[0] != 0:
                        if eFPS > 0:
                            time += 1/eFPS

                        Loading_Line_X_value = (
                            ((self.real_window_width-200)/Averageload_time)*time)+100
                    
                    if GameLoadProgressPercent <= 10:
                        text = "Initializing"
                    elif GameLoadProgressPercent <= 20:
                        text = "Creating display"
                    elif GameLoadProgressPercent <= 30:
                        text = "Creating celestial entities"
                    elif GameLoadProgressPercent <= 40:
                        text = "Loading in-game objects: Map"
                    elif GameLoadProgressPercent <= 50:
                        text = "Loading in-game textures: Skysphere"
                    elif GameLoadProgressPercent <= 60:
                        text = "Loading in-game programmes"
                    elif GameLoadProgressPercent <= 70:
                        text = "Applying programme configurations"
                    elif GameLoadProgressPercent <= 80:
                        text = "Loading in-game textures: Grass"
                    else:
                        text = "Making final touches"

                    self.skysphere_progress_line = [
                        (100, self.real_window_height-100),
                        (100, self.real_window_height-100)]

                    if self.load_time[0] != 0:
                        if Loading_Line_X_value > self.real_window_width-100:
                            Loading_Line_X_value = self.real_window_width-100

                        self.skysphere_progress_line.append(
                            (Loading_Line_X_value, self.real_window_height-100))
                        Completion_Percentage = (
                            100/(self.load_time[0]/self.load_time[1]))*time

                        if Completion_Percentage > 100:
                            Completion_Percentage = 100

                    else:
                        self.skysphere_progress_line.append((
                            ((self.real_window_width/100)
                            * GameLoadProgressPercent)-100,
                            self.real_window_height-100))

                        Completion_Percentage = GameLoadProgressPercent

                    self.mod_game_engine__.create_game_engine.GenerateLoaddisplay(
                        self,
                        LoadingFont,
                        text,
                        SecondaryFont,
                        LoadingTextFont,
                        Completion_Percentage)
                    
                    for event in self.mod_pygame__.event.get():
                        if (event.type == self.mod_pygame__.QUIT or
                            (event.type == self.mod_pygame__.KEYDOWN and
                            event.key == self.mod_pygame__.K_ESCAPE)):

                            global Global_Save_and_QUIT
                            Global_Save_and_QUIT = True
                            quit()

                    self.mod_pygame__.display.flip()

                    tempFPS = self.mod_display_utils__.display_utils.get_play_status(
                        self)

                    self.clock.tick(tempFPS)

                if self.load_time[1] >= 25:
                    self.load_time = [0, 1]

                self.mod_pygame__.display.quit()
                self.mod_pygame__.display.init()

            except Exception as Message:
                print(Message)
                self.error_message = "GameEngine > CreateEngine > RenderLoaddisplay: " + \
                    str(Message)
                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(
                    self)

        def GenerateLoaddisplay(self, LoadingFont, text, SecondaryFont, LoadingTextFont, Completion_Percentage):
            try:
                self.display.fill(self.background_color)

                self.real_window_width = self.mod_pygame__.display.get_window_size()[
                    0]
                self.real_window_height = self.mod_pygame__.display.get_window_size()[
                    1]

                PycraftTitle = self.title_font.render(
                    "Pycraft",
                    self.aa,
                    self.font_color)

                title_width = PycraftTitle.get_width()

                self.display.blit(
                    PycraftTitle,
                    ((self.real_window_width-title_width)/2, 0))

                LoadingTitle = SecondaryFont.render(
                    "Loading",
                    self.aa,
                    self.secondary_font_color)
                self.display.blit(
                    LoadingTitle,
                    (((self.real_window_width-title_width)/2)+55, 50))

                self.mod_pygame__.draw.lines(
                    self.display,
                    self.shape_color,
                    self.aa,
                    [(100, self.real_window_height-100),
                    (self.real_window_width-100, self.real_window_height-100)],
                    3)

                self.mod_pygame__.draw.lines(
                    self.display,
                    self.accent_color,
                    self.aa,
                    self.skysphere_progress_line)

                displayMessage = LoadingFont.render(
                    self.skysphere_progress_message_text,
                    self.aa,
                    self.font_color)
                displayMessageWidth = displayMessage.get_width()
                self.display.blit(
                    displayMessage,
                    ((self.real_window_width-displayMessageWidth)/2, self.real_window_height-120))

                TextFontRendered = LoadingTextFont.render(
                    f"{text}",
                    self.aa,
                    self.font_color)
                TextFontRenderedWidth = TextFontRendered.get_width()

                self.display.blit(
                    TextFontRendered,
                    ((self.real_window_width-TextFontRenderedWidth)/2, self.real_window_height-100))

                ProgressText = LoadingTextFont.render(
                    f"{round(Completion_Percentage)}% complete",
                    self.aa,
                    self.font_color)
                ProgressTextWidth = ProgressText.get_width()

                self.display.blit(
                    ProgressText,
                    ((self.real_window_width-ProgressTextWidth)/2, self.real_window_height-80))

            except Exception as Message:
                print(Message)
                self.error_message = "".join(("GameEngine > CreateEngine > ",
                                            f"GenerateLoaddisplay: {str(Message)}"))

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

        def main_game_engine():
            import os
            import moderngl_window
            if ("site-packages" in os.path.dirname(__file__) or
                    "dist-packages" in os.path.dirname(__file__)):

                import GLWindowUtils
                import DataTransferUtils

            else:
                from pycraft import GLWindowUtils
                from pycraft import DataTransferUtils

            self = DataTransferUtils.data_transfer.loadData()
                
            class GameEngine(GLWindowUtils.CameraWindow):
                GLWindowUtils.CameraWindow.title = f"Pycraft: v{self.version}: Playing"
                GLWindowUtils.CameraWindow.resource_dir = self.base_folder
                GLWindowUtils.CameraWindow.vsync = self.vsync
                GLWindowUtils.CameraWindow.resizable = True
                GLWindowUtils.CameraWindow.window_size = (
                    self.real_window_width,
                    self.real_window_height)

                if self.aa:
                    GLWindowUtils.CameraWindow.samples = int(
                        str(self.aa_quality).split("x")[0])

                def __init__(self, **kwargs):
                    try:
                        import os
                        self.mod_OS__ = os

                        self.base_folder = self.mod_OS__.path.dirname(__file__)

                        if ("site-packages" in self.base_folder or
                                "dist-packages" in self.base_folder):

                            import GameEngineUtils
                            import GLWindowUtils

                        else:

                            from pycraft import GameEngineUtils
                            from pycraft import GLWindowUtils
                            
                        GameEngineUtils.create_game_engine_context.load_data_and_initialize(self)
                        
                        super().__init__(**kwargs)

                        self.mod_pygame__.init()

                        converted_theme_col_r = (1/255)*self.background_color[0]
                        converted_theme_col_g = (1/255)*self.background_color[1]
                        converted_theme_col_b = (1/255)*self.background_color[2]
                        
                        self.ctx.clear(converted_theme_col_r,
                                            converted_theme_col_g,
                                            converted_theme_col_b)

                        try:
                            self.wnd.swap_buffers()
                        except Exception as Message:
                            print(Message)

                        global GameEngine_Initialisation
                        global GameLoadProgressPercent
                        global display_position
                        global got_display_position

                        GameEngine_Initialisation = True
                        GameLoadProgressPercent = 0
                        display_position = (0, 0)
                        got_display_position = False
                        
                        CreateLoadScreen = self.mod_threading__.Thread(
                            target=self.mod_game_engine__.create_game_engine.RenderLoaddisplay,
                            args=(self, ))

                        CreateLoadScreen.start()
                        CreateLoadScreen.name = "Thread_CreateLoadScreen"

                        self.Joystick_Rotation = [0, 0]

                        self.StartLoading = self.mod_time__.perf_counter()

                        GameLoadProgressPercent = 10

                        if self.aa:
                            self.samples = int(
                                str(self.aa_quality).split("x")[0])
                            
                        else:
                            self.samples = 1

                        self.skybox_distance = 1600

                        self.camera.projection.update(
                            near=1,
                            far=self.skybox_distance,
                            fov=70)

                        self.wnd.mouse_exclusivity = True

                        while not got_display_position:
                            self.mod_time__.sleep(0.1)

                        self.fullscreen = not self.fullscreen

                        print(self.fullscreen)

                        print(self.real_window_width)
                        print(self.fullscreen_x)
                        print(self.real_window_height)
                        print(self.fullscreen_y)

                        if self.saved_window_width == self.fullscreen_x and self.saved_window_height == self.fullscreen_y:
                            self.fullscreen = True

                        else:
                            self.fullscreen = False

                        if self.fullscreen is False:
                            try:
                                print("repos")
                                self.wnd.position = display_position
                            except Exception as Message:
                                print(Message)
                                
                            GLWindowUtils.CameraWindow.resize(
                                self,
                                *self.wnd.size)

                        self.wnd.fullscreen = not self.fullscreen
                            
                        try:
                            if self.platform == "Linux":
                                self.wnd.set_icon(
                                    self.mod_OS__.path.join(
                                        self.base_folder,
                                        ("resources//general resources//Icon.png")))
                            else:
                                self.wnd.set_icon(
                                    self.mod_OS__.path.join(
                                        self.base_folder,
                                        ("resources\\general resources\\Icon.png")))

                        except Exception as Message:
                            print(Message)

                        GameLoadProgressPercent = 20

                        # Offscreen buffer
                        offscreen_size = 1024, 1024
                        self.offscreen_depth = self.ctx.depth_texture(offscreen_size)
                        self.offscreen_depth.compare_func = ""
                        self.offscreen_depth.repeat_x = False
                        self.offscreen_depth.repeat_y = False
                        # Less ugly by default with linear. May need to be NEAREST for some techniques
                        self.offscreen_depth.filter = (self.mod_ModernGL__.LINEAR,
                                                    self.mod_ModernGL__.LINEAR)

                        self.offscreen = self.ctx.framebuffer(
                            depth_attachment=self.offscreen_depth,)

                        self.sun_radius = 50

                        self.sun = self.mod_ModernGL_window_geometry.sphere(
                            radius=self.sun_radius)

                        self.moon = self.mod_ModernGL_window_geometry.sphere(
                            radius=80)

                        self.rain_particle = self.mod_ModernGL_window_geometry.sphere(
                            radius=1)

                        GameLoadProgressPercent = 30

                        # Debug geometry
                        self.offscreen_quad = self.mod_ModernGL_window_geometry.quad_2d(
                            size=(0.5, 0.5),
                            pos=(0.75, 0.75))

                        self.offscreen_quad2 = self.mod_ModernGL_window_geometry.quad_2d(
                            size=(0.5, 0.5),
                            pos=(0.25, 0.75))

                        self.SkySphere = self.mod_ModernGL_window_geometry.sphere(
                            radius=self.skybox_distance)

                        self.objects: self.mod_typing__.Dict[
                            str,
                            self.mod_ModernGL__.VertexArray] = {}

                        self.objects_shadow: self.mod_typing__.Dict[
                            str,
                            self.mod_ModernGL__.VertexArray] = {}

                        if self.platform == "Linux":
                            # Use 'u' to do things with UVs that this really needs
                            self.scene: self.mod_ModernGL_window_.scene.Scene = self.load_scene(
                                self.mod_OS__.path.join(
                                    self.base_folder,
                                    ("resources//game engine resources//map//map2.obj")),
                                cache=True)
                        else:
                            self.scene: self.mod_ModernGL_window_.scene.Scene = self.load_scene(
                                self.mod_OS__.path.join(
                                    self.base_folder,
                                    ("resources\\game engine resources\\map\\map.obj")),
                                cache=True)

                        GameLoadProgressPercent = 40

                        if self.platform == "Linux":
                            self.SkyBox_texture_Sun = self.load_texture_array(
                                self.mod_OS__.path.join(
                                    self.base_folder,
                                    ("resources//game engine resources//skysphere//ClearSkyTransition.gif")),
                                anisotropy=self.samples)

                        else:
                            self.SkyBox_texture_Sun = self.load_texture_array(
                                self.mod_OS__.path.join(
                                    self.base_folder,
                                    ("resources\\game engine resources\\skysphere\\ClearSkyTransition.gif")),
                                anisotropy=self.samples)

                        GameLoadProgressPercent = 50

                        # Programs
                        self.mod_game_engine_utils__.LoadPrograms.LoadProgramFiles(
                            self)

                        self.mod_game_engine_utils__.LoadPrograms.LoadProgramText(
                            self)

                        GameLoadProgressPercent = 60

                        vao = self.scene.root_nodes[0].mesh.vao
                        self.objects["map"] = vao.instance(self.shadowmap)
                        self.objects_shadow["map"] = vao.instance(self.depth_prog)

                        self.skysphere_prog["texture0"].value = 0
                        self.skysphere_prog["num_layers"].value = 41.0

                        # affects the velocity of the particles over time
                        # grav?
                        self.particles_transform["gravity"].value = -.005
                        self.ctx.point_size = self.wnd.pixel_ratio * 2  # point size

                        if self.fancy_particles:
                            self.N = 5_000  # particle count
                            
                        else:
                            self.N = 2_500
                            
                        # Initial / current number of active particles
                        self.active_particles = self.N // 100
                        # Maximum number of particles to emit per frame
                        self.max_emit_count = self.N // 100
                        self.stride = 28  # byte stride for each vertex
                        self.floats = 7
                        # Note that passing dynamic=True probably doesn't mean
                        # anything to most drivers today
                        try:
                            self.vbo1 = self.ctx.buffer(reserve=self.N * self.stride)
                            self.vbo2 = self.ctx.buffer(reserve=self.N * self.stride)

                        except Exception as Message:
                            log_message = "GameEngine > GameEngine > __init__: " + \
                                str(Message)

                            self.mod_logging_utils__.create_log_message.update_log_warning(
                                self,
                                log_message)

                            self.vbo1 = self.ctx.buffer(
                                reserve=self.N * self.stride, dynamic=True)
                            self.vbo2 = self.ctx.buffer(
                                reserve=self.N * self.stride, dynamic=True)
                            
                        # Write some initial particles
                        self.vbo1.write(
                            self.mod_numpy__.fromiter(
                                self.mod_game_engine_utils__.Particles.gen_particles(
                                    self,
                                    self.active_particles),
                                count=self.active_particles * self.floats, dtype="f4"))

                        # Transform vaos. We transform data back and forth to avoid buffer copy
                        self.transform_vao1 = self.ctx.vertex_array(
                            self.particles_transform,
                            [(self.vbo1, "2f 2f 3f", "in_pos", "in_vel", "in_color")],
                        )
                        self.transform_vao2 = self.ctx.vertex_array(
                            self.particles_transform,
                            [(self.vbo2, "2f 2f 3f", "in_pos", "in_vel", "in_color")],
                        )

                        # Render vaos. The render to screen version of the tranform vaos above
                        self.render_vao1 = self.ctx.vertex_array(
                            self.particles_screen,
                            [(self.vbo1, "2f 2x4 3f", "in_pos", "in_color")],
                        )
                        self.render_vao2 = self.ctx.vertex_array(
                            self.particles_screen,
                            [(self.vbo2, "2f 2x4 3f", "in_pos", "in_color")],
                        )

                        # The emit buffer size is only max_emit_count.
                        self.emit_buffer_elements = self.max_emit_count

                        self.gpu_emitter_vao = self.ctx._vertex_array(
                            self.gpu_emitter_particles, [])

                        # Query object to inspect render calls
                        self.query = self.ctx.query(primitives=True)

                        # Cycle emit methods per frame
                        self.particles_screen["projection"].write(
                            self.mod_game_engine_utils__.Particles.projection(
                                self))

                        self.shadowmap["u_sampler_shadow"].value = 0
                        self.shadowmap["grass_color"].value = 1
                        self.shadowmap["rock_color"].value = 2

                        self.shadowmap["light_level"] = 0.5

                        self.mvp = self.shadowmap["u_mvp"]
                        self.mvp_depth = self.shadowmap["u_depth_bias_mvp"]

                        self.light = self.shadowmap["u_light"]
                        self.color = self.shadowmap["u_color"]

                        self.mvp_shadow = self.depth_prog["u_mvp"]

                        self.sun_prog["color"].value = (1.0, 1.0, 0.0, 1.0)
                        self.moon_prog["color"].value = (1.0, 1.0, 1.0, 1.0)
                        self.lightpos = 0, 0, 0

                        self.color.value = (1.0, 1.0, 1.0)

                        GameLoadProgressPercent = 70

                        if self.platform == "Linux":
                            self.tex1 = self.load_texture_2d(
                                self.mod_OS__.path.join(
                                    self.base_folder,
                                    ("resources//game engine resources//map//GrassTexture.png")),
                                mipmap=True,
                                anisotropy=self.samples)

                            self.tex2 = self.load_texture_2d(
                                self.mod_OS__.path.join(
                                    self.base_folder,
                                    ("resources//game engine resources//map//RockTexture.png")),
                                mipmap=True,
                                anisotropy=self.samples)

                        else:
                            self.tex1 = self.load_texture_2d(
                                self.mod_OS__.path.join(
                                    self.base_folder,
                                    ("resources\\game engine resources\\map\\GrassTexture.png")),
                                mipmap=True,
                                anisotropy=self.samples)

                            self.tex2 = self.load_texture_2d(
                                self.mod_OS__.path.join(
                                    self.base_folder,
                                    ("resources\\game engine resources\\map\\RockTexture.png")),
                                mipmap=True,
                                anisotropy=self.samples)

                        self.tex1.use(location=1)
                        self.tex2.use(location=2)

                        SHADOW_SIZE: self.mod_typing_Final[int] = 2 << 7

                        shadow_size = (SHADOW_SIZE,
                                    SHADOW_SIZE,)

                        GameLoadProgressPercent = 80

                        self.tex_depth = self.ctx.depth_texture(shadow_size)

                        self.tex_color_depth = self.ctx.texture(
                            shadow_size,
                            components=1,
                            dtype="f4")

                        self.fbo_depth = self.ctx.framebuffer(
                            color_attachments=[self.tex_color_depth],
                            depth_attachment=self.tex_depth)

                        self.sampler_depth = self.ctx.sampler(
                            filter=(self.mod_ModernGL__.LINEAR,
                                    self.mod_ModernGL__.LINEAR),
                            compare_func=">=",
                            repeat_x=False,
                            repeat_y=False,)

                        self.Jump = False
                        self.jump_timer = 0
                        self.StartYposition = 0
                        self.Collision = False

                        self.modifier = 10

                        self.RunForwardtimer = False
                        self.RunForwardtimer_start = 0
                        self.RunForwardtimer_start_sound = 0
                        self.Sprinting = False
                        self.Wkeydowntimer_start = 0
                        self.Wkeydown = False

                        self.IKeyPressed = False

                        self.Akeydowntimer_start = 0
                        self.Akeydown = False

                        self.Skeydowntimer_start = 0
                        self.Skeydown = False

                        self.Dkeydowntimer_start = 0
                        self.Dkeydown = False

                        z = 1000
                        size = (z, z)

                        CloudData = self.mod_game_engine_utils__.ComputeWeather.ComputeCloudNoise(
                            self,
                            size)

                        self.range = self.mod_numpy__.max(
                            CloudData) - self.mod_numpy__.min(CloudData)

                        self.CloudsProgram["CloudHeight"] = 500.0
                        self.CloudsProgram["height_max"] = self.range
                        self.CloudsProgram["render_fog"] = self.render_fog

                        self.shadowmap["render_fog"] = self.render_fog

                        vertices, index = self.mod_game_engine_utils__.ComputeWeather.ComputeCloudModel(
                            self,
                            size[0])

                        self.vbo = self.ctx.buffer(vertices.astype("f4"))
                        self.ibo = self.ctx.buffer(index.astype("i4"))

                        cloud_vao_content = [(
                            self.vbo,
                            "2f",
                            "in_vert"), ]

                        self.vao = self.ctx.vertex_array(
                            self.CloudsProgram,
                            cloud_vao_content,
                            self.ibo)

                        if self.platform == "Linux":
                            self.cloud_texture = self.load_texture_2d(
                                self.mod_OS__.path.join(
                                    self.base_folder,
                                    ("resources//game engine resources//clouds//Rnd_noise.png")),
                                anisotropy=self.samples)

                        else:
                            self.cloud_texture = self.load_texture_2d(
                                self.mod_OS__.path.join(
                                    self.base_folder,
                                    ("resources\\game engine resources\\clouds\\Rnd_noise.png")),
                                anisotropy=self.samples)

                        GameLoadProgressPercent = 90

                        #if self.fullscreen is False:
                            #self.wnd.fullscreen = True

                        self.OnStart = True

                        self.time = 0
                        self.frametime = 1

                        self.Running = True

                        self.Inventory = False
                        self.Map = False

                        self.mod_globals__.Share.initialize_controller_game(
                            self)

                        self.UpdateProjection = False

                        self.Time_Percent = 0

                        self.day = 1
                        self.daycycleTime = 0

                        self.scrollTime = 0
                        self.GameSunTime = 0

                        self.DayCycle = 1

                        self.GameTime = 0

                        self.weather = ""
                        WeatherDelta = 1
                        self.DefaultSkyCol = 1.0

                        self.mod_game_engine_utils__.ComputeWeather.ComputeWeather(
                            self)

                        self.WeatherTime = 0
                        self.Thundertimer = 0
                        self.Lightningtimer = 0
                        self.show_strobe_effects = False
                        self.Thundertimer_Target = self.mod_random__.randint(
                            15, 30)
                        switchWeather = self.mod_random__.randint(60, 120)
                        self.Flashtimer = 0
                        self.ShowFlash = False
                        self.LengthenStorm = False
                        self.PreviousWeather = self.weather

                        self.Previous_Fog_Distance_Min = self.shadowmap["w_min"].value
                        self.Previous_Fog_Distance_Max = self.shadowmap["w_max"].value

                        self.space_key_pressed = False

                        self.Previous_color = self.color.value[0]

                        self.Previous_CloudsProgram_Alpha = self.CloudsProgram["WeatherAlpha"].value
                        self.Previous_CloudsProgram_CloudColor = self.CloudsProgram["CloudColor"].value

                        self.Previous_multiplier = self.CloudsProgram["CloudHeightMultiplier"].value

                        self.Previous_prog_transparency = self.skysphere_prog["transparency"].value

                        GameLoadProgressPercent = 100

                        while self.Running:
                            # 250 is base FPS w/ shadowmapping
                            # 205 is avg w/ shadowmapping + dynamic skybox
                            start = self.mod_time__.perf_counter()
                            self.GameTimeDelta = self.time
                            if self.Inventory or self.Map:
                                self.mod_game_engine_utils__.AccessOtherGUIs.AccessGUI(
                                    self)

                            if self.mod_pygame__.mixer.music.get_busy():
                                self.mod_pygame__.mixer.music.pause()

                            self.keys = self.wnd.keys

                            self.wnd.clear()
                            self.ctx.clear(self.DefaultSkyCol,
                                        self.DefaultSkyCol,
                                        self.DefaultSkyCol)

                            if self.WeatherTime >= switchWeather:
                                switchWeather = self.mod_random__.randint(
                                    60, 120)
                                self.WeatherTime = 0
                                self.weather = ""
                                WeatherDelta += 1

                                self.PreviousWeather = self.weather

                                self.Previous_Fog_Distance_Min = self.shadowmap["w_min"].value
                                self.Previous_Fog_Distance_Max = self.shadowmap["w_max"].value

                                self.Previous_color = self.color.value[0]

                                self.Previous_CloudsProgram_Alpha = self.CloudsProgram["WeatherAlpha"].value
                                self.Previous_CloudsProgram_CloudColor = self.CloudsProgram["CloudColor"].value

                                self.Previous_multiplier = self.CloudsProgram["CloudHeightMultiplier"].value

                                self.Previous_prog_transparency = self.skysphere_prog["transparency"].value

                                self.mod_game_engine_utils__.ComputeWeather.ComputeWeather(
                                    self)

                            self.aFPS += self.eFPS
                            self.iteration += 1

                            if self.detailed_captions:
                                self.mod_caption_utils__.generate_captions.GetOpenGLCaption(
                                    self,
                                    self)

                            self.total_move_x = 0
                            self.total_move_y = 0
                            self.total_move_z = 0

                            try:
                                if (self.mod_pygame__.mixer.Channel(2).get_busy() is False and
                                        self.sound):

                                    self.mod_sound_utils__.play_sound.play_ambient_sound(
                                        self)

                            except Exception as Message:
                                self.error_message = "".join(("GameEngine > GameEngine ",
                                                                    f"> __init__: {str(Message)}"))

                                self.error_message_detailed = "".join(
                                    self.mod_traceback__.format_exception(
                                        None,
                                        Message,
                                        Message.__traceback__))

                                self.mod_error_utils__.generate_error_screen.error_screen(
                                    self)

                            try:
                                if (self.mod_pygame__.mixer.Channel(4).get_busy() is False and
                                        self.sound and
                                        self.weather != "sunny"):

                                    self.mod_sound_utils__.play_sound.play_rain_sound(
                                        self)

                            except Exception as Message:
                                self.error_message = "".join(("GameEngine > GameEngine ",
                                                                    f"> __init__: {str(Message)}"))

                                self.error_message_detailed = "".join(
                                    self.mod_traceback__.format_exception(
                                        None,
                                        Message,
                                        Message.__traceback__))

                                self.mod_error_utils__.generate_error_screen.error_screen(
                                    self)

                            if self.frametime > 0:
                                self.eFPS = 1/self.frametime

                            self.Time_Percent = ((100/1056)*(self.GameTime))

                            self.mod_game_engine_utils__.ShadowmappingMathematics.ComputeCelestialEntities(
                                self)

                            self.ctx.enable(
                                self.mod_ModernGL__.DEPTH_TEST |
                                self.mod_ModernGL__.CULL_FACE)

                            # --- PASS 1: Render shadow map
                            self.mod_game_engine_utils__.ShadowmappingMathematics.ComputeShadows(
                                self)

                            # --- PASS 2: Render scene to screen
                            self.wnd.use()
                            cam = self.camera.matrix
                            self.x = int(self.camera.position.x*100)/100
                            self.y = int(self.camera.position.y*100)/100
                            self.z = int(self.camera.position.z*100)/100

                            cam[3][0] = 0
                            cam[3][1] = 0
                            cam[3][2] = 0

                            translation = self.mod_pyrr_Matrix44_.from_translation(
                                (0.0, 0.0, 0.0),
                                dtype="f4")

                            modelview = translation

                            self.skysphere_prog["m_proj"].write(
                                self.camera.projection.matrix)
                            self.skysphere_prog["m_model"].write(modelview)
                            self.skysphere_prog["m_camera"].write(cam)

                            self.particles_screen["projection"].write(
                                self.mod_game_engine_utils__.Particles.projection(self))

                            self.daycycleTime = self.time

                            if self.Time_Percent < 40:  # day
                                self.skysphere_prog["time"].value = 0
                                self.DefaultSkyCol = 1.0

                            elif self.Time_Percent < 50:  # sunset
                                self.DefaultSkyCol = 1 - \
                                    ((0.7/10)*(self.Time_Percent-40))
                                self.skysphere_prog["time"].value = (
                                    (19/10)*(self.Time_Percent-40))+1

                            elif self.Time_Percent < 90:  # night
                                self.skysphere_prog["time"].value = 21
                                self.DefaultSkyCol = 0.3

                            else:  # sunrise
                                self.DefaultSkyCol = 1 - \
                                    ((0.7/10)*(100-self.Time_Percent))
                                self.skysphere_prog["time"].value = 21 - \
                                    (((21/10)*(self.Time_Percent-90)))

                            self.CloudsProgram["DefaultSkyCol"] = self.DefaultSkyCol

                            self.ctx.front_face = "cw"

                            self.mod_game_engine_utils__.ComputeWeather.BlendWeather(
                                self)

                            if self.Thundertimer > self.Thundertimer_Target:
                                self.Thundertimer_Target = self.mod_random__.randint(
                                    5, 30)
                                self.Thundertimer = 0
                                self.Flashtimer = 0
                                self.Lightningtimer = 0
                                if self.show_strobe_effects:
                                    self.color.value = (1.0, 1.0, 1.0)
                                self.show_strobe_effects = True
                                self.ShowFlash = True
                                if self.sound:
                                    self.mod_sound_utils__.play_sound.play_thunder_sound(
                                        self)

                            if self.weather == "rain.heavy.thundery":
                                LightningDelay = self.mod_random__.randint(
                                    30, 75)/100
                                if (self.Lightningtimer > LightningDelay and
                                        self.show_strobe_effects):

                                    self.Flashtimer = 0
                                    self.DefaultSkyCol = 1
                                    self.Lightningtimer = 0
                                    self.show_strobe_effects = False
                                    self.ShowFlash = True

                            if self.ShowFlash:
                                if self.Flashtimer <= 1/60:
                                    self.DefaultSkyCol = 1
                                    if self.show_strobe_effects:
                                        self.color.value = (1.0, 1.0, 1.0)
                                else:
                                    self.ShowFlash = False

                            if self.weather != "sunny":
                                self.mod_pygame__.mixer.Channel(4).unpause()
                                if self.weather == "rain.light":
                                    RandomiseVolumeReduction = self.mod_random__.randint(
                                        2, 5)
                                    self.mod_pygame__.mixer.Channel(2).set_volume(
                                        (self.sound_volume/100)/RandomiseVolumeReduction)

                                    self.mod_pygame__.mixer.Channel(4).set_volume(
                                        (((self.sound_volume/100)*10)/100))

                                else:
                                    self.mod_pygame__.mixer.Channel(2).pause()
                                    if self.weather == "rain.heavy.thundery":
                                        self.mod_pygame__.mixer.Channel(4).set_volume(
                                            (((self.sound_volume/100)*30)/100)
                                        )
                                    else:
                                        self.mod_pygame__.mixer.Channel(4).set_volume(
                                            (((self.sound_volume/100)*20)/200)
                                        )

                            else:
                                self.mod_pygame__.mixer.Channel(4).pause()
                                self.mod_pygame__.mixer.Channel(2).set_volume(
                                    self.sound_volume/100)

                                self.mod_pygame__.mixer.Channel(2).unpause()

                            if self.weather != "sunny":
                                self.ctx.enable(self.mod_ModernGL__.BLEND)

                            self.SkyBox_texture_Sun.use(location=0)
                            self.SkySphere.render(self.skysphere_prog)

                            if self.weather != "sunny":
                                self.ctx.disable(self.mod_ModernGL__.BLEND)

                            self.ctx.front_face = "ccw"

                            # pass 5: Render the sun position
                            self.moon.render(self.moon_prog)
                            self.sun.render(self.sun_prog)

                            self.ctx.front_face = "cw"

                            if self.weather != "sunny":
                                self.particles_transform["ft"].value = self.frametime

                                self.mod_game_engine_utils__.Particles.emit_gpu(
                                    self,
                                    self.time,
                                    self.frametime)

                            self.CloudPos = self.mod_pyrr_Vector3_(
                                (self.camera.position.x,
                                0,
                                self.camera.position.z),
                                dtype="f4")

                            self.CloudsProgram["m_proj"].write(
                                self.camera.projection.matrix)
                            self.CloudsProgram["m_camera"].write(self.camera.matrix)
                            self.CloudsProgram["m_model"].write(
                                self.mod_pyrr_Matrix44_.from_translation(
                                    self.CloudPos,
                                    dtype="f4"))

                            # shadows, variable rendering maybe

                            self.CloudsProgram["X_Offset"] = self.mod_math__.sin(
                                self.time/50)/10
                            self.CloudsProgram["Y_Offset"] = self.mod_math__.cos(
                                self.time/50)/10

                            self.cloud_texture.use(location=0)

                            self.ctx.enable(self.mod_ModernGL__.BLEND)

                            self.vao.render(
                                mode=self.mod_ModernGL__.TRIANGLE_STRIP)

                            self.ctx.blend_func = self.mod_ModernGL__.DEFAULT_BLENDING
                            # pass 2: render the scene and retro project depth shadow-map
                            # counter clock wise -> render front faces

                            self.sampler_depth.use(location=0)
                            self.tex_depth.use(location=0)
                            self.cloud_texture.use(location=0)

                            self.ctx.front_face = "ccw"

                            # pass 4: render textured scene with shadow

                            self.objects["map"].render()
                            self.ctx.disable(self.mod_ModernGL__.BLEND)

                            if self.weather == "rain.heavy.thundery" and self.LengthenStorm:
                                switchWeather = switchWeather*(self.mod_random__.randint(
                                    15,
                                    30)/10)
                                self.LengthenStorm = False

                            self.mod_game_engine_utils__.OnscreenEventFunction.game_events(
                                self)

                            self.iteration += 1
                            
                            if self.OnStart:
                                self.OnStart = False

                                GameEngine_Initialisation = False

                                if self.from_game_GUI is False:
                                    Currentload_time = self.mod_time__.perf_counter()-self.StartLoading
                                    self.load_time = [
                                        self.load_time[0] + Currentload_time,
                                        self.load_time[1] + 1]

                                else:
                                    self.from_game_GUI = False

                            if (self.FPS_overclock is False and
                                    self.vsync is False):
                                try:
                                    ComputedPause = self.mod_time__.perf_counter()-start
                                    self.mod_time__.sleep(
                                        (1/self.FPS)-ComputedPause)

                                except Exception as Message:
                                    log_message = "GameEngine > GameEngine > __init__: " + \
                                        str(Message)

                                    self.mod_logging_utils__.create_log_message.update_log_warning(
                                        self,
                                        log_message)

                                    self.mod_time__.sleep((1/self.FPS))

                            # Swap around objects for next frame
                            try:
                                self.wnd.swap_buffers()
                            except Exception as Message:
                                print(Message)

                            if self.weather != "sunny":
                                self.transform_vao1, self.transform_vao2 = self.transform_vao2, self.transform_vao1
                                self.render_vao1, self.render_vao2 = self.render_vao2, self.render_vao1
                                self.vbo1, self.vbo2 = self.vbo2, self.vbo1

                            self.frametime = self.mod_time__.perf_counter()-start
                            self.time += self.frametime
                            self.GameTime += self.frametime
                            self.WeatherTime += self.frametime

                            if self.weather == "rain.heavy.thundery":
                                if self.mod_pygame__.mixer.Channel(3).get_busy() is False:
                                    self.Thundertimer += self.frametime

                                self.Lightningtimer += self.frametime
                                self.Flashtimer += self.frametime

                            self.play_time = self.time

                            Message = self.ctx.error
                            if (Message != "GL_NO_ERROR" and Message != "GL_INVALID_OPERATION"):
                                try:
                                    self.wnd.close()
                                    self.error_message = "".join(("GameEngine > GameEngine ",
                                                                        f"> __init__: {str(Message)}"))

                                    self.error_message_detailed = self.error_message

                                    self.mod_error_utils__.generate_error_screen.error_screen(
                                        self)

                                except Exception as Message2:
                                    log_message = "GameEngine > GameEngine > __init__: " + \
                                        str(Message)

                                    self.mod_logging_utils__.create_log_message.update_log_warning(
                                        self,
                                        log_message)

                                    log_message = "GameEngine > GameEngine > __init__: " + \
                                        str(Message2)

                                    self.mod_logging_utils__.create_log_message.update_log_warning(
                                        self,
                                        log_message)

                        self.command = "Undefined"
                        self.from_play = True
                        self.fullscreen = not self.wnd.fullscreen
                        self.wnd.close()
                                    
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

            try:
                moderngl_window.run_window_config(GameEngine)
                
            except Exception as Message:
                print(Message)
