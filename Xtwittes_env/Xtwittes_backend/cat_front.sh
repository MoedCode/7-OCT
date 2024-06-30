#!/usr/bin/bash
echo "-----__HTML_Templates__"
cat templates/*.html templates/parts/*.html templates/authentication/*html
echo ""
echo ""
echo "------ __STATIC_CSS__----- "
cat static/css/*.css static/css/parts/*.css