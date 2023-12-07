import paramiko
import getpass

def delete_ufw_rule(server, username, password, root_password, ip, port):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(server, username=username, password=password)

        # Remove ufw rule for the specified IP and port
        ufw_command = f'echo {root_password} | sudo -S ufw delete allow from {ip} to any port {port}'
        stdin, stdout, stderr = ssh.exec_command(ufw_command)
        print(stdout.read().decode())
        print(stderr.read().decode())

        print(f"ufw rule deleted successfully on {server} for IP: {ip}, Port: {port}.")
    except Exception as e:
        print(f"Error deleting ufw rule on {server}: {e}")
    finally:
        ssh.close()

if __name__ == "__main__":
    # Get common details for all servers
    username = input("Enter the common username for all servers: ")
    password = getpass.getpass("Enter the user password: ")
    root_password = getpass.getpass("Enter the root password: ")

    # List of server IP addresses or hostnames
    servers = [
        "server1.example.com",
        "server2.example.com",
        # Add more servers as needed
    ]

    # Specify IP and port to be removed
    delete_ip = input("Enter the IP address to remove: ")
    delete_port = input("Enter the port to remove: ")

    # Remove ufw rule for each server
    for server in servers:
        delete_ufw_rule(server, username, password, root_password, delete_ip, delete_port)
