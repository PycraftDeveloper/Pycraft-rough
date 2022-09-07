if __name__ != "__main__":
    class GenerateInventory:
        def __init__(self):
            pass

        def inventory_exit(self):
            try:
                self.load_3D = False
                self.joystick_exit = False

                if self.sound:
                    self.mod_sound_utils__.play_sound.play_click_sound(
                        self)

                self.mod_pygame__.display.quit()
                
            except Exception as Message:
                self.error_message = "".join(("Inventory > GenerateInventory ",
                                              f"> inventory_exit: {str(Message)}"))

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

        def Inventory(self):
            try:
                self.mod_display_utils__.display_utils.set_display(self)
                self.display.fill(self.background_color)
                self.mod_pygame__.display.update()

                if self.platform == "Linux":
                    self.title_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 60)

                else:
                    self.title_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 60)

                PycraftTitle = self.title_font.render(
                    "Pycraft",
                    self.aa,
                    self.font_color).convert_alpha()
                title_width = PycraftTitle.get_width()

                self.real_window_width = self.mod_pygame__.display.get_window_size()[0]
                self.real_window_height = self.mod_pygame__.display.get_window_size()[1]

                AlphaSurface = self.mod_pygame__.Surface(
                    (self.real_window_width, self.real_window_height),
                    self.mod_pygame__.HWSURFACE|
                    self.mod_pygame__.SRCALPHA).convert_alpha()
                AlphaSurface.set_alpha(204)
                AlphaSurface.fill(self.background_color)

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
                hover8 = False

                if self.platform == "Linux":
                    ButtonFont1 = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 30)

                    ButtonFont2 = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 30)

                    ButtonFont3 = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 30)

                    ButtonFont4 = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 30)

                    ButtonFont5 = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 30)

                    ButtonFont6 = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 30)

                    ButtonFont7 = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 30)

                    ButtonFont8 = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 30)

                else:
                    ButtonFont1 = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 30)

                    ButtonFont2 = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 30)

                    ButtonFont3 = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 30)

                    ButtonFont4 = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 30)

                    ButtonFont5 = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 30)

                    ButtonFont6 = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 30)

                    ButtonFont7 = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 30)

                    ButtonFont8 = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 30)

                WeaponsText = ButtonFont1.render(
                    "Weapons",
                    self.aa,
                    self.font_color).convert_alpha()
                WeaponsTextWidth = WeaponsText.get_width()

                RangedWeaponsText = ButtonFont2.render(
                    "Ranged Weapons",
                    self.aa,
                    self.font_color).convert_alpha()
                RangedWeaponsTextWidth = RangedWeaponsText.get_width()

                ShieldsText = ButtonFont3.render(
                    "Shields",
                    self.aa,
                    self.font_color).convert_alpha()
                ShieldsTextWidth = ShieldsText.get_width()

                ArmourText = ButtonFont4.render(
                    "Armour",
                    self.aa,
                    self.font_color).convert_alpha()
                ArmourTextWidth = ArmourText.get_width()

                FoodText = ButtonFont5.render(
                    "Food",
                    self.aa,
                    self.font_color).convert_alpha()
                FoodTextWidth = FoodText.get_width()

                ItemsText = ButtonFont6.render(
                    "Items",
                    self.aa,
                    self.font_color).convert_alpha()
                ItemsTextWidth = ItemsText.get_width()

                SpecialItemsText = ButtonFont7.render(
                    "Special Items",
                    self.aa,
                    self.font_color).convert_alpha()
                SpecialItemsTextWidth = SpecialItemsText.get_width()

                OptionsText = ButtonFont7.render(
                    "Options",
                    self.aa,
                    self.font_color).convert_alpha()
                OptionsTextWidth = OptionsText.get_width()

                fullscreen_x, fullscreen_y = self.mod_pyautogui__.size()

                self.mouse_x = self.real_window_width/2
                self.mouse_y = self.real_window_height/2

                if self.aa:
                    if self.platform == "Linux":
                        pilImage = self.mod_PIL_Image_.open(
                            self.mod_OS__.path.join(
                                self.base_folder,
                                ("resources//general resources//PauseIMG.png"))).resize(
                                    (self.real_window_width,
                                     self.real_window_height),
                                    self.mod_PIL_Image_.ANTIALIAS)
                    else:
                        pilImage = self.mod_PIL_Image_.open(
                            self.mod_OS__.path.join(
                                self.base_folder,
                                ("resources\\general resources\\PauseIMG.png"))).resize(
                                    (self.real_window_width,
                                     self.real_window_height),
                                    self.mod_PIL_Image_.ANTIALIAS)

                else:
                    if self.platform == "Linux":
                        pilImage = self.mod_PIL_Image_.open(
                            self.mod_OS__.path.join(
                                self.base_folder,
                                ("resources//general resources//PauseIMG.png"))).resize(
                                    (self.real_window_width,
                                     self.real_window_height))

                    else:
                        pilImage = self.mod_PIL_Image_.open(
                            self.mod_OS__.path.join(
                                self.base_folder,
                                ("resources\\general resources\\PauseIMG.png"))).resize(
                                    (self.real_window_width,
                                     self.real_window_height))

                BLURRED_pilImage = pilImage.filter(self.mod_PIL_ImageFilter_.BoxBlur(4))

                PauseImg = self.mod_image_utils__.ConvertImage.pilImageToSurface(
                    self,
                    BLURRED_pilImage)

                self.display.blit(
                    PauseImg,
                    (0, 0))

                self.display.blit(
                    AlphaSurface,
                    (0, 0))

                while True:
                    self.mod_caption_utils__.generate_captions.get_normal_caption(
                        self,
                        "Inventory")

                    self.display.fill(self.background_color)

                    self.display.blit(
                        PauseImg,
                        (0, 0))

                    self.display.blit(
                        AlphaSurface,
                        (0, 0))

                    self.display.blit(
                        PycraftTitle,
                        ((self.real_window_width-title_width)/2, 0))

                    self.mod_display_utils__.display_functionality.core_display_functions(
                        self, checkEvents=False)

                    if self.joystick_exit:
                        GenerateInventory.inventory_exit(self)

                        return

                    for event in self.mod_pygame__.event.get():
                        if (event.type == self.mod_pygame__.QUIT or
                                (event.type == self.mod_pygame__.KEYDOWN and
                                    event.key == self.mod_pygame__.K_ESCAPE) or
                                (event.type == self.mod_pygame__.KEYDOWN and
                                    event.key == self.mod_pygame__.K_e)):

                            GenerateInventory.inventory_exit(self)
                            
                            return

                        if event.type == self.mod_pygame__.WINDOWFOCUSLOST:
                            self.window_in_focus = False
                        elif event.type == self.mod_pygame__.WINDOWFOCUSGAINED:
                            self.window_in_focus = True

                        if event.type == self.mod_pygame__.WINDOWSIZECHANGED:
                            self.real_window_width = self.mod_pygame__.display.get_window_size()[0]
                            self.real_window_height = self.mod_pygame__.display.get_window_size()[1]

                            AlphaSurface = self.mod_pygame__.Surface(
                                (self.real_window_width, self.real_window_height),
                                self.mod_pygame__.HWSURFACE|
                                self.mod_pygame__.SRCALPHA).convert_alpha()
                            AlphaSurface.set_alpha(204)
                            AlphaSurface.fill(self.background_color)

                            if self.platform == "Linux":
                                if self.aa:
                                    pilImage = self.mod_PIL_Image_.open(
                                        self.mod_OS__.path.join(
                                            self.base_folder,
                                            ("resources//general resources//PauseIMG.png"))).resize(
                                                (self.real_window_width,
                                                 self.real_window_height),
                                                self.mod_PIL_Image_.ANTIALIAS)

                                else:
                                    pilImage = self.mod_PIL_Image_.open(
                                        self.mod_OS__.path.join(
                                            self.base_folder,
                                            ("resources//general resources//PauseIMG.png"))).resize(
                                                (self.real_window_width,
                                                 self.real_window_height))

                            else:
                                if self.aa:
                                    pilImage = self.mod_PIL_Image_.open(
                                        self.mod_OS__.path.join(
                                            self.base_folder,
                                            ("resources\\general resources\\PauseIMG.png"))).resize(
                                                (self.real_window_width,
                                                 self.real_window_height),
                                                self.mod_PIL_Image_.ANTIALIAS)

                                else:
                                    pilImage = self.mod_PIL_Image_.open(
                                        self.mod_OS__.path.join(
                                            self.base_folder,
                                            ("resources\\general resources\\PauseIMG.png"))).resize(
                                                (self.real_window_width,
                                                 self.real_window_height))

                            BLURRED_pilImage = pilImage.filter(self.mod_PIL_ImageFilter_.BoxBlur(4))

                            PauseImg = self.mod_image_utils__.ConvertImage.pilImageToSurface(
                                self,
                                BLURRED_pilImage)

                        if event.type == self.mod_pygame__.KEYDOWN:
                            if event.key == self.mod_pygame__.K_F11:
                                self.mod_display_utils__.display_utils.update_display(self)

                                AlphaSurface = self.mod_pygame__.Surface(
                                    (fullscreen_x,
                                     fullscreen_y),
                                    self.mod_pygame__.HWSURFACE|
                                    self.mod_pygame__.SRCALPHA).convert_alpha()
                                AlphaSurface.set_alpha(204)
                                AlphaSurface.fill(self.background_color)

                    if (self.mouse_y >= 202*self.y_scale_factor and
                                self.mouse_y <= 247*self.y_scale_factor and
                                self.mouse_x >= 1155):

                        hover1 = True
                        if self.mouse_button_down:
                            PauseImg = self.mod_image_utils__.ConvertImage.pilImageToSurface(
                                self,
                                BLURRED_pilImage)

                            if self.sound:
                                self.mod_sound_utils__.play_sound.play_click_sound(self)

                            self.mouse_button_down = False
                    else:
                        hover1 = False

                    if (self.mouse_y >= 252*self.y_scale_factor and
                                self.mouse_y <= 297*self.y_scale_factor and
                                self.mouse_x >= 1105):

                        hover2 = True
                        if self.mouse_button_down:
                            PauseImg = self.mod_image_utils__.ConvertImage.pilImageToSurface(
                                self,
                                BLURRED_pilImage)

                            if self.sound:
                                self.mod_sound_utils__.play_sound.play_click_sound(self)
                            self.mouse_button_down = False
                    else:
                        hover2 = False

                    if (self.mouse_y >= 302*self.y_scale_factor and
                                self.mouse_y <= 347*self.y_scale_factor and
                                self.mouse_x >= 865):

                        hover3 = True
                        if self.mouse_button_down:
                            PauseImg = self.mod_image_utils__.ConvertImage.pilImageToSurface(
                                self,
                                BLURRED_pilImage)

                            if self.sound:
                                self.mod_sound_utils__.play_sound.play_click_sound(self)
                            self.mouse_button_down = False
                    else:
                        hover3 = False

                    if (self.mouse_y >= 402*self.y_scale_factor and
                                self.mouse_y <= 447*self.y_scale_factor and
                                self.mouse_x >= 1035):

                        hover4 = True
                        if self.mouse_button_down:
                            PauseImg = self.mod_image_utils__.ConvertImage.pilImageToSurface(
                                self,
                                BLURRED_pilImage)

                            if self.sound:
                                self.mod_sound_utils__.play_sound.play_click_sound(self)
                            self.mouse_button_down = False
                    else:
                        hover4 = False

                    if (self.mouse_y >= 352*self.y_scale_factor and
                                self.mouse_y <= 397*self.y_scale_factor and
                                self.mouse_x >= 880):

                        hover5 = True
                        if self.mouse_button_down:
                            PauseImg = self.mod_image_utils__.ConvertImage.pilImageToSurface(
                                self,
                                BLURRED_pilImage)

                            if self.sound:
                                self.mod_sound_utils__.play_sound.play_click_sound(self)
                            self.mouse_button_down = False
                    else:
                        hover5 = False

                    if (self.mouse_y >= 502*self.y_scale_factor and
                                self.mouse_y <= 547*self.y_scale_factor and
                                self.mouse_x >= 1095):

                        hover6 = True
                        if self.mouse_button_down:
                            PauseImg = self.mod_image_utils__.ConvertImage.pilImageToSurface(
                                self,
                                BLURRED_pilImage)

                            if self.sound:
                                self.mod_sound_utils__.play_sound.play_click_sound(self)
                            self.mouse_button_down = False
                    else:
                        hover6 = False

                    if (self.mouse_y >= 452*self.y_scale_factor and
                                self.mouse_y <= 497*self.y_scale_factor and
                                self.mouse_x >= 1095):

                        hover7 = True
                        if self.mouse_button_down:
                            PauseImg = self.mod_image_utils__.ConvertImage.pilImageToSurface(
                                self,
                                BLURRED_pilImage)

                            if self.sound:
                                self.mod_sound_utils__.play_sound.play_click_sound(self)
                            self.mouse_button_down = False
                    else:
                        hover7 = False

                    if (self.mouse_y >= 552*self.y_scale_factor and
                                self.mouse_y <= 597*self.y_scale_factor and self.mouse_x >= 1095):

                        hover8 = True
                        if self.mouse_button_down:
                            PauseImg = self.mod_image_utils__.ConvertImage.pilImageToSurface(
                                self,
                                BLURRED_pilImage)

                            if self.sound:
                                self.mod_sound_utils__.play_sound.play_click_sound(self)
                            self.mouse_button_down = False
                    else:
                        hover8 = False

                    ButtonFont1.set_underline(hover1)
                    ButtonFont2.set_underline(hover2)
                    ButtonFont3.set_underline(hover3)
                    ButtonFont4.set_underline(hover4)
                    ButtonFont5.set_underline(hover5)
                    ButtonFont6.set_underline(hover6)
                    ButtonFont7.set_underline(hover7)
                    ButtonFont8.set_underline(hover8)
                    AlphaSurface.fill(self.background_color)

                    self.display.blit(
                        WeaponsText,
                        ((self.real_window_width-WeaponsTextWidth)-2,
                         200*self.y_scale_factor))
                    if hover1:
                        AlphaSurface.blit(
                            selector,
                            (self.real_window_width-(WeaponsTextWidth+selector_width)-2,
                             200*self.y_scale_factor))

                    self.display.blit(
                        RangedWeaponsText,
                        ((self.real_window_width-RangedWeaponsTextWidth)-2,
                         250*self.y_scale_factor))
                    if hover2:
                        AlphaSurface.blit(
                            selector,
                            (self.real_window_width-(RangedWeaponsTextWidth+selector_width)-2,
                             250*self.y_scale_factor))

                    self.display.blit(
                        ShieldsText,
                        ((self.real_window_width-ShieldsTextWidth)-2,
                         300*self.y_scale_factor))
                    if hover3:
                        AlphaSurface.blit(
                            selector,
                            (self.real_window_width-(ShieldsTextWidth+selector_width)-2,
                             300*self.y_scale_factor))

                    self.display.blit(
                        ArmourText,
                        ((self.real_window_width-ArmourTextWidth)-2,
                         350*self.y_scale_factor))
                    if hover4:
                        AlphaSurface.blit(
                            selector,
                            (self.real_window_width-(FoodTextWidth+selector_width)-2,
                             400*self.y_scale_factor))

                    self.display.blit(
                        FoodText,
                        ((self.real_window_width-FoodTextWidth)-2,
                         400*self.y_scale_factor))
                    if hover5:
                        AlphaSurface.blit(
                            selector,
                            (self.real_window_width-(ArmourTextWidth+selector_width)-2,
                             350*self.y_scale_factor))

                    self.display.blit(
                        ItemsText,
                        ((self.real_window_width-ItemsTextWidth)-2,
                         450*self.y_scale_factor))
                    if hover6:
                        AlphaSurface.blit(
                            selector,
                            (self.real_window_width-(SpecialItemsTextWidth+selector_width)-2,
                             500*self.y_scale_factor))

                    self.display.blit(
                        SpecialItemsText,
                        ((self.real_window_width-SpecialItemsTextWidth)-2,
                         500*self.y_scale_factor))
                    if hover7:
                        AlphaSurface.blit(
                            selector,
                            (self.real_window_width-(ItemsTextWidth+selector_width)-2,
                             450*self.y_scale_factor))

                    self.display.blit(
                        OptionsText,
                        ((self.real_window_width-OptionsTextWidth)-2,
                         550*self.y_scale_factor))
                    if hover8:
                        AlphaSurface.blit(
                            selector,
                            (self.real_window_width-(OptionsTextWidth+selector_width)-2,
                             550*self.y_scale_factor))

                    self.mod_pygame__.display.flip()
                    self.clock.tick(
                        self.mod_display_utils__.display_utils.get_play_status(self))

                    if self.error_message is not None:
                        self.error_message = "".join(("Inventory > GenerateInventory ",
                                                     f"> Inventory: {str(self.error_message)}"))
                        return
                    
            except Exception as Message:
                self.error_message = "Inventory > GenerateInventory > Inventory: "+str(Message)

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
