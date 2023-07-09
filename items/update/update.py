#! /usr/bin/python3
from colr import Colr as colr
import os


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


# Privileges check
if os.geteuid() != 0:
    Colors.red(" \n THIS SCRIPT REQUIRES SUDO PRIVILEGES . \n")
    exit(1)
else:
    Colors.orange("\n UPDATE AND UPGRADE = y")
    Colors.orange("\n UPGRADE = n")
    Colors.orange("\n EXIT = e")
    choice = input(colr().hex("#ff8e35", "\n > ", rgb_mode=True))
    choice = choice.lower()
    if choice == "y":

        def update():
            Colors.blue("\n  [+] UPDATE STARTED")
            Colors.red("")
            os.system("sudo apt-get update")
            Colors.blue("\n  [+] UPDATE FINISHED")

        update()
        choice = input(
            colr().hex("#0000ff", "\n If you want upgrade y or n : ", rgb_mode=True)
        )
        choice = choice.lower()
        if choice == "y":

            def upgrade():
                Colors.blue("\n    [+] UPGRADE STARTED")
                Colors.red("")
                os.system("sudo apt-get full-upgrade")
                Colors.blue("\n    [+] UPGRADE FINISHED")

            upgrade()
        else:
            Colors.red("\n YOUR SYSTEM IS NOT UPGRADE \n")

    elif choice == "n":

        def upgrade():
            Colors.blue("\n  [+] UPGRADE STARTED")
            Colors.red("")
            os.system("sudo apt-get full-upgrade")
            Colors.blue("\n  [+] UPGRADE FINISHED")

        upgrade()
    elif choice == "e":
        Colors.red(" \n Exited \n")
    else:
        Colors.red(" \n You press the wrong key \n")
