map_gui
==========

----------
generate_map_gui
----------
This class is in charge of setting up, managing, loading and running the map GUI. This GUI gets loaded as a separate process at the start of the game engine and runs only when the game engine sends a command. This is run in parallel (process).

* Args:

  * None

* Keyword Args:

  * None

__init__
__________
This class is in charge of turning the dictionary the user enters as a parameter (that contains all the data required to properly display the map GUI) into a 'generate_map_gui' object in a similar style to the 'pycraft_main' program. This also initializes the map's required modules.

* Args:

  * self (dict): This is used by Pycraft as a way of storing it's current configuration and behaviour and is required by most GUIs. Its use should be reduced where possible for readability reasons.

  * dictionary (dict): This parameter holds all the data that is stored as 'self' in the game engine. This includes the configuration and user defined settings. Note that the input to this variable must be sorted first to remove any modules or module specific objects. For example a (Pygame Surface) type object as that will cause errors when creating the new process.

* Keyword Args:

  * None

* Output:

  * None

get_map_pos
__________
This maths based subroutine is used to calculate the position the map should be rendered onscreen.

* Args:

  * in_x (float): This parameter represents the user's position in game on the X axis.

  * in_z (float): This parameter represents the user's position in game on the Z axis.

* Keyword Args:

  * None

* Output:

  * x (int): The X coordinate to render the map.

  * z (int): The Y coordinate to render the map. (In 2D space there is no 'Z' or depth axis, therefore because we don't care about the user's height position here, we use their Z position in 3D space to represent their Y coordinate in 2D space.)

map_gui
__________
This subroutine is in charge of loading and running the map GUI. This GUI gets loaded as a separate process at the start of the game engine and runs only when the game engine sends a command. This is run in parallel (process).

* Args:

  * dictionary (dict): This parameter holds all the data that is stored as 'self' in the game engine. This includes the configuration and user defined settings. Note that the input to this variable must be sorted first to remove any modules or module specific objects. For example a (Pygame Surface) type object as that will cause errors when creating the new process.

  * start_inventory (Multiprocessing Event object): This parameter is an event object used to tell the inventory when the game engine wants to have the inventory displayed. When this event is not set the map will wait.

* Keyword Args:

  * None

* Output:

  * None


