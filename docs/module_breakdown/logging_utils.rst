logging_utils
==========

----------
create_log_message
----------
This class adds logging support to Pycraft.

* Args:

  * None

* Keyword Args:

  * None

* Output:

  * None

update_log_information
__________
This subroutine handles the formatting, output and logging of all non-critical information. This can be a handy debugging tool.

* Args:

  * logging_dictionary (dict): This dictionary is used to tell this subroutine if information messages are to be logged, this can be adjusted in settings.

  * text (str): This string contains the piece of information to log.

  * output_log (bool): This option tells the subroutine if logged messages should also be outputted to the console.

  * platform (str): This string tells the subroutine which operating system we are using. This is needed for OS specific operations.

  * base_folder (str): This string is a file path to the resources for Pycraft on your device.

* Keyword Args:

  * None

* Output:

  * None

update_log_warning
__________
This subroutine handles the formatting, output and logging of all non-critical warnings that could cause errors if not dealt with during the execution of Pycraft. This can be a handy debugging tool.

* Args:

  * logging_dictionary (dict): This dictionary is used to tell this subroutine if warning messages are to be logged, this can be adjusted in settings.

  * text (str): This string contains the piece of information to log.

  * output_log (bool): This option tells the subroutine if logged messages should also be outputted to the console.

  * platform (str): This string tells the subroutine which operating system we are using. This is needed for OS specific operations.

  * base_folder (str): This string is a file path to the resources for Pycraft on your device.

* Keyword Args:

  * None

* Output:

  * None

update_log_error
__________
This subroutine handles the formatting, output and logging of all critical errors in Pycraft. These must be dealt with immediately and will stop the execution of Pycraft, or could cause some things to not behave as expected.

* Args:

  * logging_dictionary (dict): This dictionary is used to tell this subroutine if error messages are to be logged, this can be adjusted in settings.

  * text (str): This string contains the piece of information to log.

  * output_log (bool): This option tells the subroutine if logged messages should also be outputted to the console.

  * platform (str): This string tells the subroutine which operating system we are using. This is needed for OS specific operations.

  * base_folder (str): This string is a file path to the resources for Pycraft on your device.

* Keyword Args:

  * None

* Output:

  * None

----------
log_file
----------
This class handles the writing to and formatting of the log file.

* Args:

  * None

* Keyword Args:

  * None

* Output:

  * None

clear_log
__________
This subroutine clears the log file. This is often called at startup to prevent the log file becoming too long.

* Args:

  * platform (str): This string tells the subroutine which operating system we are using. This is needed for OS specific operations.

  * base_folder (str): This string is a file path to the resources for Pycraft on your device.

* Keyword Args:

  * None

* Output:

  * None

update_log
__________
This subroutine updates the log file by appending new information to the end. This is usually called every time a log is made.

* Args:

  * platform (str): This string tells the subroutine which operating system we are using. This is needed for OS specific operations.

  * base_folder (str): This string is a file path to the resources for Pycraft on your device.

  * text (str): This string contains the formatted log which will be added to the log.

* Keyword Args:

  * None

* Output:

  * None


