integrated_installer_utils
==========

----------
IntegInstaller
----------
This class is in charge of connecting the installer and Pycraft together. This class is used to check for updates to Pycraft.

* Args:

  * None

* Keyword Args:

  * None

CheckVersions
__________
This subroutine runs the command 'pip list --outdated' in a thread. The results of this command are then processed to check of Pycraft is outdated. This is run in parallel (thread).

* Args:

  * self (dict): This is used by Pycraft as a way of storing it's current configuration and behaviour and is required by most GUIs. Its use should be reduced where possible for readability reasons.

* Keyword Args:

  * None

* Output:

  * None

----------
CheckConnection
----------
This class is used to check if your PC has a working network connection so that updates can be checked for successfully.

* Args:

  * None

* Keyword Args:

  * None

test
__________
This subroutine attempts to ping google's servers. If this is successfully it means there is currently an internet connection to your PC. This is not run in a thread, so therefore there is a 1 second timeout. This means that if there isn't an internet connection available it doesn't slow down Pycraft's startup too much.

* Args:

  * None

* Keyword Args:

  * None

* Output:

  * (bool): This subroutine will return True if an internet connection can be established. If an internet connection could not be established, nothing is returned.


