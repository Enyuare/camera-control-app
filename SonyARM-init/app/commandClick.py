
import socket
import json

def send_json_command(command):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 8081))
        json_command = json.dumps({"command": command})
        s.sendall(json_command.encode('utf-8'))
    except socket.error as e:
        print(f"Socket error: {e}")
    except json.JSONDecodeError as e:
        print(f"JSON error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        s.close()

if __name__ == "__main__":
    try:
        send_json_command("1")
    except Exception as e:
        print(f"Failed to send command: {e}")
