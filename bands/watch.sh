#!/bin/bash
fswatch -o bands.yml | xargs -n1 -I{} ./run.sh
