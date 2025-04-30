#!/bin/bash

source ~/Develop/virtual-envs/uvicorn/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8000
