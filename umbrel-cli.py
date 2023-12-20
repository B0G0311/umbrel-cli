#!/usr/bin/env python3
from dotenv import load_dotenv
import os
import sys
import subprocess

current_dir = os.path.dirname(os.path.realpath(__file__))
load_dotenv(os.path.join(current_dir, '.env'))

version = "0.3"
umbrel_path = os.environ.get('UMBREL_DIR')

#umbrel
def install_umbrel():
    subprocess.run(["sudo", os.path.join(umbrel_path, "scripts/install")])

def configure_umbrel():
    subprocess.run(["sudo", os.path.join(umbrel_path, "scripts/configure")])

def start_umbrel():
    subprocess.run(["sudo", os.path.join(umbrel_path, "scripts/start")])

def stop_umbrel():
    subprocess.run(["sudo", os.path.join(umbrel_path, "scripts/stop")])

def restart_umbrel():
    if stop_umbrel():
        print("Umbrel stopped successfully!")
    else:
        print("There was an error stopping Umbrel!")

    print("Attempting to start Umbrel...")
    if start_umbrel():
        print("---Success---")
    else:
        print("There was an error starting Umbrel!")

def backup_umbrel():
    subprocess.run(["sudo", os.path.join(umbrel_path, "scripts/backup/backup")])

def update_umbrel():
    subprocess.run(["sudo", os.path.join(umbrel_path, "scripts/update/update")])

def debug_umbrel():
    subprocess.run(["sudo", os.path.join(umbrel_path, "scripts/debug")])

def app_command(action=None, app_name=None):
    
    print(f"umbrel path: {umbrel_path}")
    command = ["sudo", os.path.join(umbrel_path, "scripts/app")]
    if action:
        command.append(action)
    if app_name:
        command.append(app_name)

    subprocess.run(command)

def repo_command(action=None, repo_name=None):
    umbrel_path = os.environ.get('UMBREL_DIR')
    command = ["sudo", os.path.join(umbrel_path, "scripts/repo")]
    if action:
        command.append(action)
    if repo_name:
        command.append(repo_name)

    subprocess.run(command)

#umbrel-os
def change_password():
    subprocess.run(["sudo", os.path.join(umbrel_path, "scripts/umbrel-os/change-password")])

def umbrel_details():
    subprocess.run(["sudo", os.path.join(umbrel_path, "scripts/umbrel-os/umbrel-details")])

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
          restart               Restarts your Umbrel
          backup                Creates backup for Lighting wallet
          update                Update Umbrel to latest release
          debug                 Creates debug output for Umbrel
          app                   Manage Umbrel apps
          repo                  Manage Umbrel repos
          --help                Prompt this screen again
          --version             Show version

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
    elif command == "restart":
        restart_umbrel()
    elif command == "backup":
        backup_umbrel()
    elif command == "update":
        update_umbrel()
    elif command == "debug":
        debug_umbrel()
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
    elif command == "--version":
        print(f"Umbrel-cli v{version}")
    elif command is not None or "--help":
        print(f"Unknown command: umbrel {command} /n")
        sys.exit(1)
    elif command is None or "--help":
        show_usage()
        sys.exit(1)
    else:
        print(f"Unknown command: umbrel {command} /n")
        sys.exit(1)

    sys.exit(0)

