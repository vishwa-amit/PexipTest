''''''
import os
import tqdm
import socket


class ClientProtocol:

    def __init__(self):
         """Constructor for ClientProtocol with no arguments"""
        self.s = None

    def connect(self, server_ip, server_port):
        """function to create socket connection with provided server_ip & server_port as an arguments"""
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connect to TCP server
        print(f"[+] Connecting to {server_ip}:{server_port}")
        self.s.connect((server_ip, server_port))
        print("[+] Connected.")


    def close(self):
        #self.s.shutdown(SHUT_WR)
        self.s.close()
        self.s = None

    def send_data_to_server(self, file_to_transfer):
        """method to send the data from Client to connected servers on UP and prost specii"""
        BUFFER_SIZE = 4096
        SEPARATOR = "<SEPARATOR>"
        filesize = os.path.getsize(file_to_transfer)
        print(f"File {file_to_transfer} is getting transferred from Client to Server")
        # send the filename and filesize
        self.s.send(f"{file_to_transfer}{SEPARATOR}{filesize}".encode())
        progress = tqdm.tqdm(range(filesize), f"Sending {file_to_transfer}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(file_to_transfer, "rb") as f:
            for _ in progress:
                # read the bytes from the file
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    # file transmitting is done
                    break
                # we use sendall to assure the transmission in busy network
                self.s.sendall(bytes_read)
                # update the progress bar
                progress.update(len(bytes_read))


if __name__ == '__main__':
    # Test the Client transfer to server
    cp = ClientProtocol()
    cp.connect('127.0.0.1', 9001)
    cp.send_data_to_server('Client/data.csv')
    cp.close()
