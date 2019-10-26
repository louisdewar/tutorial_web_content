#!/usr/bin/env bash

set -e

# Get directory of current file
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

if [ -e ${DIR}/bin/tutorial_web ]
then
  ${DIR}/bin/tutorial_web start-test-server -s ${DIR}/bin/static -i ${DIR}/courses
else
  echo "It doesn't look like 'tutorial_web' is installed in the bin directory"
  echo "Running install script"
  echo "======================"
  ${DIR}/install.sh

  echo "=========================================="
  echo "Now re-run this script to start the server"
fi
