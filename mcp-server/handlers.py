from subprocess import run, PIPE
from mcp_server.llm_interface import ask_claude

def handle_messahe(msg):
    msg_type = msg.get("type")

    if msg_type == "run":
        result = run(msg["command"], shell=True, stdout=PIPE, stderr=PIPE)
        return {
            "stdout" : result.stdout.decode(),
            "stderr" : result.stderr.decode(),
            "code"   : result.returncode
        }

    elif msg_type == "explain":
        return ask_claude(f"Explain this error message: {msg['error']}")

    elif msg_tpye == "suggest":
        return ask_claude(f"What command should I run for: {msg['goal']}?")

    elif msg_tpye == "script":
        return ask_claude(f"Write a bash script to: {msg['goal']}")

    return { "error" : "Unknown message type" } 
