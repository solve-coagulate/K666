import subprocess
import time
import urllib.request
import sys
import os


def main():
    # Start the development server on port 8001 without autoreload
    proc = subprocess.Popen(
        ['./start_server.sh', '8001', '--noreload'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    try:
        # Wait for the server to become responsive
        url = 'http://127.0.0.1:8001/'
        for _ in range(20):
            time.sleep(1)
            try:
                with urllib.request.urlopen(url) as resp:
                    if resp.status == 200:
                        print('Server responded with status 200')
                        return 0
            except Exception:
                pass
        print('Server did not respond in time')
        return 1
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait()


if __name__ == '__main__':
    sys.exit(main())
