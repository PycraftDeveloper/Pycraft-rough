if __name__ != "__main__":
    class determine_theme_colours:
        def __init__(self):
            pass

        def get_colors(self):
            try:
                self.themeArray = [
                    [(255, 255, 255),
                        [30, 30, 30],
                        (80, 80, 80),
                        (237, 125, 49),
                        (255, 255, 255)],

                    [(0, 0, 0),
                        [255, 255, 255],
                        (80, 80, 80),
                        (237, 125, 49),
                        (100, 100, 100)]]

                if self.theme == "dark":
                    self.font_color = self.themeArray[0][0]
                    self.background_color = self.themeArray[0][1]
                    self.shape_color = self.themeArray[0][2]
                    self.accent_color = self.themeArray[0][3]
                    self.secondary_font_color = self.themeArray[0][4]

                elif self.theme == "light":
                    self.font_color = self.themeArray[1][0]
                    self.background_color = self.themeArray[1][1]
                    self.shape_color = self.themeArray[1][2]
                    self.accent_color = self.themeArray[1][3]
                    self.secondary_font_color = self.themeArray[1][4]
                    
            except Exception as Message:
                self.error_message = "ThemeUtils > determine_theme_colours > get_colors: "+str(Message)

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)


        def get_theme_GUI(self):
            try:
                Title = self.title_font.render(
                    "Pycraft",
                    True,
                    self.font_color)
                title_width = Title.get_width()

                if self.platform == "Linux":
                    MiddleFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 30)

                    SideFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 20)

                else:
                    MiddleFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 30)

                    SideFont = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 20)

                self.mouse_button_down = False

                DarkModeFont = MiddleFont.render(
                    "Dark",
                    True,
                    self.font_color)
                DarkModeFont_Width = DarkModeFont.get_width()
                DarkModeFont_Height = DarkModeFont.get_height()

                LightModeFont = MiddleFont.render(
                    "Light",
                    True,
                    self.font_color)
                LightModeFont_Width = LightModeFont.get_width()
                LightModeFont_Height = LightModeFont.get_height()

                self.mouse_x = self.real_window_width/2
                self.mouse_y = self.real_window_height/2

                while True:
                    self.mod_display_utils__.display_functionality.core_display_functions(
                        self,
                        location="saveANDexit")
                    
                    self.mod_caption_utils__.generate_captions.get_normal_caption(
                        self,
                        "Theme selector")

                    LightRect = self.mod_pygame__.Rect(
                        0,
                        100,
                        self.real_window_width/2,
                        self.real_window_height-200)

                    DarkRect = self.mod_pygame__.Rect(
                        self.real_window_width/2,
                        100,
                        self.real_window_width/2,
                        self.real_window_height-200)

                    self.display.fill(self.background_color)

                    Title = self.title_font.render(
                        "Pycraft",
                        True,
                        self.font_color)
                    title_width = Title.get_width()

                    self.display.blit(
                        Title,
                        ((self.real_window_width-title_width)/2, 0))

                    self.theme = "light"
                    self.mod_theme_utils__.determine_theme_colours.get_colors(self)

                    self.mod_pygame__.draw.rect(
                        self.display,
                        self.background_color,
                        LightRect)

                    self.mod_pygame__.draw.rect(
                        self.display,
                        self.shape_color,
                        LightRect,
                        3)

                    LightModeFont = MiddleFont.render(
                        "Light",
                        True,
                        self.font_color)
                    LightModeFont_Width = LightModeFont.get_width()
                    LightModeFont_Height = LightModeFont.get_height()

                    self.display.blit(
                        LightModeFont,
                        (((self.real_window_width/2)-LightModeFont_Width)/2,
                            (self.real_window_height-LightModeFont_Height)/2))

                    self.theme = "dark"
                    self.mod_theme_utils__.determine_theme_colours.get_colors(self)

                    self.mod_pygame__.draw.rect(
                        self.display,
                        self.background_color,
                        DarkRect)

                    self.mod_pygame__.draw.rect(
                        self.display,
                        self.shape_color,
                        DarkRect,
                        3)

                    DarkModeFont = MiddleFont.render(
                        "Dark",
                        True,
                        self.font_color)
                    DarkModeFont_Width = DarkModeFont.get_width()
                    DarkModeFont_Height = DarkModeFont.get_height()

                    self.display.blit(
                        DarkModeFont,
                        (((self.real_window_width+(self.real_window_width/2))-DarkModeFont_Width)/2,
                            (self.real_window_height-DarkModeFont_Height)/2))

                    if self.mouse_y >= 100 and self.mouse_y <= self.real_window_height-100:
                        if self.mouse_x <= self.real_window_width/2:
                            self.mod_pygame__.draw.rect(
                                self.display,
                                self.accent_color,
                                LightRect,
                                1)

                            self.theme = "light"

                            if self.mouse_button_down:
                                if self.sound:
                                    self.mod_sound_utils__.play_sound.play_click_sound(self)
                                break

                        elif self.mouse_x >= self.real_window_width/2:
                            self.mod_pygame__.draw.rect(
                                self.display,
                                self.accent_color,
                                DarkRect,
                                1)

                            self.theme = "dark"
                            if self.mouse_button_down:
                                if self.sound:
                                    self.mod_sound_utils__.play_sound.play_click_sound(self)
                                break

                        self.mod_theme_utils__.determine_theme_colours.get_colors(self)

                    Choice = SideFont.render(
                        "".join((f"You have selected the {self.theme} ",
                                 "theme, you can change this later in settings")),

                        self.aa,
                        self.font_color)
                    ChoiceWidth = Choice.get_width()
                    choice_height = Choice.get_height()

                    self.display.blit(
                        Choice,
                        ((self.real_window_width-ChoiceWidth)/2,
                            (self.real_window_height-choice_height)))

                    self.mod_pygame__.display.update()
                    self.clock.tick(self.FPS)
                    
            except Exception as Message:
                self.error_message = "".join(("ThemeUtils > determine_theme_colours ",
                                             f"> get_theme_GUI: {str(Message)}"))

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
