#!/bin/bash

source ~/Develop/venvs/uvicorn-librouteros-api/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8000
