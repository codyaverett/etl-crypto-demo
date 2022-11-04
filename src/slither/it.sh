#!/bin/bash

# Get current working directory
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

LOCAL_DATA_DIR="$DIR/share"
mkdir -p $LOCAL_DATA_DIR

docker run -it -v $LOCAL_DATA_DIR:/share trailofbits/eth-security-toolbox
