# Simple Server
# An application to synchronise a source folder(client) and a destination folder (server) over IP

A simple file transfer server written in Python 3, that allows the user to download files or any changes from the Client to Server.
the server can handle and serve multiple clients at the same time and send files in the same/child directories.

## Usage
- Run the n_server.py file, entering the port you wish (currently used as localhost ip 127.0.0.1) for the server to run on 
    ```python n_server.py```

- Now, user can run the watcher with the folder passed as parameter and to monitor the folder and as soon as there is any new file added or updated, the files will be synched to the Server Folder automatically.
  ```python watcher.py Client``` where **Client** is Folder name, this can be absolute path or relative path to the **watcher.py** script.

- Change the existing txt file in ```/Client``` folder and the changes will be pushed to the ```/Server``` folder immdediately

## Requirements
- Python 3.7+
- Socket Module ( standard library )
- tqdm Module ( pip3 install tqdm  )
- watchdog Module (pip3 install watchdog )
- OS Module (standard library)
- sys Module (stadard library)

## Contributing
Since this is a simple project, this repository is unlikely to be majorily changed, however if you wish to contribute with bug fixes/new features/code improvements, pull requests are welcome. Issues are also welcome if you want to discuss or raise an issue.

## Limitations / Known Issues
- The Progress bar doesn't seems to be updating during file transfer
- The Code is tested on the same machine `localhost(127.0.0.1)` IP and static port 9001 however this can run on the Network by adapting the Server IP
- works well with different file format transfer however have not tested with large files
- Tested for single Client however should work for multiple clients similar way
- multiple threads not used

### another part of assignment 1.2 is not completed

## License
[MIT](https://choosealicense.com/licenses/mit/)
