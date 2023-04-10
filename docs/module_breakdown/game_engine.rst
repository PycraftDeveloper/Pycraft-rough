game_engine
==========

----------
create_game_engine
----------
This class is responsible for the setup, loading and running of the game engine.

* Args:

  * None

* Keyword Args:

  * None

start
__________
This subroutine is responsible for telling ModernGL and ModernGL_window that our Pygame display is to be rendered to.

* Args:

  * None

* Keyword Args:

  * None

* Output:

  * ctx (Context object): This is used by ModernGL for loading OpenGL resources and enabling access to OpenGL features.

  * wnd (BaseWindow): This is used by ModernGL_window as the display object to use for rendering and additional resource loading.

game_engine
__________
This subroutine is responsible for loading and running Pycraft's game engine.

* Args:

  * self (dict): This is used by Pycraft as a way of storing it's current configuration and behaviour and is required by most GUIs. Its use should be reduced where possible for readability reasons.

* Keyword Args:

  * None

* Output:

  * None


