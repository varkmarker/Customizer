from colr import Colr as colr
import main

# Privileges check
if main.os.geteuid() != 0:
    main.Colors.red(" \n THIS SCRIPT REQUIRES SUDO PRIVILEGES . \n")
    exit(1)
else:

    def choice():
        main.Colors.red("\n Welcome to customize tool by varkmarker \n")
        main.Colors.sky_blue(" \n [1] Icons    [2] Update alias ")
        main.Colors.sky_blue(" [3] Basic Software [4] All")
        main.Colors.sky_blue(" [5] Exit")
        choices = input(colr().hex("#00ccff", "\n > ", rgb_mode=True))

        try:
            if choices == "1":
                main.Base.add_icons_dir()
                choice()
            elif choices == "2":
                main.Base.add_update_alias()
                choice()
            elif choices == "3":
                main.Base.Software.tools()
                choice
            elif choices == "4":
                main.Base.all()
                main.Operators.exit_author()
            elif choices == "5":
                main.Operators.exit_author()
            else:
                main.Operators.case_default()
        except ValueError:
            main.Operators.case_default()

    choice()
