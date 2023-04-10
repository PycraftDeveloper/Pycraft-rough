benchmark_utils
==========

----------
close_benchmark
----------
This class is in charge of switching back from the benchmark UI to Pycraft and making sure that the benchmark engine is reset so it behaves as expected next time the user goes to open up the benchmark menu.

* Args:

  * None

* Keyword Args:

  * None

Exitbenchmark
__________
This procedure is in charge of switching back from the benchmark UI to Pycraft and making sure that the benchmark engine is reset so it behaves as expected next time the user goes to open up the benchmark menu.

* Args:

  * self (dict): This is used by Pycraft as a way of storing it's current configuration and behaviour and is required by most GUIs. Its use should be reduced where possible for readability reasons.

* Keyword Args:

  * None

* Output:

  * None

----------
start_benchmark
----------
This class is in charge of creating and setting up the different environments used for each component of the graphics benchmark. This is done so that they all start with the same starting conditions to make the tests fair for comparison between different stages of the benchmark, and also between different devices running this benchmark.

* Args:

  * None

* Keyword Args:

  * None

generate_benchmark
__________
This function does the bulk of the setup that you would find between different areas of the graphics benchmark to make sure that each test is repeatable and setup in the same way.

* Args:

  * None

* Keyword Args:

  * create_display (bool): This option controls wether a Pygame surface object should be created or not. Often if a Pygame surface object isn't created here then it will be in the 'generate_opengl_benchmark' function which is below this.

* Output:

  * set_fps (array): This is an array of integers that stores FPS targets for the benchmark section of Pycraft, with each element being a different FPS to try to reach, getting progressively harder. The FPS from this array is updated every 500 iterations of the benchmark.

  * set_fps_length (int): This is the length of the 'set_fps' array, we use this instead of specifying an integer in order to allow us to make changes later on in Pycraft's development about how many targets to use for the benchmark section.

  * display (Pygame Surface | None): The display object is used throughout Pycraft. This is the identifier we use when we want to interact with/draw to/update Pycraft's gui. Pygame is the main windowing engine used in Pycraft. OR If the keyword parameter 'create_display' is set to False, then None is returned.

  * iteration (int): In the benchmarking process, iteration is used to keep track of how long the benchmark has been running.

  * fps_counter (int): This is used to store the index used to calculate the next element in the 'set_fps' array, this is used so Pycraft know's what to set the FPS to next, and what to set the caption to so that it displays the current FPS being tested.

  * max_iteration (int): This is used to calculate after how many iterations we move onto the next targeted FPS, currently this is set to increase the FPS every 500 'iteration's.

generate_opengl_benchmark
__________
This function handles the specific setup for any OpenGL benchmark environment. This is still used in partnership with 'generate_benchmark' however does extend its functionality with OpenGL specific data.

* Args:

  * None

* Keyword Args:

  * None

* Output:

  * display (Pygame Surface | None): The display object is used throughout Pycraft. This is the identifier we use when we want to interact with/draw to/update Pycraft's gui. Pygame is the main windowing engine used in Pycraft. OR If the keyword parameter 'create_display' is set to False, then None is returned.

  * ctx (Context object): This is used by ModernGL for loading OpenGL resources and enabling access to OpenGL features.

  * wnd (BaseWindow): This is used by ModernGL_window as the display object to use for rendering and additional resource loading.

----------
clear_benchmark
----------
This class is in charge of running a simple spacer to act as a gap between each of the graphics benchmarks. This is used as a time to reset arguments between each test, although that is not handled here.

* Args:

  * None

* Keyword Args:

  * None

run_spacer
__________
This procedure is in charge of running a simple spacer to act as a gap between each of the graphics benchmarks. This is used as a time to reset arguments between each test, although that is not handled here.

* Args:

  * self (dict): This is used by Pycraft as a way of storing it's current configuration and behaviour and is required by most GUIs. Its use should be reduced where possible for readability reasons.

  * display (Pygame Surface): The display object is used throughout Pycraft. This is the identifier we use when we want to interact with/draw to/update Pycraft's gui. Pygame is the main windowing engine used in Pycraft.

  * background_color (array): An array containing the RGB colour values used to represent the colour of the background to the window at this time.

  * clock (Clock): The clock object is used by Pygame as a way of controlling the frame-rate and other frame-rate specific functions. We use this to limit the FPS throughout Pycraft.

* Keyword Args:

  * None

* Output:

  * None


