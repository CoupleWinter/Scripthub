# coding:utf-8

import os
import subprocess
import argparse

FLAG = None
POWERSHEL_COMMAND = 'C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe'


def launch():
    try:
        subprocess.call([POWERSHEL_COMMAND, ". \"./powershell_file_name\";", "&function_name"])
        subprocess.call([POWERSHEL_COMMAND, ". \"./powershell_file_name\";", "&function_name(parameter)"])
    except Exception as e:
        raise Exception(e.message)


if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('--path', type=str, default=os.getcwd() + 'poershell_file_name')
    FLAG, unparse = parse.parse_known_args()
    launch()
