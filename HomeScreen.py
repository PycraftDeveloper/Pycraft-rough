if __name__ != "__main__":
    class GenerateHomeScreen:
        def __init__(self):
            pass

        def CreateBanner(self):
            try:
                global show_message, MessageColor

                if self.platform == "Linux":
                    SideFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts//Book Antiqua.ttf")), 20)

                    version_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts//Book Antiqua.ttf")), 20)

                    MessageFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts//Book Antiqua.ttf")), 20)

                else:
                    SideFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts\\Book Antiqua.ttf")), 20)

                    version_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts\\Book Antiqua.ttf")), 20)

                    MessageFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts\\Book Antiqua.ttf")), 20)

                Name = SideFont.render(
                    "By PycraftDev",
                    self.aa,
                    self.font_color).convert_alpha()
                NameHeight = Name.get_height()

                Version = version_font.render(
                    f"Version: {self.version}",
                    self.aa,
                    self.font_color).convert_alpha()
                VersionWidth = Version.get_width()
                VersionHeight = Version.get_height()

                timer_start = 0
                RenderedText = False

                while self.command == "Undefined":
                    RenderRect = self.mod_pygame__.Rect(
                        0,
                        self.real_window_height-40,
                        self.real_window_width,
                        self.real_window_height)

                    self.display.fill(self.background_color, RenderRect)

                    if show_message is not None and MessageColor is not None and RenderedText is False:
                        timer_start = self.mod_time__.perf_counter()

                        MessageText = MessageFont.render(
                            show_message,
                            self.aa,
                            MessageColor).convert_alpha()
                        MessageTextWidth = MessageText.get_width()
                        MessageTextHeight = MessageText.get_height()

                        RenderedText = True

                    if RenderedText:
                        if self.mod_time__.perf_counter()-timer_start < 3:
                            self.display.blit(
                                MessageText,
                                ((self.real_window_width-MessageTextWidth)/2,
                                 (self.real_window_height-MessageTextHeight)))

                        else:
                            show_message = None
                            MessageColor = None
                            RenderedText = False
                    else:
                        if self.use_mouse_input is False:
                            MessageText = MessageFont.render(
                                "".join(("On the controller; use the D-pad to navigate the menu, ",
                                         "press 'B' to confirm or press 'Y' to exit")),
                                self.aa,
                                self.font_color).convert_alpha()
                            MessageTextWidth = MessageText.get_width()
                            MessageTextHeight = MessageText.get_height()

                            self.display.blit(
                                MessageText,
                                ((self.real_window_width-MessageTextWidth)/2,
                                 (self.real_window_height-MessageTextHeight)))

                    self.display.blit(
                        Name,
                        (0,
                         (self.real_window_height-NameHeight)))

                    self.display.blit(
                        Version,
                        ((self.real_window_width-VersionWidth)-2,
                         (self.real_window_height-VersionHeight)))

                    self.mod_pygame__.display.update(RenderRect)

                    self.clock.tick(
                        self.mod_display_utils__.display_utils.get_play_status(self)/2)
                    
            except Exception as Message:
                if str(Message) != "display Surface quit":
                    self.error_message = "".join(("HomeScreen > GenerateHomeScreen > ",
                                                 "CreateBanner (thread): {str(Message)}"))

                    self.error_message_detailed = "".join(
                        self.mod_traceback__.format_exception(
                            None,
                            Message,
                            Message.__traceback__))

                    self.mod_error_utils__.generate_error_screen.error_screen(self)

        def Home_Screen(self):
            try:
                global show_message, MessageColor

                show_message = None
                MessageColor = self.font_color

                BannerThread = self.mod_threading__.Thread(
                    target=self.mod_home_screen__.GenerateHomeScreen.CreateBanner,
                    args=(self,))
                BannerThread.name = "Thread_BannerThread_HS"
                BannerThread.daemon = True
                BannerThread.start()

                self.mod_caption_utils__.generate_captions.get_normal_caption(
                    self,
                    "Home screen")

                if self.platform == "Linux":
                    selector = self.mod_pygame__.image.load(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            (f"resources//general resources//selectorICON{self.theme}.jpg")))
                    selector.convert()

                else:
                    selector = self.mod_pygame__.image.load(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            (f"resources\\general resources\\selectorICON{self.theme}.jpg")))
                    selector.convert()

                selector_width = selector.get_width()
                hover1 = False
                hover2 = False
                hover3 = False
                hover4 = False
                hover5 = False
                hover6 = False
                hover7 = False

                PycraftTitle = self.title_font.render(
                    "Pycraft",
                    self.aa,
                    self.font_color)
                title_width = PycraftTitle.get_width()

                self.real_window_width = self.mod_pygame__.display.get_window_size()[0]
                self.real_window_height = self.mod_pygame__.display.get_window_size()[1]

                self.display.blit(
                    PycraftTitle,
                    ((self.real_window_width-title_width)/2, 0))

                self.mod_pygame__.display.flip()

                if self.platform == "Linux":
                    ButtonFont1 = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts//Book Antiqua.ttf")), 30)

                    ButtonFont2 = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts//Book Antiqua.ttf")), 30)

                    ButtonFont3 = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts//Book Antiqua.ttf")), 30)

                    ButtonFont4 = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts//Book Antiqua.ttf")), 30)

                    ButtonFont5 = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts//Book Antiqua.ttf")), 30)

                    ButtonFont6 = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts//Book Antiqua.ttf")), 30)

                    ButtonFont7 = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts//Book Antiqua.ttf")), 30)

                    devmode_information_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts//Book Antiqua.ttf")), 15)

                else:
                    ButtonFont1 = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts\\Book Antiqua.ttf")), 30)

                    ButtonFont2 = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts\\Book Antiqua.ttf")), 30)

                    ButtonFont3 = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts\\Book Antiqua.ttf")), 30)

                    ButtonFont4 = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts\\Book Antiqua.ttf")), 30)

                    ButtonFont5 = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts\\Book Antiqua.ttf")), 30)

                    ButtonFont6 = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts\\Book Antiqua.ttf")), 30)

                    ButtonFont7 = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts\\Book Antiqua.ttf")), 30)

                    devmode_information_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts\\Book Antiqua.ttf")), 15)

                oldTHEME = self.theme
                coloursARRAY = []

                anim = False

                special = [30,
                           30,
                           30]

                TargetARRAY = []

                ColourDisplacement = 80

                increment = False

                self.currently_displaying_message = False

                outdated = self.outdated

                self.mouse_x = self.real_window_width/2
                self.mouse_y = self.real_window_height/2

                while True:
                    start_time = self.mod_time__.perf_counter()

                    RenderRect = self.mod_pygame__.Rect(
                        0,
                        0,
                        self.real_window_width,
                        self.real_window_height-40)

                    if self.get_outdated == [True, False]:
                        self.get_outdated = [
                            True,
                            True]

                        outdated = self.outdated

                    if self.fancy_graphics:
                        coloursARRAY = []
                        if anim:
                            anim = False
                            TargetARRAY = []
                            for a in range(self.mod_random__.randint(0, 32)):
                                TargetARRAY.append(a)

                        if len(TargetARRAY) == 0:
                            TargetARRAY = [33]

                        for i in range(32):
                            for j in range(len(TargetARRAY)):
                                if i == TargetARRAY[j]:
                                    coloursARRAY.append(special)

                                else:
                                    coloursARRAY.append(self.shape_color)

                        if increment is False:
                            RandomInt = self.mod_random__.randint(0, 10)
                            if self.aFPS == 0 or self.iteration == 0:
                                ColourDisplacement -= RandomInt/(self.FPS/4)

                            else:
                                ColourDisplacement -= RandomInt/((self.aFPS/self.iteration)/4)

                            special[0] = ColourDisplacement
                            special[1] = ColourDisplacement
                            special[2] = ColourDisplacement

                        if increment:
                            RandomInt = self.mod_random__.randint(0, 10)
                            if self.aFPS == 0 or self.iteration == 0:
                                ColourDisplacement += RandomInt/(self.FPS/4)

                            else:
                                ColourDisplacement += RandomInt/((self.aFPS/self.iteration)/4)

                            special[0] = ColourDisplacement
                            special[1] = ColourDisplacement
                            special[2] = ColourDisplacement

                        if special[0] <= 30:
                            increment = True
                            special[0] = 30
                            special[1] = 30
                            special[2] = 30

                        if special[0] >= 80:
                            increment = False
                            anim = True
                            special[0] = 80
                            special[1] = 80
                            special[2] = 80
                    else:
                        coloursARRAY = self.fancy_graphics

                    if str(self.display) == "<Surface(Dead display)>":
                        if self.fullscreen is False:
                            self.mod_display_utils__.display_utils.set_display(self)

                        elif self.fullscreen:
                            self.mod_display_utils__.display_utils.set_display(self)

                    if not oldTHEME == self.theme:
                        if self.platform == "Linux":
                            selector = self.mod_pygame__.image.load(
                                self.mod_OS__.path.join(
                                    self.base_folder,
                                    ("".join(("resources//general resources",
                                              f"//selectorICON{self.theme}.jpg")))))
                            selector.convert()

                        else:
                            selector = self.mod_pygame__.image.load(
                                self.mod_OS__.path.join(
                                    self.base_folder,
                                    ("".join(("resources\\general resources",
                                              f"\\selectorICON{self.theme}.jpg")))))
                            selector.convert()

                        selector_width = selector.get_width()
                        oldTHEME = self.theme

                    self.display.fill(self.background_color, RenderRect)

                    PycraftTitle = self.title_font.render(
                        "Pycraft",
                        self.aa,
                        self.font_color).convert_alpha()
                    title_width = PycraftTitle.get_width()

                    Play = ButtonFont1.render(
                        "Play",
                        self.aa,
                        self.font_color).convert_alpha()
                    PlayWidth = Play.get_width()

                    SettingsText = ButtonFont2.render(
                        "Settings",
                        self.aa,
                        self.font_color).convert_alpha()
                    SettingsWidth = SettingsText.get_width()

                    Character_DesignerText = ButtonFont3.render(
                        "Character Designer",
                        self.aa,
                        self.font_color).convert_alpha()
                    CharDesignerWidth = Character_DesignerText.get_width()

                    AchievementsText = ButtonFont4.render(
                        "Achievements",
                        self.aa,
                        self.font_color).convert_alpha()
                    AchievementsWidth = AchievementsText.get_width()

                    Credits_and_Change_Log_Text = ButtonFont5.render(
                        "Credits",
                        self.aa,
                        self.font_color).convert_alpha()
                    CreditsWidth = Credits_and_Change_Log_Text.get_width()

                    BenchmarkText = ButtonFont6.render(
                        "Benchmark",
                        self.aa,
                        self.font_color).convert_alpha()
                    BenchmarkWidth = BenchmarkText.get_width()

                    InstallerText = ButtonFont7.render(
                        "Installer",
                        self.aa,
                        self.font_color).convert_alpha()
                    InstallerWidth = InstallerText.get_width()

                    self.mod_display_utils__.display_functionality.core_display_functions(
                        self,
                        location="saveANDexit")

                    self.mod_caption_utils__.generate_captions.get_normal_caption(
                        self,
                        "Home screen")

                    ButtonFont1.set_underline(hover1)
                    ButtonFont2.set_underline(hover2)
                    ButtonFont3.set_underline(hover3)
                    ButtonFont4.set_underline(hover4)
                    ButtonFont5.set_underline(hover5)
                    ButtonFont6.set_underline(hover6)
                    ButtonFont7.set_underline(hover7)

                    if self.go_to is None:
                        if (self.mouse_y >= 202*self.y_scale_factor and
                                self.mouse_y <= 247*self.y_scale_factor and
                                self.mouse_x >= (self.real_window_width-(PlayWidth+selector_width))-2):

                            hover1 = True

                            if self.mouse_button_down:
                                if self.sound:
                                    self.mod_sound_utils__.play_sound.play_click_sound(self)

                                if self.show_strobe_effects is None:
                                    self.show_strobe_effects = self.mod_tkinter_messagebox_.askquestion(
                                        "Check Permission",
                                        "".join(("Strobe effects and bright flashes of light can ",
                                                 "cause discomfort, (for example lightning), you can choose here ",
                                                 "whether to enable or disable those ",
                                                 "strobe effects in Pycraft.\n\n",
                                                 "Click 'yes' to allow for strobe effects, or 'no' ",
                                                 "to turn them off. You can always adjust this in ",
                                                 "Pycraft's settings, under 'Storage and permissions'.")))

                                    if self.show_strobe_effects == "yes":
                                        self.show_strobe_effects = True

                                    else:
                                        self.show_strobe_effects = False
                                        
                                self.go_to = "Play"
                                self.startup_animation = True
                                self.run_timer = 0

                        else:
                            hover1 = False

                        if (self.mouse_y >= 252*self.y_scale_factor and
                                self.mouse_y <= 297*self.y_scale_factor and
                                self.mouse_x >= (self.real_window_width-(SettingsWidth+selector_width))-2):

                            hover2 = True

                            if self.mouse_button_down:
                                if self.sound:
                                    self.mod_sound_utils__.play_sound.play_click_sound(self)

                                self.go_to = "Settings"
                                self.startup_animation = True
                                self.run_timer = 0

                        else:
                            hover2 = False

                        if (self.mouse_y >= 302*self.y_scale_factor and
                                self.mouse_y <= 347*self.y_scale_factor and
                                self.mouse_x >= (self.real_window_width-(CharDesignerWidth+selector_width)-2)):

                            hover3 = True

                            if self.mouse_button_down:
                                if self.sound:
                                    self.mod_sound_utils__.play_sound.play_click_sound(self)

                                self.go_to = "CharacterDesigner"
                                self.startup_animation = True
                                self.run_timer = 0

                        else:
                            hover3 = False

                        if (self.mouse_y >= 402*self.y_scale_factor and
                                self.mouse_y <= 447*self.y_scale_factor and
                                self.mouse_x >= (self.real_window_width-(AchievementsWidth+selector_width)-2)):

                            hover4 = True

                            if self.mouse_button_down:
                                if self.sound:
                                    self.mod_sound_utils__.play_sound.play_click_sound(self)

                                self.go_to = "Achievements"
                                self.startup_animation = True
                                self.run_timer = 0

                        else:
                            hover4 = False

                        if (self.mouse_y >= 352*self.y_scale_factor and
                                self.mouse_y <= 397*self.y_scale_factor and
                                self.mouse_x >= (self.real_window_width-(CreditsWidth+selector_width)-2)):

                            hover5 = True

                            if self.mouse_button_down:
                                if self.sound:
                                    self.mod_sound_utils__.play_sound.play_click_sound(self)

                                self.go_to = "Credits"
                                self.startup_animation = True
                                self.run_timer = 0

                        else:
                            hover5 = False

                        if (self.mouse_y >= 452*self.y_scale_factor and
                                self.mouse_y <= 497*self.y_scale_factor and
                                self.mouse_x >= (self.real_window_width-(BenchmarkWidth+selector_width)-2)):

                            hover6 = True

                            if self.mouse_button_down:
                                if self.sound:
                                    self.mod_sound_utils__.play_sound.play_click_sound(self)

                                self.go_to = "Benchmark"
                                self.startup_animation = True
                                self.run_timer = 0

                        else:
                            hover6 = False

                        if (self.mouse_y >= 502*self.y_scale_factor and
                                self.mouse_y <= 547*self.y_scale_factor and
                                self.mouse_x >= (self.real_window_width-(InstallerWidth+selector_width)-2)):

                            hover7 = True

                            if self.mouse_button_down:
                                if self.sound:
                                    self.mod_sound_utils__.play_sound.play_click_sound(self)

                                self.go_to = "Installer"
                                self.startup_animation = True
                                self.run_timer = 0

                        else:
                            hover7 = False

                    if show_message is None:
                        if self.updated:
                            self.updated = False
                            show_message = f"Successfully updated Pycraft to v{self.version}"
                            MessageColor = (0, 255, 0)

                        elif outdated and self.total_number_of_updates == 1:
                            outdated = False
                            show_message = f"There are {self.total_number_of_updates} updates available!"
                            MessageColor = (0, 255, 0)

                        elif outdated and self.total_number_of_updates == 1:
                            outdated = False
                            show_message = "There is an update available!"
                            MessageColor = (0, 255, 0)

                        elif self.device_connected_update:
                            if self.device_connected:
                                show_message = "".join(("There is a new input device available! ",
                                                   "You can change input modes in settings"))

                                MessageColor = (0, 255, 0)

                            else:
                                if self.use_mouse_input:
                                    show_message = "Terminated connection to an input device"
                                    MessageColor = (255, 0, 0)

                                else:
                                    show_message = "".join(("Terminated connection to current ",
                                                       "input device, returning to ",
                                                       "default setting"))

                                    MessageColor = (255, 0, 0)
                                    self.use_mouse_input = True

                            self.device_connected_update = False

                    self.display.blit(
                        PycraftTitle,
                        ((self.real_window_width-title_width)/2, 0))

                    self.display.blit(
                        Play,
                        ((self.real_window_width-PlayWidth)-2, 200*self.y_scale_factor))

                    self.display.blit(
                        SettingsText,
                        ((self.real_window_width-SettingsWidth)-2, 250*self.y_scale_factor))

                    self.display.blit(
                        Character_DesignerText,
                        ((self.real_window_width-CharDesignerWidth)-2, 300*self.y_scale_factor))

                    self.display.blit(
                        Credits_and_Change_Log_Text,
                        ((self.real_window_width-CreditsWidth)-2, 350*self.y_scale_factor))

                    self.display.blit(
                        AchievementsText,
                        ((self.real_window_width-AchievementsWidth)-2, 400*self.y_scale_factor))

                    self.display.blit(
                        BenchmarkText,
                        ((self.real_window_width-BenchmarkWidth)-2, 450*self.y_scale_factor))

                    self.display.blit(
                        InstallerText,
                        ((self.real_window_width-InstallerWidth)-2, 500*self.y_scale_factor))

                    if hover1:
                        self.display.blit(
                            selector,
                            (self.real_window_width-(PlayWidth+selector_width)-2, 200*self.y_scale_factor))

                        if self.use_mouse_input:
                            self.mod_pygame__.mouse.set_cursor(self.mod_pygame__.SYSTEM_CURSOR_HAND)

                    elif hover2:
                        self.display.blit(
                            selector,
                            (self.real_window_width-(SettingsWidth+selector_width)-2, 250*self.y_scale_factor))
                        
                        if self.use_mouse_input:
                            self.mod_pygame__.mouse.set_cursor(self.mod_pygame__.SYSTEM_CURSOR_HAND)

                    elif hover3:
                        self.display.blit(
                            selector,
                            (self.real_window_width-(CharDesignerWidth+selector_width)-2, 300*self.y_scale_factor))

                        if self.use_mouse_input:
                            self.mod_pygame__.mouse.set_cursor(self.mod_pygame__.SYSTEM_CURSOR_HAND)

                    elif hover5:
                        self.display.blit(
                            selector,
                            (self.real_window_width-(CreditsWidth+selector_width)-2, 350*self.y_scale_factor))

                        if self.use_mouse_input:
                            self.mod_pygame__.mouse.set_cursor(self.mod_pygame__.SYSTEM_CURSOR_HAND)

                    elif hover4:
                        self.display.blit(
                            selector,
                            (self.real_window_width-(AchievementsWidth+selector_width)-2, 400*self.y_scale_factor))

                        if self.use_mouse_input:
                            self.mod_pygame__.mouse.set_cursor(self.mod_pygame__.SYSTEM_CURSOR_HAND)

                    elif hover6:
                        self.display.blit(
                            selector,
                            (self.real_window_width-(BenchmarkWidth+selector_width)-2, 450*self.y_scale_factor))

                        if self.use_mouse_input:
                            self.mod_pygame__.mouse.set_cursor(self.mod_pygame__.SYSTEM_CURSOR_HAND)

                    elif hover7:
                        self.display.blit(
                            selector,
                            (self.real_window_width-(InstallerWidth+selector_width)-2, 500*self.y_scale_factor))

                        if self.use_mouse_input:
                            self.mod_pygame__.mouse.set_cursor(self.mod_pygame__.SYSTEM_CURSOR_HAND)

                    else:
                        if self.use_mouse_input:
                            self.mod_pygame__.mouse.set_cursor(
                                self.mod_pygame__.SYSTEM_CURSOR_ARROW)


                    self.mod_drawing_utils__.generate_graph.create_devmode_graph(
                        self,
                        devmode_information_font)

                    self.mod_drawing_utils__.draw_rose.create_rose(
                        self,
                        coloursARRAY)

                    if self.startup_animation is False and (self.go_to is not None):
                        return self.go_to

                    if self.go_to is None:
                        self.mod_display_utils__.display_animations.fade_in(
                            self,
                            size="limited")
                    else:
                        self.mod_display_utils__.display_animations.fade_out(
                            self,
                            size="limited")

                    self.mod_pygame__.display.update(RenderRect)

                    self.clock.tick(self.mod_display_utils__.display_utils.get_play_status(self)/2)
                    self.run_timer += self.mod_time__.perf_counter()-start_time

                    if self.error_message is not None:
                        self.error_message = "HomeScreen: "+str(self.error_message)
                        return

            except Exception as Message:
                print(Message)
                self.error_message = "HomeScreen > GenerateHomeScreen > Home_Screen: "+ str(Message)
                
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
