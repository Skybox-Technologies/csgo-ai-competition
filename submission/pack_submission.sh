#!/usr/bin/env bash

set -eu

if [ $# -lt 2 ]; then
    echo "Usage: pack_submission.sh <team-name> <submission-folder>"
    exit 1
fi

TEAMNAME=$1
SUBMISSION=$2

# Sanity checks
if [ ! -f "$SUBMISSION/run.sh" ]; then
    echo "run.sh is missing!"
    exit 1
fi

if [ ! -f "$SUBMISSION/README.md" -o -f "$SUBMISSION/README.txt" ]; then
    echo "The README file is missing!"
    exit 1
fi

pushd $SUBMISSION

zip -r "../$TEAMNAME-submission.zip" *

popd