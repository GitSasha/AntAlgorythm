import socket
import hashfunc
import time


def get_local_ip():
    global s
    try:
        # Create a temporary connection to a remote host
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))  # Use the Google DNS server and port 80
        ip_address = s.getsockname()[0]
    except socket.error:
        ip_address = input('Enter a server IP\n')
    finally:
        s.close()

    return ip_address


def file_receiving():
    try:
        start_time = time.time()  # Record the start time of file transfer

        f = open(file, 'wb')

        while True:
            received_data = client_socket.recv(bufsize)
            if not received_data:
                break
            f.write(received_data)

        end_time = time.time()  # Record the end time of file transfer

        print('Check a new file in the "server_files" folder')

        # Calculate the file transfer time and display it on the screen
        transfer_time = end_time - start_time
        print(f"File transfer time: {transfer_time:.2f} seconds")

    except Exception as ex:
        print("File receiving error: ", ex)
    finally:
        client_socket.close()
        listening_socket.close()


def file_transfer(file, host=get_local_ip(), port=2000, bufsize=1024):
    global client_socket

    listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listening_socket.bind((host, port))
    listening_socket.listen()

    try:
        client_socket, addr = listening_socket.accept()
        print("Connected by", addr)
        file_receiving()
    except Exception as ex:
        print("Connection error: ", ex)


if __name__ == "__main__":
    print(f'Your local IP address is {get_local_ip()}. It is important information for the sender.\n')
    server_file = input('A new file from a sender is coming! Save it with the name... (write it with extension)\n')
    print("Waiting for data sending...")
    file_transfer(f'server_files/{server_file}')

    # Calculate the file hash and display it
    file_hash = hashfunc.calculate_file_hash(f'server_files/{server_file}')
    print(f"File hash: {file_hash}")
