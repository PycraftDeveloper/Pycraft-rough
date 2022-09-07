if __name__ != "__main__":
    class generate_benchmark:
        def __init__(self):
            pass

        def benchmark_exit(self):
            try:
                self.joystick_exit = False
                if self.sound:
                    self.mod_sound_utils__.play_sound.play_click_sound(
                        self)
                self.startup_animation = True
                self.run_timer = 0
                self.go_to = "Home"
                
            except Exception as Message:
                self.error_message = (
                    f"Benchmark > generate_benchmark > benchmark_exit: {str(Message)}")

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

        def Benchmark(self):
            try:
                self.mod_pygame__.mixer.music.fadeout(500)

                self.mod_pygame__.display.set_caption(f"Pycraft: v{self.version}: Benchmark")

                if self.platform == "Linux":
                    subtitle_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts//Book Antiqua.ttf")), 35)

                    devmode_information_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts//Book Antiqua.ttf")), 15)

                    details_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts//Book Antiqua.ttf")), 20)

                    information_details_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts//Book Antiqua.ttf")), 15)

                else:
                    subtitle_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts\\Book Antiqua.ttf")), 35)

                    devmode_information_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts\\Book Antiqua.ttf")), 15)

                    details_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts\\Book Antiqua.ttf")), 20)

                    information_details_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts\\Book Antiqua.ttf")), 15)

                title_font = self.title_font.render(
                    "Pycraft",
                    self.aa,
                    self.font_color)

                title_width = title_font.get_width()

                benchmark_font = subtitle_font.render(
                    "Benchmark",
                    self.aa,
                    self.secondary_font_color)

                FPS_information_text = details_font.render(
                    "FPS benchmark results",
                    self.aa,
                    self.font_color)
                FPS_information_text_width = FPS_information_text.get_width()

                file_information_text = details_font.render(
                    "Read test results",
                    self.aa,
                    self.font_color)
                file_information_text_width = file_information_text.get_width()

                hardware_information_text = details_font.render(
                    "Hardware results",
                    self.aa,
                    self.font_color)
                hardware_information_text_width = hardware_information_text.get_width()

                sixty_FPS_data = devmode_information_font.render(
                    "60 Hz",
                    self.aa,
                    self.accent_color)

                one_four_four_FPS_data = devmode_information_font.render(
                    "144 Hz",
                    self.aa,
                    self.accent_color)

                two_forty_FPS_data = devmode_information_font.render(
                    "240 Hz",
                    self.aa,
                    self.accent_color)

                benchmark_information_text = ["".join(("Welcome to the Benchmark section; ",
                                                 "press SPACE to continue, or any ",
                                                 "other key to leave at any time ")),
                    " ",
                    "Purpose",
                    "The Benchmark section is designed for a few tasks:",
                    "".join(("1. To give an insight into the performance ",
                            "you will likely get when playing the ",
                            "project, which you can then use to ",
                            "change settings.")),

                    "".join(("2. The data collected in the Benchmark ",
                             "section can be used for automating control ",
                             "of settings automatically when ADAPTIVE ",
                             "mode is selected in settings.")),

                    "".join(("3. To give a repeatable demonstration ",
                             "of how the project performs with your ",
                             "current hardware setup or software configuration.")),
                    " ",
                    "Structure",
                    "".join(("The Benchmark will automatically run a ",
                             "variety of tests, this includes a disk ",
                             "read check, as well as a CPU and GPU ",
                             "based load. In the order of occurrence:")),
                    " ",
                    "".join(("1. Once the user has initiated the ",
                             "benchmark (by pressing SPACE), a small ",
                             "amount of information is collected on ",
                             "the hardware your device is running, ",
                             "we try to obtain the CPU's name, as ",
                             "well as its max clock speed, as well as ",
                             "the amount of available memory and how ",
                             "much is used. This is used solely for ",
                             "the results GUI at the end of the menu ",
                             "and is not stored or shared anywhere).")),

                    "".join(("2. Next we enter 1 of 3 graphics oriented ",
                             "tests, starting with a blank screen test ",
                             "to establish a baseline.")),

                    "".join(("3. Then we enter test 2 of the 3 graphics ",
                             "test, this is much more CPU intensive, ",
                             "as lots more data is being processed ",
                             "and drawn to the display.")),

                    "".join(("4. To conclude the graphics test, we enter ",
                             "graphics test 3, this tests 3D performance ",
                             "as well as basic lighting, it is likely ",
                             "your device will get a very good score here ",
                             "as this is very GPU dependant but not ",
                             "difficult to run.")),

                    "".join(("5. Finally we enter a disk read test, in ",
                             "which a 1 MB file is read over a period ",
                             "of time to establish a rough indication ",
                             "of drive performance.")),
                    " ",
                    "Results",
                    "".join(("Once the series of tests has completed, ",
                             "you will be shown a screen that displays ",
                             "your results, listing the scores (minimum ",
                             "and maximum) for the graphics tests, as ",
                             "well as displaying them on a line graph. ",
                             "It is at this point that you are given the ",
                             "results of the disk read test, as well as ",
                             "the information on the hardware in your ",
                             "system, which we collected earlier.")),
                    " ",
                    "Important things to note",
                    "".join(("During this test, the open window may ",
                             "appear unresponsive, or that nothing is ",
                             "happening, you can observe that the ",
                             "caption details some information on the ",
                             "test what section the process is on, if ",
                             "the details change after a period of time ",
                             "then the window is responding. You may ",
                             "also observer your device heating up, ",
                             "this array of tests is designed to ",
                             "challenge and push your hardware, ",
                             "it is unlikely that your device ",
                             "will reach these temperatures whilst ",
                             "playing the game, but the Benchmark is ",
                             "engineered so that the more CPU/GPU ",
                             "intensive tests are quicker, to avoid ",
                             "damage to hardware. The only data ",
                             "collected by this benchmark is scores ",
                             "on how your system has done, which ",
                             "can be used in the ADAPTIVE pre-set ",
                             "in settings, where settings are ",
                             "toggled automatically based on your ",
                             "performance in this test. No data ",
                             "is shared externally."))]

                stage = 0

                resize = False

                while True:
                    start_time = self.mod_time__.perf_counter()

                    self.mod_display_utils__.display_functionality.core_display_functions(
                        self, checkEvents=False)

                    if stage == -1:
                        pass

                    if stage == 0:
                        self.display.fill(self.background_color)
                        cover_Rect = self.mod_pygame__.Rect(
                            0,
                            0,
                            1280,
                            90)

                        self.mod_pygame__.draw.rect(
                            self.display,
                            self.background_color,
                            cover_Rect)

                        self.display.blit(
                            title_font,
                            ((self.real_window_width-title_width)/2, 0))

                        self.display.blit(
                            benchmark_font,
                            (((self.real_window_width-title_width)/2)+65, 50))

                        Ypos = 100
                        for i in range(len(benchmark_information_text)):
                            Ypos += self.mod_text_utils__.TextWrap.blit_text(
                                self,
                                benchmark_information_text[i],
                                (3, Ypos),
                                devmode_information_font,
                                self.font_color,
                                self.real_window_width)

                    if stage == 1:
                        self.mod_pygame__.display.set_caption(
                            f"Pycraft: v{self.version}: Benchmark | Getting System Information")

                        CPUname = self.mod_cpuinfo__.get_cpu_info()["brand_raw"]
                        CPUcores = self.mod_psutil__.cpu_count(logical=False)
                        CPU_max_Freq = self.mod_psutil__.cpu_freq().max
                        CPUid = f"{CPUname} w/{CPUcores} cores @ {CPU_max_Freq} MHz"

                        RAMtotal = round((self.mod_psutil__.virtual_memory().total/1000000000), 2)
                        RAMpercent = self.mod_psutil__.virtual_memory().percent
                        RAMid = f"{RAMtotal} GB of memory, with {RAMpercent}% used"

                        CPUhwINFO = devmode_information_font.render(
                            CPUid,
                            self.aa,
                            self.font_color)
                        CPUhwINFOwidth = CPUhwINFO.get_width()

                        RAMhwINFO = devmode_information_font.render(
                            RAMid,
                            self.aa,
                            self.font_color)
                        RAMhwINFOwidth = RAMhwINFO.get_width()

                        stage += 1

                    if stage == 2:
                        try:
                            FPS_Results = self.mod_extended_benchmark__.LoadBenchmark.run(self)
                            FPSlistX = FPS_Results[0]
                            FPSlistY = FPS_Results[1]
                            FPSlistX2 = FPS_Results[2]
                            FPSlistY2 = FPS_Results[3]
                            FPSlistX3 = FPS_Results[4]
                            FPSlistY3 = FPS_Results[5]
                            
                        except Exception as Message:
                            log_message = "Benchmark > generate_benchmark > Benchmark: "+str(Message)
                            
                            self.mod_logging_utils__.create_log_message.update_log_warning(
                                self,
                                log_message)
                            
                            self.mod_display_utils__.display_utils.set_display(self)
                            self.mod_pygame__.display.set_caption(
                                f"Pycraft: v{self.version}: Benchmark | Cancelled benchmark")

                            self.startup_animation = True
                            self.run_timer = 0
                            self.go_to = "Home"
                            stage = -1
                            
                        else:
                            self.mod_pygame__.display.set_caption(
                                "".join((f"Pycraft: v{self.version}: Benchmark",
                                         "|",
                                         "Finished FPS based benchmarks")))

                            self.mod_display_utils__.display_utils.set_display(self)

                            stage += 1

                    if stage == 3:
                        self.mod_pygame__.display.set_caption(
                            f"Pycraft: v{self.version}: Benchmark | Starting disk read test")
                        Readiteration = 5
                        for i in range(Readiteration):
                            if self.platform == "Linux":
                                with open(
                                    self.mod_OS__.path.join(
                                        self.base_folder,
                                        ("data files//BenchmarkData.txt")),"r") as Bench:

                                    Benchdata = Bench.read()
                            else:
                                with open(
                                    self.mod_OS__.path.join(
                                        self.base_folder,
                                        ("data files\\BenchmarkData.txt")), "r") as Bench:

                                    Benchdata = Bench.read()
                        aTime = 0
                        Readiteration = 50
                        for i in range(Readiteration):
                            start = self.mod_time__.perf_counter()
                            if self.platform == "Linux":
                                with open(
                                    self.mod_OS__.path.join(
                                        self.base_folder,
                                        ("data files//BenchmarkData.txt")), "r") as Bench:

                                    Benchdata = Bench.read()
                            else:
                                with open(
                                    self.mod_OS__.path.join(
                                        self.base_folder,
                                        ("data files\\BenchmarkData.txt")), "r") as Bench:

                                    Benchdata = Bench.read()

                            aTime += self.mod_time__.perf_counter()-start
                        aTime = aTime/(Readiteration+1)
                        ReadSpeed = (1/(aTime))
                        stage += 1

                    if stage == 4:
                        self.mod_pygame__.display.set_caption(
                            f"Pycraft: v{self.version}: Benchmark | Processing Results")
                        try:
                            Max1 = max(FPSlistY)
                            Min1 = min(FPSlistY)

                            Max2 = max(FPSlistY2)
                            Min2 = min(FPSlistY2)

                            Max3 = max(FPSlistY3)
                            Min3 = min(FPSlistY3)
                            
                        except Exception as Message:
                            log_message = "".join(("(User cancelled) Benchmark ",
                                                       "> generate_benchmark > Benchmark:",
                                                       f"{str(Message)}"))
                            
                            self.mod_logging_utils__.create_log_message.update_log_warning(
                                self,
                                log_message)

                            self.mod_display_utils__.display_utils.set_display(self)
                            self.mod_pygame__.display.set_caption(
                                f"Pycraft: v{self.version}: Benchmark | Cancelled benchmark")

                            self.startup_animation = True
                            self.run_timer = 0
                            self.go_to = "Home"

                        GlobalMaxArray = [Max1, Max2, Max3]

                        GlobalMax = max(GlobalMaxArray)

                        self.adaptive_FPS = GlobalMax/2

                        multiplier = len(FPSlistY)/(self.real_window_width-20)
                        temp = []
                        for i in range(len(FPSlistY)):
                            temp.append(130+(300-((300/GlobalMax)*FPSlistY[i])))
                        FPSListY = temp

                        temp = []
                        for i in range(len(FPSlistY2)):
                            temp.append(130+(300-((300/GlobalMax)*FPSlistY2[i])))
                        FPSListY2 = temp

                        temp = []
                        for i in range(len(FPSlistY2)):
                            temp.append(130+(300-((300/GlobalMax)*FPSlistY3[i])))
                        FPSListY3 = temp

                        Results1 = []
                        for i in range(len(FPSlistY)):
                            Results1.append([(FPSlistX[i]/multiplier), FPSListY[i]])

                        Results2 = []
                        for i in range(len(FPSlistY2)):
                            Results2.append([(FPSlistX2[i]/multiplier), FPSListY2[i]])

                        Results3 = []
                        for i in range(len(FPSlistY3)):
                            Results3.append([(FPSlistX3[i]/multiplier), FPSListY3[i]])

                        stage += 1

                    if stage == 5:
                        self.mod_pygame__.display.set_caption(
                            f"Pycraft: v{self.version}: Benchmark | Results")

                        self.display.fill(self.background_color)

                        self.display.blit(
                            title_font,
                            ((self.real_window_width-title_width)/2, 0))

                        self.display.blit(
                            benchmark_font,
                            (((self.real_window_width-title_width)/2)+65, 50))

                        FPSRect = self.mod_pygame__.Rect(
                            10,
                            130,
                            self.real_window_width-20,
                            300)

                        self.mod_pygame__.draw.rect(
                            self.display,
                            self.shape_color,
                            FPSRect,
                            0)

                        self.mod_pygame__.draw.lines(
                            self.display,
                            (255, 0, 0),
                            False,
                            Results3)

                        self.mod_pygame__.draw.lines(
                            self.display,
                            (0, 255, 0),
                            False,
                            Results1)

                        self.mod_pygame__.draw.lines(
                            self.display,
                            (0, 0, 255),
                            False,
                            Results2)

                        self.mod_pygame__.draw.line(
                            self.display,
                            self.accent_color,
                            (10, int(130+(300-((300/GlobalMax)*60)))),
                            (self.real_window_width-20, int(130+(300-((300/GlobalMax)*60)))))

                        self.display.blit(
                            sixty_FPS_data,
                            (13, int(130+(300-((300/GlobalMax)*60)))))

                        self.mod_pygame__.draw.line(
                            self.display,
                            self.accent_color,
                            (10, int(130+(300-((300/GlobalMax)*144)))),
                            (self.real_window_width-20, int(130+(300-((300/GlobalMax)*144)))))

                        self.display.blit(
                            one_four_four_FPS_data,
                            (13, int(130+(300-((300/GlobalMax)*140)))))

                        self.mod_pygame__.draw.line(
                            self.display,
                            self.accent_color,
                            (10, int(130+(300-((300/GlobalMax)*240)))),
                            (self.real_window_width-20, int(130+(300-((300/GlobalMax)*240)))))

                        self.display.blit(two_forty_FPS_data,
                                          (13, int(130+(300-((300/GlobalMax)*240)))))

                        HideRect = self.mod_pygame__.Rect(
                            0,
                            110,
                            self.real_window_width,
                            330)

                        self.mod_pygame__.draw.rect(
                            self.display,
                            self.background_color,
                            HideRect,
                            20)

                        self.display.blit(
                            FPS_information_text,
                            ((self.real_window_width-FPS_information_text_width)-3, 100))

                        self.display.blit(
                            file_information_text,
                            ((self.real_window_width-file_information_text_width)-3, 430))

                        Device_Results = "".join(("Your device achieved a score of: ",
                                                  f"{round(ReadSpeed, 2)}/100 ",
                                                  f"({round((100/100)*ReadSpeed)}%)"))

                        FileResults = devmode_information_font.render(
                            Device_Results,
                            self.aa,
                            self.font_color)

                        FileResultsWidth = FileResults.get_width()
                        self.display.blit(
                            FileResults,
                            ((self.real_window_width-FileResultsWidth)-3, 460))

                        self.display.blit(
                            hardware_information_text,
                            ((self.real_window_width-hardware_information_text_width)-3, 480))

                        self.display.blit(
                            CPUhwINFO,
                            ((self.real_window_width-CPUhwINFOwidth)-3, 500))

                        self.display.blit(
                            RAMhwINFO,
                            ((self.real_window_width-RAMhwINFOwidth)-3, 516))

                        GreenResults = "".join(("Blank screen test (green); Minimum: ",
                                                f"{round(Min1, 4)} FPS, Maximum: ",
                                                f"{round(Max1, 4)} FPS"))

                        BlueResults = "".join(("Blank screen test (blue); Minimum: ",
                                                f"{round(Min2, 4)} FPS, Maximum: ",
                                                f"{round(Max2, 4)} FPS"))

                        RedResults = "".join(("Blank screen test (red); Minimum: ",
                                               f"{round(Min3, 4)} FPS, Maximum: ",
                                               f"{round(Max3, 4)} FPS"))

                        GreenInfo = information_details_font.render(
                            GreenResults,
                            self.aa,
                            self.font_color)

                        BlueInfo = information_details_font.render(
                            BlueResults,
                            self.aa,
                            self.font_color)

                        RedInfo = information_details_font.render(
                            RedResults,
                            self.aa,
                            self.font_color)

                        self.display.blit(
                            GreenInfo,
                            (3, 430))
                        self.display.blit(
                            BlueInfo,
                            (3, 445))
                        self.display.blit(
                            RedInfo,
                            (3, 460))

                        if resize:
                            stage = 4
                            resize = False

                    if self.use_mouse_input is False:
                        if (stage == 0 and
                                self.mouse_button_down):

                            stage += 1

                        if self.joystick_exit:
                            self.joystick_exit = False
                            generate_benchmark.benchmark_exit(self)

                    for event in self.mod_pygame__.event.get():
                        if ((event.type == self.mod_pygame__.QUIT or
                            (event.type == self.mod_pygame__.KEYDOWN and
                                (event.key != self.mod_pygame__.K_SPACE) and
                                    stage <= 3) or
                            (event.type == self.mod_pygame__.KEYDOWN and
                                    event.key == self.mod_pygame__.K_ESCAPE)) and
                                self.use_mouse_input):

                            generate_benchmark.benchmark_exit(self)
                            
                        if ((event.type == self.mod_pygame__.KEYDOWN and
                              event.key == self.mod_pygame__.K_SPACE) and
                            stage == 0):

                            stage += 1
                        if event.type == self.mod_pygame__.VIDEORESIZE:
                            resize = True

                    if self.go_to is None:
                        self.mod_display_utils__.display_animations.fade_in(self)
                    else:
                        self.mod_display_utils__.display_animations.fade_out(self)

                    if self.startup_animation is False and (self.go_to is not None):
                        return None

                    self.mod_pygame__.display.flip()
                    self.clock.tick(
                        self.mod_display_utils__.display_utils.get_play_status(self))

                    if not self.error_message is None:
                        self.error_message = "".join(("Benchmark > generate_benchmark",
                                                     f"> Benchmark: {str(self.error_message)}"))
                        return
                    self.run_timer += self.mod_time__.perf_counter()-start_time
                    
            except Exception as Message:
                self.error_message = "Benchmark > generate_benchmark > Benchmark: "+str(Message)

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
