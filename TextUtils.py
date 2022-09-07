if __name__ != "__main__":
    print("Started <Pycraft_TextUtils>")
    
    class InstallerText:
        def __init__(self):
            pass

        def CreateText(InstallerImportData, root, OUTPUTtext):
            text = InstallerImportData.mod_Tkinter_tk_.Text(
                root,
                wrap=InstallerImportData.mod_Tkinter_tk_.WORD,
                relief=InstallerImportData.mod_Tkinter_tk_.FLAT,
                font=(None, 10))

            text.insert(
                InstallerImportData.mod_Tkinter_tk_.INSERT,
                OUTPUTtext)

            text["state"] = InstallerImportData.mod_Tkinter_tk_.DISABLED
            text.place(x=200, y=80)
            root.update_idletasks()

    class GenerateText:
        def __init__(self):
            pass

        def LoadQuickText(self):
            try:
                LoadingText = ["Use W, A, S, D to move",
                               "Use W to move forward",
                               "Use S to move backward",
                               "Use A to move left",
                               "Use D to move right",
                               "Access your inventory with E",
                               "Access your map with R",
                               "Use SPACE to jump",
                               "Did you know there is a light mode?",
                               "Did you know there is a dark mode?",
                               "Check us out on GitHub",
                               "Use ESC to exit",
                               "Hold W for 3 seconds to sprint",
                               "Did you know you can change the sound volume in settings?",
                               "Did you know you can change the music volume in settings?",
                               "Did you know you can use L to lock the camera",
                               "Did you know the project now supports controllers?",
                               "Use L to free your cursor",
                               "Now with time",
                               "Did you know a full day and night cycle is 20 minutes long?",
                               "Use F11 to full-screen your game!",
                               "Now with less bugs",
                               "What is that lurking in those shadows?",
                               "Pycraft is now a shady place!",
                               "Now with animations!",
                               "Check us out on Twitter!",
                               f"This is Pycraft v{self.version}",
                               "Now with clouds!",
                               "Check us out on Twitter: @PycraftDev",
                               "Like and subscribe",
                               "Now with lightning",
                               "Lights, camera and... action!",
                               "Now in 3D!"]

                locat = self.mod_random__.randint(0, (len(LoadingText)-1))
                text = LoadingText[locat]
                return text
            
            except Exception as Message:
                self.error_message = "TextUtils > GenerateText > LoadQuickText: " + \
                    str(Message)

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

    class TextWrap:
        def __init__(self):
            pass

        def blit_text(self, text, pos, font, color, surface_size):
            try:
                # 2D array where each row is a list of words.
                words = [word.split(" ") for word in text.splitlines()]
                # The width of a space.
                space = font.size(" ")[0]
                x, y = pos
                TextHeight = 0
                for line in words:
                    for word in line:
                        word_surface = font.render(
                            word,
                            self.aa,
                            color)

                        word_width, word_height = word_surface.get_size()
                        if x + word_width >= surface_size:
                            TextHeight += word_height
                            # Reset the x.
                            x = pos[0]
                            # Start on new row.
                            y += word_height

                        self.display.blit(
                            word_surface,
                            (x, y))

                        x += word_width + space

                    TextHeight += word_height
                    # Reset the x.
                    x = pos[0]
                    # Start on new row.
                    y += word_height
                return TextHeight
            
            except Exception as Message:
                self.error_message = "TextUtils > TextWrap > blit_text: " + \
                    str(Message)

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror(
        "Startup Fail",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
