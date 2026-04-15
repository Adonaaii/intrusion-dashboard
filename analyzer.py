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


            print("RAW LINE:", line)
            print("TIMESTAMP:", time)
            print("REQUEST:", request)
            print("CLEAN LINE:", clean_line)
            print("PARTS:", parts)
            
            
        except:
            print("something went wrong")

            
parse_logs(['192.168.1.25 - - [10/Jan/2026:18:01:17] "POST /login HTTP/1.1" 401 128'])


