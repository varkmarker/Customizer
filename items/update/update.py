#! /usr/bin/python3
import os
from colr import Colr as colr


# Color's functions
class Colors:
    def red(data):
        print(colr().hex("#ff0000", data, rgb_mode=True))

    def light_green(data):
        print(colr().hex("#21ff00", data, rgb_mode=True))

    def orange(data):
        print(colr().hex("#ff8e35", data, rgb_mode=True))

    def cream(data):
        print(colr().hex("#ff9999", data, rgb_mode=True))

    def light_blue(data):
        print(colr().hex("#6666ff", data, rgb_mode=True))


def exit_line():
    print(
        colr().hex("#ff0000", "\n\n YOU ARE EXITING FROM OUR PROGRAM  ", rgb_mode=True),
        colr().hex("#ff8e35", "(^-^)\n\n", rgb_mode=True),
    )


def update():
    Colors.orange("\n           UPDATE STARTED")
    Colors.light_green("")
    os.system("sudo apt-get update")
    Colors.orange("\n           UPDATE FINISHED")


def upgrade():
    Colors.orange("\n           UPGRADE STARTED")
    Colors.light_green("")
    os.system(
        "sudo apt-get full-upgrade && sudo apt-get autoremove -y && sudo apt-get clean -y && sudo apt-get remove -y"
    )
    Colors.red(
        "\n\n IF YOU ABORT UPGRADING STEP \n YOU MUST UPGRADE SOMETIME LATER \n OTHERWISE YOUR SYSTEM WILL SLOW AND ALSO SOME LAG\n"
    )


def upgrade_q():
    choice = input(
        colr().hex("#ff8e35", "\n If you want upgrade y or n : ", rgb_mode=True)
    )
    choice = choice.lower()
    if choice == "y":
        upgrade()
    elif choice == "n":
        Colors.red("\n YOUR SYSTEM IS NOT UPGRADE")
    else:
        Colors.red(" \n YOU PRESS THE WRONG KEY ")
        print(
            colr().hex("#ff0000", " INVALID KEY :", rgb_mode=True),
            colr().hex("#6666ff", choice, rgb_mode=True),
        )
        upgrade_q()


def restart():
    Colors.orange(
        "\n Check Any software is open or note Your are go to the restart your computer "
    )
    choice = input(
        colr().hex("#ff8e35", "\n If you want restart y or n : ", rgb_mode=True)
    )
    choice = choice.lower()
    if choice == "y":
        os.system("reboot")
    elif choice == "n":
        Colors.red(
            "\n You system is not restart you need to restart after some time for better performance"
        )
        exit_line()
    else:
        Colors.red(" \n YOU PRESS THE WRONG KEY ")
        print(
            colr().hex("#ff0000", " INVALID KEY :", rgb_mode=True),
            colr().hex("#6666ff", choice, rgb_mode=True),
        )
        restart()


def upgrade_choice_reboot_q():
    choice = input(
        colr().hex("#ff8e35", "\n If you want upgrade y or n : ", rgb_mode=True)
    )
    choice = choice.lower()
    if choice == "y":
        upgrade()
        restart()
    elif choice == "n":
        Colors.red("\n YOUR SYSTEM IS NOT UPGRADE")
        exit_line()
    else:
        Colors.red(" \n YOU PRESS THE WRONG KEY ")
        print(
            colr().hex("#ff0000", " INVALID KEY :", rgb_mode=True),
            colr().hex("#6666ff", choice, rgb_mode=True),
        )
        upgrade_choice_reboot_q()


if os.geteuid() != 0:
    exit(
        colr().hex(
            "#ff0000",
            "\n You need to have root privileges to run this script.\n Please try again, this time using 'sudo'. Exiting.",
            rgb_mode=True,
        )
    )
# Main menu

Colors.cream("\n	 CMD SYSTEM UPDATER")
Colors.orange("\n UPDATE = y")
Colors.orange(" UPGRADE = n")
Colors.orange("\n UPDATE AND UPGRADE = yn")
Colors.orange(" UPGRADE AND RESTART = nr")
Colors.orange("\n UPDATE AND UPGRADE AND RESTART = ynr")
Colors.red(" EXIT = e")
try:
    choice = input(colr().hex("#ff8e35", "\n UPDATE OR UPGRADE $  ", rgb_mode=True))
    choice = choice.lower()
    if choice == "y":
        update()
        exit_line()
    elif choice == "n":
        upgrade_q()
        exit_line()
    elif choice == "nr":
        upgrade_choice_reboot_q()
    elif choice == "yn":
        update()

        upgrade_q()
        exit_line()
    elif choice == "ynr":
        update()
        upgrade_choice_reboot_q()

    elif choice == "e":
        exit_line()
        exit()
    else:
        Colors.red(" \n YOU PRESS THE WRONG KEY ")
        print(
            colr().hex("#ff0000", " INVALID KEY :", rgb_mode=True),
            colr().hex("#6666ff", choice, rgb_mode=True),
        )
except KeyboardInterrupt:
    Colors.red("\n\n .......Keyboard Interrupted.....\n\n")
