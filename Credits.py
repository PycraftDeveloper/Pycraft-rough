if __name__ != "__main__":
    class GenerateCredits:
        def __init__(self):
            pass

        def Credits(self):
            try:
                self.mod_caption_utils__.generate_captions.get_normal_caption(
                    self,
                    "Credits")

                if self.platform == "Linux":
                    devmode_information_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts//Book Antiqua.ttf")), 15)

                    LargeCreditsFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts//Book Antiqua.ttf")), 20)

                    subtitle_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts//Book Antiqua.ttf")), 35)

                    SmallCreditsFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts//Book Antiqua.ttf")), 15)

                else:
                    devmode_information_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts\\Book Antiqua.ttf")), 15)

                    LargeCreditsFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts\\Book Antiqua.ttf")), 20)

                    subtitle_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts\\Book Antiqua.ttf")), 35)

                    SmallCreditsFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts\\Book Antiqua.ttf")), 15)

                title_font = self.title_font.render(
                    "Pycraft",
                    self.aa,
                    self.font_color)
                title_width = title_font.get_width()
                TitleHeight = title_font.get_height()

                CreditsFont = subtitle_font.render(
                    "Credits",
                    self.aa,
                    self.secondary_font_color)

                CreditsString = [f"Pycraft: v{self.version}",
                                    " ",
                                    " ",
                                    "Game Director: Tom Jebbo",
                                    " ",
                                    "Art and Music Lead: Tom Jebbo",
                                    " ",
                                    "Additional Music Credits:",
                                    "".join(("Freesound: - Erokia's 'ambient wave compilation' ",
                                             "@ freesound.org/s/473545")),

                                    "".join(("Freesound: - Soundholder's ",
                                                "'ambient meadow near forest' @ ",
                                                "freesound.org/s/425368")),

                                    "".join(("Freesound: - Monte32's 'Footsteps_6_Dirt_shoe' ",
                                                "@ freesound.org/people/monte32/sounds/353799")),

                                    "".join(("Freesound: - Straget's 'Thunder' @ ",
                                                "https://freesound.org/people/straget/sounds/527664/")),

                                    "".join(("Freesound: - FlatHill's 'Rain and Thunder 4' @ ",
                                                "https://freesound.org/people/FlatHill/sounds/237729/")),

                                    "".join(("Freesound: - BlueDelta's 'Heavy Thunder Strike ",
                                                "- no Rain - QUADRO' @ ",
                                                "https://freesound.org/people/BlueDelta/sounds/446753/")),

                                    "".join(("Freesound: - Justkiddink's 'Thunder » Dry thunder1' @ ",
                                                "https://freesound.org/people/juskiddink/sounds/101933/")),

                                    "".join(("Freesound: - Netaj's 'Thunder' @ ",
                                                "https://freesound.org/people/netaj/sounds/193170/")),

                                    "".join(("Freesound: - Nimlos' 'Thunders » Rain Thunder' @ ",
                                                "https://freesound.org/people/Nimlos/sounds/359151/")),

                                    "".join(("Freesound: - Kangaroovindaloo's 'Thunder Clap' @ ",
                                                "https://freesound.org/people/kangaroovindaloo/sounds/585077/")),

                                    "".join(("Freesound: - Laribum's 'Thunder » thunder_01' @ "
                                             "https://freesound.org/people/laribum/sounds/353025/")),

                                    "".join(("Freesound: - Jmbphilmes's 'Rain » Rain light 2 (rural)' @ "
                                             "https://freesound.org/people/jmbphilmes/sounds/200273/")),

                                    " ",
                                    "Pycraft was developed in collaboration with:",
                                    "Dogukan Demir (https://github.com/demirdogukan)",
                                    "Henry Post (https://github.com/HenryFBP)",
                                    "".join(("Count of Freshness Traversal ",
                                             "(https://twitter.com/DmitryChunikhinn)")),
                                    " ",
                                    "With thanks to the developers of:",
                                    "Glcontext",
                                    "GPUtil",
                                    "Moderngl",
                                    "Moderngl-Window",
                                    "MouseInfo",
                                    "MultipleDispatch",
                                    "Numpy",
                                    "Pillow",
                                    "Psutil",
                                    "py-Cpuinfo",
                                    "PyAutoGUI",
                                    "Pygame",
                                    "PyGetWindow",
                                    "Pyglet",
                                    "PyJoystick",
                                    "PyMsgBox",
                                    "Pyperclip",
                                    "PyRect",
                                    "Pyrr",
                                    "PyScreeze",
                                    "PySDL2",
                                    "pytweening",
                                    "PyWavefront",
                                    "Resource-Man",
                                    "Six",
                                    "Microsoft Visual Studio Code",
                                    "",
                                    "".join(("For a more in depth accreditation ",
                                             "please check Pycraft's GitHub Page ",
                                             "here: github.com/PycraftDeveloper/Pycraft")),
                                    " ",
                                    "With thanks to:",
                                    "".join(("All my Twitter followers, and you for installing ",
                                             "this game, that's massively appreciated!")),
                                    "For more information please visit Pycraft's GitHub repository",
                                    " ",
                                    "Final Comments:",
                                    "".join(("Thank you greatly for supporting this project ",
                                             "simply by running it, I am sorry in advance ",
                                             "for any spelling mistakes. The programs will ",
                                             "be updated frequently and I shall do my best ",
                                             "to keep this up to date too. I also want to ",
                                             "add that you are welcome to view and change ",
                                             "the program and share it with your friends ",
                                             "however please may I have some credit, just ",
                                             "a name would do and if you find any bugs or ",
                                             "errors, please feel free to comment in the ",
                                             "comments section any feedback so I can ",
                                             "improve my program, it will all be much ",
                                             "appreciated and give as much detail as ",
                                             "you wish to give out.")),
                                    " ",
                                    " ",
                                    "Thank You!"]

                VisualYdisplacement = self.real_window_height
                IntroYDisplacement = (self.real_window_height-TitleHeight)/2
                timer = 5

                HoldOnExit = False
                Holdtimer = 0

                LoadText = False
                while True:
                    start_time = self.mod_time__.perf_counter()

                    self.mod_caption_utils__.generate_captions.get_normal_caption(
                        self,
                        "Credits")

                    self.mod_display_utils__.display_functionality.core_display_functions(
                        self)

                    self.display.fill(self.background_color)

                    Ypos = 0
                    for i in range(len(CreditsString)):
                        if LoadText:
                            if i > 0:
                                if CreditsString[i-1] == " ":
                                    TextSurface = LargeCreditsFont.render(
                                        CreditsString[i],
                                        self.aa,
                                        self.font_color)
                                else:
                                    TextSurface = SmallCreditsFont.render(
                                        CreditsString[i],
                                        self.aa,
                                        self.font_color)
                            else:
                                TextSurface = LargeCreditsFont.render(
                                    CreditsString[i],
                                    self.aa,
                                    self.font_color)

                            TextSurfaceHeight = TextSurface.get_height()
                            TextSurfaceWidth = TextSurface.get_width()

                            if TextSurfaceWidth > self.real_window_width:
                                Ypos += self.mod_text_utils__.TextWrap.blit_text(
                                    self,
                                    CreditsString[i],
                                    (3, Ypos+VisualYdisplacement),
                                    SmallCreditsFont,
                                    self.accent_color,
                                    self.real_window_width)
                            else:
                                if i+1 == len(CreditsString) and HoldOnExit:
                                    TextSurface_x_pos = (self.real_window_width-TextSurfaceWidth)/2
                                    TextSurface_y_pos = (self.real_window_height-TextSurfaceHeight)/2

                                    self.display.blit(
                                        TextSurface,
                                        (TextSurface_x_pos, TextSurface_y_pos))
                                else:
                                    if (Ypos+VisualYdisplacement >= 0 and
                                        Ypos+VisualYdisplacement <= self.real_window_height):

                                        TextSurface_x_pos = (self.real_window_width-TextSurfaceWidth)/2
                                        TextSurface_y_pos = Ypos+VisualYdisplacement

                                        self.display.blit(
                                            TextSurface,
                                            (TextSurface_x_pos, TextSurface_y_pos))

                            Ypos += TextSurfaceHeight

                    if timer >= 1:
                        self.display.blit(
                            title_font,
                            ((self.real_window_width-title_width)/2, 0+IntroYDisplacement))

                        timer -= 1/(self.aFPS/self.iteration)
                        VisualYdisplacement = self.real_window_height
                    else:
                        if IntroYDisplacement <= 0:
                            cover_Rect = self.mod_pygame__.Rect(
                                0,
                                0,
                                self.real_window_width,
                                90)

                            self.mod_pygame__.draw.rect(
                                self.display,
                                self.background_color,
                                cover_Rect)

                            self.display.blit(
                                title_font,
                                ((self.real_window_width-title_width)/2, 0))

                            self.display.blit(
                                CreditsFont,
                                (((self.real_window_width-title_width)/2)+65, 50))

                            VisualYdisplacement -= 60/(self.aFPS/self.iteration)
                            LoadText = True
                            if Ypos+VisualYdisplacement <= 360:
                                HoldOnExit = True
                                Holdtimer += 1/(self.aFPS/self.iteration)
                                if Holdtimer >= 5:
                                    self.go_to = "Home"
                        else:
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
                                ((self.real_window_width-title_width)/2, 0+IntroYDisplacement))

                            self.display.blit(
                                CreditsFont,
                                (((self.real_window_width-title_width)/2)+65, 50+IntroYDisplacement))

                            IntroYDisplacement -= 90/(self.aFPS/self.iteration)
                            VisualYdisplacement = self.real_window_height

                    self.mod_drawing_utils__.generate_graph.create_devmode_graph(
                        self,
                        devmode_information_font)

                    if self.go_to is None:
                        self.mod_display_utils__.display_animations.fade_in(self)
                    else:
                        self.mod_display_utils__.display_animations.fade_out(
                            self)

                    if self.startup_animation is False and (self.go_to is not None):
                        return None

                    self.mod_pygame__.display.flip()
                    self.clock.tick(
                        self.mod_display_utils__.display_utils.get_play_status(self))

                    if self.error_message is not None:
                        self.error_message = "".join(("Credits > GenerateCredits ",
                                                     f"> Credits: {str(self.error_message)}"))
                        return

                    self.run_timer += self.mod_time__.perf_counter()-start_time
                    
            except Exception as Message:
                self.error_message = "Credits > GenerateCredits > Credits: "+str(Message)
                self.error_message_detailed = "".join(self.mod_traceback__.format_exception(
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
