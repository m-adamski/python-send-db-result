#!/usr/bin/env bash

if [ -d "./venv/Scripts" ] && [ -f "./venv/Scripts/activate" ]; then
    source ./venv/Scripts/activate &&
        python main "$@" &&
        deactivate
fi
