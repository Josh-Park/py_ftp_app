# py_ftp_app

## Set-up

Fill in the fields on auth_constants.py to match the authentication required for the server you're connecting to. The constants marked with `TEST` are used for testing purposes only and do not have to be filled in.

## Build

To build the app, open a powershell window in the project root directory and type

```Powershell
py -m PyInstaller ingram_ftp_script.py -F
```

This will build an executable and place it in a dist folder in the root directory.