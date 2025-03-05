#! /bin/bash
# use with crontab
cd /root/domain-watchdog
echo "running the command" >> log
source .venv/bin/activate
/root/.local/bin/uv run domain-watchdog.py
