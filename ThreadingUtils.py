if __name__ != "__main__":
    class ThreadingUtils:
        def __init__(self):
            pass

        def general_threading_utility(self):
            try:
                while True:
                    if self.draw_devmode_graph:
                        if self.timer >= 2:
                            CPUPercent = self.mod_psutil__.cpu_percent(0.5)
                            if CPUPercent > self.data_CPU_usage_Max:
                                self.data_CPU_usage_Max = CPUPercent

                            self.data_CPU_usage.append([
                                ((self.real_window_width/2)+100)+(self.timer),
                                200-(2)*CPUPercent])

                        self.mod_time__.sleep(0.5)

                    else:
                        self.mod_time__.sleep(1)

                    if self.iteration > 1000:
                        self.aFPS = (self.aFPS/self.iteration)
                        self.iteration = 1

                    if (self.FPS < 15 or
                            self.FPS > 500):
                        
                        self.mod_logging_utils__.create_log_message.update_log_information(
                            self,
                            "".join(("ThreadingUtil > ThreadingUtils > ",
                                        "general_threading_utility: 'self.FPS' ",
                                        "variable contained an invalid value, ",
                                        f"this has been reset to 60 from {self.FPS} previously")))
                        
                        self.FPS = 60

                    else:
                        if self.FPS_overclock is False:
                            self.FPS = int(self.FPS)

                    if self.FPS_overclock is False:
                        self.eFPS = int(self.eFPS)

                    else:
                        if self.aFPS == float("inf"):
                            self.aFPS = 1
                            self.iteration = 1
                            
            except Exception as Message:
                self.error_message = "".join(("ThreadingUtils > ThreadingUtils ",
                                             f"> general_threading_utility: {str(Message)}"))

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)
            finally:
                self.mod_logging_utils__.create_log_message.update_log_information(
                    self,
                    "'thread_pycraft_general' has stopped")

        def AdaptiveMode(self):
            try:
                while True:
                    if self.settings_preset == "adaptive":
                        ProcessPercent = self.mod_psutil__.Process().cpu_percent(0.1)
                        CPUPercent = self.mod_psutil__.cpu_percent(0.1)

                        try:
                            gpus = self.mod_GPUtil__.getGPUs()

                            GPUPercent = 0
                            NumOfGPUs = 0

                            for gpu in gpus:
                                NumOfGPUs += 1
                                GPUPercent += gpu.load*100

                            GPUPercent = GPUPercent/NumOfGPUs

                        except Exception as Message:
                            log_message = "ThreadingUtils > ThreadingUtils > AdaptiveMode: "+str(Message)
                            
                            self.mod_logging_utils__.create_log_message.update_log_warning(
                                self,
                                log_message)
                            
                            GPUPercent = CPUPercent

                        if CPUPercent > 75 and self.FPS > 25:
                            self.FPS -= 1
                            if CPUPercent > 90 and self.FPS > 25:
                                self.FPS -= 9

                        elif ProcessPercent > 50 and self.FPS > 25:
                            self.FPS -= 1
                            if ProcessPercent > 75 and self.FPS > 25:
                                self.FPS -= 9

                        else:
                            if GPUPercent > 50 and self.FPS > 25:
                                self.FPS -= 1
                                if GPUPercent > 75 and self.FPS > 25:
                                    self.FPS -= 9

                            else:
                                if self.FPS < 500:
                                    self.FPS += 1
                    else:
                        self.mod_time__.sleep(1)
                        
            except Exception as Message:
                self.error_message = "ThreadingUtils > ThreadingUtils > AdaptiveMode: "+str(Message)

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)
            finally:
                self.mod_logging_utils__.create_log_message.update_log_information(
                    self,
                    "'thread_adaptive_mode' has stopped")

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
