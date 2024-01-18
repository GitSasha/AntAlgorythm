import socket
import hashfunc
import time


def file_sending():
    try:
        start_time = time.time()
        
        f = open(file, 'rb')
        send_data = ''

        while send_data != b'':
            send_data = f.read(bufsize)
            client_socket.send(send_data)
            
        end_time = time.time()
        transfer_time = end_time - start_time
        print(f"File transfer time: {transfer_time:.2f} seconds")
        
    except Exception as ex:
        print("File sending error: ", ex)
    finally:
        client_socket.close()


def file_transfer(file, host="127.0.0.1", port=2000, bufsize=1024):
    """
    Function for sending a file to the server
    :param host: Server IP address (entered from the keyboard)
    :param port: Server port for sending the file data
    :param bufsize: Size of the data buffer
    :param file: Path to the file being transmitted (client_files/...); entered from the keyboard
    :return: No return values
    """
    global client_socket
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        file_sending()
    except Exception as ex:
        print("Connection error:", ex)


if __name__ == "__main__":
    server_ip = input('Enter the server IP address:\n')
    client_file = input('Put the file in the "client_files" folder and enter the file name:\n')
    _ = input("Check if everything is set up on the server. If yes, press Enter to start data sending.")
    file_transfer(file=f'client_files/{client_file}', host=server_ip)

    # Calculate the file hash and display it
    file_hash = hashfunc.calculate_file_hash(f'client_files/{client_file}')
    print(f"File hash: {file_hash}")
