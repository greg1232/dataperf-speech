#!/bin/bash

# Safely execute this bash script
# e exit on first failure
# u unset variables are errors
# f disable globbing on *
# pipefail | produces a failure code if any stage fails
set -Eeuoxfa pipefail

# Get the directory of this script
LOCAL_DIRECTORY="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

PYTHONPATH=$LOCAL_DIRECTORY/.. python3 $LOCAL_DIRECTORY/../dataperf_speech/cli/cli.py $@

