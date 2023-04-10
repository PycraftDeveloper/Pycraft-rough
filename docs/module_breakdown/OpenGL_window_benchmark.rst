OpenGL_window_benchmark
==========

----------
run_opengl_window_benchmark
----------
This class is in charge of the OpenGL window benchmark seen in the benchmark section of Pycraft.

* Args:

  * None

* Keyword Args:

  * None

setup
__________
This subroutine is in charge of loading the resources required by the OpenGL benchmark, including: 1x Texture 1x 3D Scene 1x GLSL Shader And also sets the window parameters so that the OpenGL benchmark sets up in the same way on all devices for consistency.

* Args:

  * self (dict): This is used by Pycraft as a way of storing it's current configuration and behaviour and is required by most GUIs. Its use should be reduced where possible for readability reasons.

  * wnd (BaseWindow): This is used by ModernGL_window as the display object to use for rendering and additional resource loading.

* Keyword Args:

  * None

* Output:

  * texture (ModernGL_window Texture): This texture is rendered to the scene to add additional complexity.

  * mvp (ModernGL_window Shader Attribute): This matrix is used to render the position and rotation of the scene.

  * light (ModernGL_window Shader Attribute): This attribute is used to shade the scene based on the position of the camera.

  * vao (ModernGL VertexArray): This is the scene we render (a cube).

  * timer (float): This is used to keep track of how long this section of the benchmark has been running for, and is used in calculating the rotation of our scene.

  * aspect_ratio (float): This float represents the aspect ratio we want our display to be rendering at.

start
__________
This subroutine is used to render the OpenGL window benchmark, accessible when run through the benchmark section of Pycraft. This test is the final of 3 tests designed to test different aspects of your hardware. This stresses your GPU as well as your CPU and this is often the most difficult benchmark to run.

* Args:

  * self (dict): This is used by Pycraft as a way of storing it's current configuration and behaviour and is required by most GUIs. Its use should be reduced where possible for readability reasons.

  * iteration (int): In the benchmarking process, iteration is used to keep track of how long the benchmark has been running

  * Setfpslength (int): This is the length of the 'Setfps' array, we use this instead of specifying an integer in order to allow us to make changes later on in Pycraft's development about how many targets to use for the benchmark section.

  * Setfps (array): This is an array of integers that stores FPS targets for the benchmark section of Pycraft, with each element being a different FPS to try to reach, getting progressively harder. The FPS from this array is updated every 500 iterations of the benchmark.

  * fpscounter (int): This is used to store the index used to calculate the next element in the 'Setfps' array, this is used so Pycraft know's what to set the FPS to next, and what to set the caption to so that it displays the current FPS being tested.

  * Maxiteration (int): This is used to calculate after how many iterations we move onto the next targeted FPS, currently this is set to increase the FPS every 500 'iteration's.

  * ctx (Context object): This is used by ModernGL for loading OpenGL resources and enabling access to OpenGL features.

  * texture (ModernGL_window Texture): This texture is rendered to the scene to add additional complexity.

  * mvp (ModernGL_window Shader Attribute): This matrix is used to render the position and rotation of the scene.

  * light (ModernGL_window Shader Attribute): This attribute is used to shade the scene based on the position of the camera.

  * vao (ModernGL VertexArray): This is the scene we render (a cube).

  * timer (float): This is used to keep track of how long this section of the benchmark has been running for, and is used in calculating the rotation of our scene.

  * aspect_ratio (float): This float represents the aspect ratio we want our display to be rendering at.

* Keyword Args:

  * None

* Output:

  * fpslistX (array): Used to store the iteration of the benchmark. This correlates to a point, with this making up the X coordinate and 'fpslistY' making up the Y coordinate. These points are later plotted (after a bit of processing) in the benchmark results screen on a line graph.

  * fpslistY (array): Used to store the FPS at a given iteration of the benchmark. This correlates to a point, with this making up the Y coordinate and 'fpslistX' making up the X coordinate. These points are later plotted (after a bit of processing) in the benchmark results screen on a line graph.


