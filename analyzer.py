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

def parse_logs(log_lines):
    parsed_logs = []
    for line in log_lines:
        line = line.strip()
        data = {}
        try:
            start = line.find("[")
            end = line.find("]")
            time = line[start+1:end]
            

            first_quote = line.find('"')
            second_quote = line.find('"', first_quote+1)
            request = line[first_quote+1:second_quote]
            
            line_no_time = line[:start] + line[end+1:]
            
            first_quote = line_no_time.find('"')
            second_quote = line_no_time.find('"', first_quote + 1)
            
            clean_line = line_no_time[:first_quote] + line_no_time[second_quote+1:]
            parts = clean_line.split()

            data["ip"] = parts[0]
            data["user"] = parts[2]
            data["status"] = int(parts[-2])
            data["size"] = int(parts[-1]) 
            data["timestamp"] = time  
            method, endpoint, _ = request.split()
            data["method"] = method
            data["endpoint"] = endpoint

            parsed_logs.append(data)
            
        except Exception as e:
            print("Error:", e)
    return parsed_logs

logs = read_logs("logs/sample.log")[:2]
parsed = parse_logs(logs)

print(parsed)          
#parse_logs(['192.168.1.25 - - [10/Jan/2026:18:01:17] "POST /login HTTP/1.1" 401 128'])


