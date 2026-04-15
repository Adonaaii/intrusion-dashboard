def read_logs(file_path):
    log_lines = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip():
                    log_lines.append(line)
    except FileNotFoundError:
        print("File does not exist")
        return []
    except Exception as e:
        print("Error:", e)
        return []
    return log_lines

if __name__ == "__main__":
    logs = read_logs("logs/sample.log")
    print(len(logs))        # how many logs
    print(logs[:5])         # first 5 logs


