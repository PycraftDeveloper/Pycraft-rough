display_utils
==========

----------
display_functionality
----------
This class is in charge of handling calls to subroutines, as well as enabling basic GUI functionality to Pycraft, this is called by many GUIs and is heavily customisable. This is designed to simplify GUI design and make it easier to roll out some changes to every GUI in Pycraft.

* Args:

  * None

* Keyword Args:

  * None

core_display_functions
__________
This subroutine is in charge of the basic functionality you would expect from Pycraft's GUIs, it handles events, mouse and controller positions, as well as allowing for great customisability, meaning its designed to be called by most GUI's and be flexible enough to be functional.

* Args:

  * platform (str): This string tells the subroutine which operating system we are using. This is needed for OS specific operations.

  * base_folder (str): This string is a file path to the resources for Pycraft on your device.

  * display (Pygame Surface): The display object is used throughout Pycraft. This is the identifier we use when we want to interact with/draw to/update Pycraft's gui. Pygame is the main windowing engine used in Pycraft.

  * use_mouse_input (bool):

  * average_fps (float):

  * iteration (int):

  * mouse_x (int):

  * mouse_y (int):

  * x_scale_factor (float):

  * y_scale_factor (float):

  * go_to (str):

  * joystick_exit (bool):

  * joystick_hat_pressed (bool):

  * window_in_focus (bool):

  * saved_window_width (int):

  * saved_window_height (int):

  * clock (Pygame Clock):

  * sound (bool):

  * input_key (dict):

  * input_configuration (dict):

  * extended_developer_options (bool):

  * logging_dictionary (dict): This dictionary is used to tell this subroutine if information messages are to be logged, this can be adjusted in settings.

  * output_log (bool): This option tells the subroutine if logged messages should also be outputted to the console.

  * vsync (bool):

  * window_icon (Pygame Surface): This is the icon we use in the caption (and in the taskbar on some supported OS') for Pycraft.

  * sound_volume (float):

  * variable_data (dict):

  * version (str)

  * Pycraft's current version.

  * background_color (tuple):

  * font_color (tuple):

  * fullscreen (bool):

  * startup_animation (bool):

  * run_timer (float):

  * data_average_fps (arr):

  * data_CPU_usage (arr):

  * data_current_fps (arr):

  * data_memory_usage (arr):

  * timer (float):

  * data_average_fps_Max (float):

  * data_CPU_usage_Max (float):

  * data_current_fps_Max (float):

  * data_memory_usage_Max (float):

  * joystick_zoom (str):

  * mouse_button_down (bool):

  * error_message (str):

  * error_message_detailed (str):

* Keyword Args:

  * location="home" (str):

  * checkEvents=True (bool):

  * resize=True (bool):

  * return_events=False (bool):

  * disable_events=False (bool):

* Output:

  * displayEvents (arr):

  * display (Pygame Surface): The display object is used throughout Pycraft. This is the identifier we use when we want to interact with/draw to/update Pycraft's gui. Pygame is the main windowing engine used in Pycraft.

  * mouse_button_down (bool):

  * go_to (str):

  * startup_animation (bool):

  * run_timer (float):

  * current_fps (float):

  * average_fps (float):

  * iteration (int):

  * saved_window_width (int):

  * saved_window_height (int):

  * window_in_focus (bool):

  * joystick_exit (bool):

  * x_scale_factor (float):

  * y_scale_factor (float):

  * real_window_width (int):

  * real_window_height (int):

  * mouse_x (int):

  * mouse_y (int):

  * data_average_fps (arr):

  * data_CPU_usage (arr):

  * data_current_fps (arr):

  * data_memory_usage (arr):

  * timer (float):

  * data_average_fps_Max (float):

  * data_CPU_usage_Max (float):

  * data_current_fps_Max (float):

  * data_memory_usage_Max (float):

  * joystick_zoom (str):

  * clock (Pygame Clock):

  * joystick_hat_pressed (bool):

  * fullscreen (bool):

  * joystick_connected (bool):

----------
display_utils
----------
update_display
__________
set_display
__________
generate_min_display
__________
get_display_location
__________
get_play_status
__________
----------
display_animations
----------
fade_in
__________
fade_out
__________

