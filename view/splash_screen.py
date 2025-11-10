#  ===========================================================================
# splash_screen.py
# ============================================================================

"""
Splash Screen - Elegant loading screen with animation
"""

import tkinter as tk
from tkinter import ttk


class SplashScreen:
    """Elegant splash screen with loading animation"""
    
    def __init__(self, duration=3):
        self.duration = duration  # Duration in seconds
        self.splash = tk.Tk()
        self.splash.title("Loading...")
        
        # Window setup
        window_width = 500
        window_height = 400
        screen_width = self.splash.winfo_screenwidth()
        screen_height = self.splash.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        self.splash.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.splash.overrideredirect(True)  # Remove window decorations
        self.splash.configure(bg="#0a2342")
        
        self.create_splash_content()
        
    def create_splash_content(self):
        """Create the splash screen UI"""
        main_frame = tk.Frame(self.splash, bg="#0a2342")
        main_frame.pack(expand=True, fill="both", padx=40, pady=40)
        
        # Logo/Icon
        icon_label = tk.Label(
            main_frame,
            text="💱",
            font=("Arial", 80),
            bg="#0a2342",
            fg="#00d4ff"
        )
        icon_label.pack(pady=(30, 20))
        
        # App Title
        title = tk.Label(
            main_frame,
            text="Cellusys Build Up",
            font=("Arial", 24, "bold"),
            fg="white",
            bg="#0a2342"
        )
        title.pack(pady=(0, 5))
        
        subtitle = tk.Label(
            main_frame,
            text="Currency Converter",
            font=("Arial", 18),
            fg="#00d4ff",
            bg="#0a2342"
        )
        subtitle.pack(pady=(0, 30))
        
        # Loading text
        self.loading_label = tk.Label(
            main_frame,
            text="Loading exchange rates...",
            font=("Arial", 11),
            fg="#cbd9ff",
            bg="#0a2342"
        )
        self.loading_label.pack(pady=(10, 15))
        
        # Progress bar
        style = ttk.Style()
        style.theme_use('clam')
        style.configure(
            "Custom.Horizontal.TProgressbar",
            troughcolor='#06172d',
            background='#00d4ff',
            bordercolor='#0a2342',
            lightcolor='#00d4ff',
            darkcolor='#00d4ff'
        )
        
        self.progress = ttk.Progressbar(
            main_frame,
            style="Custom.Horizontal.TProgressbar",
            length=350,
            mode='determinate',
            maximum=100
        )
        self.progress.pack(pady=(0, 20))
        
        # Version info
        version_label = tk.Label(
            main_frame,
            text="Version 1.0 • Powered by ExchangeRate API",
            font=("Arial", 9),
            fg="#7a8ba3",
            bg="#0a2342"
        )
        version_label.pack(side="bottom", pady=(20, 0))
        
    def update_progress(self):
        """Animate the progress bar"""
        steps = 50  # Number of update steps
        increment = 100 / steps
        delay = (self.duration * 1000) / steps  # milliseconds
        
        def animate(step=0):
            if step <= steps:
                self.progress['value'] = step * increment
                
                # Update loading text
                if step < steps // 3:
                    self.loading_label.config(text="Connecting to server...")
                elif step < 2 * steps // 3:
                    self.loading_label.config(text="Fetching exchange rates...")
                else:
                    self.loading_label.config(text="Almost ready...")
                
                self.splash.after(int(delay), lambda: animate(step + 1))
            else:
                self.close()
        
        animate()
    
    def close(self):
        """Close the splash screen"""
        self.splash.destroy()
    
    def show(self):
        """Display the splash screen"""
        self.update_progress()
        self.splash.mainloop()

# MAIN ENTRY POINT WITH SPLASH SCREEN

def main():
    # Show splash screen first (change duration here: 3 seconds default)
    # For 1 minute, use: splash = SplashScreen(duration=60)
    splash = SplashScreen(duration=3)  # 3 seconds for testing
    splash.show()
    
    # After splash screen closes, show main application
    
if __name__ == "__main__":
    main()