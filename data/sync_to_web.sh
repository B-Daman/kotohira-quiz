#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
SRC_DIR="$HOME/hisho-bot/data/quiz"
DST_DIR="$ROOT_DIR/web/public/data"

mkdir -p "$DST_DIR"
cp "$SRC_DIR/kotohira_questions.json" "$DST_DIR/"
cp "$SRC_DIR/english_questions.json" "$DST_DIR/"
echo "Synced quiz data to $DST_DIR"
