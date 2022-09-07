if __name__ != "_main_":
    class GenerateStartupScreen:
        def _init_(self):
            pass

        def Start(self):
            try:
                if self.theme is False:
                    self.theme = "dark"
                    update_theme_later = True
                else:
                    update_theme_later = False
                    
                self.mod_theme_utils__.determine_theme_colours.get_colors(self)

                if update_theme_later:
                    self.theme = False
                
                if self.platform == "Linux":
                    PresentsFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 35)

                    PycraftFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 60)

                    NameFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 45)

                else:
                    PresentsFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 35)

                    PycraftFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 60)

                    NameFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 45)

                NameText = NameFont.render(
                    "PycraftDev",
                    True,
                    self.font_color)
                NameTextWidth = NameText.get_width()
                NameTextHeight = NameText.get_height()

                self.real_window_width = self.mod_pygame__.display.get_window_size()[0]
                self.real_window_height = self.mod_pygame__.display.get_window_size()[1]

                self.display.fill(self.background_color)
                self.mod_pygame__.display.flip()
                self.mod_pygame__.display.set_caption(f"Pycraft: v{self.version}: Welcome")

                PresentsText = PresentsFont.render(
                    "presents",
                    True,
                    self.font_color)

                presentOffSet = 39

                PycraftText = PycraftFont.render(
                    "Pycraft",
                    True,
                    self.font_color)
                TitleTextWidth = PycraftText.get_width()

                PycraftStartPos = self.mod_pygame__.Vector2(
                    ((self.real_window_width-TitleTextWidth)/2,
                        self.real_window_height/2 - NameTextHeight))

                PycraftEndPos = self.mod_pygame__.Vector2(
                    PycraftStartPos.x,
                    0)

                self.clock = self.mod_pygame__.time.Clock()

                InterpolateSpeed = 0.02

                timer = 2

                while timer > 0 and self.run_full_startup:
                    self.mod_display_utils__.display_functionality.core_display_functions(
                        self,
                        location="exit",
                        resize=False)

                    self.display.fill(self.background_color)

                    timer -= 0.01

                    self.display.blit(
                        NameText,
                        ((self.real_window_width-NameTextWidth)/2,
                            self.real_window_height/2 - NameTextHeight))

                    if timer <= 1:
                        self.display.blit(
                            PresentsText,
                            ((self.real_window_width-NameTextWidth)/2 + presentOffSet,
                                self.real_window_height/2 + NameTextHeight - 77))

                    self.clock.tick(60)
                    self.mod_pygame__.display.flip()

                Thread_ResourceCheck = self.mod_threading__.Thread(
                    target=self.mod_pycraft_startup_test__.StartupTest.PycraftResourceTest,
                    args=(self, False,))
                Thread_ResourceCheck.name = "Thread_ResourceCheck"
                Thread_ResourceCheck.start()

                runtimer = 0

                while True:
                    self.mod_display_utils__.display_functionality.core_display_functions(
                        self,
                        location="exit",
                        resize=False)

                    RefreshTime = self.mod_time__.perf_counter()

                    self.display.fill(self.background_color)

                    if "Thread_ResourceCheck" not in str(self.mod_threading__.enumerate()):
                        PycraftStartPos = self.mod_pygame__.math.Vector2.lerp(
                            PycraftStartPos,
                            PycraftEndPos,
                            InterpolateSpeed)

                    self.display.blit(
                        PycraftText,
                        (PycraftStartPos.x, PycraftStartPos.y))

                    self.mod_pygame__.display.flip()
                    self.clock.tick(60)

                    if PycraftStartPos.y <= 1:
                        PycraftStartPos = PycraftEndPos
                        self.run_full_startup = False
                        break

                    runtimer += self.mod_time__.perf_counter()-RefreshTime

            except Exception as Message:
                self.error_message = "".join(("StartupAnimation > GenerateStartupScreen ",
                                             f"> Start: {str(Message)}"))

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
