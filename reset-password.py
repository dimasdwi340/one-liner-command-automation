import paramiko
import getpass

def change_password(server, username, old_password, new_password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(server, username=username, password=old_password)

        # Change the password using the 'passwd' command
        stdin, stdout, stderr = ssh.exec_command(f'echo -e "{old_password}\n{new_password}\n{new_password}" | passwd')

        # Print the output and errors (if any)
        print(f"Server: {server}")
        print(stdout.read().decode())
        print(stderr.read().decode())
        print("Password changed successfully.")
    except Exception as e:
        print(f"Error changing password on {server}: {e}")
    finally:
        ssh.close()

if __name__ == "__main__":
    # Get common details for all servers
    username = input("Enter the common username for all servers: ")
    old_password = getpass.getpass("Enter the old password: ")
    new_password = getpass.getpass("Enter the new password: ")

    # List of server IP addresses or hostnames
    servers = [
        "server1.example.com",
        "server2.example.com",
        # Add more servers as needed
    ]

    # Change password for each server
    for server in servers:
        change_password(server, username, old_password, new_password)
