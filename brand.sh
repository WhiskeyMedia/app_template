#!/bin/bash

set -e

APP_NAME=${1:?brand.sh APP_NAME}
PACKAGE_NAME=${APP_NAME//_/-}

cd $(dirname $(which "$0"))

test -d APP_NAME.egg-info && echo 'please remove APP_NAME.egg-info directory' && exit

echo "Moving directories"
find . -type d -name '*APP_NAME*' -not -path './.git/*' | tac | while read d
do
    echo "$d -> ${d/%APP_NAME/$APP_NAME}"
    git mv "$d" "${d/%APP_NAME/$APP_NAME}"
done

echo "Editting files"
find . -type f -not -name "brand.sh" -not -path './.git/*' | xargs sed -i -e "s;APP_NAME;$APP_NAME;g" -e "s;PACKAGE_NAME;$PACKAGE_NAME;"

echo "Removing self"
git rm "brand.sh"

echo "Done"
