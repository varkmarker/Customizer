from colr import Colr as colr
import os
import time
from pathlib import Path


class Colors:
    def red(data):
        print(colr().hex("#ff0000", data, rgb_mode=True))

    def rose(data):
        print(colr().hex("#ff0066", data, rgb_mode=True))

    def green(data):
        print(colr().hex("#00ff8d", data, rgb_mode=True))

    def gnome_green(data):
        print(colr().hex("#2ed1b4", data, rgb_mode=True))

    def yellow_green(data):
        print(colr().hex("#a8c836", data, rgb_mode=True))

    def dark_orange(data):
        print(colr().hex("#cf301b", data, rgb_mode=True))

    def light_gnome(data):
        print(colr().hex("#00ffc4", data, rgb_mode=True))

    def yellow_green(data):
        print(colr().hex("#7ed666", data, rgb_mode=True))

    def violet(data):
        print(colr().hex("#cc33ff", data, rgb_mode=True))

    def light_green(data):
        print(colr().hex("#21ff00", data, rgb_mode=True))

    def orange(data):
        print(colr().hex("#ff8e35", data, rgb_mode=True))

    def yellow(data):
        print(colr().hex("#fff300", data, rgb_mode=True))

    def sky_blue(data):
        print(colr().hex("#00ccff", data, rgb_mode=True))

    def blue(data):
        print(colr().hex("#0000ff", data, rgb_mode=True))

    def cream(data):
        print(colr().hex("#ff9999", data, rgb_mode=True))

    def dark_rose(data):
        print(colr().hex("#cc0066", data, rgb_mode=True))

    def dark_red(data):
        print(colr().hex("#cc0000", data, rgb_mode=True))

    def dark_green(data):
        print(colr().hex("#009933", data, rgb_mode=True))

    def light_blue(data):
        print(colr().hex("#6666ff", data, rgb_mode=True))


# Operator's
class Operators:
    # Normal exit
    def exit():
        os.system("exit")
        time.sleep(0.5)
        Colors.red("\n You are exited \n")

    # Author information
    def author():
        Colors.sky_blue("\n                     AUTHOR")
        time.sleep(0.5)
        Colors.orange(
            " \n If this script saves you time. You can give a star on GitHub"
        )
        Colors.orange(
            f" \n If you have any suggestions about this tool you can contact me on Twitter."
        )
        time.sleep(0.5)
        Colors.orange(" \n Twitter link: https://twitter.com/varkmarker")
        time.sleep(0.5)
        Colors.light_blue(" \n AUTHOR: VARKMARKER \n")
        time.sleep(0.5)

    # Invalid error message
    def case_default():
        print(
            colr().hex(
                "#00ffff",
                """\n                 (__) 
                 (oo) 
           /------\/ 
          / |    ||   
         *  /\---/\ 
            ~~   ~~""",
            ),
        )

        Colors.red("    ....Invalid option....")

    def exit_author():
        Operators.author()
        os.system("exit")


path1 = "items/icons/McMojave-cursors_theme.tar.xz"
path2 = "items/icons/Mkos-Big-Sur-icon-theme.tar.xz"
path3 = "items/usertheme/WhiteSur-Dark.tar.xz"
movepath1 = "/usr/share/icons/"
movepath2 = "/usr/share/themes/"
background_img = "items/images/background.jpg"
grub_img = "items/images/grub.png"
boot_folder = "/boot/grub/"
# Set the root directory where you want to start searching
root_dir = "/home"
for root, dirs, files in os.walk(root_dir):
    # Check if any directory contains "Pictures" in its name
    if "Pictures" in dirs:
        # Get the absolute path of the "Pictures" directory
        pictures_dir = os.path.join(root, "Pictures")
        print("Pictures directory:", pictures_dir)

    # Check if ".bashrc" or ".zshrc" files exist in the current directory
    if ".bashrc" in files:
        bashrc_path = os.path.join(root, ".bashrc")

    elif ".zshrc" in files:
        bashrc_path = os.path.join(root, ".zshrc")


class Base:
    def add_icons_dir():
        time.sleep(0.5)
        print(
            colr().hex("#0000ff", "\n[+]", rgb_mode=True),
            colr().hex("#6666ff", " Extrating McMojave-cursors\n", rgb_mode=True),
        )
        time.sleep(0.5)
        Colors.red("")
        os.system(f"tar -xvf {path1} ")
        time.sleep(0.5)
        print(
            colr().hex("#0000ff", "\n[+]", rgb_mode=True),
            colr().hex("#6666ff", " Extrating Mkos-Big-Sur-icon\n", rgb_mode=True),
        )
        time.sleep(0.5)
        Colors.red("")
        os.system(f"tar -xvf {path2}")
        time.sleep(0.5)
        print(
            colr().hex("#0000ff", "\n[+]", rgb_mode=True),
            colr().hex("#6666ff", " Extrating WhiteSur-Dark\n", rgb_mode=True),
        )
        time.sleep(0.5)
        Colors.red("")
        os.system(f"tar -xvf {path3}")
        time.sleep(0.5)
        print(
            colr().hex("#0000ff", "\n[+]", rgb_mode=True),
            colr().hex("#6666ff", " Moving Icons\n", rgb_mode=True),
        )
        time.sleep(0.5)
        Colors.red("")
        os.system(
            f" sudo mv -v McMojave-cursors Mkos-Big-Sur-Panel-white Mkos-Big-Sur Mkos-Big-Sur-Night {movepath1}"
        )
        time.sleep(0.5)
        print(
            colr().hex("#0000ff", "\n[+]", rgb_mode=True),
            colr().hex("#6666ff", " Moving UserTheme\n", rgb_mode=True),
        )
        time.sleep(0.5)
        Colors.red("")
        os.system(f"sudo mv -v WhiteSur-Dark {movepath2}")
        time.sleep(0.5)
        print(
            colr().hex("#0000ff", "\n[+]", rgb_mode=True),
            colr().hex("#6666ff", " Moving Background Images\n", rgb_mode=True),
        )
        time.sleep(0.5)
        Colors.red("")
        os.system(f" sudo cp -v {background_img} {pictures_dir}")
        time.sleep(0.5)
        print(
            colr().hex("#0000ff", "\n[+]", rgb_mode=True),
            colr().hex("#6666ff", " Moving Grub Images\n", rgb_mode=True),
        )
        time.sleep(0.5)
        Colors.red("")
        os.system(f"sudo cp -v {grub_img} {boot_folder}")
        time.sleep(0.5)
        print(
            colr().hex("#0000ff", "\n[+]", rgb_mode=True),
            colr().hex("#6666ff", " Updating grub\n", rgb_mode=True),
        )
        time.sleep(0.5)
        Colors.red("")
        os.system("update-grub")

    def add_software():

        print("sof")

    def add_update_alias():
        time.sleep(0.5)
        print(
            colr().hex("#0000ff", "\n[+]", rgb_mode=True),
            colr().hex("#6666ff", " Moving Update.py\n", rgb_mode=True),
        )
        Colors.red("")
        os.system("sudo cp -rv items/update /usr/bin/")
        time.sleep(0.5)
        print(
            colr().hex("#0000ff", "\n[+]", rgb_mode=True),
            colr().hex("#6666ff", " Adding line\n", rgb_mode=True),
        )

        one_string = "alias up='sudo /usr/bin/update/update.py'"
        second_string = "#alias up='sudo /usr/bin/update/update.py'"

        with open(bashrc_path, "r") as f:
            file_contents = f.read()

        # Check if the line is found in the file
        if second_string in file_contents:

            replace = ["alias up='sudo /usr/bin/update/update.py'"]

            with open(bashrc_path, "r") as file:
                alias_command = file.read()

                alias_command = alias_command.replace(
                    "#alias up='sudo /usr/bin/update/update.py'",
                    replace[0],
                )
            with open(bashrc_path, "w") as file:
                file.write("" + alias_command)
            time.sleep(0.5)
            Colors.blue(f"[+] Alias added to {bashrc_path}")
            print(
                colr().hex("#0000ff", "[+]"),
                colr().hex("#ff0000", "up"),
                colr().hex("#0000ff", ": is the run command"),
            )

        elif one_string in file_contents:
            time.sleep(0.5)
            Colors.blue(f"[+] Alias added to {bashrc_path}")
            print(
                colr().hex("#0000ff", "[+]"),
                colr().hex("#ff0000", "up"),
                colr().hex("#0000ff", ": is the run command"),
            )
        else:
            with open(bashrc_path, "a") as file:
                file.write(
                    "\n".join(
                        [
                            "#Customize alias",
                            "alias up='sudo /usr/bin/update/update.py'",
                        ]
                    )
                )
            time.sleep(0.5)
            Colors.blue(f"[+] Alias added to {bashrc_path}")
            print(
                colr().hex("#0000ff", "[+]"),
                colr().hex("#ff0000", "up"),
                colr().hex("#0000ff", ": is the run command"),
            )

    def all():
        # call add update alias in the .bashrc file
        Base.add_update_alias()
        # call software downloading function
        Base.add_software()

        Base.add_icons_dir
