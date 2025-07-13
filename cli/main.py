import argparse
import requests

def send_message(msg) -> None:
    resp = requests.post("https://localhost:8000/message")
    print(resp.json())

parser = argparse.ArgumentParser()
parser.add_argument("type", choices=["run", "suggest", "explain", "script"])
parser.add_argument("input", help="Input message or command")

args = parser.parse_args()

msg = {"type" : args.type}
msg["command" if args.type == "run" else "goal" if args.type in ["suggest", "explain", "script"] else "error"] = args.input

print(f"Sending message, {msg}")
send_message(msg)
