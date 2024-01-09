import paramiko
import getpass

def configure_command(server, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(server, username=username, password=password)
        
        # Connection for execute the command with sudo
        
        command = f"echo {password} | sudo -S <write  your command here>" # write the command without <>
        stdin, stdout, stderr = ssh.exec_command(command)
        print(stdout.read().decode())
        print(stderr.read().decode())
        print(f"<the command> configured successfully on {server} ")
        
        # Connection for execute the command without sudo
        
        command = "<write  your command here>" # write the command without <>
        stdin, stdout, stderr = ssh.exec_command(command)
        print(stdout.read().decode())
        print(stderr.read().decode())
        print(f"<the command> configured successfully on {server} ")
        
    except Exception as e:
        print(f"Error configuring ufw on {server}: {e}")
    finally:
        ssh.close()

if __name__ == "__main__":
    # Get common details for all servers
    username = input("Enter the common username for all servers: ")
    password = getpass.getpass("Enter the user password: ")
    

    # List of server IP addresses or hostnames
    servers = [
        #"server1.example.com",
        #"server2.example.com",
        # Add more servers as needed
    ]

    # Configure ufw for each server
    for server in servers:
        configure_command(server, username, password)
