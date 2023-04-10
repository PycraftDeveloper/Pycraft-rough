pycraft_startup_test
==========

----------
startup_test
----------
This class is in charge running checks on your hardware and Pycraft's file structure to make sure any problems with incorrect file paths are identified quickly and you get the best experience on your hardware.

* Args:

  * None

* Keyword Args:

  * None

* Output:

  * None

__init__
__________
This subroutine checks a given file path to see if the resource it is expecting to find is present. If a resource is not at the required location then an error is returned.

* Args:

  * base_folder (str): This string is a file path to the resources for Pycraft on your device.

  * name (str): This is the name of the file we are trying to find.

  * path (str): This is the path from the 'pycraft' directory to where we are expecting the file to be.

* Keyword Args:

  * None

* Output:

  * error_message (str) OR None: If an error occurs whilst navigating to the required file path (potentially a folder may have moved) or the file we where expecting to find is not present then 'error_message' is returned. If no problems occur and the resource is found then 'None' gets returned.

  * error_message_detailed (str) OR None: If an error occurs whilst navigating to the required file path (potentially a folder may have moved) or the file we where expecting to find is not present then 'error_message_detailed' is returned. If no problems occur and the resource is found then 'None' gets returned. This output contains more details about exactly what error has occured and can be enabled

  * for testing or debug purposes usually

  * in the settings menu. This is a handy debugging tool.

test_for_resource
__________
This subroutine checks a given file path to see if the resource it is expecting to find is present. If a resource is not at the required location then an error is returned.

* Args:

  * base_folder (str): This string is a file path to the resources for Pycraft on your device.

  * name (str): This is the name of the file we are trying to find.

  * path (str): This is the path from the 'pycraft' directory to where we are expecting the file to be.

* Keyword Args:

  * None

* Output:

  * error_message (str) OR None: If an error occurs whilst navigating to the required file path (potentially a folder may have moved) or the file we where expecting to find is not present then 'error_message' is returned. If no problems occur and the resource is found then 'None' gets returned.

  * error_message_detailed (str) OR None: If an error occurs whilst navigating to the required file path (potentially a folder may have moved) or the file we where expecting to find is not present then 'error_message_detailed' is returned. If no problems occur and the resource is found then 'None' gets returned. This output contains more details about exactly what error has occured and can be enabled

  * for testing or debug purposes usually

  * in the settings menu. This is a handy debugging tool.

resource_not_found
__________
This subroutine creates the error message that gets returned if a resource is not at its expected location.

* Args:

  * name (str): This is the name of the file we are trying to find.

  * path (str): This is the path from the 'pycraft' directory to where we are expecting the file to be.

* Keyword Args:

  * None

* Output:

  * error_message (str): If an error occurs whilst navigating to the required file path (potentially a folder may have moved) or the file we where expecting to find is not present then 'error_message' is returned.

  * error_message_detailed (str): If an error occurs whilst navigating to the required file path (potentially a folder may have moved) or the file we where expecting to find is not present then 'error_message_detailed' is returned. This output contains more details about exactly what error has occured and can be enabled

  * for testing or debug purposes usually

  * in the settings menu. This is a handy debugging tool.

pycraft_self_test
__________
This subroutine compares the minimum requirements of Pycraft to the specs of your hardware to see if we can run Pycraft on your PC. Specs:

  * OpenGL v2.8 or newer (potentially needs to be reviewed).

  * SDL v2 or newer.

  * 260 MB of RAM or more (potentially need to be reviewed).

* Args:

  * window_icon (Pygame Surface): This is the icon we use in the caption (and in the taskbar on some supported OS') for Pycraft.

* Keyword Args:

  * None

* Output:

  * None

pycraft_resource_test
__________
This subroutine is in charge of checking for every resource required by Pycraft to make sure that it is where Pycraft will expect it to be when it is required by other areas of the game. Any problems raised here may mean something is wrong with the structure of Pycraft. Problems here after an update or when you first install Pycraft can indicate an error with the install. This is run in parallel (thread).

* Args:

  * self (dict): This is used by Pycraft as a way of storing it's current configuration and behaviour and is required by most GUIs. Its use should be reduced where possible for readability reasons.

  * override (bool): This is used to forcefully run 'pycraft_resource_test'. This is used to allow the user to check for problems in the settings menu (in the 'Storage and permissions' section).

* Keyword Args:

  * None

* Output:

  * None


