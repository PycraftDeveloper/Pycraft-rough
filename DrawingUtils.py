from xmlrpc.client import FastMarshaller


if __name__ != "__main__":
    class draw_rose:
        def __init__(self):
            pass

        def create_rose(self, coloursARRAY):
            try:
                if coloursARRAY is False:
                    coloursARRAY = []
                    for _ in range(32):
                        coloursARRAY.append(self.shape_color)

                defLargeOctagon = [(205*self.x_scale_factor, 142*self.y_scale_factor),
                                   (51*self.x_scale_factor, 295*self.y_scale_factor),
                                   (51*self.x_scale_factor, 512*self.y_scale_factor),
                                   (205*self.x_scale_factor, 666*self.y_scale_factor),
                                   (422*self.x_scale_factor, 666*self.y_scale_factor),
                                   (575*self.x_scale_factor, 512*self.y_scale_factor),
                                   (575*self.x_scale_factor, 295*self.y_scale_factor),
                                   (422*self.x_scale_factor, 142*self.y_scale_factor)]

                self.mod_pygame__.draw.polygon(
                    self.display,
                    self.shape_color,
                    defLargeOctagon,
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[0],
                    (205*self.x_scale_factor,142*self.y_scale_factor),
                    (51*self.x_scale_factor, 512*self.y_scale_factor),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[1],
                    (205*self.x_scale_factor, 142*self.y_scale_factor),
                    (205*self.x_scale_factor, 666*self.y_scale_factor),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[2],
                    (205*self.x_scale_factor, 142*self.y_scale_factor),
                    (422*self.x_scale_factor, 666*self.y_scale_factor),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[3],
                    (205*self.x_scale_factor, 142*self.y_scale_factor),
                    (575*self.x_scale_factor, 512*self.y_scale_factor),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[4],
                    (205*self.x_scale_factor, 142*self.y_scale_factor),
                    (575*self.x_scale_factor, 295*self.y_scale_factor),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[5],
                    (51*self.x_scale_factor, 295*self.y_scale_factor),
                    (51*self.x_scale_factor, 512*self.y_scale_factor),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[6],
                    (51*self.x_scale_factor, 295*self.y_scale_factor),
                    (205*self.x_scale_factor, 666*self.y_scale_factor),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[7],
                    (51*self.x_scale_factor, 295*self.y_scale_factor),
                    (422*self.x_scale_factor, 666*self.y_scale_factor),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[8],
                    (51*self.x_scale_factor, 295*self.y_scale_factor),
                    (575*self.x_scale_factor, 512*self.y_scale_factor),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[9],
                    (51*self.x_scale_factor, 295*self.y_scale_factor),
                    (575*self.x_scale_factor, 295*self.y_scale_factor),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[10],
                    (51*self.x_scale_factor, 295*self.y_scale_factor),
                    (422*self.x_scale_factor, 142*self.y_scale_factor),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[11],
                    (51*self.x_scale_factor, 512*self.y_scale_factor),
                    (51*self.x_scale_factor, 295*self.y_scale_factor),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[12],
                    (51*self.x_scale_factor, 512*self.y_scale_factor),
                    (205*self.x_scale_factor, 666*self.y_scale_factor),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[13],
                    (51*self.x_scale_factor, 512*self.y_scale_factor),
                    (422*self.x_scale_factor, 666*self.y_scale_factor),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[14],
                    (51*self.x_scale_factor, 512*self.y_scale_factor),
                    (575*self.x_scale_factor, 512*self.y_scale_factor),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[15],
                    (51*self.x_scale_factor, 512*self.y_scale_factor),
                    (575*self.x_scale_factor, 295*self.y_scale_factor),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[16],
                    (51*self.x_scale_factor, 512*self.y_scale_factor),
                    (422*self.x_scale_factor, 142*self.y_scale_factor),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[17],
                    (205*self.x_scale_factor, 666*self.y_scale_factor),
                    (51*self.x_scale_factor, 512*self.y_scale_factor),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[18],
                    (205*self.x_scale_factor, 666*self.y_scale_factor),
                    (51*self.x_scale_factor, 295*self.y_scale_factor),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[19],
                    (205*self.x_scale_factor, 666*self.y_scale_factor),
                    (422*self.x_scale_factor, 666*self.y_scale_factor),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[20],
                    (205*self.x_scale_factor, 666*self.y_scale_factor),
                    (575*self.x_scale_factor, 512*self.y_scale_factor),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[21],
                    (205*self.x_scale_factor, 666*self.y_scale_factor),
                    (575*self.x_scale_factor, 295*self.y_scale_factor),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[22],
                    (205*self.x_scale_factor, 666*self.y_scale_factor),
                    (422*self.x_scale_factor, 142*self.y_scale_factor),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[23],
                    (51*self.x_scale_factor, 295*self.y_scale_factor),
                    (51*self.x_scale_factor, 512*self.y_scale_factor),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[24],
                    (51*self.x_scale_factor, 295*self.y_scale_factor),
                    (205*self.x_scale_factor, 666*self.y_scale_factor),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[25],
                    (51*self.x_scale_factor, 295*self.y_scale_factor),
                    (422*self.x_scale_factor, 666*self.y_scale_factor),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[25],
                    (51*self.x_scale_factor, 295*self.y_scale_factor),
                    (575*self.x_scale_factor, 512*self.y_scale_factor),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[27],
                    (51*self.x_scale_factor, 295*self.y_scale_factor),
                    (575*self.x_scale_factor, 295*self.y_scale_factor),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[28],
                    (51*self.x_scale_factor, 295*self.y_scale_factor),
                    (422*self.x_scale_factor, 142*self.y_scale_factor),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[29],
                    (422*self.x_scale_factor, 666*self.y_scale_factor),
                    (422*self.x_scale_factor, 142*self.y_scale_factor),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[30],
                    (422*self.x_scale_factor, 666*self.y_scale_factor),
                    (575*self.x_scale_factor, 295*self.y_scale_factor),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[31],
                    (575*self.x_scale_factor, 512*self.y_scale_factor),
                    (422*self.x_scale_factor, 142*self.y_scale_factor),
                    width=2)

            except Exception as Message:
                self.error_message = "DrawingUtils > draw_rose > create_rose: "+str(Message)

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

    class generate_graph:
        def __init__(self):
            pass

        def create_devmode_graph(self, devmode_information_font):
            try:
                if self.draw_devmode_graph:
                    if ((self.real_window_width/2)+100)+self.timer >= self.real_window_width:
                        self.data_aFPS = []
                        self.data_CPU_usage = []
                        self.data_eFPS = []
                        self.data_memory_usage = []

                        self.timer = 0

                        self.data_aFPS_Max = 1
                        self.data_CPU_usage_Max = 1
                        self.data_eFPS_Max = 1
                        self.data_memory_usage_Max = 50
                        self.data_CPU_usage_Max = 50

                    BackingRect = self.mod_pygame__.Rect(
                        (self.real_window_width/2)+100,
                        0,
                        self.real_window_width,
                        200)

                    self.mod_pygame__.draw.rect(
                        self.display,
                        self.shape_color,
                        BackingRect)

                    SwapMemory = self.mod_psutil__.swap_memory()
                    VirtualMemory = self.mod_psutil__.virtual_memory()

                    TotalMemory = SwapMemory.total+VirtualMemory.total
                    UsedMemory = SwapMemory.used+VirtualMemory.used

                    self.current_memory_usage = (100/TotalMemory)*(UsedMemory)

                    if self.timer >= 2:
                        self.data_aFPS.append(
                            [((self.real_window_width/2)+100)+self.timer,
                             200-(100/self.data_aFPS_Max)*(self.aFPS/(self.iteration))])

                        try:
                            self.data_eFPS.append(
                                [((self.real_window_width/2)+100)+self.timer,
                                 200-(100/self.data_eFPS_Max)*int(self.eFPS)])

                        except:
                            self.data_eFPS.append(
                                [((self.real_window_width/2)+100)+self.timer,
                                 200-(100/self.data_eFPS_Max)*int(2000)])

                        self.data_memory_usage.append(
                            [((self.real_window_width/2)+100)+self.timer,
                             200-(2)*self.current_memory_usage])

                    if self.FPS_overclock:
                        self.data_aFPS_Max = 2000
                    elif (self.aFPS/(self.iteration)) > self.data_aFPS_Max:
                        self.data_aFPS_Max = (self.aFPS/(self.iteration))

                    if self.eFPS > self.data_eFPS_Max:
                        self.data_eFPS_Max = self.eFPS

                    if self.current_memory_usage > self.data_memory_usage_Max:
                        self.data_memory_usage_Max = self.current_memory_usage

                    self.timer += 0.2
                    if self.timer >= 5:
                        self.mod_pygame__.draw.lines(
                            self.display,
                            (255, 0, 0),
                            False,
                            self.data_aFPS)

                        self.mod_pygame__.draw.lines(
                            self.display,
                            (0, 255, 0),
                            False,
                            self.data_eFPS)

                        self.mod_pygame__.draw.lines(
                            self.display,
                            (0, 0, 255),
                            False,
                            self.data_memory_usage)

                    if len(self.data_CPU_usage) >= 2:
                        self.mod_pygame__.draw.lines(
                            self.display,
                            (255, 0, 255),
                            False,
                            self.data_CPU_usage)

                    if self.FPS_overclock:
                        try:
                            runFont = devmode_information_font.render(
                                "".join((f"MemUsE: {int(self.current_memory_usage)}% | ",
                                         f"CPUUsE: {self.mod_psutil__.cpu_percent()}% | ",
                                         f"FPS: {self.FPS} eFPS: {int(self.eFPS)} aFPS: ",
                                         f"N/A iteration: {self.iteration}")),
                                self.aa,
                                (255, 255, 255))

                        except:
                            runFont = devmode_information_font.render(
                                "".join((f"MemUsE: {int(self.current_memory_usage)}% | ",
                                         f"CPUUsE: {self.mod_psutil__.cpu_percent()}% | ",
                                         f"FPS: {self.FPS} eFPS: NaN* aFPS: ",
                                         f"N/A iteration: {self.iteration}")),
                                self.aa,
                                (255, 255, 255))
                    else:
                        runFont = devmode_information_font.render(
                            "".join((f"MemUsE: {int(self.current_memory_usage)}% | ",
                                     f"CPUUsE: {self.mod_psutil__.cpu_percent()}% | ",
                                     f"FPS: {self.FPS} eFPS: {int(self.eFPS)} aFPS: ",
                                     f"{int(self.aFPS/self.iteration)} ",
                                     f"iteration: {self.iteration}")),
                            self.aa,
                            (255, 255, 255))

                    self.display.blit(
                        runFont,
                        ((self.real_window_width/2)+105, 0))

            except Exception as Message:
                self.error_message = "".join(("DrawingUtils > generate_graph ",
                                                f"> create_devmode_graph: {str(Message)}"))
                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

    class draw_setting_elements:
        def __init__(self):
            pass

        def create_information_message(self, general_font, text, saved_y_position, max_x, info_offset):
            try:
                position = ((self.real_window_width/2) + 40,
                            (saved_y_position + 10) - info_offset)
                
                width = self.real_window_width - (max_x + 43)

                info_text_height = self.mod_text_utils__.TextWrap.blit_text(
                    self,
                    text,
                    position,
                    general_font,
                    self.font_color,
                    width)

                rect = self.mod_pygame__.Rect(
                    position[0] - 10,
                    position[1] - 10,
                    (width - position[0]) + 20,
                    info_text_height + 20)

                self.mod_pygame__.draw.rect(
                    self.display,
                    self.font_color,
                    rect,
                    width=1,
                    border_radius=10)

                max_y_value = position[1] + info_text_height + info_offset + 20
                if max_y_value > self.real_window_height:
                    info_offset = (max_y_value - self.real_window_height) + 10

                else:
                    info_offset = 0

                return info_offset
            
            except Exception as Message:
                self.error_message = "".join(("DrawingUtils > draw_setting_elements ",
                                              f"> create_information_message: {str(Message)}"))
                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

        def draw_directory_structure(self, slider_pos, general_font, hovering, mouse_over, hover_id, hovering_over_key, scrollbar_needed):
            try:
                if scrollbar_needed:
                    scroll_x_offset = 9
                    
                else:
                    scroll_x_offset = 0
                    
                position = [
                    scroll_x_offset,
                    slider_pos]

                height = 23
                total_height = height
                length = self.real_window_width/2

                rect = self.mod_pygame__.Rect(
                    position[0],
                    position[1],
                    length,
                    height)

                self.mod_pygame__.draw.rect(
                    self.display,
                    self.shape_color,
                    rect,
                    border_radius=10)

                x_pos = 0
                hover_area = False
                for key in self.file_structure:
                    width = ((self.real_window_width/2)/self.folder_size) * self.file_structure[key]["size"]

                    if ((self.mouse_x > position[0] + x_pos and
                                self.mouse_x < position[0] + x_pos + width and
                                self.mouse_y > position[1] and
                                self.mouse_y < position[1] + height) or
                            hover_id == self.file_structure[key]):

                        hovering = True
                        mouse_over = True

                        if hover_id != self.file_structure[key]:
                            hover_id = self.file_structure[key]
                            hover_area = True
                    
                    inside_rect = self.mod_pygame__.Rect(
                        position[0] + x_pos,
                        position[1],
                        width,
                        height)

                    if hover_id is not None:
                        if hover_id == self.file_structure[key]:
                            self.mod_pygame__.draw.rect(
                                self.display,
                                self.file_structure[key]["color"],
                                inside_rect)
                            
                    else:
                        self.mod_pygame__.draw.rect(
                            self.display,
                            self.file_structure[key]["color"],
                            inside_rect)

                    x_pos += width

                self.mod_pygame__.draw.rect(
                    self.display,
                    self.background_color,
                    rect,
                    width=3,
                    border_radius=10)

                padding_rect = self.mod_pygame__.Rect(
                    position[0]-10,
                    position[1]-10,
                    length+20,
                    height+20)

                self.mod_pygame__.draw.rect(
                    self.display,
                    self.background_color,
                    padding_rect,
                    width=10,
                    border_radius=20)

                total_height += 20

                text_position = [scroll_x_offset, slider_pos + height + 20]

                text_max_height = 0

                hover_text = False
                for key in self.file_structure:
                    percentage = (100/self.folder_size) * self.file_structure[key]["size"]
                        
                    if (hover_id is not None or
                            hovering_over_key):
                        
                        text = general_font.render(
                            f"{str(key)}: {int(percentage)}%",
                            self.aa,
                            self.font_color)

                    else:
                        text = general_font.render(
                            f"{str(key)}: {int(percentage)}%",
                            self.aa,
                            self.file_structure[key]["color"])
                        
                    text_width = text.get_width()
                    text_height = text.get_height()

                    if text_position[0] + text_width > (self.real_window_width / 2):
                        text_position[0] = scroll_x_offset
                        text_position[1] += text_height + 20
                        total_height += text_height + 20

                    if ((self.mouse_x > text_position[0] - 10 and
                                self.mouse_x < text_position[0] + text_width + 10 and
                                self.mouse_y > text_position[1] - 10 and
                                self.mouse_y < text_position[1] + text_height + 10) or
                            hover_id == self.file_structure[key]):

                        hovering = True
                        hovering_over_key = True
                        mouse_over = True
                        
                        text = general_font.render(
                            f"{str(key)}: {int(percentage)}%",
                            self.aa,
                            self.file_structure[key]["color"])
                        
                        if hover_id != self.file_structure[key]:
                            hover_id = self.file_structure[key]
                            hover_text = True
                    
                    if text_height > text_max_height:
                        text_max_height = text_height
                        
                    self.display.blit(text, text_position)
                    text_position[0] += text_width + 20

                if hover_area is False and hover_text is False:
                    hover_id = None

                if (self.mouse_x > position[0] and
                        self.mouse_x < length and
                        self.mouse_y > position[1] - 15 and
                        self.mouse_y < position[1] + height + 15):

                    hovering = True
                    mouse_over = True

                    self.mod_pygame__.event.set_allowed(
                        self.mod_pygame__.MOUSEMOTION)

                    self.mod_pygame__.draw.rect(
                        self.display,
                        self.font_color,
                        rect,
                        width=1,
                        border_radius=10)

                else:
                    self.mod_pygame__.draw.rect(
                        self.display,
                        self.shape_color,
                        rect,
                        width=1,
                        border_radius=10)

                total_height += text_height + 40

                return total_height, hovering, mouse_over, hover_id
            
            except Exception as Message:
                self.error_message = "".join(("DrawingUtils > draw_setting_elements ",
                                              f"> draw_directory_structure: {str(Message)}"))
                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

        def draw_multi_buttons(self, button_pos, button_text_array, general_font, argument_variable, hovering, mouse_over, scrollbar_needed):
            try:
                if scrollbar_needed:
                    scroll_x_offset = 9
                    
                else:
                    scroll_x_offset = 0
                    
                position = [
                    scroll_x_offset,
                    button_pos]

                for i in range(len(button_text_array)):
                    button_text = general_font.render(
                        button_text_array[i],
                        self.aa,
                        self.font_color).convert_alpha()

                    button_text_width = button_text.get_width() + 20
                    button_text_height = button_text.get_height() + 20

                    rect = self.mod_pygame__.Rect(
                        position[0],
                        position[1],
                        button_text_width,
                        button_text_height)

                    if (self.mouse_x > position[0] and
                        self.mouse_x < position[0] + button_text_width and
                        self.mouse_y > position[1] and
                            self.mouse_y < position[1] + button_text_height):

                        hovering = True
                        mouse_over = True

                        if self.mouse_button_down:
                            self.mouse_button_down = False

                            if self.use_mouse_input is False:
                                self.mouse_y = button_pos + 5 + button_text_height

                            if self.sound:
                                self.mod_sound_utils__.play_sound.play_click_sound(
                                    self)

                            self.mod_pygame__.draw.rect(
                                self.display,
                                self.accent_color,
                                rect,
                                width=1,
                                border_radius=10)

                            self.__dict__[argument_variable][button_text_array[i]] = not self.__dict__[argument_variable][button_text_array[i]]

                            self.mod_theme_utils__.determine_theme_colours.get_colors(
                                self)

                            self.mod_settings__.generate_settings.update_profile(
                                self)

                        else:
                            self.mod_pygame__.draw.rect(
                                self.display,
                                self.font_color,
                                rect,
                                width=1,
                                border_radius=10)

                    else:
                        if self.__dict__[argument_variable][button_text_array[i]]:
                            self.mod_pygame__.draw.rect(
                                self.display,
                                self.accent_color,
                                rect,
                                width=1,
                                border_radius=10)

                        else:
                            self.mod_pygame__.draw.rect(
                                self.display,
                                self.shape_color,
                                rect,
                                width=1,
                                border_radius=10)

                    self.display.blit(
                        button_text,
                        (position[0]+10,
                            position[1]+10))

                    position[0] += button_text_width + 3

                return button_text_height + 20, hovering, mouse_over
            
            except Exception as Message:
                self.error_message = "".join(("DrawingUtils > draw_setting_elements ",
                                              f"> draw_multi_buttons: {str(Message)}"))
                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

        def draw_buttons(self, button_pos, button_text_array, general_font, value, argument_variable, hovering, mouse_over, files_to_remove, scanned_files, scrollbar_needed):
            try:
                if scrollbar_needed:
                    scroll_x_offset = 9
                    
                else:
                    scroll_x_offset = 0
                    
                if (argument_variable == "aa_quality" and
                        self.aa is False):

                    enable = False

                elif (argument_variable == "clear_cache" and
                            (files_to_remove is False or
                                self.remove_file_permission is False)):

                    enable = False

                elif (argument_variable == "scan_pycraft" and
                        scanned_files):

                    enable = False

                else:
                    enable = True
                    
                position = [
                    scroll_x_offset,
                    button_pos]

                for i in range(len(button_text_array)):
                    if enable:
                        button_text = general_font.render(
                            button_text_array[i],
                            self.aa,
                            self.font_color).convert_alpha()
                        
                    else:
                        button_text = general_font.render(
                            button_text_array[i],
                            self.aa,
                            self.shape_color).convert_alpha()

                    button_text_width = button_text.get_width() + 20
                    button_text_height = button_text.get_height() + 20

                    rect = self.mod_pygame__.Rect(
                        position[0],
                        position[1],
                        button_text_width,
                        button_text_height)

                    if (self.mouse_x > position[0] and
                        self.mouse_x < position[0] + button_text_width and
                        self.mouse_y > position[1] and
                        self.mouse_y < position[1] + button_text_height and
                            enable):

                        hovering = True
                        mouse_over = True

                        if self.mouse_button_down:
                            self.mouse_button_down = False

                            if self.use_mouse_input is False:
                                self.mouse_y = button_pos + 5 + button_text_height

                            if self.sound:
                                self.mod_sound_utils__.play_sound.play_click_sound(
                                    self)

                            self.mod_pygame__.draw.rect(
                                self.display,
                                self.accent_color,
                                rect,
                                width=1,
                                border_radius=10)

                            self.__dict__[argument_variable] = button_text_array[i]

                            self.mod_theme_utils__.determine_theme_colours.get_colors(
                                self)

                            self.mod_settings__.generate_settings.update_profile(
                                self)

                        else:
                            self.mod_pygame__.draw.rect(
                                self.display,
                                self.font_color,
                                rect,
                                width=1,
                                border_radius=10)

                    else:
                        if button_text_array[i] == value:
                            self.mod_pygame__.draw.rect(
                                self.display,
                                self.accent_color,
                                rect,
                                width=1,
                                border_radius=10)

                        else:
                            self.mod_pygame__.draw.rect(
                                self.display,
                                self.shape_color,
                                rect,
                                width=1,
                                border_radius=10)

                    self.display.blit(
                        button_text,
                        (position[0]+10,
                            position[1]+10))

                    position[0] += button_text_width + 3

                return button_text_height + 20, hovering, mouse_over
            
            except Exception as Message:
                self.error_message = "".join(("DrawingUtils > draw_setting_elements ",
                                              f"> draw_buttons: {str(Message)}"))
                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

        def draw_remap_function(self, remap_pos, options, hovering, mouse_over, general_font, maximum_remap_width, display_events, scrollbar_needed):
            try:
                if scrollbar_needed:
                    scroll_x_offset = 9
                    
                else:
                    scroll_x_offset = 0
                    
                position = [
                    scroll_x_offset,
                    remap_pos]

                index = 0
                enable = False
                maximum_height = 0
                for key in options:
                    text = f"Function: {list(options.keys())[index]}, is bound to: {options[key]}."
                    button_text = general_font.render(
                        text,
                        self.aa,
                        self.font_color).convert_alpha()

                    button_text_width = button_text.get_width() + 20

                    if button_text_width > maximum_remap_width:
                        maximum_remap_width = button_text_width
                        
                    button_text_height = button_text.get_height() + 20

                    self.display.blit(button_text, (position[0] + 10, position[1] + 10))

                    rect = self.mod_pygame__.Rect(
                        position[0],
                        position[1],
                        maximum_remap_width,
                        button_text_height)

                    if (self.mouse_x > position[0] and
                        self.mouse_x < position[0] + maximum_remap_width and
                        self.mouse_y > position[1] and
                        self.mouse_y < position[1] + button_text_height):

                        hovering = True
                        mouse_over = True
                        disable_events = True
                        enable = True

                        keydown = False

                        for event in display_events:
                            if (event.type == self.mod_pygame__.KEYDOWN and
                                    self.selected_input_reconfig == "keyboard"):
                                
                                keydown = True

                                try:
                                    i = 0
                                    for element in self.input_key:
                                        if event.key == self.input_key[element][0]:
                                            rebind = True
                                            for bound_key in options:
                                                if options[bound_key] == list(self.input_key.keys())[i]:
                                                    rebind = False

                                            if rebind:
                                                key_pressed = list(self.input_key.keys())[i]
                                                break
                                            
                                        i += 1

                                    for key_id, value in self.input_key.items():
                                        if self.input_key[key_pressed] == value:
                                            break
                                        
                                    options[list(options.keys())[index]] = key_id

                                except Exception as Message:
                                    log_message = "DrawingUtils > draw_setting_elements > draw_remap_function: " + str(Message)

                                    self.mod_logging_utils__.create_log_message.update_log_warning(
                                        self,
                                        log_message)

                        if keydown:
                            self.mod_pygame__.draw.rect(
                                self.display,
                                self.accent_color,
                                rect,
                                width=1,
                                border_radius=10)
                            
                        else:
                            self.mod_pygame__.draw.rect(
                                self.display,
                                self.font_color,
                                rect,
                                width=1,
                                border_radius=10)

                    else:
                        self.mod_pygame__.draw.rect(
                            self.display,
                            self.shape_color,
                            rect,
                            width=1,
                            border_radius=10)

                    position[1] += button_text_height + 3
                    maximum_height += button_text_height + 3

                    index += 1

                if enable is False:
                    disable_events = False

                return maximum_height, hovering, mouse_over, maximum_remap_width, disable_events
            except Exception as Message:
                self.error_message = "".join(("DrawingUtils > draw_setting_elements ",
                                              f"> draw_remap_function: {str(Message)}"))
                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

        def draw_slider(self, slider_pos, minimum, maximum, value, argument_variable, hovering, mouse_over, scrollbar_needed):
            try:
                if scrollbar_needed:
                    scroll_x_offset = 9
                    
                else:
                    scroll_x_offset = 0
                    
                if (argument_variable == "music_volume" and
                        self.music is False):

                    enable = False

                elif (argument_variable == "sound_volume" and
                        self.sound is False):

                    enable = False

                elif (argument_variable == "FPS" and
                        self.vsync):

                    enable = False

                else:
                    enable = True

                position = [
                    scroll_x_offset,
                    slider_pos]

                height = 10
                slider_range = maximum - minimum
                length = self.real_window_width/2

                rect = self.mod_pygame__.Rect(
                    position[0],
                    position[1],
                    length,
                    height)

                self.mod_pygame__.draw.rect(
                    self.display,
                    self.shape_color,
                    rect,
                    border_radius=10)

                self.mod_pygame__.draw.rect(
                    self.display,
                    self.background_color,
                    rect,
                    width=3,
                    border_radius=10)

                circle_pos_x = ((value - minimum) /
                                (slider_range / length)) + scroll_x_offset
                circle_pos_y = position[1] + height/2
                circle_pos = (circle_pos_x, circle_pos_y)

                if (self.mouse_x > position[0] and
                        self.mouse_x < length and
                        self.mouse_y > position[1] - 15 and
                        self.mouse_y < position[1] + height + 15 and
                        enable):

                    hovering = True
                    mouse_over = True

                    if self.mouse_button_down:
                        self.mod_pygame__.event.set_blocked(
                            self.mod_pygame__.MOUSEMOTION)
                        self.__dict__[argument_variable] = (
                            (slider_range / length) * self.mouse_x) + minimum

                        self.mod_pygame__.draw.rect(
                            self.display,
                            self.accent_color,
                            rect,
                            width=1,
                            border_radius=10)

                        self.mod_pygame__.draw.circle(
                            self.display,
                            self.accent_color,
                            circle_pos,
                            radius=10)

                        self.mod_pygame__.draw.circle(
                            self.display,
                            self.background_color,
                            circle_pos,
                            radius=6)

                    else:
                        self.mod_pygame__.event.set_allowed(
                            self.mod_pygame__.MOUSEMOTION)

                        self.mod_pygame__.draw.rect(
                            self.display,
                            self.font_color,
                            rect,
                            width=1,
                            border_radius=10)

                        self.mod_pygame__.draw.circle(
                            self.display,
                            self.font_color,
                            circle_pos,
                            radius=10)

                        self.mod_pygame__.draw.circle(
                            self.display,
                            self.background_color,
                            circle_pos,
                            radius=6)

                else:
                    self.mod_pygame__.draw.rect(
                        self.display,
                        self.shape_color,
                        rect,
                        width=1,
                        border_radius=10)

                    self.mod_pygame__.draw.circle(
                        self.display,
                        self.shape_color,
                        circle_pos,
                        radius=10)

                    self.mod_pygame__.draw.circle(
                        self.display,
                        self.background_color,
                        circle_pos,
                        radius=6)

                return height + 20, hovering, mouse_over
            
            except Exception as Message:
                self.error_message = "".join(("DrawingUtils > draw_setting_elements ",
                                              f"> draw_slider: {str(Message)}"))
                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

        def draw_toggle(self, toggle_pos, value_0, value_1, value, argument_variable, hovering, mouse_over, scrollbar_needed):
            try:
                if scrollbar_needed:
                    scroll_x_offset = 9
                    
                else:
                    scroll_x_offset = 0
                    
                position = [scroll_x_offset, toggle_pos]
                    
                height = 10

                rect = self.mod_pygame__.Rect(
                    position[0],
                    position[1],
                    36,
                    height)

                self.mod_pygame__.draw.rect(
                    self.display,
                    self.shape_color,
                    rect,
                    border_radius=10)

                self.mod_pygame__.draw.rect(
                    self.display,
                    self.background_color,
                    rect,
                    width=3,
                    border_radius=10)

                if value == value_0:
                    toggle_value = 30 + scroll_x_offset
                        
                if value == value_1:
                    toggle_value = 10 + scroll_x_offset

                circle_pos_x = toggle_value
                circle_pos_y = position[1] + height/2
                circle_pos = (circle_pos_x, circle_pos_y)

                if self.music is False:
                    self.mod_pygame__.mixer.music.fadeout(500)

                if (self.mouse_x > position[0] and
                        self.mouse_x < 36 + 20 and
                        self.mouse_y > position[1] - 15 and
                        self.mouse_y < position[1] + height + 15):

                    hovering = True
                    mouse_over = True

                    if self.mouse_button_down:
                        self.mouse_button_down = False

                        self.__dict__[argument_variable] = not self.__dict__[
                            argument_variable]

                        if self.use_mouse_input is False:
                            self.mouse_x += 36

                        if self.sound:
                            self.mod_sound_utils__.play_sound.play_click_sound(
                                self)

                    else:
                        self.mod_pygame__.draw.rect(
                            self.display,
                            self.font_color,
                            rect,
                            width=1,
                            border_radius=10)

                        self.mod_pygame__.draw.circle(
                            self.display,
                            self.font_color,
                            circle_pos,
                            radius=10)

                        self.mod_pygame__.draw.circle(
                            self.display,
                            self.background_color,
                            circle_pos,
                            radius=6)

                else:
                    if value:
                        self.mod_pygame__.draw.rect(
                            self.display,
                            self.accent_color,
                            rect,
                            width=1,
                            border_radius=10)

                        self.mod_pygame__.draw.circle(
                            self.display,
                            self.accent_color,
                            circle_pos,
                            radius=10)
                        self.mod_pygame__.draw.circle(
                            self.display,
                            self.background_color,
                            circle_pos,
                            radius=6)

                    else:
                        self.mod_pygame__.draw.rect(
                            self.display,
                            self.shape_color,
                            rect,
                            width=1,
                            border_radius=10)

                        self.mod_pygame__.draw.circle(
                            self.display,
                            self.shape_color,
                            circle_pos,
                            radius=10)

                        self.mod_pygame__.draw.circle(
                            self.display,
                            self.background_color,
                            circle_pos,
                            radius=6)

                return height + 20, hovering, mouse_over
            
            except Exception as Message:
                self.error_message = "".join(("DrawingUtils > draw_setting_elements ",
                                              f"> draw_toggle: {str(Message)}"))
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
