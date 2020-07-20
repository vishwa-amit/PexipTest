
import time
import sys
import n_client
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Class to utilize the watchdog libraries.
class Watcher:

    def __init__(self):
        self.observer = Observer()

    def run(self, dir_to_watch):
        event_handler = Handler()
        self.observer.schedule(event_handler, dir_to_watch, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error occurred during watching any changes to the folder or program cancelled....")
        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'modified':
            # Take any action here when a file is first created.
            print("Received modified event - %s." % event.src_path)
            # create a client instance to bind with server  cp = ClientProtocol()
            fcp = n_client.ClientProtocol()
            fcp.connect('127.0.0.1', 9001)
            fcp.send_data_to_server(event.src_path)
            fcp.close()

        elif event.event_type == 'created':
            # Taken any action here when a file is modified.
            print("Received created event - %s." % event.src_path)
            # create a client instance to bind with server  cp = ClientProtocol()
            fcp = n_client.ClientProtocol()
            fcp.connect('127.0.0.1', 9001)
            fcp.send_data_to_server(event.src_path)
            fcp.close()


if __name__ == '__main__':

    # Take the argument as directory
    args = sys.argv[1]
    print(args)
    watcher = Watcher()
    watcher.run(args)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        watcher.stop()

    watcher.join()

