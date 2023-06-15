from colr import Colr as colr
import os
import time


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


class Base:
    def icons():
        time.sleep(0.5)
        print(
            colr().hex("#0000ff", "[+]", rgb_mode=True),
            colr().hex("#6666ff", "\nExtrating McMojave-cursors\n", rgb_mode=True),
        )
        time.sleep(0.5)
        os.system(f"tar -xvf {path1} ")
        time.sleep(0.5)
        print(
            colr().hex("#0000ff", "[+]", rgb_mode=True),
            colr().hex("#6666ff", "\nExtrating Mkos-Big-Sur-icon\n", rgb_mode=True),
        )
        time.sleep(0.5)
        os.system(f"tar -xvf {path2}")
        time.sleep(0.5)
        print(
            colr().hex("#0000ff", "[+]", rgb_mode=True),
            colr().hex("#6666ff", "\nExtrating WhiteSur-Dark\n", rgb_mode=True),
        )
        time.sleep(0.5)
        os.system(f"tar -xvf {path3}")
        time.sleep(0.5)
        print(
            colr().hex("#0000ff", "[+]", rgb_mode=True),
            colr().hex("#6666ff", "\nMoving Icons\n", rgb_mode=True),
        )
        time.sleep(0.5)
        os.system(
            f" sudo mv -v McMojave-cursors Mkos-Big-Sur-Panel-white Mkos-Big-Sur Mkos-Big-Sur-Night {movepath1}"
        )
        time.sleep(0.5)
        print(
            colr().hex("#0000ff", "[+]", rgb_mode=True),
            colr().hex("#6666ff", "\nMoving UserTheme\n", rgb_mode=True),
        )
        time.sleep(0.5)
        os.system(f"sudo mv -v WhiteSur-Dark {movepath2}")
        time.sleep(0.5)

    def software():
        print("software")

    def update():
        print("update")

    def all():
        print("icons")
        print("software")
        print("update")
