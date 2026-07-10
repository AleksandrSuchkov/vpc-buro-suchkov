#!/bin/bash
# Двойной клик = закоммитить изменения и запушить сайт на GitHub Pages
cd "$(dirname "$0")"
./push.sh
echo
echo "Окно можно закрыть."
