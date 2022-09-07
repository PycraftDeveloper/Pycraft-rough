if __name__ != "__main__":
    class generate_settings:
        def __init__(self):
            pass

        def restart_function(self):
            try:
                if self.platform == "Linux":
                    self.mod_subprocess__.call(
                        [self.mod_sys__.executable,
                            (str(self.base_folder) + "//main.py")] + self.mod_sys__.argv[1:])
                    
                else:
                    self.mod_subprocess__.call(
                        [self.mod_sys__.executable,
                        (str(self.base_folder) + "\\main.py")] + self.mod_sys__.argv[1:])
                    
            except Exception as Message:
                self.error_message = "Settings > generate_settings > restart_function: "+str(Message)

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

        def update_profile(self):
            try:
                if self.settings_preset == "low":
                    self.FPS = 15
                    self.aa = False
                    self.render_fog = False
                    self.fancy_graphics = False
                    self.fancy_particles = False
                    self.aFPS = (self.aFPS/self.iteration)
                    self.iteration = 1

                elif self.settings_preset == "medium":
                    self.FPS = 30
                    self.aa = True
                    self.render_fog = False
                    self.fancy_graphics = True
                    self.fancy_particles = False
                    self.aFPS = (self.aFPS/self.iteration)
                    self.iteration = 1
                    
                elif self.settings_preset == "high":
                    self.FPS = 60
                    self.aa = True
                    self.render_fog = True
                    self.fancy_graphics = True
                    self.fancy_particles = True
                    self.aFPS = (self.aFPS/self.iteration)
                    self.iteration = 1
                    
                elif self.settings_preset == "adaptive":
                    CPU_Freq = (self.mod_psutil__.cpu_freq(percpu=True)[0][2])/10
                    MEM_Total = self.mod_psutil__.virtual_memory().total

                    if (CPU_Freq > 300 and
                            MEM_Total > 8589934592):

                        self.aa = True
                        self.render_fog = True
                        self.fancy_graphics = True
                        self.fancy_particles = True

                    elif (CPU_Freq > 200 and
                            MEM_Total > 4294967296):

                        self.aa = True
                        self.render_fog = True
                        self.fancy_graphics = True
                        self.fancy_particles = False

                    elif (CPU_Freq > 100 and
                            MEM_Total > 2147483648):

                        self.aa = False
                        self.render_fog = False
                        self.fancy_graphics = True
                        self.fancy_particles = False

                    elif (CPU_Freq < 100 and
                            CPU_Freq > 75 and
                            MEM_Total > 1073741824):

                        self.aa = False
                        self.render_fog = False
                        self.fancy_graphics = False
                        self.fancy_particles = False
                        
            except Exception as Message:
                self.error_message = "".join(("Settings > generate_settings > ",
                                             f"update_profile: {str(Message)}"))

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

        def Settings(self):
            try:
                self.mod_caption_utils__.generate_captions.get_normal_caption(
                    self,
                    "Settings")

                if self.platform == "Linux":
                    subtitle_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 35)

                    button_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 30)

                    general_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 15)
                    
                else:
                    subtitle_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 35)

                    button_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 30)

                    general_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 15)

                title_font = self.title_font.render(
                    "Pycraft",
                    self.aa,
                    self.font_color)

                title_width = title_font.get_width()

                settings_font = subtitle_font.render(
                    "Settings",
                    self.aa,
                    self.secondary_font_color)

                button_offset = 0

                current_menu = "General"
                hover_menu = None

                self.mouse_x = self.real_window_width/2
                self.mouse_y = self.real_window_height/2

                if self.platform == "Linux":
                    with open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("data files//settings_config.json")), "r") as openFile:

                        settings_structure = self.mod_json__.load(openFile)

                    selector = self.mod_pygame__.image.load(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            (f"resources//general resources//selectorICON{self.theme}.jpg")))
                    selector.convert()

                else:
                    with open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("data files\\settings_config.json")), "r") as openFile:

                        settings_structure = self.mod_json__.load(openFile)

                    selector = self.mod_pygame__.image.load(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            (f"resources\\general resources\\selectorICON{self.theme}.jpg")))
                    selector.convert()

                selector_width = selector.get_width()

                initial_theme = self.theme

                hovering = False
                max_x = 0
                info_offset = 0
                hover_id = None
                files_to_remove = True
                scanned_files = False
                hovering_over_key = False
                scan_directory = False
                maximum_remap_width = 0
                disable_events = False

                scrollbar_needed = False
                general_y_position = 0
                scroll = 0
                scroll_enabled = True

                while True:
                    start_time = self.mod_time__.perf_counter()
                    
                    display_events = self.mod_display_utils__.display_functionality.core_display_functions(
                        self,
                        return_events=True,
                        disable_events=disable_events)

                    for event in display_events:
                        if event.type == self.mod_pygame__.MOUSEWHEEL and scrollbar_needed:
                            if self.use_mouse_input:
                                self.mod_pygame__.mouse.set_cursor(
                                    self.mod_pygame__.SYSTEM_CURSOR_SIZENS)
                                if str(event.y)[0] == "-":
                                    if scroll > 0:
                                        scroll -= 5

                                else:
                                    if scroll_enabled:
                                        scroll += 5

                    self.mod_caption_utils__.generate_captions.get_normal_caption(
                        self,
                        "Settings")

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
                        settings_font,
                        (((self.real_window_width-title_width)/2)+55, 50))

                    if initial_theme != self.theme:
                        title_font = self.title_font.render(
                            "Pycraft",
                            self.aa,
                            self.font_color)

                        title_width = title_font.get_width()

                        settings_font = subtitle_font.render(
                            "Settings",
                            self.aa,
                            self.secondary_font_color)
                
                        initial_theme = self.theme
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

                    button_y_position = 0
                    button_id = 0
                            
                    for key in settings_structure:
                        
                        if (key == "Developer options" and
                                self.extended_developer_options is False):
                            
                            font_color = self.shape_color
                            button_font.set_underline(False)
                            
                        else:
                            if key == hover_menu:
                                button_font.set_underline(True)

                            else:
                                button_font.set_underline(False)

                            
                            font_color = self.font_color
                            
                        button = button_font.render(
                            key,
                            self.aa,
                            font_color).convert_alpha()
                        button_width = button.get_width()
                        button_height = button.get_height()

                        if button_width > max_x:
                            max_x = button_width
                        
                        button_height += 50 - button_height

                        button_blit_y = (button_y_position * self.y_scale_factor) + button_offset
                        button_blit_x = (self.real_window_width-button_width)-2

                        if key == hover_menu:
                            if not (key == "Developer options" and
                                    self.extended_developer_options is False):
                        
                                self.display.blit(
                                    selector,
                                    (self.real_window_width-(button_width+selector_width)-2,
                                        button_blit_y))
                            
                        self.display.blit(
                            button,
                            (button_blit_x,
                                button_blit_y))

                        if ((self.mouse_x > button_blit_x and
                                    self.mouse_x < self.real_window_width and
                                    self.mouse_y > button_blit_y and
                                    self.mouse_y < button_blit_y + button_height) and
                                not (key == "Developer options" and 
                                        self.extended_developer_options is False)):
                            
                            hover_menu = key
                            hovering = True

                            if (self.mouse_button_down and
                                    current_menu != key):
                                
                                current_menu = key
                                scrollbar_needed = False
                                scroll = 0
                                self.mouse_button_down = False
                                
                                if current_menu == "Storage and permissions":
                                    scan_directory = True
                                
                                if self.sound:
                                    self.mod_sound_utils__.play_sound.play_click_sound(
                                        self)
                                    
                        else:
                            if hover_menu == key:
                                hover_menu = None

                        button_y_position += button_height

                        sub_menu = settings_structure[current_menu]

                        general_y_position = 100

                        if scan_directory:
                            scan_directory = False
                            self.mod_file_utils__.scan_folder.search_files(
                                self,
                                self.base_folder)

                        if self.clear_cache:
                            self.clear_cache = False
                            
                            if files_to_remove:
                                self.mod_file_utils__.delete_files.clear_temporary_files(
                                    self)

                                files_to_remove = False
                                scan_directory = True

                        if self.scan_pycraft:
                            self.scan_pycraft = False

                            self.mod_pycraft_startup_test__.StartupTest.PycraftResourceTest(
                                self,
                                True)

                            scanned_files = True

                        if self.reset_pycraft:
                            self.reset_pycraft = False

                            theme = self.theme
                            for key in self.save_keys:
                                setattr(self, key, self.save_keys[key])

                            self.theme = theme

                            if self.connection_permission is None:
                                permission_message = "Can we have your permission to check the internet for updates to Pycraft?"
                                self.connection_permission = self.mod_tkinter_utils__.TkinterInfo.GetPermissions(
                                    self,
                                    permission_message)

                            if self.remove_file_permission is None:
                                permission_message = "Can we have your permission to send files from the Pycraft directory to the recycle bin?"
                                self.remove_file_permission = self.mod_tkinter_utils__.TkinterInfo.GetPermissions(
                                    self,
                                    permission_message)

                            if self.show_strobe_effects is None:
                                self.show_strobe_effects = self.mod_tkinter_messagebox_.askquestion(
                                    "Check Permission",
                                    "".join(("Strobe effects and bright flashes of light can ",
                                                "cause discomfort, (for example lightning), you can choose here ",
                                                "whether to enable or disable those ",
                                                "strobe effects in Pycraft.\n",
                                                "Click 'yes' to allow for strobe effects, or 'no' ",
                                                "to turn them off. You can always adjust this in ",
                                                "Pycraft's settings, under 'Storage and permissions'.")))

                                if self.show_strobe_effects == "yes":
                                    self.show_strobe_effects = True

                                else:
                                    self.show_strobe_effects = False
                            
                        if self.exit_mode == "restart":
                            if self.save_on_exit:
                                self.mod_file_utils__.pycraft_config_utils.save_pycraft_config(
                                self)
                                
                            if self.error_message is not None:
                                self.mod_error_utils__.generate_error_screen.error_screen(
                                    self)
                                
                            self.mod_threading__.Thread(
                                target=generate_settings.restart_function,
                                args=(self,)).start()

                            self.mod_pygame__.quit()
                            while True:
                                self.mod_time__.sleep(30)

                        if self.exit_mode == "exit":
                            if self.save_on_exit:
                                self.mod_file_utils__.pycraft_config_utils.save_pycraft_config(
                                self)
                                
                            if self.error_message is not None:
                                self.mod_error_utils__.generate_error_screen.error_screen(
                                    self)
                                
                            self.mod_pygame__.quit()
                            self.mod_sys__.exit()

                        if sub_menu[0] is not None:
                            for item in range(len(sub_menu)):
                                data = []
                                mouse_over = False

                                if scrollbar_needed:
                                    scroll_x_offset = 9

                                else:
                                    scroll_x_offset = 0
                                    
                                for entry in range(3, len(sub_menu[item])):
                                    if str(sub_menu[item][entry]) != "directory_structure":
                                        if str(sub_menu[item][entry]) == "aFPS":
                                            argument = int(self.aFPS/self.iteration)

                                        elif str(sub_menu[item][entry]) == "keybinds":
                                            pass
                                        
                                        else:
                                            if str(sub_menu[item][entry]) == "use_mouse_input":
                                                argument = not self.__dict__[sub_menu[item][entry]]
                                            else:
                                                argument = self.__dict__[sub_menu[item][entry]]
                                                
                                            if "float" in str(type(argument)):
                                                argument = int(argument)
                                                
                                            if argument is True:
                                                argument = "Enabled"
                                                
                                            if argument is False:
                                                argument = "Disabled"
                                        
                                    data.append(argument)

                                if (sub_menu[item][3] == "music_volume" and
                                        self.music is False):
                                    
                                    font_color = self.shape_color
                                    
                                elif (sub_menu[item][3] == "sound_volume" and
                                        self.sound is False):
                                    
                                    font_color = self.shape_color

                                elif (sub_menu[item][3] == "FPS" and
                                        self.vsync):

                                    font_color = self.shape_color

                                elif (sub_menu[item][3] == "aa_quality" and
                                        self.aa is False):

                                    font_color = self.shape_color

                                elif (sub_menu[item][3] == "clear_cache" and
                                        files_to_remove is False):

                                    font_color = self.shape_color
                                    text_to_render = str(sub_menu[item][0]) + ": Done."

                                elif (sub_menu[item][3] == "scan_pycraft" and
                                        scanned_files is True):

                                    font_color = self.shape_color
                                    text_to_render = str(sub_menu[item][0]) + ": Done, no errors were found."
                                    
                                else:
                                    font_color = self.font_color
                                    text_to_render = str(sub_menu[item][0]).format(*data)
                                    
                                text = general_font.render(
                                    text_to_render,
                                    self.aa,
                                    font_color).convert_alpha()
                                text_height = text.get_height()
                                
                                self.display.blit(
                                    text,
                                    (scroll_x_offset, general_y_position - scroll))
                                            
                                argument_variable = sub_menu[item][3]
                                saved_y_position = general_y_position

                                if list(sub_menu[item][2].keys())[0] == "remap_function":
                                    remap_pos = (general_y_position + text_height + 10) - scroll
                                    options = self.input_configuration[self.selected_input_reconfig]
                                    
                                    keybind_height, mouse_over, hover_id, maximum_remap_width, disable_events = self.mod_drawing_utils__.draw_setting_elements.draw_remap_function(
                                        self,
                                        remap_pos,
                                        options,
                                        hovering,
                                        mouse_over,
                                        general_font,
                                        maximum_remap_width,
                                        display_events,
                                        scrollbar_needed)

                                    general_y_position += keybind_height

                                elif list(sub_menu[item][2].keys())[0] == "directory_structure":
                                    button_pos = (general_y_position + text_height + 10) - scroll

                                    graph_height, hovering, mouse_over, hover_id = self.mod_drawing_utils__.draw_setting_elements.draw_directory_structure(
                                        self,
                                        button_pos,
                                        general_font,
                                        hovering,
                                        mouse_over,
                                        hover_id,
                                        hovering_over_key,
                                        scrollbar_needed)

                                    general_y_position += graph_height

                                else:
                                    name = str(sub_menu[item][entry])
                                    if name == "use_mouse_input":
                                        value = not self.__dict__[argument_variable]

                                    else:
                                        value = self.__dict__[argument_variable]
                                    
                                    if list(sub_menu[item][2].keys())[0] == "button":
                                        button_pos = (general_y_position + text_height + 10) - scroll
                                        button_text_array = sub_menu[item][2]["button"]
                                        
                                        button_height, hovering, mouse_over = self.mod_drawing_utils__.draw_setting_elements.draw_buttons(
                                            self,
                                            button_pos,
                                            button_text_array,
                                            general_font,
                                            value,
                                            argument_variable,
                                            hovering,
                                            mouse_over,
                                            files_to_remove,
                                            scanned_files,
                                            scrollbar_needed)
                                        
                                        general_y_position += button_height

                                    if list(sub_menu[item][2].keys())[0] == "multi-button":
                                        button_pos = (general_y_position + text_height + 10) - scroll
                                        button_text_array = sub_menu[item][2]["multi-button"]

                                        button_height, hovering, mouse_over = self.mod_drawing_utils__.draw_setting_elements.draw_multi_buttons(
                                            self,
                                            button_pos,
                                            button_text_array,
                                            general_font,
                                            argument_variable,
                                            hovering,
                                            mouse_over,
                                            scrollbar_needed)

                                        general_y_position += button_height

                                    if list(sub_menu[item][2].keys())[0] == "slider":
                                        slider_pos = (general_y_position + text_height + 10) - scroll
                                        slider_array = sub_menu[item][2]["slider"]
                                        minimum = slider_array[0]
                                        maximum = slider_array[1]
                                        
                                        slider_height, hovering, mouse_over = self.mod_drawing_utils__.draw_setting_elements.draw_slider(
                                            self,
                                            slider_pos,
                                            minimum,
                                            maximum,
                                            value,
                                            argument_variable,
                                            hovering,
                                            mouse_over,
                                            scrollbar_needed)
                                        
                                        general_y_position += slider_height

                                    if list(sub_menu[item][2].keys())[0] == "toggle":
                                        toggle_pos = (general_y_position + text_height + 10) - scroll
                                        slider_array = sub_menu[item][2]["toggle"]
                                        value_0 = slider_array[0]
                                        value_1 = slider_array[1]
                                        
                                        toggle_height, hovering, mouse_over = self.mod_drawing_utils__.draw_setting_elements.draw_toggle(
                                            self,
                                            toggle_pos,
                                            value_0,
                                            value_1,
                                            value,
                                            argument_variable,
                                            hovering,
                                            mouse_over,
                                            scrollbar_needed)
                                        
                                        general_y_position += toggle_height

                                if mouse_over:
                                    info_offset = self.mod_drawing_utils__.draw_setting_elements.create_information_message(
                                        self,
                                        general_font,
                                        sub_menu[item][1],
                                        saved_y_position,
                                        max_x,
                                        info_offset)
                                    
                                general_y_position += text_height

                            if (general_y_position - scroll) + 10 > self.real_window_height:
                                scroll_enabled = True

                            else:
                                scroll_enabled = False

                            if general_y_position > self.real_window_height:
                                scrollbar_needed = True

                                ### style 1
                                '''rect = self.mod_pygame__.Rect(
                                    2,
                                    scroll + 2,
                                    3,
                                    (self.real_window_height - (general_y_position - self.real_window_height)) - 26)'''

                                ### style 2
                                rect = self.mod_pygame__.Rect(
                                    2,
                                    scroll + 2,
                                    3,
                                    self.real_window_height - (general_y_position % self.real_window_height) - 18)

                                self.mod_pygame__.draw.rect(
                                    self.display,
                                    self.shape_color,
                                    rect,
                                    border_radius=2)

                            else:
                                scrollbar_needed = False
                                scroll = 0

                        button_id += 1
                        
                    button_y_position *= self.y_scale_factor

                    button_offset = (self.real_window_height - button_y_position) / 2

                    self.mod_drawing_utils__.generate_graph.create_devmode_graph(
                        self,
                        general_font)

                    if self.go_to is None:
                        self.mod_display_utils__.display_animations.fade_in(
                            self)
                    else:
                        self.mod_display_utils__.display_animations.fade_out(
                            self)

                    if not self.startup_animation and (self.go_to is not None):
                        return None

                    if hovering:
                        hovering = False
                        self.mod_pygame__.mouse.set_cursor(
                                self.mod_pygame__.cursors.Cursor(
                                    self.mod_pygame__.SYSTEM_CURSOR_HAND))
                    else:
                        self.mod_pygame__.mouse.set_cursor(
                            self.mod_pygame__.cursors.Cursor(
                                self.mod_pygame__.SYSTEM_CURSOR_ARROW))
                        
                    self.mod_pygame__.display.flip()
                    self.clock.tick(
                        self.mod_display_utils__.display_utils.get_play_status(self))

                    if self.error_message is not None:
                        self.error_message = "".join(
                            ("Settings > generate_settings > Settings: ",
                             str(self.error_message)))

                        return

                    self.run_timer += self.mod_time__.perf_counter()-start_time
                    
            except Exception as Message:
                self.error_message = (
                    f"Settings > generate_settings > Settings: {str(Message)}")

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
