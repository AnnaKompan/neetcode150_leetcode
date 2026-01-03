#!/bin/bash

if [ -z "$1" ]; then
    echo "Add problem name"
    exit 1
fi
message="Solve: $1"

git status
git add .
git commit -m "$message"
git push origin main

echo "Pushed $message"