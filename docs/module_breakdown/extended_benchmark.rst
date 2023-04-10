extended_benchmark
==========

----------
Loadbenchmark
----------
This class is in charge of loading and running the 3 window benchmarks in the correct order and returning the results of each run back to the benchmark GUI for processing.

* Args:

  * None

* Keyword Args:

  * None

run
__________
This subroutine is in charge of loading and running the 3 window benchmarks in the correct order and returning the results of each run back to the benchmark GUI for processing.

* Args:

  * None

* Keyword Args:

  * None

* Output:

  * fps_list_x_1 (array): Used to store the iteration of the benchmark. This correlates to a point, with this making up the X coordinate and 'fps_list_y_1' making up the Y coordinate. These points are later plotted (after a bit of processing) in the benchmark results screen on a line graph.

  * fps_list_y_1 (array): Used to store the FPS at a given iteration of the benchmark. This correlates to a point, with this making up the Y coordinate and 'fps_list_x_1' making up the X coordinate. These points are later plotted (after a bit of processing) in the benchmark results screen on a line graph.

  * fps_list_x_2 (array): Used to store the iteration of the benchmark. This correlates to a point, with this making up the X coordinate and 'fps_list_y_2' making up the Y coordinate. These points are later plotted (after a bit of processing) in the benchmark results screen on a line graph.

  * fps_list_y_2 (array): Used to store the FPS at a given iteration of the benchmark. This correlates to a point, with this making up the Y coordinate and 'fps_list_x_2' making up the X coordinate. These points are later plotted (after a bit of processing) in the benchmark results screen on a line graph.

  * fps_list_x_3 (array): Used to store the iteration of the benchmark. This correlates to a point, with this making up the X coordinate and 'fps_list_y_1' making up the Y coordinate. These points are later plotted (after a bit of processing) in the benchmark results screen on a line graph.

  * fps_list_y_1 (array): Used to store the FPS at a given iteration of the benchmark. This correlates to a point, with this making up the Y coordinate and 'fps_list_x_3' making up the X coordinate. These points are later plotted (after a bit of processing) in the benchmark results screen on a line graph.


