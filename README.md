## Setup

### Create Venv
```bash
python3 -m venv .venv
```

### Activate Venv
- macOS/linux
```bash
source ./.venv/bin/activate
```
- windows
```bash
.\.venv\Scripts\Activate.ps1
```

### Install Reqs
```bash
pip install -r requirements.txt
```

### Set api key env variable
- macOS/linux
```bash
export CLAUDE_API_KEY=<your_api_key>
```
- windows
```bash
$env:CLAUDE_API_KEY=<your_api_key>
```

### Run Server 
- macOS/linux
```bash
.venv/bin/python -m uvicorn mcp_server.main:app --reload
```
- windows
```bash
.venv\bin\python.exe -m uvicorn mcp_server.main:app --reload
```

### Example Client Usage
```bash
╰─ python3 cli/main.py suggest "how do I list file contents"
```