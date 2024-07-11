import socket
import json

def send_json_command(command):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 8081))
    json_command = json.dumps({"command": command})
    s.sendall(json_command.encode('utf-8'))
    s.close()

if __name__ == "__main__":
    send_json_command("1")
