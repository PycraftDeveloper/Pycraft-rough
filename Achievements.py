if __name__ != "__main__":
    class generate_achievements:
        def __init__(self):
            pass

        def Achievements(self):
            try:
                self.mod_caption_utils__.generate_captions.get_normal_caption(
                    self,
                    "Achievements")

                if self.platform == "Linux":
                    subtitle_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts//Book Antiqua.ttf")), 35)

                    devmode_information_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts//Book Antiqua.ttf")), 15)
                else:
                    subtitle_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts\\Book Antiqua.ttf")), 35)

                    devmode_information_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder, ("fonts\\Book Antiqua.ttf")), 15)

                title_font = self.title_font.render(
                    "Pycraft",
                    self.aa,
                    self.font_color)

                title_width = title_font.get_width()

                achievements_font = subtitle_font.render(
                    "Achievements",
                    self.aa,
                    self.secondary_font_color)

                while True:
                    start_time = self.mod_time__.perf_counter()

                    self.mod_display_utils__.display_functionality.core_display_functions(
                        self)

                    self.mod_caption_utils__.generate_captions.get_normal_caption(
                        self,
                        "Achievements")

                    self.display.fill(self.background_color)

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
                        achievements_font,
                        (((self.real_window_width-title_width)/2)+55, 50))

                    self.mod_drawing_utils__.generate_graph.create_devmode_graph(
                        self,
                        devmode_information_font)

                    if self.go_to is None:
                        self.mod_display_utils__.display_animations.fade_in(self)
                    else:
                        self.mod_display_utils__.display_animations.fade_out(self)

                    if not self.startup_animation and (self.go_to is not None):
                        return None

                    self.mod_pygame__.display.flip()
                    self.clock.tick(
                        self.mod_display_utils__.display_utils.get_play_status(self))

                    if self.error_message is not None:
                        self.error_message = "".join(
                            ("Achievements > generate_achievements > Achievements: ",
                             str(self.error_message)))

                        return

                    self.run_timer += self.mod_time__.perf_counter()-start_time
                    
            except Exception as Message:
                self.error_message = (
                    f"Achievements > generate_achievements > Achievements: {str(Message)}")

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
