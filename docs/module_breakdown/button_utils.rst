button_utils
==========

----------
draw_setting_elements
----------
This class is in charge of rendering the button element that you can see used in the settings menu for Pycraft.  Please note that the use of 'self' in this module is purely as a way to make changes to variables in Pycraft, and is not/should not be used in any other way for simplicity.

* Args:

  * None

* Keyword Args:

  * None

draw_multi_buttons
__________
This function is in charge of rendering the multi-button element (where multiple options can be selected) that you can see used in the settings menu for Pycraft.  Please note that the use of 'self' in this module is purely as a way to make changes to variables in Pycraft, and is not/should not be used in any other way for simplicity.

* Args:

  * self (dict): This is used by Pycraft as a way of storing it's current configuration and behaviour and is required by most GUIs. Its use should be reduced where possible for readability reasons.

  * button_pos (int): This is used to store the Y coordinate of the buttons position onscreen, so that elements can be rendered in the correct place.

  * button_text_array (array): This array stores a sequence of 1 or more strings that will be used to title each button.

  * font (Pygame Font): This parameter stores the font that will be used by default to render any text supplied to the function.

  * backup_font (Pygame Font): This parameter stores the font that will be used to render text supplied to this function when the default font can't be used. (likely due to limited support for some characters).

  * argument_variable (str): This parameter represents the dictionary key for the variable that this function modifies, for example, if the variable using self was used it may look like 'self.variable_name', then this parameter would be 'variable_name'.

  * hovering (bool): This parameter is used so that the setting menu knows when the user is hovering over a setting.

  * mouse_over (bool): This parameter is used to tell the settings menu when to display information messages for an option (often then the user's mouse is hovering over a setting, although the functionality for this is different to the 'hovering' parameter).

  * scrollbar_needed (bool): This parameter controls when the graphic this function draws should be offset to allow for a scroll-bar to be rendered.

  * aa (bool): This controls wether anti-aliasing should be used when rendering font.

  * font_color (tuple): This tuple controls which colour the font should be rendered with and is also the colour that the graphic will turn when it is currently being overed over. This is adjustable through the theme selection menu.

  * display (Pygame Surface): The display object is used throughout Pycraft. This is the identifier we use when we want to interact with/draw to/update Pycraft's gui. Pygame is the main windowing engine used in Pycraft.

  * mouse_x (int): This stores the current X position of the user's cursor relative to the top-left corner of the window

  * mouse_y (int): This stores the current Y position of the user's cursor relative to the top-left corner of the window

  * accent_color (tuple): This tuple controls which colour the graphic should be rendered with, when that option is enabled.

  * shape_color (tuple): This tuple controls which colour the graphic should be rendered with, by default.

  * platform (str): This string tells the subroutine which operating system we are using. This is needed for OS specific operations.

  * base_folder (str): This string is a file path to the resources for Pycraft on your device.

  * use_mouse_input (bool): This parameter tells the function wether the user is using a keyboard and mouse, or a controller to interact with the element onscreen, as this can change how the element should detect events.

  * sound (bool): This input controls wether the element onscreen should play a sound when it is interacted with.

  * theme (str): This parameter represents what theme the user has currently selected.

  * sound_volume (float): This parameter controls the volume at which should should be played at when the element is interacted with.

  * settings_preset (str): This parameter controls which pre-set settings the user has chosen to use, this can be either 'low', 'medium', 'high' or 'adaptive', where each option focuses on either performance or visual quality in game.

  * themeArray (array): This parameter stores all of the information needed to adjust the theme the user has selected, including 'font_color', 'background_color', 'shape_color', 'accent_color', 'secondary_font_color' for each of the 3 available themes.

  * background_color (array): This array stores the RGB colour value used to represent the background colour of the element (this should be the same as the background colour to the rest of the window)

  * secondary_font_color (tuple): This parameter stores the second font colour that can be used to add greater effect to a widget, for example better showing when an option is disabled.

  * fps (float): This is the frame rate the game is targeted to try and run at. This is not a guaranteed value and should represent the maximum frame rate the game should be allowed to run at.

  * render_fog (bool): This controls the rendering of fog effects in game, disabling this setting can improve performance, but lower visual quality.

  * fancy_graphics (bool): This controls the rendering of more complex visual effects that serve only to look good, so that the user can control performance or visual quality.

  * fancy_particles (bool): This controls the rendering of higher quality particles in game, so that the user can control performance or visual quality.

  * average_fps (float): This stores the cumulative achieved frame rate from the last 1000 game cycles. This can be used then to calculate an average frame rate.

  * iteration (int): This counter is used to count up to 1000, and is used to calculate an average frame rate for those 1000 samples. Then this counter gets reset to 1 (to avoid ZeroDivisionError).

  * mouse_button_down (bool): This parameter controls when the user has opted to select an option, and although this can be remapped, it often represents when the user clicks on the onscreen element.

  * language (str): This procedure contains a list of all the supported languages Pycraft can be translated into.

  * logging_dictionary (dict): This dictionary is used to tell this subroutine if information messages are to be logged, this can be adjusted in settings.

  * output_log (bool): This option tells the subroutine if logged messages should also be outputted to the console.

  * translated_text (dict): This dictionary stores all the text that has been previously translated (like a cache). This improves performance and reduces the number of calls to external language servers (google translate). All text that is to be translated must first check this dictionary!

  * connection_permission (bool): This parameter controls wether Pycraft is allowed to connect to the internet. This can then be used to control a range of features, for example text translations and checking for updates to Pycraft.

* Keyword Args:

  * None

* Output:

  * button_text_height + 20 (int): This output represents the vertical height of the onscreen element, so that the next setting can be rendered below it. We add 20 as a form of padding between setting options, and this represents 20 pixels.

  * hovering (bool): This parameter is used so that the setting menu knows when the user is hovering over a setting.

  * mouse_over (bool): This parameter is used to tell the settings menu when to display information messages for an option (often then the user's mouse is hovering over a setting, although the functionality for this is different to the 'hovering' parameter).

  * fps (float): This is the frame rate the game is targeted to try and run at. This is not a guaranteed value and should represent the maximum frame rate the game should be allowed to run at.

  * aa (bool): This controls wether anti-aliasing should be used when rendering font.

  * render_fog (bool): This controls the rendering of fog effects in game, disabling this setting can improve performance, but lower visual quality.

  * fancy_graphics (bool): This controls the rendering of more complex visual effects that serve only to look good, so that the user can control performance or visual quality.

  * fancy_particles (bool): This controls the rendering of higher quality particles in game, so that the user can control performance or visual quality.

  * average_fps (float): This stores the cumulative achieved frame rate from the last 1000 game cycles. This can be used then to calculate an average frame rate.

  * iteration (int): This counter is used to count up to 1000, and is used to calculate an average frame rate for those 1000 samples. Then this counter gets reset to 1 (to avoid ZeroDivisionError).

  * themeArray (array): This parameter stores all of the information needed to adjust the theme the user has selected, including 'font_color', 'background_color', 'shape_color', 'accent_color', 'secondary_font_color' for each of the 3 available themes.

  * font_color (tuple): This tuple controls which colour the font should be rendered with and is also the colour that the graphic will turn when it is currently being overed over. This is adjustable through the theme selection menu.

  * background_color (array): This array stores the RGB colour value used to represent the background colour of the element (this should be the same as the background colour to the rest of the window)

  * shape_color (tuple): This tuple controls which colour the graphic should be rendered with, by default.

  * accent_color (tuple): This tuple controls which colour the graphic should be rendered with, when that option is enabled.

  * secondary_font_color (tuple): This parameter stores the second font colour that can be used to add greater effect to a widget, for example better showing when an option is disabled.

  * theme (str): This parameter represents what theme the user has currently selected.

  * mouse_button_down (bool): This parameter controls when the user has opted to select an option, and although this can be remapped, it often represents when the user clicks on the onscreen element.

  * translated_text (dict): This dictionary stores all the text that has been previously translated (like a cache). This improves performance and reduces the number of calls to external language servers (google translate). All text that is to be translated must first check this dictionary!

draw_buttons
__________
This function is in charge of rendering the chained button element (where only one option can be chosen) that you can see used in the settings menu for Pycraft.  Please note that the use of 'self' in this module is purely as a way to make changes to variables in Pycraft, and is not/should not be used in any other way for simplicity.

* Args:

  * button_pos ():

  * self ():

  * button_text_array ():

  * font ():

  * value ():

  * backup_font ():

  * argument_variable ():

  * hovering ():

  * mouse_over ():

  * files_to_remove ():

  * clear_languages ():

  * scanned_files ():

  * scrollbar_needed ():

  * font_color ():

  * aa ():

  * display ():

  * mouse_x ():

  * mouse_y ():

  * sound ():

  * accent_color ():

  * shape_color ():

  * platform ():

  * base_folder ():

  * remove_file_permission

  * settings_preset ():

  * fps ():

  * render_fog ():

  * fancy_graphics ():

  * fancy_particles ():

  * average_fps ():

  * iteration ():

  * use_mouse_input ():

  * sound_volume ():

  * themeArray ():

  * background_color ():

  * secondary_font_color ():

  * language ():

  * logging_dictionary ():

  * output_log ():

  * translated_text ():

  * connection_permission ():

* Keyword Args:

  * None

* Output:

  * button_text_height + 20 ():

  * hovering ():

  * mouse_over ():

  * fps ():

  * aa ():

  * render_fog ():

  * fancy_graphics ():

  * fancy_particles ():

  * average_fps ():

  * iteration ():

  * themeArray ():

  * font_color ():

  * background_color ():

  * shape_color ():

  * accent_color ():

  * secondary_font_color ():

  * translated_text ():


