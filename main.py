from colr import Colr as colr
import os
from time import sleep
import shutil


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
        sleep(0.5)
        Colors.red("\n You are exited \n")

    # Author information
    def author():
        Colors.sky_blue("\n                     AUTHOR")
        sleep(0.5)
        Colors.orange(
            " \n If this script saves you time. You can give a star on GitHub"
        )
        Colors.orange(
            f" \n If you have any suggestions about this tool you can contact me on Twitter."
        )
        sleep(0.5)
        Colors.orange(" \n Twitter link: https://twitter.com/varkmarker")
        sleep(0.5)
        Colors.light_blue(" \n AUTHOR: VARKMARKER \n")
        sleep(0.5)

    # Invalid error message
    def case_default():
        print(
            colr().hex(
                "#00ffff",
                """\n                 (__)
                 (oo)
           /------\/
          / |    ||
         *  /\---/\ \n            ~~   ~~   """,
            ),
        )

        Colors.red("    ....Invalid option....")

    def exit_author():
        Operators.author()
        os.system("exit")


path1 = "items/icons/McMojave-cursors_theme.tar.xz"
path2 = "items/icons/Mkos-Big-Sur-icon-theme.tar.xz"
path3 = "items/usertheme/WhiteSur-Dark.tar.xz"
app_icons = "items/icons/app_icons"
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


class Base:
    def add_icons_dir():
        sleep(0.5)
        print(
            colr().hex("#0000ff", "\n[+]", rgb_mode=True),
            colr().hex("#6666ff", " Extrating McMojave-cursors\n", rgb_mode=True),
        )
        sleep(0.5)
        Colors.red("")
        os.system(f"tar -xvf {path1} ")
        sleep(0.5)
        print(
            colr().hex("#0000ff", "\n[+]", rgb_mode=True),
            colr().hex("#6666ff", " Extrating Mkos-Big-Sur-icon\n", rgb_mode=True),
        )
        sleep(0.5)
        Colors.red("")
        os.system(f"tar -xvf {path2}")
        sleep(0.5)
        print(
            colr().hex("#0000ff", "\n[+]", rgb_mode=True),
            colr().hex("#6666ff", " Extrating WhiteSur-Dark\n", rgb_mode=True),
        )
        sleep(0.5)
        Colors.red("")
        os.system(f"tar -xvf {path3}")
        sleep(0.5)
        print(
            colr().hex("#0000ff", "\n[+]", rgb_mode=True),
            colr().hex("#6666ff", " Moving Icons\n", rgb_mode=True),
        )
        sleep(0.5)
        Colors.red("")
        os.system(f" sudo mv -v McMojave-cursors Mkos-Big-Sur* {movepath1}")
        sleep(0.5)
        print(
            colr().hex("#0000ff", "\n[+]", rgb_mode=True),
            colr().hex("#6666ff", " Moving UserTheme\n", rgb_mode=True),
        )
        sleep(0.5)
        Colors.red("")
        os.system(f"sudo mv -v WhiteSur-Dark {movepath2}")
        sleep(0.5)
        print(
            colr().hex("#0000ff", "\n[+]", rgb_mode=True),
            colr().hex("#6666ff", " Moving Background Images\n", rgb_mode=True),
        )
        sleep(0.5)
        Colors.red("")
        os.system(f" sudo cp -v {background_img} {pictures_dir}")
        sleep(0.5)
        print(
            colr().hex("#0000ff", "\n[+]", rgb_mode=True),
            colr().hex("#6666ff", " Moving Additional Icons\n", rgb_mode=True),
        )
        Colors.red("")
        os.system(f"sudo cp -rv {app_icons} /usr/share/")
        sleep(0.5)

    # def add_grub_image()
    #     sleep(0.5)
    #     print(
    #         colr().hex("#0000ff", "\n[+]", rgb_mode=True),
    #         colr().hex("#6666ff", " Moving Grub Images\n", rgb_mode=True),
    #     )
    #     sleep(0.5)
    #     Colors.red("")
    #     os.system(f"sudo cp -v {grub_img} {boot_folder}")
    #     sleep(0.5)
    #     print(
    #         colr().hex("#0000ff", "\n[+]", rgb_mode=True),
    #         colr().hex("#6666ff", " Updating grub\n", rgb_mode=True),
    #     )
    #     sleep(0.5)
    #     Colors.red("")
    #     os.system("update-grub")

    def add_update_alias():
        def add_alias():
            choice = input(
                colr().hex(
                    "#0000ff",
                    "\n[+] If you running this script in parrot os = p or kali linux = k or other = n : ",
                    rgb_mode=True,
                )
            )
            choice = choice.lower()
            if choice == "p":
                # Set the root directory where you want to start searching
                root_dir = "/home"
                for root, dirs, files in os.walk(root_dir):
                    # Check if ".bashrc"  files exist in the current directory
                    if ".bashrc" in files:
                        bashrc_path = os.path.join(root, ".bashrc")

                print(
                    colr().hex(
                        "#0000ff",
                        "\n [+] Enter your home directory path.Use the",
                        rgb_mode=True,
                    ),
                    colr().hex("#ff0000", "pwd", rgb_mode=True),
                    colr().hex("#0000ff", "command to seeit \n [+] Eg: /home/user/"),
                )
                home_path = input(colr().hex("#0000ff", "\n  > ", rgb_mode=True))
                # Checking the .bashrc file exists or not
                if os.path.exists(home_path + ".bashrc"):
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
                        sleep(0.5)
                        Colors.blue(f"\n[+] Alias added to {bashrc_path}")
                        print(
                            colr().hex("#0000ff", "[+]"),
                            colr().hex("#ff0000", "up"),
                            colr().hex(
                                "#0000ff", ": is the command for run the script"
                            ),
                        )

                    elif one_string in file_contents:
                        sleep(0.5)
                        Colors.blue(f"\n[+] Alias added to {bashrc_path}")
                        print(
                            colr().hex("#0000ff", "[+]"),
                            colr().hex("#ff0000", "up"),
                            colr().hex(
                                "#0000ff", ": is the command for run the script"
                            ),
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
                        sleep(0.5)
                        Colors.blue(f"\n[+] Alias added to {bashrc_path}")
                        print(
                            colr().hex("#0000ff", "[+]"),
                            colr().hex("#ff0000", "up"),
                            colr().hex(
                                "#0000ff", ": is the command for run the script"
                            ),
                        )
                else:
                    Colors.red("")
                    os.system(f"sudo cp -v /root/.bashrc {home_path}")
                    bashrc_path = home_path + ".bashrc"
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
                        sleep(0.5)
                        Colors.blue(f"\n[+] Alias added to {bashrc_path}")
                        print(
                            colr().hex("#0000ff", "[+]"),
                            colr().hex("#ff0000", "up"),
                            colr().hex(
                                "#0000ff", ": is the command for run the script"
                            ),
                        )

                    elif one_string in file_contents:
                        sleep(0.5)
                        Colors.blue(f"\n[+] Alias added to {bashrc_path}")
                        print(
                            colr().hex("#0000ff", "[+]"),
                            colr().hex("#ff0000", "up"),
                            colr().hex(
                                "#0000ff", ": is the command for run the script"
                            ),
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
                        sleep(0.5)
                        Colors.blue(f"\n[+] Alias added to {bashrc_path}")
                        print(
                            colr().hex("#0000ff", "[+]"),
                            colr().hex("#ff0000", "up"),
                            colr().hex(
                                "#0000ff", ": is the command for run the script"
                            ),
                        )
            elif choice == "k":
                # Set the root directory where you want to start searching
                root_dir = "/home"
                for root, dirs, files in os.walk(root_dir):
                    # Check if ".bashrc"  files exist in the current directory
                    if ".zshrc" in files:
                        zshrc_path = os.path.join(root, ".zshrc")
                one_string = "alias up='sudo /usr/bin/update/update.py'"
                second_string = "#alias up='sudo /usr/bin/update/update.py'"

                with open(zshrc_path, "r") as f:
                    file_contents = f.read()

                # Check if the line is found in the file
                if second_string in file_contents:
                    replace = ["alias up='sudo /usr/bin/update/update.py'"]

                    with open(zshrc_path, "r") as file:
                        alias_command = file.read()

                        alias_command = alias_command.replace(
                            "#alias up='sudo /usr/bin/update/update.py'",
                            replace[0],
                        )
                    with open(zshrc_path, "w") as file:
                        file.write("" + alias_command)
                    sleep(0.5)
                    Colors.blue(f"\n[+] Alias added to {zshrc_path}")
                    print(
                        colr().hex("#0000ff", "[+]"),
                        colr().hex("#ff0000", "up"),
                        colr().hex("#0000ff", ": is the command for run the script"),
                    )

                elif one_string in file_contents:
                    sleep(0.5)
                    Colors.blue(f"\n[+] Alias added to {zshrc_path}")
                    print(
                        colr().hex("#0000ff", "[+]"),
                        colr().hex("#ff0000", "up"),
                        colr().hex("#0000ff", ": is the command for run the script"),
                    )
                else:
                    with open(zshrc_path, "a") as file:
                        file.write(
                            "\n".join(
                                [
                                    "#Customize alias",
                                    "alias up='sudo /usr/bin/update/update.py'",
                                ]
                            )
                        )
                    sleep(0.5)
                    Colors.blue(f"\n[+] Alias added to {zshrc_path}")
                    print(
                        colr().hex("#0000ff", "[+]"),
                        colr().hex("#ff0000", "up"),
                        colr().hex("#0000ff", ": is the command for run the script"),
                    )

            elif choice == "n":
                # Set the root directory where you want to start searching
                root_dir = "/home"
                for root, dirs, files in os.walk(root_dir):
                    # Check if ".bashrc" or ".zshrc" files exist in the current directory
                    if ".bashrc" in files:
                        bashrc_path = os.path.join(root, ".bashrc")
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
                    sleep(0.5)
                    Colors.blue(f"[+] Alias added to {bashrc_path}")
                    print(
                        colr().hex("#0000ff", "[+]"),
                        colr().hex("#ff0000", "up"),
                        colr().hex("#0000ff", ": is the command for run the script"),
                    )

                elif one_string in file_contents:
                    sleep(0.5)
                    Colors.blue(f"[+] Alias added to {bashrc_path}")
                    print(
                        colr().hex("#0000ff", "[+]"),
                        colr().hex("#ff0000", "up"),
                        colr().hex("#0000ff", ": is the command for run the script"),
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
                    sleep(0.5)
                    Colors.blue(f"[+] Alias added to {bashrc_path}")
                    print(
                        colr().hex("#0000ff", "[+]"),
                        colr().hex("#ff0000", "up"),
                        colr().hex("#0000ff", ": is the command for run the script"),
                    )
            else:
                Operators.case_default()

        sleep(0.5)
        update_dir = "/usr/bin/update"
        # checking the update directory exist or not
        if os.path.exists(update_dir) and os.path.isdir(update_dir):
            # calling the alias adding function
            add_alias()
        else:
            print(
                colr().hex("#0000ff", "\n[+]", rgb_mode=True),
                colr().hex("#6666ff", " Moving Update.py\n", rgb_mode=True),
            )
            Colors.red("")
            os.system("sudo cp -rv items/update /usr/bin/")
            sleep(0.5)
            print(
                colr().hex("#0000ff", "\n[+]", rgb_mode=True),
                colr().hex("#6666ff", " Adding line\n", rgb_mode=True),
            )
            # calling the alias adding function
            add_alias()

    class Software:
        def tools():
            sleep(0.5)
            Colors.blue(f"\n[+] Installing basic ")
            # Updating , upgrading the system and installing some software
            Colors.red("")
            os.system(
                "sudo apt-get update -y && sudo apt-get full-upgrade && sudo apt-get install -y tlp timeshift ftp vlc filezilla neofetch htop net-tools wireless-tools thunderbird nano vim flatpak build-essential cmake p7zip p7zip-full unrar-free unzip"
            )
            Colors.blue("\n[+] Installation completed")

        def gui_software():
            gc_url = "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
            vs_url = "https://az764295.vo.msecnd.net/stable/74f6148eb9ea00507ec113ec51c489d6ffb4b771/code_1.80.1-1689183569_amd64.deb"
            Colors.sky_blue("\n  SOFTWARE INSTALLATION\n")
            Colors.blue("  [1] Chrome  [2] vscode")
            choice = input(colr().hex("#0000ff", "\n   >", rgb_mode=True))
            choice = choice.lower()
            if choice == "1":
                sleep(0.5)
                Colors.blue(" \n[+] INSTALLING GOOGLE_CHROME")
                Colors.red("")
                os.system(f"sudo wget -O google_chrome.deb {gc_url}")
                # get the absolute path of the google_chrome.deb file
                # gc_path = os.path.abspath("google_chrome.deb")
                os.system(f"sudo apt-get install ./google_chrome.deb")
            elif choice == "2":
                sleep(0.5)
                Colors.blue(" \n[+] INSTALLING VSCODE")
                Colors.red("")
                os.system(f" sudo wget -O vscode.deb {vs_url}")
                # get the absolute path of the vscode.deb file
                # vc_path = os.path.abspath("vscode.deb")
                os.system(f"sudo apt-get install ./vscode.deb")
            else:
                Operators.case_default()

    class Error:
        def sudo_su_error():
            def sudo_su_solution():
                sleep(0.5)
                print("\n")
                username = input(
                    colr().hex(
                        "#0000ff",
                        "Enter your user name you want to add the sudo permission : ",
                        rgb_mode=True,
                    )
                )
                sleep(0.5)
                os.system(f"sudo usermod -a -G sudo {username} ")
                sleep(0.5)
                Colors.sky_blue("\n                       User Result\n")
                os.system(f"groups {username} ")
                print(
                    colr().hex(
                        "#0000ff",
                        "# Check the user result in the above that contain sudo word \n# If in there try",
                        rgb_mode=True,
                    ),
                    colr().hex("#ff0000", "sudo su", rgb_mode=True),
                    colr().hex(
                        "#0000ff", "\n# if you get any error from the", rgb_mode=True
                    ),
                    colr().hex("#ff0000", "sudo su", rgb_mode=True),
                    colr().hex(
                        "#0000ff",
                        "command reboot or restart your system then try it \n# It will work ",
                        rgb_mode=True,
                    ),
                )

            sleep(0.5)
            Colors.blue("\n[+] sudo su error solutions")
            Colors.red(
                "Error: \n\n   # <your username> is not in the sudoers file.This incident will be reported\n"
            )
            choice = input(
                colr().hex("#0000ff", "If the same error y or n : ", rgb_mode=True)
            )
            choice = choice.lower()
            if choice == "y" or choice == "yes":
                sudo_su_solution()
            elif choice == "n" or choice == "no":
                Colors.blue("\nOk do it later")

        def firmware_error():
            def search_and_copy_missing_files(
                source_dir, destination_dir, files_to_search
            ):
                sleep(0.5)
                Colors.blue(
                    "\n [+] Search the file that exist or not to the /usr/lib/firmware/i915 folder. "
                )
                missing_files = []
                for file_name in files_to_search:
                    destination_path = os.path.join(destination_dir, file_name)
                    if not os.path.exists(destination_path):
                        missing_files.append(file_name)

                if not missing_files:
                    Colors.sky_blue(
                        f"\n [+] All files already exist in the {destination_dir}."
                    )
                    sleep(0.5)
                    Colors.sky_blue("\n [+] Updating Initramfs")
                    Colors.red("")
                    os.system("sudo update-initramfs -c -k all ")

                else:
                    for file_name in missing_files:
                        copy_missing_file(source_dir, destination_dir, file_name)
                    sleep(0.5)
                    Colors.sky_blue("\n [+] Updating Initramfs")
                    Colors.red("")
                    os.system("sudo update-initramfs -c -k all ")

            def copy_missing_file(source_dir, destination_dir, file_name):
                source_path = os.path.join(source_dir, file_name)
                destination_path = os.path.join(destination_dir, file_name)

                if not os.path.exists(destination_path):
                    shutil.copy(source_path, destination_dir)
                    Colors.red(
                        f"\n [+] Copied {file_name} from {source_dir} to {destination_dir}"
                    )

            # search the files if it already download in the items/firmware folder
            def search_files():
                sleep(0.5)
                Colors.blue(
                    "\n [+] Search the file that Download or not to the items/firmware folder. "
                )
                checking_dir = "items/firmware"
                source_directory = "items/firmware"
                destination_directory = "/usr/lib/firmware/i915"
                files_to_search = [
                    "adlp_dmc.bin",
                    "adlp_dmc_ver2_09.bin",
                    "adlp_dmc_ver2_10.bin",
                    "adlp_dmc_ver2_12.bin",
                    "adlp_dmc_ver2_14.bin",
                    "adlp_dmc_ver2_16.bin",
                    "adlp_guc_62.0.3.bin",
                    "adlp_guc_69.0.3.bin",
                    "adlp_guc_70.1.1.bin",
                    "adlp_guc_70.bin",
                    "adls_dmc_ver2_01.bin",
                    "bxt_dmc_ver1_07.bin",
                    "bxt_guc_32.0.3.bin",
                    "bxt_guc_33.0.0.bin",
                    "bxt_guc_49.0.1.bin",
                    "bxt_guc_62.0.0.bin",
                    "bxt_guc_69.0.3.bin",
                    "bxt_guc_70.1.1.bin",
                    "bxt_guc_ver8_7.bin",
                    "bxt_guc_ver9_29.bin",
                    "bxt_huc_2.0.0.bin",
                    "bxt_huc_ver01_07_1398.bin",
                    "bxt_huc_ver01_8_2893.bin",
                    "cml_guc_33.0.0.bin",
                    "cml_guc_49.0.1.bin",
                    "cml_guc_62.0.0.bin",
                    "cml_guc_69.0.3.bin",
                    "cml_guc_70.1.1.bin",
                    "cml_huc_4.0.0.bin",
                    "cnl_dmc_ver1_06.bin",
                    "cnl_dmc_ver1_07.bin",
                    "dg1_dmc_ver2_02.bin",
                    "dg1_guc_49.0.1.bin",
                    "dg1_guc_62.0.0.bin",
                    "dg1_guc_69.0.3.bin",
                    "dg1_guc_70.1.1.bin",
                    "dg1_guc_70.bin",
                    "dg1_huc_7.7.1.bin",
                    "dg1_huc_7.9.3.bin",
                    "dg1_huc.bin",
                    "dg2_dmc_ver2_06.bin",
                    "dg2_dmc_ver2_07.bin",
                    "dg2_dmc_ver2_08.bin",
                    "dg2_guc_70.1.2.bin",
                    "dg2_guc_70.4.1.bin",
                    "dg2_guc_70.bin",
                    "dg2_huc_gsc.bin",
                    "ehl_guc_33.0.4.bin",
                    "ehl_guc_49.0.1.bin",
                    "ehl_guc_62.0.0.bin",
                    "ehl_guc_69.0.3.bin",
                    "ehl_guc_70.1.1.bin",
                    "ehl_huc_9.0.0.bin",
                    "glk_dmc_ver1_04.bin",
                    "glk_guc_32.0.3.bin",
                    "glk_guc_33.0.0.bin",
                    "glk_guc_49.0.1.bin",
                    "glk_guc_62.0.0.bin",
                    "glk_guc_69.0.3.bin",
                    "glk_guc_70.1.1.bin",
                    "glk_huc_4.0.0.bin",
                    "glk_huc_ver03_01_2893.bin",
                    "icl_dmc_ver1_07.bin",
                    "icl_dmc_ver1_09.bin",
                    "icl_guc_32.0.3.bin",
                    "icl_guc_33.0.0.bin",
                    "icl_guc_49.0.1.bin",
                    "icl_guc_62.0.0.bin",
                    "icl_guc_69.0.3.bin",
                    "icl_guc_70.1.1.bin",
                    "icl_huc_9.0.0.bin",
                    "icl_huc_ver8_4_3238.bin",
                    "kbl_dmc_ver1_01.bin",
                    "kbl_dmc_ver1_04.bin",
                    "kbl_guc_32.0.3.bin",
                    "kbl_guc_33.0.0.bin",
                    "kbl_guc_49.0.1.bin",
                    "kbl_guc_62.0.0.bin",
                    "kbl_guc_69.0.3.bin",
                    "kbl_guc_70.1.1.bin",
                    "kbl_guc_ver9_14.bin",
                    "kbl_guc_ver9_39.bin",
                    "kbl_huc_4.0.0.bin",
                    "kbl_huc_ver02_00_1810.bin",
                    "mtl_dmc.bin",
                    "mtl_dmc_ver2_10.bin",
                    "mtl_guc_70.bin",
                    "mtl_huc_gsc.bin",
                    "rkl_dmc_ver2_02.bin",
                    "rkl_dmc_ver2_03.bin",
                    "skl_dmc_ver1_23.bin",
                    "skl_dmc_ver1_26.bin",
                    "skl_dmc_ver1_27.bin",
                    "skl_guc_32.0.3.bin",
                    "skl_guc_33.0.0.bin",
                    "skl_guc_49.0.1.bin",
                    "skl_guc_62.0.0.bin",
                    "skl_guc_69.0.3.bin",
                    "skl_guc_70.1.1.bin",
                    "skl_guc_ver1.bin",
                    "skl_guc_ver4.bin",
                    "skl_guc_ver6_1.bin",
                    "skl_guc_ver9_33.bin",
                    "skl_huc_2.0.0.bin",
                    "skl_huc_ver01_07_1398.bin",
                    "tgl_dmc_ver2_04.bin",
                    "tgl_dmc_ver2_06.bin",
                    "tgl_dmc_ver2_08.bin",
                    "tgl_dmc_ver2_12.bin",
                    "tgl_guc_35.2.0.bin",
                    "tgl_guc_49.0.1.bin",
                    "tgl_guc_62.0.0.bin",
                    "tgl_guc_69.0.3.bin",
                    "tgl_guc_70.1.1.bin",
                    "tgl_guc_70.bin",
                    "tgl_huc_7.0.12.bin",
                    "tgl_huc_7.0.3.bin",
                    "tgl_huc_7.5.0.bin",
                    "tgl_huc_7.9.3.bin",
                    "tgl_huc.bin",
                ]

                missing_files = []
                for file_name in files_to_search:
                    destination_path = os.path.join(checking_dir, file_name)
                    if not os.path.exists(destination_path):
                        missing_files.append(file_name)

                if not missing_files:
                    sleep(0.5)
                    Colors.sky_blue(
                        f"\n [+] All files already exist in the {checking_dir}."
                    )
                    sleep(0.5)
                    Colors.red("")
                    search_and_copy_missing_files(
                        source_directory, destination_directory, files_to_search
                    )
                else:
                    sleep(0.5)
                    Colors.blue(
                        "\n [+] Downloading the firmware i915 to items/firmware"
                    )
                    sleep(0.5)
                    Colors.red("")
                    os.system(
                        "wget -r -nd -e robots=no -A '*.bin' --accept-regex '/plain/' -P items/firmware https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/tree/i915/"
                    )
                    Colors.red("")
                    search_and_copy_missing_files(
                        source_directory, destination_directory, files_to_search
                    )

            search_files()

    def add_icons_update_alias():
        # call add icons to themes and icons folder
        Base.add_icons_dir()

        # call add update alias in the .bashrc or .zshrc file
        Base.add_update_alias()
