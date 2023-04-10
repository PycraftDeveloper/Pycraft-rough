inventory
==========

----------
generate_inventory
----------
This class is in charge of setting up, managing, loading and running the inventory GUI. This GUI gets loaded as a separate process at the start of the game engine and runs only when the game engine sends a command. This is run in parallel (process).

* Args:

  * None

* Keyword Args:

  * None

__init__
__________
This class is in charge of turning the dictionary the user enters as a parameter (that contains all the data required to properly display the inventory GUI) into a 'generate_inventory' object in a similar style to the 'pycraft_main' program. This also initializes the inventory's required modules.

* Args:

  * self (dict): This is used by Pycraft as a way of storing it's current configuration and behaviour and is required by most GUIs. Its use should be reduced where possible for readability reasons.

  * dictionary (dict): This parameter holds all the data that is stored as 'self' in the game engine. This includes the configuration and user defined settings. Note that the input to this variable must be sorted first to remove any modules or module specific objects. For example a (Pygame Surface) type object as that will cause errors when creating the new process.

* Keyword Args:

  * None

* Output:

  * None

inventory_gui
__________
This subroutine is in charge of loading and running the inventory GUI. This GUI gets loaded as a separate process at the start of the game engine and runs only when the game engine sends a command. This is run in parallel (process).

* Args:

  * dictionary (dict): This parameter holds all the data that is stored as 'self' in the game engine. This includes the configuration and user defined settings. Note that the input to this variable must be sorted first to remove any modules or module specific objects. For example a (Pygame Surface) type object as that will cause errors when creating the new process.

  * start_inventory (Multiprocessing Event object): This parameter is an event object used to tell the inventory when the game engine wants to have the inventory displayed. When this event is not set the inventory will wait.

* Keyword Args:

  * None

* Output:

  * None


