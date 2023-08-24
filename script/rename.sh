#!/bin/bash -eux

TEMP_DIR=_book
OUT_DIR=docs

if [ -d $OUT_DIR ]; then
	rm -rf $OUT_DIR
fi

mv $TEMP_DIR $OUT_DIR
