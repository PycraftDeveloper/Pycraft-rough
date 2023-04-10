settings
==========

----------
generate_settings
----------
This class is in charge of loading the structure for the settings menu, and rendering the settings menu properly.

* Args:

  * None

* Keyword Args:

  * None

restart_function
__________
This subroutine adds restarting functionality into Pycraft. To do this we run a command in a separate process 'python main.py' which launches a separate instance of Pycraft before we then close the current instance.

* Args:

  * platform (str): This string tells the subroutine which operating system we are using. This is needed for OS specific operations.

  * base_folder (str): This string is a file path to the resources for Pycraft on your device.

* Keyword Args:

  * None

* Output:

  * None

settings_gui
__________
This subroutine is in charge of rendering the settings menu and applying all changes to their corresponding variables throughout Pycraft.

* Args:

  * self (dict): This is used by Pycraft as a way of storing it's current configuration and behaviour and is required by most GUIs. Its use should be reduced where possible for readability reasons.

* Keyword Args:

  * None

* Output:

  * None


