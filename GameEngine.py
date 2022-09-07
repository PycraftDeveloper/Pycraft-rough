if __name__ != "__main__":
    import os
    if ("site-packages" in os.path.dirname(__file__) or
            "dist-packages" in os.path.dirname(__file__)):
        try:
            from pycraft import DataTransferUtils

        except:
            import DataTransferUtils

    else:
        import DataTransferUtils

    shared_data = DataTransferUtils.data_transfer.loadData()

    import os
    shared_data.mod_OS__ = os

    import traceback
    shared_data.mod_traceback__ = traceback

    import datetime
    shared_data.mod_datetime__ = datetime

    import platform
    shared_data.mod_platform__ = platform

    import json
    shared_data.mod_json__ = json

    import pygame
    shared_data.mod_pygame__ = pygame

    import pyautogui
    shared_data.mod_pyautogui__ = pyautogui

    import random
    shared_data.mod_random__ = random

    if ("site-packages" in shared_data.base_folder or
            "dist-packages" in shared_data.base_folder):

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

    shared_data.mod_module_utils__ = ModuleUtils
    shared_data.mod_logging_utils__ = LoggingUtils
    shared_data.mod_error_utils__ = ErrorUtils
    shared_data.mod_file_utils__ = FileUtils
    shared_data.mod_registry__ = Registry

    shared_data.mod_logging_utils__.create_log_message.update_log_information(
        shared_data, "Imported os")
    shared_data.mod_logging_utils__.create_log_message.update_log_information(
        shared_data, "Imported traceback")
    shared_data.mod_logging_utils__.create_log_message.update_log_information(
        shared_data, "Imported datetime")
    shared_data.mod_logging_utils__.create_log_message.update_log_information(
        shared_data, "Imported platform")
    shared_data.mod_logging_utils__.create_log_message.update_log_information(
        shared_data, "Imported json")
    shared_data.mod_logging_utils__.create_log_message.update_log_information(
        shared_data, "Imported pygame")
    shared_data.mod_logging_utils__.create_log_message.update_log_information(
        shared_data, "Imported pyautogui")
    shared_data.mod_logging_utils__.create_log_message.update_log_information(
        shared_data, "Imported random")

    shared_data.mod_logging_utils__.create_log_message.update_log_information(
        shared_data, "Imported ModuleUtils")
    shared_data.mod_logging_utils__.create_log_message.update_log_information(
        shared_data, "Imported LoggingUtils")
    shared_data.mod_logging_utils__.create_log_message.update_log_information(
        shared_data, "Imported ErrorUtils")
    shared_data.mod_logging_utils__.create_log_message.update_log_information(
        shared_data, "Imported FileUtils")
    shared_data.mod_logging_utils__.create_log_message.update_log_information(
        shared_data, "Imported Registry")

    shared_data.mod_module_utils__.initialize_modules.initialize_external_modules(
        shared_data)
    shared_data.mod_module_utils__.initialize_modules.initialize_internal_modules(
        shared_data)

    shared_data.clock = shared_data.mod_pygame__.time.Clock()
    shared_data.fullscreen_x = shared_data.mod_pyautogui__.size()[
                                                                0]
    shared_data.fullscreen_y = shared_data.mod_pyautogui__.size()[
                                                                1]
    shared_data.mod_pygame__.init()

    if shared_data.platform == "Linux":
        shared_data.title_font = shared_data.mod_pygame__.font.Font(
            shared_data.mod_OS__.path.join(
                shared_data.base_folder,
                ("fonts//Book Antiqua.ttf")), 60)

        shared_data.window_icon = shared_data.mod_pygame__.image.load(
            shared_data.mod_OS__.path.join(
                shared_data.base_folder,
                ("resources//general resources//Icon.png")))

    else:
        shared_data.window_icon = shared_data.mod_pygame__.image.load(
            shared_data.mod_OS__.path.join(
                shared_data.base_folder,
                ("resources\\general resources\\Icon.png")))

        shared_data.title_font = shared_data.mod_pygame__.font.Font(
            shared_data.mod_OS__.path.join(
                shared_data.base_folder,
                ("fonts\\Book Antiqua.ttf")), 60)

    shared_data.mod_ModernGL_window_.setup_basic_logging(0)
    
    class GameEngine(shared_data.mod_base__.CameraWindow):
        shared_data.mod_base__.CameraWindow.title = f"Pycraft: v{shared_data.version}: Playing"
        shared_data.mod_base__.CameraWindow.resource_dir = shared_data.base_folder
        shared_data.mod_base__.CameraWindow.vsync = shared_data.vsync
        shared_data.mod_base__.CameraWindow.resizable = True
        shared_data.mod_base__.CameraWindow.window_size = (
            shared_data.real_window_width,
            shared_data.real_window_height)

        if shared_data.aa:
            shared_data.mod_base__.CameraWindow.samples = int(str(shared_data.aa_quality).split("x")[0])

        def __init__(self, **kwargs):
            try:
                global GameEngine_Initialisation
                global GameLoadProgressPercent

                GameLoadProgressPercent = 0

                self.Joystick_Rotation = [0, 0]

                WindowSize = shared_data.real_window_width, shared_data.real_window_height
                CurrentWindowSize = WindowSize

                self.StartLoading = shared_data.mod_time__.perf_counter()

                GameLoadProgressPercent = 10

                GameEngine_Initialisation = True

                CreateLoadScreen = shared_data.mod_threading__.Thread(
                    target=shared_data.mod_game_engine__.CreateEngine.RenderLoaddisplay)

                CreateLoadScreen.start()
                CreateLoadScreen.name = "Thread_CreateLoadScreen"

                #print(1)
                super().__init__(**kwargs)
                #print(2)
                if shared_data.aa:
                    self.samples = int(str(shared_data.aa_quality).split("x")[0])
                else:
                    self.samples = 1

                try:
                    displayPosition = shared_data.mod_display_utils__.display_utils.get_display_location(
                        shared_data)
                    
                except Exception as Message:
                    log_message = "GameEngine > GameEngine > __init__: "+str(Message)
                    
                    shared_data.mod_logging_utils__.create_log_message.update_log_warning(
                        shared_data,
                        log_message)
                    
                    CurrentWindowSize = self.window_size
                    displayPosition = (int((shared_data.fullscreen_x-CurrentWindowSize[0])/2),
                                        int((shared_data.fullscreen_y-CurrentWindowSize[1])/2))

                self.skybox_distance = 1600

                self.camera.projection.update(
                    near=1,
                    far=self.skybox_distance,
                    fov=70)

                self.wnd.mouse_exclusivity = True

                if shared_data.fullscreen:
                    self.wnd.position = displayPosition
                    shared_data.mod_base__.CameraWindow.resize(
                        self,
                        self.wnd.size[0],
                        self.wnd.size[1])

                try:
                    if shared_data.platform == "Linux":
                        self.wnd.set_icon(
                            shared_data.mod_OS__.path.join(
                                shared_data.base_folder,
                                ("resources//general resources//Icon.png")))
                    else:
                        self.wnd.set_icon(
                            shared_data.mod_OS__.path.join(
                                shared_data.base_folder,
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
                self.offscreen_depth.filter = (shared_data.mod_ModernGL__.LINEAR,
                                               shared_data.mod_ModernGL__.LINEAR)

                self.offscreen = self.ctx.framebuffer(depth_attachment=self.offscreen_depth,)

                self.sun_radius = 50

                self.sun = shared_data.mod_ModernGL_window_geometry.sphere(
                    radius=self.sun_radius)

                self.moon = shared_data.mod_ModernGL_window_geometry.sphere(
                    radius=80)

                self.rain_particle = shared_data.mod_ModernGL_window_geometry.sphere(
                    radius=1)

                GameLoadProgressPercent = 30

                # Debug geometry
                self.offscreen_quad = shared_data.mod_ModernGL_window_geometry.quad_2d(
                    size=(0.5, 0.5),
                    pos=(0.75, 0.75))

                self.offscreen_quad2 = shared_data.mod_ModernGL_window_geometry.quad_2d(
                    size=(0.5, 0.5),
                    pos=(0.25, 0.75))

                self.SkySphere = shared_data.mod_ModernGL_window_geometry.sphere(
                    radius=self.skybox_distance)

                self.objects: shared_data.mod_typing__.Dict[
                    str,
                    shared_data.mod_ModernGL__.VertexArray] = {}

                self.objects_shadow: shared_data.mod_typing__.Dict[
                    str,
                    shared_data.mod_ModernGL__.VertexArray] = {}

                if shared_data.platform == "Linux":
                    # Use 'u' to do things with UVs that this really needs
                    self.scene: shared_data.mod_ModernGL_window_.scene.Scene = self.load_scene(
                        shared_data.mod_OS__.path.join(
                            shared_data.base_folder,
                            ("resources//game engine resources//map//map2.obj")),
                        cache=True)
                else:
                    self.scene: shared_data.mod_ModernGL_window_.scene.Scene = self.load_scene(
                        shared_data.mod_OS__.path.join(
                            shared_data.base_folder,
                            ("resources\\game engine resources\\map\\map.obj")),
                        cache=True)

                GameLoadProgressPercent = 40

                if shared_data.platform == "Linux":
                    self.SkyBox_texture_Sun = self.load_texture_array(
                        shared_data.mod_OS__.path.join(
                            shared_data.base_folder,
                            ("resources//game engine resources//skysphere//ClearSkyTransition.gif")),
                        anisotropy=self.samples)

                else:
                    self.SkyBox_texture_Sun = self.load_texture_array(
                        shared_data.mod_OS__.path.join(
                            shared_data.base_folder,
                            ("resources\\game engine resources\\skysphere\\ClearSkyTransition.gif")),
                        anisotropy=self.samples)
                        
                GameLoadProgressPercent = 50
                
                # Programs
                shared_data.mod_game_engine_utils__.LoadPrograms.LoadProgramFiles(self)

                shared_data.mod_game_engine_utils__.LoadPrograms.LoadProgramText(self)

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

                if shared_data.fancy_particles:
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
                    log_message = "GameEngine > GameEngine > __init__: "+str(Message)
                    
                    shared_data.mod_logging_utils__.create_log_message.update_log_warning(
                        shared_data,
                        log_message)
                    
                    self.vbo1 = self.ctx.buffer(reserve=self.N * self.stride, dynamic=True)
                    self.vbo2 = self.ctx.buffer(reserve=self.N * self.stride, dynamic=True)
                # Write some initial particles
                self.vbo1.write(
                    shared_data.mod_numpy__.fromiter(
                        shared_data.mod_game_engine_utils__.Particles.gen_particles(
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

                self.gpu_emitter_vao = self.ctx._vertex_array(self.gpu_emitter_particles, [])

                # Query object to inspect render calls
                self.query = self.ctx.query(primitives=True)

                # Cycle emit methods per frame
                self.particles_screen["projection"].write(
                    shared_data.mod_game_engine_utils__.Particles.projection(
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

                if shared_data.platform == "Linux":
                    self.tex1 = self.load_texture_2d(
                        shared_data.mod_OS__.path.join(
                            shared_data.base_folder,
                            ("resources//game engine resources//map//GrassTexture.png")),
                        mipmap=True,
                        anisotropy=self.samples)

                    self.tex2 = self.load_texture_2d(
                        shared_data.mod_OS__.path.join(
                            shared_data.base_folder,
                            ("resources//game engine resources//map//RockTexture.png")),
                        mipmap=True,
                        anisotropy=self.samples)

                else:
                    self.tex1 = self.load_texture_2d(
                        shared_data.mod_OS__.path.join(
                            shared_data.base_folder,
                            ("resources\\game engine resources\\map\\GrassTexture.png")),
                        mipmap=True,
                        anisotropy=self.samples)

                    self.tex2 = self.load_texture_2d(
                        shared_data.mod_OS__.path.join(
                            shared_data.base_folder,
                            ("resources\\game engine resources\\map\\RockTexture.png")),
                        mipmap=True,
                        anisotropy=self.samples)
                        
                self.tex1.use(location=1)
                self.tex2.use(location=2)

                SHADOW_SIZE: shared_data.mod_typing_Final[int] = 2 << 7

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
                    filter=(shared_data.mod_ModernGL__.LINEAR,
                            shared_data.mod_ModernGL__.LINEAR),
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

                CloudData = shared_data.mod_game_engine_utils__.ComputeWeather.ComputeCloudNoise(
                    self,
                    size)

                self.range = shared_data.mod_numpy__.max(CloudData) - shared_data.mod_numpy__.min(CloudData)

                self.CloudsProgram["CloudHeight"] = 500.0
                self.CloudsProgram["height_max"] = self.range
                self.CloudsProgram["render_fog"] = shared_data.render_fog

                self.shadowmap["render_fog"] = shared_data.render_fog

                vertices, index = shared_data.mod_game_engine_utils__.ComputeWeather.ComputeCloudModel(
                    self,
                    size[0])

                self.vbo = self.ctx.buffer(vertices.astype("f4"))
                self.ibo = self.ctx.buffer(index.astype("i4"))

                cloud_vao_content = [(
                    self.vbo,
                    "2f",
                    "in_vert"),]

                self.vao = self.ctx.vertex_array(
                    self.CloudsProgram,
                    cloud_vao_content,
                    self.ibo)

                if shared_data.platform == "Linux":
                    self.cloud_texture = self.load_texture_2d(
                        shared_data.mod_OS__.path.join(
                            shared_data.base_folder,
                            ("resources//game engine resources//clouds//Rnd_noise.png")),
                        anisotropy=self.samples)

                else:
                    self.cloud_texture = self.load_texture_2d(
                        shared_data.mod_OS__.path.join(
                            shared_data.base_folder,
                            ("resources\\game engine resources\\clouds\\Rnd_noise.png")),
                        anisotropy=self.samples)

                GameLoadProgressPercent = 90

                if shared_data.fullscreen is False:
                    self.wnd.fullscreen = True

                self.OnStart = True

                self.time = 0
                self.frametime = 1

                self.Running = True

                self.Inventory = False
                self.Map = False

                shared_data.mod_globals__.Share.initialize_controller_game(self)

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

                shared_data.mod_game_engine_utils__.ComputeWeather.ComputeWeather(self)

                self.WeatherTime = 0
                self.Thundertimer = 0
                self.Lightningtimer = 0
                self.show_strobe_effects = False
                self.Thundertimer_Target = shared_data.mod_random__.randint(15, 30)
                switchWeather = shared_data.mod_random__.randint(60, 120)
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
                    start = shared_data.mod_time__.perf_counter()
                    self.GameTimeDelta = self.time
                    if self.Inventory or self.Map:
                        shared_data.mod_game_engine_utils__.AccessOtherGUIs.AccessGUI(self)

                    if shared_data.mod_pygame__.mixer.music.get_busy():
                        shared_data.mod_pygame__.mixer.music.pause()

                    self.keys = self.wnd.keys

                    self.wnd.clear()
                    self.ctx.clear(self.DefaultSkyCol,
                                   self.DefaultSkyCol,
                                   self.DefaultSkyCol)

                    if self.WeatherTime >= switchWeather:
                        switchWeather = shared_data.mod_random__.randint(60, 120)
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

                        shared_data.mod_game_engine_utils__.ComputeWeather.ComputeWeather(self)

                    shared_data.aFPS += shared_data.eFPS
                    shared_data.iteration += 1

                    if shared_data.detailed_captions:
                        shared_data.mod_caption_utils__.generate_captions.GetOpenGLCaption(
                            shared_data,
                            self)

                    shared_data.total_move_x = 0
                    shared_data.total_move_y = 0
                    shared_data.total_move_z = 0

                    try:
                        if (shared_data.mod_pygame__.mixer.Channel(2).get_busy() is False and
                                shared_data.sound):

                            shared_data.mod_sound_utils__.play_sound.play_ambient_sound(shared_data)
                            
                    except Exception as Message:
                        shared_data.error_message = "".join(("GameEngine > GameEngine ",
                                                                f"> __init__: {str(Message)}"))

                        shared_data.error_message_detailed = "".join(
                            self.mod_traceback__.format_exception(
                                None,
                                Message,
                                Message.__traceback__))

                        shared_data.mod_error_utils__.generate_error_screen.error_screen(
                            shared_data)

                    try:
                        if (shared_data.mod_pygame__.mixer.Channel(4).get_busy() is False and
                                shared_data.sound and
                                self.weather != "sunny"):

                            shared_data.mod_sound_utils__.play_sound.play_rain_sound(shared_data)
                            
                    except Exception as Message:
                        shared_data.error_message = "".join(("GameEngine > GameEngine ",
                                                                f"> __init__: {str(Message)}"))

                        shared_data.error_message_detailed = "".join(
                            self.mod_traceback__.format_exception(
                                None,
                                Message,
                                Message.__traceback__))

                        shared_data.mod_error_utils__.generate_error_screen.error_screen(
                            shared_data)

                    if self.frametime > 0:
                        shared_data.eFPS = 1/self.frametime

                    self.Time_Percent = ((100/1056)*(self.GameTime))

                    shared_data.mod_game_engine_utils__.ShadowmappingMathematics.ComputeCelestialEntities(
                        self)

                    self.ctx.enable(
                        shared_data.mod_ModernGL__.DEPTH_TEST |
                        shared_data.mod_ModernGL__.CULL_FACE)

                    # --- PASS 1: Render shadow map
                    shared_data.mod_game_engine_utils__.ShadowmappingMathematics.ComputeShadows(
                        self)

                    # --- PASS 2: Render scene to screen
                    self.wnd.use()
                    cam = self.camera.matrix
                    shared_data.x = int(self.camera.position.x*100)/100
                    shared_data.y = int(self.camera.position.y*100)/100
                    shared_data.z = int(self.camera.position.z*100)/100

                    cam[3][0] = 0
                    cam[3][1] = 0
                    cam[3][2] = 0

                    translation = shared_data.mod_pyrr_Matrix44_.from_translation(
                        (0.0, 0.0, 0.0),
                        dtype="f4")

                    modelview = translation

                    self.skysphere_prog["m_proj"].write(self.camera.projection.matrix)
                    self.skysphere_prog["m_model"].write(modelview)
                    self.skysphere_prog["m_camera"].write(cam)

                    self.particles_screen["projection"].write(shared_data.mod_game_engine_utils__.Particles.projection(self))

                    self.daycycleTime = self.time

                    if self.Time_Percent < 40: # day
                        self.skysphere_prog["time"].value = 0
                        self.DefaultSkyCol = 1.0

                    elif self.Time_Percent < 50: # sunset
                        self.DefaultSkyCol = 1-((0.7/10)*(self.Time_Percent-40))
                        self.skysphere_prog["time"].value = ((19/10)*(self.Time_Percent-40))+1

                    elif self.Time_Percent < 90: # night
                        self.skysphere_prog["time"].value = 21
                        self.DefaultSkyCol = 0.3

                    else: # sunrise
                        self.DefaultSkyCol = 1-((0.7/10)*(100-self.Time_Percent))
                        self.skysphere_prog["time"].value = 21-(((21/10)*(self.Time_Percent-90)))

                    self.CloudsProgram["DefaultSkyCol"] = self.DefaultSkyCol

                    self.ctx.front_face = "cw"

                    shared_data.mod_game_engine_utils__.ComputeWeather.BlendWeather(
                        self)

                    if self.Thundertimer > self.Thundertimer_Target:
                        self.Thundertimer_Target = shared_data.mod_random__.randint(5, 30)
                        self.Thundertimer = 0
                        self.Flashtimer = 0
                        self.Lightningtimer = 0
                        if shared_data.show_strobe_effects:
                            self.color.value = (1.0, 1.0, 1.0)
                        self.show_strobe_effects = True
                        self.ShowFlash = True
                        if shared_data.sound:
                            shared_data.mod_sound_utils__.play_sound.play_thunder_sound(
                                shared_data)

                    if self.weather == "rain.heavy.thundery":
                        LightningDelay = shared_data.mod_random__.randint(30, 75)/100
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
                            if shared_data.show_strobe_effects:
                                self.color.value = (1.0, 1.0, 1.0)
                        else:
                            self.ShowFlash = False

                    if self.weather != "sunny":
                        shared_data.mod_pygame__.mixer.Channel(4).unpause()
                        if self.weather == "rain.light":
                            RandomiseVolumeReduction = shared_data.mod_random__.randint(2, 5)
                            shared_data.mod_pygame__.mixer.Channel(2).set_volume(
                                (shared_data.sound_volume/100)/RandomiseVolumeReduction)

                            shared_data.mod_pygame__.mixer.Channel(4).set_volume(
                                (((shared_data.sound_volume/100)*10)/100))

                        else:
                            shared_data.mod_pygame__.mixer.Channel(2).pause()
                            if self.weather == "rain.heavy.thundery":
                                shared_data.mod_pygame__.mixer.Channel(4).set_volume(
                                    (((shared_data.sound_volume/100)*30)/100)
                                )
                            else:
                                shared_data.mod_pygame__.mixer.Channel(4).set_volume(
                                    (((shared_data.sound_volume/100)*20)/200)
                                )

                    else:
                        shared_data.mod_pygame__.mixer.Channel(4).pause()
                        shared_data.mod_pygame__.mixer.Channel(2).set_volume(
                            shared_data.sound_volume/100)

                        shared_data.mod_pygame__.mixer.Channel(2).unpause()

                    if self.weather != "sunny":
                        self.ctx.enable(shared_data.mod_ModernGL__.BLEND)

                    self.SkyBox_texture_Sun.use(location=0)
                    self.SkySphere.render(self.skysphere_prog)

                    if self.weather != "sunny":
                        self.ctx.disable(shared_data.mod_ModernGL__.BLEND)

                    self.ctx.front_face = "ccw"

                    # pass 5: Render the sun position
                    self.moon.render(self.moon_prog)
                    self.sun.render(self.sun_prog)

                    self.ctx.front_face = "cw"

                    if self.weather != "sunny":
                        self.particles_transform["ft"].value = self.frametime

                        shared_data.mod_game_engine_utils__.Particles.emit_gpu(
                            self,
                            self.time,
                            self.frametime)

                    self.CloudPos = shared_data.mod_pyrr_Vector3_(
                            (self.camera.position.x,
                            0,
                            self.camera.position.z),
                        dtype="f4")

                    self.CloudsProgram["m_proj"].write(self.camera.projection.matrix)
                    self.CloudsProgram["m_camera"].write(self.camera.matrix)
                    self.CloudsProgram["m_model"].write(
                        shared_data.mod_pyrr_Matrix44_.from_translation(
                            self.CloudPos,
                            dtype="f4"))

                     # shadows, variable rendering maybe

                    self.CloudsProgram["X_Offset"] = shared_data.mod_math__.sin(self.time/50)/10
                    self.CloudsProgram["Y_Offset"] = shared_data.mod_math__.cos(self.time/50)/10

                    self.cloud_texture.use(location=0)

                    self.ctx.enable(shared_data.mod_ModernGL__.BLEND)

                    self.vao.render(mode=shared_data.mod_ModernGL__.TRIANGLE_STRIP)

                    self.ctx.blend_func = shared_data.mod_ModernGL__.DEFAULT_BLENDING
                    # pass 2: render the scene and retro project depth shadow-map
                    # counter clock wise -> render front faces

                    self.sampler_depth.use(location=0)
                    self.tex_depth.use(location=0)
                    self.cloud_texture.use(location=0)

                    self.ctx.front_face = "ccw"

                    # pass 4: render textured scene with shadow

                    self.objects["map"].render()
                    self.ctx.disable(shared_data.mod_ModernGL__.BLEND)

                    if self.weather == "rain.heavy.thundery" and self.LengthenStorm:
                        switchWeather = switchWeather*(shared_data.mod_random__.randint(
                            15,
                            30)/10)
                        self.LengthenStorm = False

                    shared_data.mod_game_engine_utils__.OnscreenEventFunction.game_events(self)

                    shared_data.iteration += 1
                    if self.OnStart:
                        self.OnStart = False

                        GameEngine_Initialisation = False

                        if shared_data.from_game_GUI is False:
                            Currentload_time = shared_data.mod_time__.perf_counter()-self.StartLoading
                            shared_data.load_time = [
                                shared_data.load_time[0] + Currentload_time,
                                shared_data.load_time[1] + 1]

                        else:
                            shared_data.from_game_GUI = False

                    if (shared_data.FPS_overclock is False and
                            shared_data.vsync is False):
                        try:
                            ComputedPause = shared_data.mod_time__.perf_counter()-start
                            shared_data.mod_time__.sleep((1/shared_data.FPS)-ComputedPause)
                            
                        except Exception as Message:
                            log_message = "GameEngine > GameEngine > __init__: "+str(Message)
                            
                            shared_data.mod_logging_utils__.create_log_message.update_log_warning(
                                shared_data,
                                log_message)
                            
                            shared_data.mod_time__.sleep((1/shared_data.FPS))

                    # Swap around objects for next frame
                    self.wnd.swap_buffers()

                    if self.weather != "sunny":
                        self.transform_vao1, self.transform_vao2 = self.transform_vao2, self.transform_vao1
                        self.render_vao1, self.render_vao2 = self.render_vao2, self.render_vao1
                        self.vbo1, self.vbo2 = self.vbo2, self.vbo1

                    self.frametime = shared_data.mod_time__.perf_counter()-start
                    self.time += self.frametime
                    self.GameTime += self.frametime
                    self.WeatherTime += self.frametime

                    if self.weather == "rain.heavy.thundery":
                        if shared_data.mod_pygame__.mixer.Channel(3).get_busy() is False:
                            self.Thundertimer += self.frametime

                        self.Lightningtimer += self.frametime
                        self.Flashtimer += self.frametime

                    shared_data.play_time = self.time

                    Message = self.ctx.error
                    if (Message != "GL_NO_ERROR" and Message != "GL_INVALID_OPERATION"):
                        try:
                            self.wnd.close()
                            shared_data.error_message = "".join(("GameEngine > GameEngine ",
                                                                    f"> __init__: {str(Message)}"))

                            shared_data.error_message_detailed = shared_data.error_message

                            shared_data.mod_error_utils__.generate_error_screen.error_screen(
                                shared_data)

                        except Exception as Message2:
                            log_message = "GameEngine > GameEngine > __init__: "+str(Message)
                            
                            shared_data.mod_logging_utils__.create_log_message.update_log_warning(
                                self,
                                log_message)

                            log_message = "GameEngine > GameEngine > __init__: "+str(Message2)
                            
                            shared_data.mod_logging_utils__.create_log_message.update_log_warning(
                                self,
                                log_message)

                shared_data.command = "Undefined"
                shared_data.from_play = True
                shared_data.fullscreen = not self.wnd.fullscreen
                self.wnd.close()
                shared_data.mod_pygame__.display.quit()
                shared_data.mod_pygame__.init()
                shared_data.mod_main__.Initialize.menu_selector(self)
                
            except Exception as Message:
                shared_data.mod_game_engine_utils__.Crash.CreateReport(self, Message)

    class CreateEngine:
        def __init__(self):
            pass


        def RenderLoaddisplay():
            try:
                shared_data.mod_pygame__.display.init()
                
                shared_data.mod_caption_utils__.generate_captions.get_normal_caption(
                    shared_data,
                    "Loading Pycraft")

                shared_data.mod_display_utils__.display_utils.set_display(shared_data)

                if shared_data.platform == "Linux":
                    SecondaryFont = shared_data.mod_pygame__.font.Font(
                        shared_data.mod_OS__.path.join(
                            shared_data.base_folder,
                            ("fonts//Book Antiqua.ttf")), 35)

                    LoadingFont = shared_data.mod_pygame__.font.Font(
                        shared_data.mod_OS__.path.join(
                            shared_data.base_folder,
                            ("fonts//Book Antiqua.ttf")), 15)

                    LoadingTextFont = shared_data.mod_pygame__.font.Font(
                        shared_data.mod_OS__.path.join(
                            shared_data.base_folder,
                            ("fonts//Book Antiqua.ttf")), 15)

                else:
                    SecondaryFont = shared_data.mod_pygame__.font.Font(
                        shared_data.mod_OS__.path.join(
                            shared_data.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 35)

                    LoadingFont = shared_data.mod_pygame__.font.Font(
                        shared_data.mod_OS__.path.join(
                            shared_data.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 15)

                    LoadingTextFont = shared_data.mod_pygame__.font.Font(
                        shared_data.mod_OS__.path.join(
                            shared_data.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 15)

                global GameEngine_Initialisation
                global GameLoadProgressPercent

                time = 0

                shared_data.clock = shared_data.mod_pygame__.time.Clock()

                shared_data.skysphere_progress_message_text = shared_data.mod_text_utils__.GenerateText.LoadQuickText(shared_data)

                Completion_Percentage = 0

                Averageload_time = shared_data.load_time[0]/shared_data.load_time[1]

                while GameEngine_Initialisation:
                    print(GameLoadProgressPercent)
                    eFPS = shared_data.clock.get_fps()
                    if shared_data.load_time[0] != 0:
                        if eFPS > 0:
                            time += 1/eFPS

                        Loading_Line_X_value = (((shared_data.real_window_width-200)/Averageload_time)*time)+100

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

                    shared_data.skysphere_progress_line = [
                        (100, shared_data.real_window_height-100),
                        (100, shared_data.real_window_height-100)]

                    if shared_data.load_time[0] != 0:
                        if Loading_Line_X_value > shared_data.real_window_width-100:
                            Loading_Line_X_value = shared_data.real_window_width-100

                        shared_data.skysphere_progress_line.append((Loading_Line_X_value, shared_data.real_window_height-100))
                        Completion_Percentage = (100/(shared_data.load_time[0]/shared_data.load_time[1]))*time
                        
                        if Completion_Percentage > 100:
                            Completion_Percentage = 100
                            
                    else:
                        shared_data.skysphere_progress_line.append((
                            ((shared_data.real_window_width/100)*GameLoadProgressPercent)-100,
                            shared_data.real_window_height-100))

                        Completion_Percentage = GameLoadProgressPercent

                    shared_data.mod_game_engine__.CreateEngine.GenerateLoaddisplay(
                        LoadingFont,
                        text,
                        SecondaryFont,
                        LoadingTextFont,
                        Completion_Percentage)

                    for event in shared_data.mod_pygame__.event.get():
                        if (event.type == shared_data.mod_pygame__.QUIT or
                            (event.type == shared_data.mod_pygame__.KEYDOWN and
                             event.key == shared_data.mod_pygame__.K_ESCAPE)):

                            global Global_Save_and_QUIT
                            Global_Save_and_QUIT = True
                            quit()

                    shared_data.mod_pygame__.display.flip()

                    tempFPS = shared_data.mod_display_utils__.display_utils.get_play_status(shared_data)

                    shared_data.clock.tick(tempFPS)

                if shared_data.load_time[1] >= 25:
                    shared_data.load_time = [0, 1]

                #shared_data.mod_pygame__.display.quit()
                shared_data.mod_pygame__.init()
                
            except Exception as Message:
                print(Message)
                shared_data.error_message = "GameEngine > CreateEngine > RenderLoaddisplay: "+str(Message)
                shared_data.error_message_detailed = "".join(
                    shared_data.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                shared_data.mod_error_utils__.generate_error_screen.error_screen(shared_data)


        def GenerateLoaddisplay(LoadingFont,text, SecondaryFont,LoadingTextFont, Completion_Percentage):
            try:
                shared_data.display.fill(shared_data.background_color)

                shared_data.real_window_width = shared_data.mod_pygame__.display.get_window_size()[0]
                shared_data.real_window_height = shared_data.mod_pygame__.display.get_window_size()[1]

                PycraftTitle = shared_data.title_font.render(
                    "Pycraft",
                    shared_data.aa,
                    shared_data.font_color)
                                
                title_width = PycraftTitle.get_width()

                shared_data.display.blit(
                    PycraftTitle,
                    ((shared_data.real_window_width-title_width)/2, 0))

                LoadingTitle = SecondaryFont.render(
                    "Loading",
                    shared_data.aa,
                    shared_data.secondary_font_color)
                shared_data.display.blit(
                    LoadingTitle,
                    (((shared_data.real_window_width-title_width)/2)+55, 50))

                shared_data.mod_pygame__.draw.lines(
                    shared_data.display,
                    shared_data.shape_color,
                    shared_data.aa,
                    [(100, shared_data.real_window_height-100),
                     (shared_data.real_window_width-100, shared_data.real_window_height-100)],
                    3)

                shared_data.mod_pygame__.draw.lines(
                    shared_data.display,
                    shared_data.accent_color,
                    shared_data.aa,
                    shared_data.skysphere_progress_line)

                displayMessage = LoadingFont.render(
                    shared_data.skysphere_progress_message_text,
                    shared_data.aa,
                    shared_data.font_color)
                displayMessageWidth = displayMessage.get_width()
                shared_data.display.blit(
                    displayMessage,
                    ((shared_data.real_window_width-displayMessageWidth)/2, shared_data.real_window_height-120))

                TextFontRendered = LoadingTextFont.render(
                    f"{text}",
                    shared_data.aa,
                    shared_data.font_color)
                TextFontRenderedWidth = TextFontRendered.get_width()

                shared_data.display.blit(
                    TextFontRendered,
                    ((shared_data.real_window_width-TextFontRenderedWidth)/2, shared_data.real_window_height-100))

                ProgressText = LoadingTextFont.render(
                    f"{round(Completion_Percentage)}% complete",
                    shared_data.aa,
                    shared_data.font_color)
                ProgressTextWidth = ProgressText.get_width()
                
                shared_data.display.blit(
                    ProgressText,
                    ((shared_data.real_window_width-ProgressTextWidth)/2, shared_data.real_window_height-80))

            except Exception as Message:
                print(Message)
                shared_data.error_message = "".join(("GameEngine > CreateEngine > ",
                                             f"GenerateLoaddisplay: {str(Message)}"))

                shared_data.error_message_detailed = "".join(
                    shared_data.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                shared_data.mod_error_utils__.generate_error_screen.error_screen(shared_data)

        def Play(self):
            try:
                shared_data.mod_pygame__.init()
                shared_data.mod_pygame__.mouse.set_cursor(shared_data.mod_pygame__.SYSTEM_CURSOR_WAIT)
                
                if shared_data.platform == "Linux":
                    shared_data.title_font = shared_data.mod_pygame__.font.Font(
                        shared_data.mod_OS__.path.join(
                            shared_data.base_folder, ("fonts//Book Antiqua.ttf")), 60)

                    shared_data.window_icon = shared_data.mod_pygame__.image.load(
                        shared_data.mod_OS__.path.join(
                            shared_data.base_folder, ("resources//general resources//Icon.png")))

                else:
                    shared_data.title_font = shared_data.mod_pygame__.font.Font(
                        shared_data.mod_OS__.path.join(
                            shared_data.base_folder, ("fonts\\Book Antiqua.ttf")), 60)

                    shared_data.window_icon = shared_data.mod_pygame__.image.load(
                        shared_data.mod_OS__.path.join(
                            shared_data.base_folder, ("resources\\general resources\\Icon.png")))

                try:
                    shared_data.mod_ModernGL_window_.run_window_config(GameEngine)
                    
                except Exception as Message:
                    log_message = "GameEngine > CreateEngine > Play: "+str(Message)
                    
                    shared_data.mod_logging_utils__.create_log_message.update_log_warning(
                        self,
                        log_message)
                    
                    if ((str(Message) != "argument 2: <class 'TypeError'>: wrong type" or
                         str(Message) == "'NoneType' object has no attribute 'flip'")):

                        shared_data.error_message = "GameEngine > CreateEngine > Play: " + str(Message)
                        shared_data.command = "Undefined"

                return shared_data.command
            
            except Exception as Message:
                print(Message)
                shared_data.error_message = "GameEngine > CreateEngine > Play: " + str(Message)
                shared_data.error_message_detailed = "".join(
                    shared_data.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                shared_data.mod_error_utils__.generate_error_screen.error_screen(self)

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
