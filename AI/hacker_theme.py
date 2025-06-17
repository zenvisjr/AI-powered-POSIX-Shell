import os

ascii_logo = r"""
 ██╗ ██╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██║  ██╔╝██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██████╔╝ ███████║██║     █████╔╝ █████╗  ██████╔╝
██╔═ ██╗ ██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║  ██╗ ██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

"""

# Set shell colors (export to .shellrc or trigger in runtime config if possible)
print(ascii_logo)
print("\033[92m")  # Set text color to bright green
os.system("setterm -foreground green -background black")

# Optional: sound on keypress (Linux only)
os.system("paplay /usr/share/sounds/freedesktop/stereo/message.oga &")  # Or custom sound
