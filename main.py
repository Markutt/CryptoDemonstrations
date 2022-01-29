import sys
import platform
from subprocess import Popen


def main():
    names = 'Alice', 'Bob'
    if platform.system() == "Windows":
        new_window_command = "cmd.exe /c start".split()
    else:
        new_window_command = "x-terminal-emulator -e".split()

    # open new consoles, display messages
    echo = [sys.executable, "-c",
            "import sys; print(sys.argv[1]);exec(open(sys.argv[2]).read());"]
    processes = [Popen(new_window_command + echo + ["Middleman", "middleman.py"])]
    processes.extend([Popen(new_window_command + echo + [name, "client.py"]) for name in names])

    # wait for the windows to be closed
    for proc in processes:
        proc.wait()


if __name__ == '__main__':
    main()
