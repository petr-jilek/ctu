#!/bin/sh
set -e

cd ../tex

find . -name '*.pdf' -exec cp {} ../subjects/{} \;
