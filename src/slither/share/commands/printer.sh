#!/bin/bash

mkdir -p $OUTPUT_DIR/$2
pushd $OUTPUT_DIR/$2

slither --print $2 --json $OUTPUT_DIR/$2/$CURRENT_RUN_LINE.json --etherscan-apikey $ETHERSCAN_API_KEY $CURRENT_RUN_LINE

popd
