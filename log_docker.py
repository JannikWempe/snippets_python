""" Writing logs from all running docker container to folder ./logs. """

import subprocess
import shlex
import os
import sys


def main():
    print("Writing all logs to ./logs...", "\n")
    cmd_text ="docker container ls"
    cmd = shlex.split(cmd_text)
    print(f"Executing command: {cmd}", "\n")

    container_ids = []
    container_names = []
    completed_process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    output = completed_process.stdout

    check_return_code(completed_process.returncode)

    print(output)

    for line in output.split('\n')[1:-1]:
        container_ids.append(line[:12])
        container_names.append(line[156:])

    output_path = './logs/'
    output_filename = '{name}.log'
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    for container_name in container_names:
        name = container_name.split('_')[1]
        cmd_text = f"docker-compose -f deployment/docker-compose.prod.yml logs {name}"
        cmd = shlex.split(cmd_text)
        completed_process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        check_return_code(completed_process.returncode)
        output = completed_process.stdout

        file = f'{output_path}{output_filename}'.format(name=name)
        with open(file, mode='w') as f:
            for line in output:
                f.write(line)

        print(f"Finished writing {file}")

def check_return_code(returncode):
    if returncode:
        print(f"Error getting Docker information. Exiting status code {returncode}.")
        sys.exit(returncode)


if __name__ == '__main__':
    main()
