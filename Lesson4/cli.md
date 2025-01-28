# Command Line Interface Table

|Number | Command | Description | Example |
|-------|---------|-------------|-------- |
|1|pwd|displays the path name of the current directory|`$ pwd`|
|2|dir or ls|list the files from a directory|`$ dir` or `$ ls`|
|3|mkdir  [directoryName]|Creates one or more directories/folders|`$ mkdir  Data Data1`|
|4|cd [directoryName]|goes to a directory|`$ cd Data`|
|5|touch [new-filename.extension]|Creates a file|`$ touch data.txt1`|
|6|cd ..|Used to go back to the previous directory|`$ cd ..`|
|7|mv [current-filename] [new-filename]|renames a file|`$ mv main.py  functions.py`|
|8|rm [filename]|deletes a file|`$ rm data.txt`|
|9|rmdir|deletes a directory|`$ rmdir Data1`|
|10|clear|clears the screen|`$ clear`|
|11|echo [message]|displays a message|`$ echo ‘Hello World!’`|
|12|echo [message] \| tee -a [filename.extension]|appends contents to a file|`$ echo ‘def sayHello():’ \| tee -a functions.py`|
|13|cat [filename.extension]|displays file contents|`$ cat functions.py`|
|14|mv [fileName] [directoryName]|moves file from one directory to another|`$ mv functions.py Data`|
|15|help [command name]|displays help docs for a command|`$ help echo`|
