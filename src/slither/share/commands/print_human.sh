#!/bin/bash

slither --print human-summary --json $OUTPUT_DIR/$CURRENT_RUN_LINE.json --etherscan-apikey $ETHERSCAN_API_KEY $CURRENT_RUN_LINE 2> $OUTPUT_DIR/error

