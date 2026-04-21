import time
from core.detection_engine import parse_log_line

def start_monitor(log_file_path, process_func):
    with open(log_file_path, "r") as file:
        file.seek(0, 2)  # move to end of file

        while True:
            line = file.readline()

            if not line:
                time.sleep(0.5)
                continue

            parsed = parse_log_line(line)

            if parsed:
                process_func(parsed)