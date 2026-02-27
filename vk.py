#!/usr/bin/env python3
"""
VISUAL KRISHNA - Beautiful Image Display with Fun GUI
Version: 2.0 Glamorous Edition
Author: Fun Creator
Description: A beautiful full-screen interactive GUI featuring Visahl Krishna
"""

import os
import sys
import time
import random
import subprocess
import urllib.request
import importlib
import tkinter as tk
from tkinter import Label, Button, Frame, messagebox
from PIL import Image, ImageTk, ImageEnhance, ImageFilter, ImageDraw
import ctypes
import math

# ==================== AUTO INSTALLER ====================

def install_pillow():
    """Ensure PIL is installed"""
    try:
        from PIL import Image
    except ImportError:
        print("Installing Pillow for image support...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pillow'])
        print("Installation complete!")

install_pillow()

# ==================== CONFIGURATION ====================

class Config:
    IMAGE_URL = "https://github.com/Sabari425/Others-Projects/blob/main/vk.png"
    WINDOW_TITLE = "✨ VISAHI KRISHNA - BEAUTY BEYOND WORDS ✨"
    BG_COLOR = "#ffd9e6"  # Soft pink
    BUTTON_COLOR = "#ff99cc"  # Hot pink
    BUTTON_HOVER = "#ff66b2"  # Darker pink
    TEXT_COLOR = "#660033"  # Dark purple
    ACCENT_COLOR = "#ff4d94"  # Bright pink

# ==================== IMAGE DOWNLOADER ====================

def download_image(url):
    """Download image from GitHub"""
    # Convert to raw URL
    if 'github.com' in url and '/blob/' in url:
        raw_url = url.replace('github.com', 'raw.githubusercontent.com').replace('/blob/', '/')
    else:
        raw_url = url
    
    save_path = os.path.join(os.environ['TEMP'], 'visahl_krishna.jpg')
    
    try:
        print("📸 Loading beautiful image of Visahl Krishna...")
        
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(raw_url, headers=headers)
        
        with urllib.request.urlopen(req, timeout=15) as response:
            with open(save_path, 'wb') as out_file:
                out_file.write(response.read())
        
        if os.path.exists(save_path) and os.path.getsize(save_path) > 0:
            return save_path
        else:
            return None
            
    except Exception as e:
        print(f"Download error: {e}")
        return None

# ==================== MAIN GUI APPLICATION ====================

class VisahlKrishnaGUI:
    def __init__(self, image_path):
        self.image_path = image_path
        self.root = tk.Tk()
        self.root.title(Config.WINDOW_TITLE)
        self.root.configure(bg=Config.BG_COLOR)
        
        # Make full screen
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-topmost', True)
        
        # Get screen dimensions
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        
        # Animation variables
        self.dance_animation_id = None
        self.dancing = False
        self.dance_step = 0
        self.original_image = None
        self.photo_image = None
        self.compliment_index = 0
        
        # Setup UI
        self.setup_ui()
        
        # Load image
        self.load_image()
        
        # Bind escape key
        self.root.bind('<Escape>', self.exit_app)
        self.root.bind('<q>', self.exit_app)
        self.root.bind('<Q>', self.exit_app)
    
    def load_image(self):
        """Load and prepare the image"""
        try:
            # Open image
            self.original_image = Image.open(self.image_path)
            
            # Enhance image
            self.original_image = self.enhance_image(self.original_image)
            
            # Calculate display size (80% of screen)
            display_width = int(self.screen_width * 0.6)
            display_height = int(self.screen_height * 0.6)
            
            # Resize while maintaining aspect ratio
            self.original_image.thumbnail((display_width, display_height), Image.Resampling.LANCZOS)
            
            # Store original size for animation
            self.original_size = self.original_image.size
            
            # Display image
            self.display_image(self.original_image)
            
        except Exception as e:
            print(f"Image loading error: {e}")
            self.show_error_image()
    
    def enhance_image(self, image):
        """Apply enhancements for better display"""
        # Enhance contrast
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(1.1)
        
        # Enhance color
        enhancer = ImageEnhance.Color(image)
        image = enhancer.enhance(1.2)
        
        # Enhance sharpness
        enhancer = ImageEnhance.Sharpness(image)
        image = enhancer.enhance(1.1)
        
        return image
    
    def display_image(self, image):
        """Display image in the label"""
        self.current_image = image
        self.photo_image = ImageTk.PhotoImage(image)
        self.image_label.config(image=self.photo_image)
        self.image_label.image = self.photo_image
    
    def show_error_image(self):
        """Show error message if image fails"""
        error_text = "✨ Visahl Krishna is too beautiful to load! ✨\nImagine the most gorgeous person ever!"
        self.image_label.config(text=error_text, font=("Arial", 24), fg=Config.TEXT_COLOR)
    
    def setup_ui(self):
        """Setup the user interface"""
        # Main container
        main_container = Frame(self.root, bg=Config.BG_COLOR)
        main_container.pack(expand=True, fill='both', padx=50, pady=30)
        
        # Title Section
        title_frame = Frame(main_container, bg=Config.BG_COLOR)
        title_frame.pack(fill='x', pady=(0, 20))
        
        title_label = Label(
            title_frame,
            text="✨ VISAHI KRISHNA ✨",
            font=("Helvetica", 48, "bold"),
            bg=Config.BG_COLOR,
            fg=Config.TEXT_COLOR
        )
        title_label.pack()
        
        subtitle_label = Label(
            title_frame,
            text="The Most Beautiful Person in the Digital World",
            font=("Helvetica", 20, "italic"),
            bg=Config.BG_COLOR,
            fg=Config.ACCENT_COLOR
        )
        subtitle_label.pack()
        
        # Image Section
        image_frame = Frame(main_container, bg='white', relief='ridge', bd=5)
        image_frame.pack(expand=True, fill='both', pady=20)
        
        self.image_label = Label(image_frame, bg='white')
        self.image_label.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Interactive Message Section
        self.message_frame = Frame(main_container, bg=Config.BG_COLOR)
        self.message_frame.pack(fill='x', pady=10)
        
        self.message_label = Label(
            self.message_frame,
            text="✨ Click the buttons below for some fun! ✨",
            font=("Helvetica", 16),
            bg=Config.BG_COLOR,
            fg=Config.TEXT_COLOR,
            wraplength=800
        )
        self.message_label.pack()
        
        # Button Section
        button_frame = Frame(main_container, bg=Config.BG_COLOR)
        button_frame.pack(fill='x', pady=20)
        
        # Button styling
        button_style = {
            'font': ("Helvetica", 16, "bold"),
            'bg': Config.BUTTON_COLOR,
            'fg': 'white',
            'activebackground': Config.BUTTON_HOVER,
            'activeforeground': 'white',
            'relief': 'raised',
            'bd': 3,
            'padx': 30,
            'pady': 15,
            'cursor': 'hand2'
        }
        
        # Row 1 buttons
        row1_frame = Frame(button_frame, bg=Config.BG_COLOR)
        row1_frame.pack(pady=10)
        
        self.compliment_btn = Button(
            row1_frame,
            text="💝 Get Compliment",
            command=self.show_compliment,
            **button_style
        )
        self.compliment_btn.pack(side='left', padx=10)
        
        self.dance_btn = Button(
            row1_frame,
            text="💃 Dance Party",
            command=self.toggle_dance,
            **button_style
        )
        self.dance_btn.pack(side='left', padx=10)
        
        self.sparkle_btn = Button(
            row1_frame,
            text="✨ Add Sparkles",
            command=self.add_sparkles,
            **button_style
        )
        self.sparkle_btn.pack(side='left', padx=10)
        
        # Row 2 buttons
        row2_frame = Frame(button_frame, bg=Config.BG_COLOR)
        row2_frame.pack(pady=10)
        
        self.heart_btn = Button(
            row2_frame,
            text="❤️ Heart Effect",
            command=self.heart_effect,
            **button_style
        )
        self.heart_btn.pack(side='left', padx=10)
        
        self.zoom_btn = Button(
            row2_frame,
            text="🔍 Zoom Magic",
            command=self.zoom_effect,
            **button_style
        )
        self.zoom_btn.pack(side='left', padx=10)
        
        self.exit_btn = Button(
            row2_frame,
            text="❌ Exit",
            command=self.exit_app,
            **{**button_style, 'bg': '#ff6666', 'activebackground': '#ff3333'}
        )
        self.exit_btn.pack(side='left', padx=10)
        
        # Footer
        footer_label = Label(
            main_container,
            text="✨ Press ESC or click Exit to close ✨",
            font=("Helvetica", 12),
            bg=Config.BG_COLOR,
            fg='#999999'
        )
        footer_label.pack(pady=(10, 0))
        
        # Compliments list
        self.compliments = [
            "✨ You're more beautiful than a sunset!",
            "💖 Your smile lights up the digital world!",
            "🌟 If beauty was a crime, you'd be life imprisonment!",
            "🌸 You're made of sugar and spice and everything nice!",
            "💫 You're so beautiful, even the stars are jealous!",
            "🌺 Like a flower in full bloom!",
            "✨ You're the human equivalent of a perfect selfie!",
            "💝 Beauty: 100/100, Grace: 100/100, You: 1000/100!",
            "🌟 You're so gorgeous, even filters are intimidated!",
            "💖 If beauty was time, you'd be eternity!"
        ]
    
    # ==================== BUTTON FUNCTIONS ====================
    
    def show_compliment(self):
        """Show a random compliment"""
        compliment = random.choice(self.compliments)
        self.message_label.config(text=compliment, fg=random.choice(['#ff0066', '#9900cc', '#0066cc', '#009900']))
        self.root.after(3000, self.reset_message)
    
    def reset_message(self):
        """Reset message to default"""
        self.message_label.config(
            text="✨ Click the buttons below for some fun! ✨",
            fg=Config.TEXT_COLOR
        )
    
    def toggle_dance(self):
        """Toggle dance animation"""
        if not self.dancing:
            self.dancing = True
            self.dance_btn.config(text="🛑 Stop Dancing")
            self.dance_animation()
        else:
            self.dancing = False
            self.dance_btn.config(text="💃 Dance Party")
            if self.dance_animation_id:
                self.root.after_cancel(self.dance_animation_id)
            self.display_image(self.original_image)
    
    def dance_animation(self):
        """Animate the image dancing"""
        if self.dancing and self.original_image:
            # Calculate dance movement
            self.dance_step += 1
            
            # Create dancing effect (rotation and slight movement)
            img_copy = self.original_image.copy()
            
            # Apply slight rotation based on step
            angle = math.sin(self.dance_step * 0.5) * 5
            rotated = img_copy.rotate(angle, expand=True, fillcolor='white')
            
            # Convert to PhotoImage and display
            self.display_image(rotated)
            
            # Continue animation
            self.dance_animation_id = self.root.after(100, self.dance_animation)
    
    def add_sparkles(self):
        """Add sparkle effect to image"""
        if self.original_image:
            img_copy = self.original_image.copy()
            draw = ImageDraw.Draw(img_copy)
            
            # Add random sparkles
            width, height = img_copy.size
            for _ in range(20):
                x = random.randint(0, width-20)
                y = random.randint(0, height-20)
                sparkle = random.choice(["✨", "💫", "⭐"])
                
                # Simple rectangle sparkle
                for i in range(3):
                    draw.ellipse([x-5-i, y-5-i, x+5+i, y+5+i], 
                               outline=(255, 255, 0, 100-i*30), width=2)
            
            self.display_image(img_copy)
            self.message_label.config(text="✨ Sparkling beauty! ✨")
            self.root.after(2000, self.reset_image)
    
    def heart_effect(self):
        """Add heart effect"""
        if self.original_image:
            img_copy = self.original_image.copy()
            draw = ImageDraw.Draw(img_copy)
            
            # Add hearts
            width, height = img_copy.size
            for _ in range(15):
                x = random.randint(0, width-30)
                y = random.randint(0, height-30)
                
                # Draw simple heart (approximation)
                draw.polygon([(x+15, y), (x+30, y+15), (x+15, y+30), (x, y+15)], 
                           fill=(255, 105, 180, 150))
            
            self.display_image(img_copy)
            self.message_label.config(text="❤️ Heart overload! ❤️")
            self.root.after(2000, self.reset_image)
    
    def zoom_effect(self):
        """Zoom in and out effect"""
        if self.original_image:
            def zoom_step(step=0):
                if step < 10:
                    # Zoom in
                    scale = 1.0 + (step * 0.02)
                    new_width = int(self.original_size[0] * scale)
                    new_height = int(self.original_size[1] * scale)
                    
                    zoomed = self.original_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
                    self.display_image(zoomed)
                    
                    self.root.after(50, lambda: zoom_step(step+1))
                elif step < 20:
                    # Zoom out
                    scale = 1.2 - ((step-10) * 0.02)
                    new_width = int(self.original_size[0] * scale)
                    new_height = int(self.original_size[1] * scale)
                    
                    zoomed = self.original_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
                    self.display_image(zoomed)
                    
                    self.root.after(50, lambda: zoom_step(step+1))
                else:
                    # Back to original
                    self.reset_image()
            
            self.message_label.config(text="🔍 Zoom zoom! Getting closer to beauty!")
            zoom_step()
    
    def reset_image(self):
        """Reset image to original"""
        if self.original_image:
            self.display_image(self.original_image)
            self.reset_message()
    
    def exit_app(self, event=None):
        """Exit the application"""
        if messagebox.askyesno("Exit", "Are you sure you want to leave this beauty?"):
            self.root.quit()
            self.root.destroy()
            sys.exit(0)
    
    def run(self):
        """Run the application"""
        self.root.mainloop()

# ==================== MAIN FUNCTION ====================

def main():
    """Main function"""
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Welcome message
    print("=" * 60)
    print("✨ VISUAL KRISHNA - BEAUTIFUL IMAGE DISPLAY ✨".center(60))
    print("=" * 60)
    print()
    
    # Download image
    print("📸 Loading beautiful image...")
    image_path = download_image(Config.IMAGE_URL)
    
    if image_path:
        print("✅ Image loaded successfully!")
        print("🎨 Opening beautiful display...")
        time.sleep(1)
        
        # Create and run GUI
        app = VisahlKrishnaGUI(image_path)
        app.run()
    else:
        print("❌ Could not load image. Using imagination mode!")
        time.sleep(2)
        
        # Create a simple GUI with message
        root = tk.Tk()
        root.title("✨ Visahl Krishna ✨")
        root.attributes('-fullscreen', True)
        root.configure(bg='#ffd9e6')
        
        label = Label(
            root,
            text="✨ VISAHI KRISHNA ✨\n\nThe Most Beautiful Person Ever!\n\nImagine the most gorgeous image...\n\nIt's too beautiful to display!",
            font=("Arial", 32),
            bg='#ffd9e6',
            fg='#660033'
        )
        label.pack(expand=True)
        
        exit_btn = Button(
            root,
            text="Exit",
            command=root.quit,
            font=("Arial", 20),
            bg='#ff99cc',
            padx=50,
            pady=20
        )
        exit_btn.pack(pady=50)
        
        root.bind('<Escape>', lambda e: root.quit())
        root.mainloop()

# ==================== ENTRY POINT ====================

if __name__ == "__main__":
    main()