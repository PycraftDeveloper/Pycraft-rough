pycraft_main
==========

----------
Startup
----------
This class is used to make sure Pycraft starts up and initializes properly.

* Args:

  * None

* Keyword Args:

  * None

__init__
__________
This class initializes Pycraft, this class also creates the 'self' dictionary used throughout Pycraft.

* Args:

  * self (dict): This is used by Pycraft as a way of storing it's current configuration and behaviour and is required by most GUIs. Its use should be reduced where possible for readability reasons.

* Keyword Args:

  * None

* Output:

  * None

----------
Initialize
----------
This class is used to start Pycraft. It is also responsible for 'connecting' you to different menus and making sure Pycraft starts up correctly.

* Args:

  * None

* Keyword Args:

  * None

menu_selector
__________
This subroutine is used to transfer you between different GUIs and programs used in Pycraft. This is also used to make sure that different menus in Pycraft get everything they need in order to start properly.

* Args:

  * self (dict): This is used by Pycraft as a way of storing it's current configuration and behaviour and is required by most GUIs. Its use should be reduced where possible for readability reasons.

* Keyword Args:

  * None

* Output:

  * None

Start
__________
This subroutine is used as the default start-up option for Pycraft. This will initialize a display, create all the variables (by using an earlier subroutine in this module) and get Pycraft ready for handing over to the main menu (home). Calling this subroutine starts Pycraft.

* Args:

  * None

* Keyword Args:

  * None

* Output:

  * None

QueryVersion
__________
This subroutine can be used to return the current version of Pycraft.  Version Naming Pycraft's versions will always now follow the structure; "vA.B.C" * Where "A" is the major revision number. * Where "B" is the minor revision number. * Where "C" is the patch and developer preview numbers (combined).  Every version of Pycraft as of the 27/10/2022 (DD/MM/YYYY) must feature all 3 values. Updates also now go sequentially, so Pycraft v9.6.4 is newer than Pycraft v9.5.7. If either of the "A" or "B" version numbers is incremented in a release, documentation MUST be suitably updated, in addition Pycraft MUST be released on PyPi, SourceForge and as a release on GitHub.

* Args:

  * None

* Keyword Args:

  * None

* Output:

  * version (str): Pycraft's current version.

start
__________
This subroutine is responsible for starting Pycraft, this can be used to call Pycraft externally, potentially as part of another program.

* Args:

  * None

* Keyword Args:

  * None

* Output:

  * None


