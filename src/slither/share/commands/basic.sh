#!/bin/bash

slither --json "$OUTPUT_DIR/$CURRENT_RUN_LINE.json" --etherscan-apikey "$ETHERSCAN_API_KEY" $CURRENT_RUN_LINE