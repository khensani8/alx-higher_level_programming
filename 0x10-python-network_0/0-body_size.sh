#!/usr/bin/env bash
# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Make a request to the URL using curl and get the size of the response body
response_size=$(curl -sI "$1" | grep -i content-length | awk '{print $2}' | tr -d '\r\n')

# Display the size of the response body in bytes
echo "Size of the response body: ${response_size} bytes"
