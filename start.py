from colr import Colr as colr
import main

# Privileges check
if main.os.geteuid() != 0:
    main.Colors.red(" \n THIS SCRIPT REQUIRES SUDO PRIVILEGES . \n")
    exit(1)
else:

    def choice():
        main.Colors.red("\n Welcome to customize tool by varkmarker \n")
        main.Colors.sky_blue(" \n [1] Icons                [2] Update alias ")
        main.Colors.sky_blue(" [3] Basic Software       [4] Sudo su error")
        main.Colors.sky_blue(
            " [5] icons + update alias [6] Software (eg : google chrome)"
        )
        main.Colors.sky_blue(" [7] Firmware Error       [8] Exit")
        choices = input(colr().hex("#00ccff", "\n  > ", rgb_mode=True))

        try:
            if choices == "1":
                main.Base.add_icons_dir()
                choice()
            elif choices == "2":
                main.Base.add_update_alias()
                choice()
            elif choices == "3":
                main.Base.Software.tools()
                choice()
            elif choices == "4":
                main.Base.Error.sudo_su_error()
                choice()
            elif choices == "5":
                main.Base.add_icons_update_alias()
            elif choices == "6":
                main.Base.Software.gui_software()
            elif choices == "7":
                main.Base.Error.firmware_error()
            elif choices == "8":
                main.Operators.exit_author()
            else:
                main.Operators.case_default()
        except ValueError:
            main.Operators.case_default()

    choice()
