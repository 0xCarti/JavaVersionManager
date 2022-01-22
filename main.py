import os, ctypes, sys


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def check_version(version):
    for versions in version_directories:
        if str(version).isdigit():
            if version in versions:
                return versions
        if versions == version:
            return versions
    return 'error'


if is_admin():
    java_install_directory = 'C:\\Program Files\\Java\\'

    if len(sys.argv) > 1:
        java_install_directory = sys.argv[1]

    version_directories = []
    for directory in os.listdir(java_install_directory):
        if 'jdk' in directory:
            version_directories.append(directory)
            print(f'Version Discovered: {directory}')

    while True:
        version = input("\nPlease select a version to use: ")
        version = check_version(version)
        if version == 'error':
            print('ERROR: Version not found. Please select an installed version.')
        else:
            print(f'Selected version: {version}')
            break

    path = java_install_directory + version + '\\bin;'
    master_path = path + os.getenv('Path').replace(path, '')
    os.system(f'setx PATH "{master_path}" /M')
    print('Successfully set path variable.')
    input('Press ENTER to exit')
else:
    ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, " ".join(sys.argv), None, 1)
