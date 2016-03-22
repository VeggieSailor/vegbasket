#!/bin/bash
rm -r screenshots/*
casperjs screenshots.js https://dev.veggiesailor.com/
casperjs screenshots.js https://dev.veggiesailor.com/en/search?q=vegan
casperjs screenshots.js https://dev.veggiesailor.com/en/vegan-bar-9667/
find screenshots/  -name *png -exec  /tmp/atlassian-cli-5.1.0/hipchat.sh -t ykPWE7LXklFMlD2Td4vYZjCIj9NPfSjzbdLU1blH --action shareFile --server https://veggiesailor.hipchat.com  --room 2043965 --file '{}' \;
