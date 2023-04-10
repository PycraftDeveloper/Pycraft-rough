registry_utils
==========

----------
generate_registry
----------
This class is in charge of setting all the default values, and making sure every variable defined in 'self' exists, reducing the risk of errors because variables are not defined. This is sorted alphabetically.

* Args:

  * None

* Keyword Args:

  * None

* Output:

  * None

registry
__________
This subroutine is in charge of setting all the default values, and making sure every variable defined in 'self' exists, reducing the risk of errors because variables are not defined. This is sorted alphabetically. This must always be called at startup (in 'pycraft_main').

* Args:

  * self (dict): This is used by Pycraft as a way of storing it's current configuration and behaviour and is required by most GUIs. Its use should be reduced where possible for readability reasons.

* Keyword Args:

  * None

* Output:

  * None


