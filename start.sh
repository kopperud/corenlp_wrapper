#!/bin/bash

~/natural_language_processing/start.sh &

python3 run.py

ps aux | grep "CoreNLPServer" | awk '{print $2}' | xargs kill

