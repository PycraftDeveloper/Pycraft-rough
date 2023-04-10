loading_screen
==========

----------
generate_load_screen
----------
This class is in charge of setting up, managing, loading and running the loading GUI. This GUI gets loaded as a separate process at the start of the game engine and runs whilst the game engine loads to indicate that Pycraft hasn't crashed and how far through loading the game engine we are. This is run in parallel (process).

* Args:

  * None

* Keyword Args:

  * None

__init__
__________
This class is in charge of turning the dictionary the user enters as a parameter (that contains all the data required to properly display the loading screen GUI) into a 'generate_load_screen' object in a similar style to the 'pycraft_main' program. This also initializes the load screen's required modules.

* Args:

  * self (dict): This is used by Pycraft as a way of storing it's current configuration and behaviour and is required by most GUIs. Its use should be reduced where possible for readability reasons.

  * dictionary (dict): This parameter holds all the data that is stored as 'self' in the game engine. This includes the configuration and user defined settings. Note that the input to this variable must be sorted first to remove any modules or module specific objects. For example a (Pygame Surface) type object as that will cause errors when creating the new process.

* Keyword Args:

  * None

* Output:

  * None

load
__________
This subroutine is in charge of loading and running the loading GUI. This GUI gets loaded as a separate process at the start of the game engine and runs whilst the game engine loads to indicate that Pycraft hasn't crashed and how far through loading the game engine we are. This is run in parallel (process).

* Args:

  * dictionary (dict): This parameter holds all the data that is stored as 'self' in the game engine. This includes the configuration and user defined settings. Note that the input to this variable must be sorted first to remove any modules or module specific objects. For example a (Pygame Surface) type object as that will cause errors when creating the new process.

  * start_loading (Multiprocessing Event object): This parameter is an event object used to tell the load screen when the game engine starts to load. When this event is not set the load screen will wait to be called again.

* Keyword Args:

  * None

* Output:

  * None


