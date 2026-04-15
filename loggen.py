# log_generator.py - PASTE AND RUN!
import random
from datetime import datetime, timedelta
import argparse
import json

class LogGenerator:
    def __init__(self):
        self.ips = [f"192.168.1.{i}" for i in range(1, 51)] + [f"10.0.1.{i}" for i in range(1, 51)]
        self.users = ['alice', 'bob', 'charlie', 'admin', 'service']
        self.endpoints = ['/', '/home', '/about', '/products', '/contact', '/api/data']
        
    def generate_logs(self, count=10000, include_attacks=False):
        logs = []
        base_time = datetime(2026, 1, 10, 13, 0, 0)
        if include_attacks:
            logs.extend(self._brute_force_attack(base_time))
            logs.extend(self._sql_injection_attack(base_time))
            logs.extend(self._scanner_attack(base_time))
        
        # ADD ATTACKS FIRST
        
        
        # FILL WITH NORMAL TRAFFIC
        remaining = max(0, count - len(logs))
        for i in range(remaining):
            time_offset = random.randint(0, 86400)
            timestamp = (base_time + timedelta(seconds=time_offset)).strftime('%d/%b/%Y:%H:%M:%S')
            ip = random.choice(self.ips)
            user = random.choice(self.users + ['-', '-'])
            method = random.choices(['GET', 'POST', 'PUT'], weights=[0.8, 0.15, 0.05])[0]
            
            if method == 'GET':
                endpoint = random.choice(self.endpoints)
                status = random.choices([200, 404], weights=[0.9, 0.1])[0]
            else:  # POST/PUT
                endpoint = random.choice(['/login', '/api/login'])
                status = random.choices([200, 401, 302], weights=[0.6, 0.3, 0.1])[0]
            
            size = random.randint(500, 5000)
            log = f'{ip} - {user} [{timestamp}] "{method} {endpoint} HTTP/1.1" {status} {size}'
            logs.append(log)
        
        random.shuffle(logs)
        return logs
    
    def _brute_force_attack(self, base_time):
        logs = []
        attacker_ip = "203.0.113.15"
        for i in range(45):
            timestamp = (base_time + timedelta(minutes=30+i)).strftime('%d/%b/%Y:%H:%M:%S')
            log = f'{attacker_ip} - - [{timestamp}] "POST /login HTTP/1.1" 401 128'
            logs.append(log)
        # One success
        timestamp = (base_time + timedelta(minutes=30+45)).strftime('%d/%b/%Y:%H:%M:%S')
        logs.append(f'{attacker_ip} - admin [{timestamp}] "POST /login HTTP/1.1" 302 256')
        return logs
    
    def _sql_injection_attack(self, base_time):
        logs = []
        attacker_ip = "198.51.100.67"
        payloads = [
            "/products?id=1' OR '1'='1",
            "/search?q=1; DROP TABLE users",
            "/login?user=admin'--"
        ]
        for i, payload in enumerate(payloads):
            timestamp = (base_time + timedelta(hours=2+i)).strftime('%d/%b/%Y:%H:%M:%S')
            log = f'{attacker_ip} - - [{timestamp}] "GET {payload} HTTP/1.1" 200 1024'
            logs.append(log)
        return logs
    
    def _scanner_attack(self, base_time):
        logs = []
        attacker_ip = "203.0.113.99"
        targets = ['/admin', '/.git', '/backup', '/wp-admin', '/phpmyadmin']
        for i, target in enumerate(targets):
            timestamp = (base_time + timedelta(hours=1+i*0.5)).strftime('%d/%b/%Y:%H:%M:%S')
            status = 404 if random.random() < 0.8 else 403
            log = f'{attacker_ip} - - [{timestamp}] "GET {target} HTTP/1.1" {status} 512'
            logs.append(log)
        return logs

def main():
    parser = argparse.ArgumentParser(description='Generate security test logs FAST')
    parser.add_argument('--count', type=int, default=10000, help='Number of logs')
    parser.add_argument('--output', default='logs/sample.log', help='Output file')
    parser.add_argument('--attacks', action='store_true', help='Include attack logs')
    args = parser.parse_args()
    
    print("🚀 GENERATING LOGS...")
    generator = LogGenerator()
    logs = generator.generate_logs(args.count, include_attacks=args.attacks)
    
    with open(args.output, 'a') as f:
        f.write('\n'.join(logs))
    
    if args.attacks:
        print("🔍 Attacks included: Brute Force (46), SQLi (3), Scanner (5)")
    else:
        print("🔍 No attacks included")

def run_generator(output="logs/sample.log", count=100):
    generator = LogGenerator()
    logs = generator.generate_logs(count)
    
    with open(output, "a") as f:
        for log in logs:
            f.write(log + "\n")

if __name__ == "__main__":
    main()