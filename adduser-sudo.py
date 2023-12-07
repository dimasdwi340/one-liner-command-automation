import time
import paramiko
import getpass


def add_user(server, username, password, new_username, new_password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(server, username=username, password=password)

        # Add a new user using the adduser command
        adduser_command = f'echo {password} | sudo -S adduser {new_username} --gecos "" --disabled-password'
        stdin, stdout, stderr = ssh.exec_command(adduser_command)
        print(stdout.read().decode())
        print(stderr.read().decode())

        # Set the password for the new user using passwd command
        passwd_command = f'echo -e "{password}\n{new_password}\n{new_password}" | sudo -S passwd {new_username}'
        stdin, stdout, stderr = ssh.exec_command(passwd_command)
        print(stdout.read().decode())
        print(stderr.read().decode())

        # Set the user mode sudo
        usermod_command = f'echo {password} | sudo -S usermod -aG sudo {new_username}'
        stdin, stdout, stderr = ssh.exec_command(usermod_command)
        print(stdout.read().decode())
        print(stderr.read().decode())

        print(f"User {new_username} added successfully on {server}.")
    except Exception as e:
        print(f"Error adding user on {server}: {e}")
    finally:
        ssh.close()

if __name__ == "__main__":
    # Get common details for all servers
    username = input("Enter the common username for all servers: ")
    password = getpass.getpass("Enter the user password: ")

    # List of server IP addresses or hostnames
    servers = [
        "server1.example.com",
        "server2.example.com",
        # Add more servers as needed
    ]

    # Get details for the new user
    new_username = input("Enter the new username: ")
    new_password = getpass.getpass("Enter the new user password: ")

    # Add new user for each server
    for server in servers:
        add_user(server, username, password, new_username, new_password)
        time.sleep(5)
