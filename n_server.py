import os
from socket import *
import tqdm


class ServerProtocol:

    def __init__(self):
        self.socket = None
        self.output_dir = '.'
        self.file_num = 1

    def listen(self, server_ip, server_port):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind((server_ip, server_port))
        self.socket.listen(1)
        print(f"[+] Server initial at IP -  {server_ip}: & Port -  {server_port}")

    def handle_file_transfer(self):
        """ funtion is to handle the incoming file transfer from Client to the server ip and port"""
        BUFFER_SIZE = 4096
        SEPARATOR = "<SEPARATOR>"
        try:
            while True:
                (connection, addr) = self.socket.accept()
                # if above code is executed, that means the sender is connected
                print(f"[+] {addr} is connected.")
                try:
                    received_file = connection.recv(BUFFER_SIZE).decode()
                    filename, filesize = received_file.split(SEPARATOR)
                    # remove absolute path if there is
                    filename = os.path.basename(filename)
                    # convert to integer
                    filesize = int(filesize)
                    # start receiving the file from the socket
                    # and writing to the file stream
                    progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
                    with open('Server/' + filename, "wb") as f:
                        for _ in progress:
                            # read 1024 bytes from the socket (receive)
                            bytes_read = connection.recv(BUFFER_SIZE)
                            if not bytes_read:
                                # nothing is received
                                # file transmitting is done
                                break
                            # write to the file the bytes we just received
                            f.write(bytes_read)
                            # update the progress bar
                            progress.update(len(bytes_read))
                finally:
                    connection.shutdown(SHUT_WR)
                    connection.close()
        finally:
            self.close()

    def close(self):
        self.socket.close()
        self.socket = None


if __name__ == '__main__':
    sp = ServerProtocol()
    sp.listen('127.0.0.1', 9001)
    sp.handle_file_transfer()
    sp.close()
