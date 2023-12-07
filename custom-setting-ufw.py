import paramiko
import getpass

def configure_ufw(server, username, password, root_password, allowed_ips):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(server, username=username, password=password)

        

        # Allow connections from specified IP addresses
        for ip in allowed_ips:
            ufw_command = f'echo {root_password} | sudo -S ufw allow from {ip} to any port 22'
            stdin, stdout, stderr = ssh.exec_command(ufw_command)
            print(stdout.read().decode())
            print(stderr.read().decode())

        print(f"ufw configured successfully on {server} to allow connections from {', '.join(allowed_ips)}.")
    except Exception as e:
        print(f"Error configuring ufw on {server}: {e}")
    finally:
        ssh.close()

if __name__ == "__main__":
    # Get common details for all servers
    username = input("Enter the common username for all servers: ")
    password = getpass.getpass("Enter the user password: ")
    root_password = getpass.getpass("Enter the root password: ")

    # List of server IP addresses or hostnames
    servers = [
        
        # Add more servers as needed
    ]

    # List of IP addresses to allow
    allowed_ips = [
        "server1.example.com",
        "server2.example.com",
        # Add more IP addresses as needed
    ]

    # Configure ufw for each server
    for server in servers:
        configure_ufw(server, username, password, root_password, allowed_ips)
