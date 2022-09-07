if __name__ != "__main__":
    import numpy, math
    class create_game_engine_context:
        def __init__(self):
            pass

        def load_data_and_initialize(self):
            import os

            if ("site-packages" in os.path.dirname(__file__) or
                    "dist-packages" in os.path.dirname(__file__)):

                import DataTransferUtils

            else:
                from pycraft import DataTransferUtils

            import pickle
            dbfile = open('transfer', 'rb')
            db = pickle.load(dbfile)
            for key in db:
                setattr(self, key, db[key])
                
            dbfile.close()

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

            self.mod_data_transfer_utils__ = DataTransferUtils
            self.mod_module_utils__ = ModuleUtils
            self.mod_logging_utils__ = LoggingUtils
            self.mod_error_utils__ = ErrorUtils
            self.mod_file_utils__ = FileUtils
            self.mod_registry__ = Registry

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

            return self
        
    class Crash:
        def __init__(self):
            pass

        def CreateReport(self, Message):
            print(Message, "".join(
                self.mod_traceback__.format_exception(
                    None,
                    Message,
                    Message.__traceback__)))

            try:
                self.wnd.close()
                self.error_message = "".join(("GameEngine > GameEngine ",
                                                        f"> __init__: {str(Message)}"))

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(
                    self)

            except Exception as Message2:
                try:
                    self.error_message = "".join(("GameEngine > GameEngine ",
                                                            f"> __init__: {str(Message2)}"))

                    self.error_message_detailed = "".join(
                        self.mod_traceback__.format_exception(
                            None,
                            Message2,
                            Message2.__traceback__))

                    self.mod_error_utils__.generate_error_screen.error_screen(
                        self)
                    
                except:
                    print(Message)
                    print(Message2)

    class LoadPrograms:
        def __init__(self):
            pass

        def LoadProgramText(self, ctx):
            try:
                particles_transform = ctx.program(
                    vertex_shader='''
                        #version 330

                        in vec2 in_pos;
                        in vec2 in_vel;
                        in vec3 in_color;

                        out vec2 vs_vel;
                        out vec3 vs_color;

                        void main() {
                            gl_Position = vec4(in_pos, 1.0, 1.0);
                            vs_vel = in_vel;
                            vs_color = in_color;
                        }
                        ''',
                    geometry_shader='''
                        #version 330

                        layout(points) in;
                        layout(points, max_vertices = 1) out;

                        uniform float gravity;
                        uniform float ft;

                        in vec2 vs_vel[1];
                        in vec3 vs_color[1];

                        out vec2 out_pos;
                        out vec2 out_vel;
                        out vec3 out_color;

                        void main() {
                            vec2 pos = gl_in[0].gl_Position.xy;
                            vec2 velocity = vs_vel[0];

                            if (pos.y > -1.0) {
                                vec2 vel = velocity + vec2(0.0, gravity);
                                out_pos = pos + vel * ft;
                                out_vel = vel;
                                if (out_pos.x == 0.0) {
                                    out_pos.y = -1.1;
                                }
                                out_color = vs_color[0];
                                EmitVertex();
                                EndPrimitive();
                            }
                        }
                        ''',
                    varyings=['out_pos', 'out_vel', 'out_color'],
                )

                gpu_emitter_particles = ctx.program(
                    vertex_shader='''
                        # version 330
                        #define M_PI 3.1415926535897932384626433832795
                        uniform vec2 mouse_pos;
                        uniform vec2 mouse_vel;
                        uniform float time;

                        out vec2 out_pos;
                        out vec2 out_vel;
                        out vec3 out_color;

                        float rand(float n){
                            return fract(sin(n) * 43758.5453123);
                            }

                        void main() {
                            float a = mod(time * gl_VertexID, M_PI * 2.0);
                            float r = clamp(rand(time + gl_VertexID), 0.1, 0.9);
                            out_pos = mouse_pos;
                            out_vel = vec2(sin(a), cos(a)) * r + mouse_vel;
                            out_color = vec3(0.0, 0.0, rand(time * 2.0 + gl_VertexID));
                        }
                        ''',
                    varyings=['out_pos', 'out_vel', 'out_color'],
                )

                return particles_transform, gpu_emitter_particles
                
            except Exception as Message:
                self.error_message = "".join(("GameEngineUtils > LoadPrograms ",
                                              f"> LoadProgramText: {str(Message)}"))
                
                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

        def LoadProgramFiles(self, wnd):
            try:
                if self.platform == "Linux":
                    CloudsProgram = self.mod_ModernGL_window_.WindowConfig.load_program(
                        wnd,
                        path=self.mod_OS__.path.join(
                            self.base_folder,
                            ("programs//clouds.glsl")))

                    depth_prog = self.mod_ModernGL_window_.WindowConfig.load_program(
                        wnd,
                        path=self.mod_OS__.path.join(
                            self.base_folder,
                            ("programs//raw_depth.glsl")))

                    shadowmap = self.mod_ModernGL_window_.WindowConfig.load_program(
                        wnd,
                        path=self.mod_OS__.path.join(
                            self.base_folder,
                            ("programs//shadowmap.glsl")))

                    sun_prog = self.mod_ModernGL_window_.WindowConfig.load_program(
                        wnd,
                        path=self.mod_OS__.path.join(
                            self.base_folder,
                            ("programs//orbital_prog.glsl")))

                    moon_prog = self.mod_ModernGL_window_.WindowConfig.load_program(
                        wnd,
                        path=self.mod_OS__.path.join(
                            self.base_folder,
                            ("programs//orbital_prog.glsl")))

                    skysphere_prog = self.mod_ModernGL_window_.WindowConfig.load_program(
                        wnd,
                        path=self.mod_OS__.path.join(
                            self.base_folder,
                            ("programs//skysphere.glsl")))

                    particles_screen = self.mod_ModernGL_window_.WindowConfig.load_program(
                        wnd,
                        path=self.mod_OS__.path.join(
                            self.base_folder,
                            ("programs//particles_screen.glsl")))

                else:
                    CloudsProgram = self.mod_ModernGL_window_.WindowConfig.load_program(
                        wnd,
                        path=self.mod_OS__.path.join(
                            self.base_folder,
                            ("programs\\clouds.glsl")))

                    depth_prog = self.mod_ModernGL_window_.WindowConfig.load_program(
                        wnd,
                        path=self.mod_OS__.path.join(
                            self.base_folder,
                            ("programs\\raw_depth.glsl")))

                    shadowmap = self.mod_ModernGL_window_.WindowConfig.load_program(
                        wnd,
                        path=self.mod_OS__.path.join(
                            self.base_folder,
                            ("programs\\shadowmap.glsl")))

                    sun_prog = self.mod_ModernGL_window_.WindowConfig.load_program(
                        wnd,
                        path=self.mod_OS__.path.join(
                            self.base_folder,
                            ("programs\\orbital_prog.glsl")))

                    moon_prog = self.mod_ModernGL_window_.WindowConfig.load_program(
                        wnd,
                        path=self.mod_OS__.path.join(
                            self.base_folder,
                            ("programs\\orbital_prog.glsl")))

                    skysphere_prog = self.mod_ModernGL_window_.WindowConfig.load_program(
                        wnd,
                        path=self.mod_OS__.path.join(
                            self.base_folder,
                            ("programs\\skysphere.glsl")))

                    particles_screen = self.mod_ModernGL_window_.WindowConfig.load_program(
                        wnd,
                        path=self.mod_OS__.path.join(
                            self.base_folder,
                            ("programs\\particles_screen.glsl")))

                return CloudsProgram, depth_prog, shadowmap, sun_prog, moon_prog, skysphere_prog, particles_screen
            except Exception as Message:
                self.error_message = "".join(("GameEngineUtils > LoadPrograms ",
                                              f"> LoadProgramFiles: {str(Message)}"))
                
                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_game_engine_utils__.Crash.CreateReport(self, Message)

    class Particles:
        def __init__(self):
            pass

        def emit_gpu(self, query, transform_vao1, vbo2, N, emit_buffer_elements, max_emit_count, gpu_emitter_particles, weather, time, gpu_emitter_vao, stride, render_vao2, active_particles):
            try:
                # Transform all particles recoding how many elements were emitted by geometry shader
                with query:
                    transform_vao1.transform(
                        vbo2,
                        self.mod_ModernGL__.POINTS,
                        vertices=active_particles)

                emit_count = min(N - query.primitives,
                                emit_buffer_elements,
                                max_emit_count)

                if emit_count > 0:
                    gpu_emitter_particles["mouse_pos"].value = (0, 2)

                    if weather == "rain.light":
                        gpu_emitter_particles["mouse_vel"].value = (
                            0,
                            self.mod_random__.randint(50, 100)/100)

                    if weather == "rain.heavy":
                        gpu_emitter_particles["mouse_vel"].value = (
                            0,
                            self.mod_random__.randint(75, 125)/100)

                    if weather == "rain.heavy.thundery":
                        gpu_emitter_particles["mouse_vel"].value = (
                            0,
                            self.mod_random__.randint(75, 150)/100)

                    gpu_emitter_particles["time"].value = max(time, 0)
                    gpu_emitter_vao.transform(
                        vbo2,
                        vertices=emit_count,
                        buffer_offset=query.primitives * stride)

                active_particles = query.primitives + emit_count
                render_vao2.render(
                    self.mod_ModernGL__.POINTS, vertices=active_particles)

                return active_particles
                
            except Exception as Message:
                self.error_message = "".join(("GameEngineUtils > Particles ",
                                              f"> emit_gpu: {str(Message)}"))
                
                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

        def gen_particles(self, n):
            try:
                for _ in range(n):
                    # Current mouse position (2 floats)
                    yield 0
                    yield 2
                    # Random velocity (2 floats)
                    a = self.mod_numpy__.random.uniform(
                        0.0, self.mod_numpy__.pi * 2.0)
                    r = self.mod_numpy__.random.uniform(0.1, 0.9)
                    yield self.mod_math__.cos(a) * r + 0
                    yield self.mod_math__.sin(a) * r + 0
                    # Random color (4 floats)
                    yield 0.0
                    yield 0.0
                    if self.fancy_particles:
                        yield self.mod_numpy__.random.uniform(0.0, 1.0)
                    else:
                        yield 1.0
                    #yield self.mod_numpy__.random.uniform(0.0, 1.0)
                    
            except Exception as Message:
                self.error_message = "".join(("GameEngineUtils > Particles ",
                                              f"> gen_particles: {str(Message)}"))
                
                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

        def projection(self):
            try:
                return self.mod_pyrr_matrix44_.create_orthogonal_projection(
                    -self.wnd.aspect_ratio, self.wnd.aspect_ratio,
                    -1, 1,
                    -1, 100,
                    dtype='f4',
                )
                
            except Exception as Message:
                self.error_message = "".join(("GameEngineUtils > Particles ",
                                              f"> gen_particles: {str(Message)}"))
                
                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

    class ComputeWeather:
        # 0 = transparent
        # 1 = opaque
        def __init__(self):
            pass

        def ComputeCloudModel(self, size):
            try:
                vertices = self.mod_numpy__.dstack(
                    self.mod_numpy__.mgrid[0:size, 0:size][::-1]) / size

                temp = self.mod_numpy__.dstack(
                    [self.mod_numpy__.arange(0, size * size - size),
                    self.mod_numpy__.arange(size, size * size)])

                index = self.mod_numpy__.pad(
                    temp.reshape(size - 1, 2 * size),
                    [[0, 0], [0, 1]],
                    "constant",
                    constant_values=-1)

                return vertices, index
            
            except Exception as Message:
                self.error_message = "".join(("GameEngineUtils > ComputeWeather ",
                                                        f"> ComputeCloudModel: {str(Message)}"))

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(
                    self)

        def generate_perlin_noise_2d(self, shape, res):
            try:
                def f(t):
                    return 6*t**5 - 15*t**4 + 10*t**3

                delta = (res[0] / shape[0], res[1] / shape[1])
                d = (shape[0] // res[0], shape[1] // res[1])
                grid = self.mod_numpy__.mgrid[0:res[0]:delta[0],0:res[1]:delta[1]].transpose(1, 2, 0) % 1
                # Gradients
                angles = 2*self.mod_numpy__.pi*self.mod_numpy__.random.rand(res[0]+1, res[1]+1)
                gradients = self.mod_numpy__.dstack((self.mod_numpy__.cos(angles), self.mod_numpy__.sin(angles)))
                g00 = gradients[0:-1,0:-1].repeat(d[0], 0).repeat(d[1], 1)
                g10 = gradients[1:,0:-1].repeat(d[0], 0).repeat(d[1], 1)
                g01 = gradients[0:-1,1:].repeat(d[0], 0).repeat(d[1], 1)
                g11 = gradients[1:,1:].repeat(d[0], 0).repeat(d[1], 1)
                # Ramps
                n00 = self.mod_numpy__.sum(grid * g00, 2)
                n10 = self.mod_numpy__.sum(self.mod_numpy__.dstack((grid[:,:,0]-1, grid[:,:,1])) * g10, 2)
                n01 = self.mod_numpy__.sum(self.mod_numpy__.dstack((grid[:,:,0], grid[:,:,1]-1)) * g01, 2)
                n11 = self.mod_numpy__.sum(self.mod_numpy__.dstack((grid[:,:,0]-1, grid[:,:,1]-1)) * g11, 2)
                # Interpolation
                t = f(grid)
                n0 = n00*(1-t[:,:,0]) + t[:,:,0]*n10
                n1 = n01*(1-t[:,:,0]) + t[:,:,0]*n11
                return self.mod_numpy__.sqrt(2)*((1-t[:,:,1])*n0 + t[:,:,1]*n1)
            
            except Exception as Message:
                self.error_message = "".join(("GameEngineUtils > ComputeWeather ",
                                              f"> generate_perlin_noise_2d: {str(Message)}"))
                
                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(
                    self)
    
        def ComputeCloudNoise(self, shape):
            try:
                world = ComputeWeather.generate_perlin_noise_2d(
                    self,
                    shape,
                    (25, 25)) # multiple of shape[0]

                CloudData = world

                if self.remove_file_permission:
                    image = self.mod_PIL_Image_.fromarray(
                        self.mod_numpy__.uint8(
                            self.mod_matplotlib_cm_.gist_earth(world)*255))

                    if self.platform == "Linux":
                        try:
                            self.mod_send2trash__.send2trash(
                                self.mod_OS__.path.join(
                                    self.base_folder,
                                    ("resources//game engine resources//clouds//Rnd_noise.png")))
                            
                        except Exception as Message:
                            log_message = "".join(("Unable to clear the previous Perlin-noise image, ",
                                                "attempting to overwrite instead. More Details:",
                                                str(Message)))

                            self.mod_logging_utils__.create_log_message.update_log_warning(
                                self,
                                log_message)

                        image.save(
                            self.mod_OS__.path.join(
                                self.base_folder,
                                ("resources//game engine resources//clouds//Rnd_noise.png")))

                    else:
                        try:
                            self.mod_send2trash__.send2trash(
                                self.mod_OS__.path.join(
                                    self.base_folder,
                                    ("resources\\game engine resources\\clouds\\Rnd_noise.png")))
                            
                        except Exception as Message:
                            log_message = "".join(("Unable to clear the previous Perlin-noise image, ",
                                                        "attempting to overwrite instead. More Details:",
                                                        f"{str(Message)}"))

                            self.mod_logging_utils__.create_log_message.update_log_warning(
                                self,
                                log_message)

                        image.save(
                            self.mod_OS__.path.join(
                                self.base_folder,
                                ("resources\\game engine resources\\clouds\\Rnd_noise.png")))

                    image.close()
                return CloudData
            
            except Exception as Message:
                self.error_message = "".join(("GameEngineUtils > ComputeWeather ",
                                                        f"> ComputeCloudNoise: {str(Message)}"))

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(
                    self)

        def BlendWeather(self, weather, PreviousWeather, WeatherTime, shadowmap, Previous_Fog_Distance_Min, Previous_Fog_Distance_Max, Previous_color, color, CloudsProgram, Previous_CloudsProgram_Alpha, Previous_CloudsProgram_CloudColor, Previous_multiplier, CloudHeightMultiplier, skysphere_prog, Previous_prog_transparency, skysphere_prog_Transparency):
            try:
                def mix(start, end, time, duration):
                    return (((end-start)/duration)*time)+start

                if weather != PreviousWeather and WeatherTime < 3:
                    if weather == "sunny":
                        shadowmap["w_min"] = mix(
                            Previous_Fog_Distance_Min,
                            1200.0,
                            WeatherTime,
                            3)

                        shadowmap["w_max"] = mix(
                            Previous_Fog_Distance_Max,
                            1600.0,
                            WeatherTime,
                            3)

                        Temporary_color = mix(
                            Previous_color,
                            1.0,
                            WeatherTime,
                            3)

                        color.value = (
                            Temporary_color,
                            Temporary_color,
                            Temporary_color)

                        CloudsProgram["w_min"] = mix(
                            Previous_Fog_Distance_Min,
                            1200.0,
                            WeatherTime,
                            3)

                        CloudsProgram["w_max"] = mix(
                            Previous_Fog_Distance_Max,
                            1600.0,
                            WeatherTime,
                            3)

                        CloudsProgram["WeatherAlpha"] = mix(
                            Previous_CloudsProgram_Alpha,
                            0.0,
                            WeatherTime,
                            3)

                        CloudsProgram["CloudColor"] = mix(
                            Previous_CloudsProgram_CloudColor,
                            1.0,
                            WeatherTime,
                            3)

                        multiplier = mix(
                            Previous_multiplier,
                            CloudHeightMultiplier,
                            WeatherTime,
                            3)

                        CloudsProgram["CloudHeightMultiplier"] = multiplier

                        skysphere_prog["transparency"] = mix(
                            Previous_prog_transparency,
                            1.0,
                            WeatherTime,
                            3)

                    elif weather == "rain.light":
                        shadowmap["w_min"] = mix(
                            Previous_Fog_Distance_Min,
                            1000.0,
                            WeatherTime,
                            3)

                        shadowmap["w_max"] = mix(
                            Previous_Fog_Distance_Max,
                            1600.0,
                            WeatherTime,
                            3)

                        Temporary_color = mix(
                            Previous_color,
                            0.8,
                            WeatherTime,
                            3)

                        color.value = (
                            Temporary_color,
                            Temporary_color,
                            Temporary_color)

                        CloudsProgram["w_min"] = mix(
                            Previous_Fog_Distance_Min,
                            1200.0,
                            WeatherTime,
                            3)

                        CloudsProgram["w_max"] = mix(
                            Previous_Fog_Distance_Max,
                            1600.0,
                            WeatherTime,
                            3)

                        CloudsProgram["WeatherAlpha"] = mix(
                            Previous_CloudsProgram_Alpha,
                            0.75,
                            WeatherTime,
                            3)

                        CloudsProgram["CloudColor"] = mix(
                            Previous_CloudsProgram_CloudColor,
                            0.75,
                            WeatherTime,
                            3)

                        multiplier = mix(
                            Previous_multiplier,
                            CloudHeightMultiplier,
                            WeatherTime,
                            3)

                        CloudsProgram["CloudHeightMultiplier"] = multiplier

                        skysphere_prog["transparency"] = mix(
                            Previous_prog_transparency,
                            skysphere_prog_Transparency,
                            WeatherTime,
                            3)

                    elif weather == "rain.heavy":
                        shadowmap["w_min"] = mix(
                            Previous_Fog_Distance_Min,
                            1000.0,
                            WeatherTime,
                            3)

                        shadowmap["w_max"] = mix(
                            Previous_Fog_Distance_Max,
                            1600.0,
                            WeatherTime,
                            3)

                        Temporary_color = mix(
                            Previous_color,
                            0.7,
                            WeatherTime,
                            3)

                        color.value = (
                            Temporary_color,
                            Temporary_color,
                            Temporary_color)

                        CloudsProgram["w_min"] = mix(
                            Previous_Fog_Distance_Min,
                            800.0,
                            WeatherTime,
                            3)

                        CloudsProgram["w_max"] = mix(
                            Previous_Fog_Distance_Max,
                            1200.0,
                            WeatherTime,
                            3)

                        CloudsProgram["WeatherAlpha"] = mix(
                            Previous_CloudsProgram_Alpha,
                            1.0,
                            WeatherTime,
                            3)

                        CloudsProgram["CloudColor"] = mix(
                            Previous_CloudsProgram_CloudColor,
                            0.35,
                            WeatherTime,
                            3)

                        multiplier = mix(
                            Previous_multiplier,
                            CloudHeightMultiplier,
                            WeatherTime,
                            3)

                        CloudsProgram["CloudHeightMultiplier"] = multiplier

                        skysphere_prog["transparency"] = mix(
                            Previous_prog_transparency,
                            skysphere_prog_Transparency,
                            WeatherTime,
                            3)

                    else:
                        shadowmap["w_min"] = mix(
                            Previous_Fog_Distance_Min,
                            600.0,
                            WeatherTime,
                            3)

                        shadowmap["w_max"] = mix(
                            Previous_Fog_Distance_Max,
                            800.0,
                            WeatherTime,
                            3)

                        Temporary_color = mix(
                            Previous_color,
                            0.6,
                            WeatherTime,
                            3)

                        color.value = (
                            Temporary_color,
                            Temporary_color,
                            Temporary_color)

                        CloudsProgram["w_min"] = mix(
                            Previous_Fog_Distance_Min,
                            800.0,
                            WeatherTime,
                            3)

                        CloudsProgram["w_max"] = mix(
                            Previous_Fog_Distance_Max,
                            1200.0,
                            WeatherTime,
                            3)

                        CloudsProgram["WeatherAlpha"] = mix(
                            Previous_CloudsProgram_Alpha,
                            1.0,
                            WeatherTime,
                            3)

                        CloudsProgram["CloudColor"] = mix(
                            Previous_CloudsProgram_CloudColor,
                            0.25,
                            WeatherTime,
                            3)

                        multiplier = mix(
                            Previous_multiplier,
                            CloudHeightMultiplier,
                            WeatherTime,
                            3)

                        CloudsProgram["CloudHeightMultiplier"] = multiplier

                        skysphere_prog["transparency"] = mix(
                            Previous_prog_transparency,
                            skysphere_prog_Transparency,
                            WeatherTime,
                            3)

                else:
                    if weather == "sunny":
                        color.value = (1.0, 1.0, 1.0)

                    elif weather == "rain.light":
                        color.value = (0.8, 0.8, 0.8)

                    elif weather == "rain.heavy":
                        color.value = (0.7, 0.7, 0.7)

                    else:
                        color.value = (0.6, 0.6, 0.6)
                        
            except Exception as Message:
                self.error_message = "".join(("GameEngineUtils > ComputeWeather ",
                                              f"> BlendWeather: {str(Message)}"))

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(
                    self)

        def ComputeWeather(self, color, shadowmap, CloudsProgram, skysphere_prog, Time_Percent):
            try:
                LengthenStorm = False
                weather = ""
                skysphere_prog_Transparency = 0.0
                if self.mod_random__.randint(0, 100) <= 65:
                    weather += "sunny"

                    color.value = (1.0, 1.0, 1.0)

                    shadowmap["w_min"] = 1200.0
                    shadowmap["w_max"] = 1600.0

                    CloudsProgram["w_min"] = 1200.0
                    CloudsProgram["w_max"] = 1600.0
                    CloudsProgram["WeatherAlpha"] = 0.0
                    CloudsProgram["CloudColor"] = 1.0

                    CloudHeightMultiplier = self.mod_random__.randint(1, 500)
                    CloudsProgram["CloudHeightMultiplier"] = CloudHeightMultiplier

                    skysphere_prog["transparency"] = 1.0

                else:
                    weather += "rain"

                    if self.mod_random__.randint(0, 100) <= 80:
                        weather += ".light"

                        color.value = (0.8, 0.8, 0.8)

                        shadowmap["w_min"] = 1000.0
                        shadowmap["w_max"] = 1600.0

                        CloudsProgram["w_min"] = 1000.0
                        CloudsProgram["w_max"] = 1600.0
                        CloudsProgram["WeatherAlpha"] = 0.75
                        CloudsProgram["CloudColor"] = 0.75

                        CloudHeightMultiplier = self.mod_random__.randint(139, 500)
                        CloudsProgram["CloudHeightMultiplier"] = CloudHeightMultiplier

                        if Time_Percent > 50: # night
                            skysphere_prog_Transparency = self.mod_random__.randint(35, 50)/100
                        else: # day
                            skysphere_prog_Transparency = self.mod_random__.randint(25, 40)/100
                        skysphere_prog["transparency"] = skysphere_prog_Transparency

                    else:
                        weather += ".heavy"
                        CloudsProgram["WeatherAlpha"] = 1

                        if self.mod_random__.randint(0, 100) <= 50:
                            weather += ".thundery"

                            color.value = (0.6, 0.6, 0.6)

                            LengthenStorm = True

                            shadowmap["w_min"] = 600.0
                            shadowmap["w_max"] = 800.0

                            CloudsProgram["w_min"] = 600.0
                            CloudsProgram["w_max"] = 800.0
                            CloudsProgram["CloudColor"] = 0.25

                            CloudHeightMultiplier = self.mod_random__.randint(
                                278,
                                500)

                            CloudsProgram["CloudHeightMultiplier"] = CloudHeightMultiplier

                            skysphere_prog_Transparency = self.mod_random__.randint(0, 25)/100
                            skysphere_prog["transparency"] = skysphere_prog_Transparency

                        else:
                            color.value = (0.7, 0.7, 0.7)

                            shadowmap["w_min"] = 800.0
                            shadowmap["w_max"] = 1200.0

                            CloudsProgram["w_min"] = 800.0
                            CloudsProgram["w_max"] = 1200.0
                            CloudsProgram["CloudColor"] = 0.35

                            CloudHeightMultiplier = self.mod_random__.randint(
                                361,
                                500)

                            CloudsProgram["CloudHeightMultiplier"] = CloudHeightMultiplier

                            skysphere_prog_Transparency = self.mod_random__.randint(10, 45)/100
                            skysphere_prog["transparency"] = skysphere_prog_Transparency

                return LengthenStorm, weather, CloudHeightMultiplier, skysphere_prog_Transparency
            except Exception as Message:
                self.error_message = "".join(("GameEngineUtils > ComputeWeather ",
                                                        f"> ComputeWeather: {str(Message)}"))

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(
                    self)

    class AccessOtherGUIs:
        def __init__(self):
            pass

        def AccessGUI(self):
            try:
                fullscreen = self.wnd.fullscreen
                self.fullscreen = not fullscreen
                WindowSize = self.wnd.width, self.wnd.height
                WindowPos = self.wnd.position
                
                self.wnd.position = (-WindowSize[0],
                                        -WindowSize[1])

                self.wnd.mouse_exclusivity = False
                
                self.mod_pygame__.init()

                if self.Inventory:
                    if self.platform == "Linux":
                        self.mod_ModernGL_window_screenshot.create(
                            source=self.wnd.fbo,
                            name=self.mod_OS__.path.join(
                                self.base_folder,
                                ("resources//general resources//PauseIMG.png")))
                        
                    else:
                        self.mod_ModernGL_window_screenshot.create(
                            source=self.wnd.fbo,
                            name=self.mod_OS__.path.join(
                                self.base_folder,
                                ("resources\\general resources\\PauseIMG.png")))

                    self.command = "Inventory"
                    self.mod_inventory__.GenerateInventory.Inventory(self)
                    self.Inventory = False

                elif self.Map:
                    self.command = "Map"
                    self.mod_map_GUI__.GenerateMapGUI.MapGUI(self)
                    self.Map = False

                self.wnd.mouse_exclusivity = self.camera_enabled
                self.wnd.position = WindowPos
                self.wnd.fullscreen = fullscreen
                self.command = "Play"
                
            except Exception as Message:
                self.error_message = "".join(("GameEngineUtils > AccessOtherGUIs ",
                                                        f"> AccessGUI: {str(Message)}"))

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

    class ShadowmappingMathematics:
        import numba
        def __init__(self):
            pass

        def ComputeCelestialEntities(self, skybox_distance, sun_radius, GameTime, day, sun_prog, moon_prog, scene_pos, projection_matrix, matrix, position):
            try:
                distance = (skybox_distance-sun_radius)/1.355

                if GameTime >= 1056:
                    GameTime = 0
                    day += 1

                sun_prepro_time = (GameTime/168)-1.5707975

                SunPos_YZ = self.mod_math__.cos(
                    sun_prepro_time) * distance

                SunPos_X = self.mod_math__.sin(
                    sun_prepro_time) * distance

                sun_lightpos = self.mod_numpy__.array(
                    (SunPos_X + position.x, SunPos_YZ + position.y, 0), dtype="f4")

                moon_prepro_time = (GameTime/168)-4.7123925

                MoonPos_YZ = self.mod_math__.cos(
                    moon_prepro_time) * distance
                MoonPos_X = self.mod_math__.sin(
                    moon_prepro_time) * distance

                moon_lightpos = self.mod_numpy__.array(
                    (MoonPos_X + position.x, MoonPos_YZ + position.y, 0), dtype="f4")

                sun_prog["m_proj"].write(projection_matrix)
                sun_prog["m_camera"].write(matrix)
                sun_prog["m_model"].write(
                    self.mod_pyrr_Matrix44_.from_translation(
                        sun_lightpos + scene_pos,
                        dtype="f4"))

                moon_prog["m_proj"].write(projection_matrix)
                moon_prog["m_camera"].write(matrix)
                moon_prog["m_model"].write(
                    self.mod_pyrr_Matrix44_.from_translation(
                        moon_lightpos + scene_pos,
                        dtype="f4"))

                return GameTime, day, sun_lightpos, moon_lightpos
                
            except Exception as Message:
                print(Message)
                self.error_message = "".join(("GameEngineUtils > ShadowmappingMathematics ",
                                              f"> ComputeCelestialEntities: {str(Message)}"))
                
                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(
                    self)

        @numba.njit(fastmath=True, cache=True)
        def perspective_fov(fov, aspect_ratio, near_plane, far_plane):
            num = 1.0 / math.tan(fov / 2.0)
            num9 = num / aspect_ratio
            return numpy.array([
                [num9, 0.0, 0.0, 0.0],
                [0.0, num, 0.0, 0.0],
                [0.0, 0.0, far_plane / (near_plane - far_plane), -1.0],
                [0.0, 0.0, (near_plane * far_plane) / (near_plane - far_plane), 0.0]
            ], dtype="f4")

        @numba.njit(fastmath=True, cache=True)
        def look_at(camera_position, camera_target, up_vector):
            vector = camera_target - camera_position

            x = numpy.linalg.norm(vector)
            vector = vector / x

            vector2 = numpy.cross(up_vector, vector)
            vector2 = vector2 / numpy.linalg.norm(vector2)

            vector3 = numpy.cross(vector, vector2)
            return numpy.array([
                [vector2[0], vector3[0], vector[0], 0.0],
                [vector2[1], vector3[1], vector[1], 0.0],
                [vector2[2], vector3[2], vector[2], 0.0],
                [-numpy.dot(vector2, camera_position), -numpy.dot(
                    vector3, camera_position), numpy.dot(vector, camera_position), 1.0]
                ], dtype="f4")

        @numba.njit(fastmath=True, cache=True)
        def multiply(light_proj, sun_light_look_at):
            return light_proj * sun_light_look_at

        def ComputeShadows(self, mvp, light, sun_lightpos, aspect_ratio, mvp_depth, mvp_shadow, bias_matrix, projection, matrix, target, up):
            try:
                mvp[0].write(projection.astype("f4").tobytes())
                mvp[1].write(matrix.astype("f4").tobytes())

                # build light camera
                light.value = tuple(sun_lightpos)
                
                sun_light_look_at = ShadowmappingMathematics.look_at(sun_lightpos, target, up)
                
                # light projection matrix (scene dependant)
                light_proj = ShadowmappingMathematics.perspective_fov(90.0 / 2, aspect_ratio, 0.01, 2000.0)

                # light model view projection matrix
                mvp_light = ShadowmappingMathematics.multiply(light_proj, sun_light_look_at)

                # send uniforms to shaders
                mvp_depth[0].write(bias_matrix.astype("f4").tobytes())
                mvp_depth[1].write(mvp_light.astype("f4").tobytes())
                mvp_shadow.write(mvp_light.astype("f4").tobytes())
            except Exception as Message:
                self.error_message = "GameEngine > GameEngine > __init__: "+str(Message)
                
                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

    class OnscreenEventFunction:
        def __init__(self):
            pass

        def game_events(self):
            try:
                CurrentTime = self.mod_time__.perf_counter()
                if self.Wkeydown or self.Akeydown or self.Skeydown or self.Dkeydown:
                    random_value = self.mod_random__.randint(
                        50, 100)/100
                    
                    random_value_sprint = self.mod_random__.randint(
                        25, 75)/100
                    
                if self.use_mouse_input is False:
                    self.camera.rot_state(
                        -self.Joystick_Rotation[0]*self.camera_angle_speed,
                        -self.Joystick_Rotation[1]*self.camera_angle_speed)

                if self.RunForwardtimer:
                    if self.mod_time__.perf_counter()-self.RunForwardtimer_start > 3.5:
                        self.Sprinting = True
                else:
                    self.Sprinting = False

                if self.Akeydown:
                    if self.sound:
                        APressedTime = CurrentTime-self.Akeydowntimer_start

                        if APressedTime >= random_value:
                            self.mod_sound_utils__.play_sound.play_footsteps_sound(
                                self)

                            self.Akeydowntimer_start = self.mod_time__.perf_counter()
                    self.total_move_z -= 10
                    if self.use_mouse_input is False:
                        self.camera.key_input(
                            self.keys.A,
                            self.keys.ACTION_PRESS,
                            None)

                else:
                    if self.use_mouse_input is False:
                        self.camera.key_input(
                            self.keys.A,
                            self.keys.ACTION_RELEASE,
                            None)

                if self.Skeydown:
                    if self.sound:
                        SPressedTime = CurrentTime-self.Skeydowntimer_start

                        if SPressedTime >= random_value:
                            self.mod_sound_utils__.play_sound.play_footsteps_sound(
                                self)

                            self.Skeydowntimer_start = self.mod_time__.perf_counter()
                            
                    self.total_move_x -= 10
                    if self.use_mouse_input is False:
                        self.camera.key_input(
                            self.keys.S,
                            self.keys.ACTION_PRESS,
                            None)

                else:
                    if self.use_mouse_input is False:
                        self.camera.key_input(
                            self.keys.S,
                            self.keys.ACTION_RELEASE,
                            None)

                if self.Dkeydown:
                    if self.sound:
                        DPressedTime = CurrentTime-self.Dkeydowntimer_start

                        if DPressedTime >= random_value:
                            self.mod_sound_utils__.play_sound.play_footsteps_sound(
                                self)

                            self.Dkeydowntimer_start = self.mod_time__.perf_counter()
                    self.total_move_z += 10
                    if self.use_mouse_input is False:
                        self.camera.key_input(
                            self.keys.D,
                            self.keys.ACTION_PRESS,
                            None)

                else:
                    if self.use_mouse_input is False:
                        self.camera.key_input(
                            self.keys.D,
                            self.keys.ACTION_RELEASE,
                            None)

                
                if self.Wkeydown:
                    if self.sound:
                        WPressedTime = CurrentTime-self.RunForwardtimer_start_sound
                        if self.Sprinting:
                            if WPressedTime >= random_value_sprint:
                                self.mod_sound_utils__.play_sound.play_footsteps_sound(
                                    self)

                                self.RunForwardtimer_start_sound = self.mod_time__.perf_counter()

                        else:
                            if WPressedTime >= random_value:
                                self.mod_sound_utils__.play_sound.play_footsteps_sound(
                                    self)

                                self.RunForwardtimer_start_sound = self.mod_time__.perf_counter()

                    if self.Sprinting:
                        self.RunForwardtimer_start = self.mod_time__.perf_counter()
                        if self.use_mouse_input is False:
                            self.camera.key_input(
                                self.keys.W,
                                self.keys.ACTION_PRESS,
                                None)
                            
                        if self.increased_speed and self.IKeyPressed:
                            self.camera.velocity = 55
                            self.camera.projection.update(
                                near=0.1,
                                far=2000.0,
                                fov=100)

                            self.total_move_x += 35
                        else:
                            self.camera.projection.update(
                                near=0.1,
                                far=2000.0,
                                fov=80)

                            self.camera.velocity = 15 #2.2352
                            self.total_move_x += 15

                    else:
                        self.total_move_x += 10
                        if self.use_mouse_input is False:
                            self.camera.key_input(
                                self.keys.W,
                                self.keys.ACTION_PRESS,
                                None)
                            
                else:
                    if self.use_mouse_input is False:
                        self.camera.key_input(
                            self.keys.W,
                            self.keys.ACTION_RELEASE,
                            None)
                        
                    if self.increased_speed and self.IKeyPressed:
                        self.camera.velocity = 35
                        self.camera.projection.update(
                            near=0.1,
                            far=2000.0,
                            fov=90)

                    else:
                        self.camera.velocity = 10 #1.42
                        self.camera.projection.update(
                            near=0.1,
                            far=2000.0,
                            fov=70)

                if self.space_key_pressed and self.Jump is False:
                    self.Jump = True
                    self.jump_timer = self.mod_time__.perf_counter()
                    self.StartYposition = self.camera.position.y

                if self.Jump:
                    current_time = self.mod_time__.perf_counter()
                    delta = current_time - self.jump_timer
                    offset = delta*180
                    offset_radians = self.mod_math__.radians(offset)

                    if self.increased_speed:
                        calculation = self.StartYposition + (self.mod_math__.sin(
                            offset_radians) / (2 / self.modifier))
                        
                    else:
                        calculation = self.StartYposition + (self.mod_math__.sin(
                            offset_radians) / 2)
                    
                    self.camera.position.y = calculation
                    if delta > 1:
                        self.Jump = False
                        if self.Collision == False:
                            self.camera.position.y = self.StartYposition

            except Exception as Message:
                self.error_message = "GameEngine > GameEngine > __init__: "+str(Message)
                
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
