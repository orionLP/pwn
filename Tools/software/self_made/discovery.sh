#!/bin/bash

# first find all files

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'

echo -e "${GREEN}Finding all files in /home/ directory that are readable${NC}"
find /home/ -type f -readable -exec ls -ld {} \; 

echo -e "${GREEN}Finding all files in /home/ directory that you can execute${NC}"
find /home/ -type f -executable -exec ls -ld {} \;
