print("Started <Pycraft_Installer_Main>")

class RunInstaller:
    def __init__(InstallerImportData):
        import os
        InstallerImportData.mod_Os__ = os
        import platform
        InstallerImportData.mod_platform__ = platform
        InstallerImportData.base_folder = os.path.dirname(__file__)
        InstallerImportData.platform = platform.system()

        import tkinter as tk
        InstallerImportData.mod_Tkinter_tk_ = tk
        from tkinter import messagebox
        InstallerImportData.mod_Tkinter_messagebox_ = messagebox
        from tkinter import filedialog
        InstallerImportData.mod_Tkinter_filedialog_ = filedialog
        import tkinter.ttk as ttk
        InstallerImportData.mod_Tkinter_ttk_ = ttk
        import subprocess
        InstallerImportData.mod_subprocess__ = subprocess
        import time
        InstallerImportData.mod_time__ = time
        import json
        InstallerImportData.mod_Json__ = json
        import threading
        InstallerImportData.mod_threading__ = threading
        import sys
        InstallerImportData.mod_sys__ = sys
        import shutil
        InstallerImportData.mod_shutil__ = shutil
        import site
        InstallerImportData.mod_Site__ = site
        import PIL.Image as Image
        InstallerImportData.mod_PIL_Image_ = Image
        import PIL.ImageTk as ImageTk
        InstallerImportData.mod_PIL_ImageTk_ = ImageTk
        if InstallerImportData.platform == "Windows":
            from win32com.shell import shell, shellcon
            InstallerImportData.mod_shutil_shell_ = shell
            InstallerImportData.mod_shutil_shellcon_ = shellcon
            import win32com.client
            InstallerImportData.mod_win32com_client_ = win32com.client

        if ("site-packages" in InstallerImportData.base_folder or
                "dist-packages" in InstallerImportData.base_folder):

            from pycraft import TkinterUtils
            InstallerImportData.mod_tkinter_utils__ = TkinterUtils
            from pycraft import ImageUtils
            InstallerImportData.mod_image_utils__ = ImageUtils
            from pycraft import InstallerUtils
            InstallerImportData.mod_InstallerUtil__ = InstallerUtils
            from pycraft import Installer_HomeScreen
            InstallerImportData.mod_Installer_HomeScreen_ = Installer_HomeScreen
            from pycraft import Install
            InstallerImportData.mod_Installer_Install_ = Install
            from pycraft import TextUtils
            InstallerImportData.mod_Installer_TextUtils_ = TextUtils
            from pycraft import Uninstall
            InstallerImportData.mod_Installer_Uninstall_ = Uninstall
            from pycraft import Update
            InstallerImportData.mod_Installer_Update_ = Update
        else:
            import TkinterUtils
            InstallerImportData.mod_tkinter_utils__ = TkinterUtils
            import ImageUtils
            InstallerImportData.mod_image_utils__ = ImageUtils
            import InstallerUtils
            InstallerImportData.mod_InstallerUtil__ = InstallerUtils
            import Installer_HomeScreen
            InstallerImportData.mod_Installer_HomeScreen_ = Installer_HomeScreen
            import Install
            InstallerImportData.mod_Installer_Install_ = Install
            import TextUtils
            InstallerImportData.mod_Installer_TextUtils_ = TextUtils
            import Uninstall
            InstallerImportData.mod_Installer_Uninstall_ = Uninstall
            import Update
            InstallerImportData.mod_Installer_Update_ = Update

    def Initialize():
        InstallerImportData = RunInstaller()
        root = None

        ChooseBETA = False
        Choice = "Latest"

        root = InstallerImportData.mod_tkinter_utils__.TkinterInstaller.Createdisplay(
            InstallerImportData,
            root)

        PycPath = InstallerImportData.mod_InstallerUtil__.GetInstallerData.GetData(
            InstallerImportData)

        InstallerImportData.mod_Installer_HomeScreen_.Installer_Home.Start(
            InstallerImportData,
            root,
            PycPath,
            ChooseBETA,
            Choice)

        root.mainloop()

if __name__ == "__main__":
    RunInstaller.Initialize()
