#!/usr/bin/env python3
import sys
import subprocess

version = "0.1"
#umbrel
def install_umbrel():
    subprocess.run(["./install"])

def configure_umbrel():
    subprocess.run(["./configure"])

def start_umbrel():
    subprocess.run(["./start"])

def stop_umbrel():
    subprocess.run(["./stop"])

def debug_umbrel():
    subprocess.run(["../debug"])

def backup_umbrel():
    subprocess.run(["./backup/backup"])

def app_command(action=None, app_name=None):
    command = ["./app"]
    if action:
        command.append(action)
    if app_name:
        command.append(app_name)

    subprocess.run(command)

def repo_command(action=None, repo=None):
    command = ["./repo"]
    if action:
        command.append(action)
    if repo_name:
        command.append(repo_name)

    subprocess.run(command)

#umbrel-os
def change_password():
    subprocess.run("./umbrel-os/change-password")

def umbrel_details():
    subprocess.run("./umbrel-os/umbrel-details")

#print cli command options
def show_usage():
    print(f'''
        CLI (v${version}) for managing Umbrel

        Usage: umbrel <command> [<arguments>]

        Commands:
          install               Installs Umbrel
          configure             Updates the Umbrel configuration
          start                 Starts your Umbrel
          stop                  Stops your Umbrel
          debug                 Creates debug output for Umbrel
          backup                Creates baackup for Lighting wallet
          app                   Manage Umbrel apps
          repo                  Manage Umbrel repos

        Umbrel-OS compatible:
          change-password       Change Umbrel password
          details               Prints the details of your Umbrel
    ''')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_usage()
        sys.exit(1)

    command = sys.argv[1]

    if command == "install":
        install_umbrel()
    elif command == "configure":
        configure_umbrel()
    elif command == "start":
        start_umbrel()
    elif command == "stop":
        stop_umbrel()
    elif command == "debug":
        debug_umbrel()
    elif command == "backup":
        backup_umbrel()
    elif command == "app":
        app_action = sys.argv[2] if len(sys.argv) >= 3 else None
        app_name = sys.argv[3] if len(sys.argv) == 4 else None
        app_command(app_action, app_name)
    elif command == "repo":
        repo_action = sys.argv[2] if len(sys.argv) >= 3 else None
        repo_name = sys.argv[3] if len(sys.argv) == 4 else None
        repo_command(repo_action, repo_name)
    elif command == "change-password":
        change_password()
    elif command == "details":
        umbrel_details()
    else:
        show_usage()
        sys.exit(1)

    sys.exit(0)

