#!/usr/bin/env bash
# Generate swagger client from Amun's swagger specification.
# Fridolin Pokorny <fridolin.pokorny@gmail.com>
#
# This file automates generation of the swagger client and makes it reproducible. Run this
# file to automatically generate Python swagger client for interacting with Amun.

set -ex

AMUN_SWAGGER_YAML=${1:-'https://raw.githubusercontent.com/thoth-station/amun-api/master/amun/swagger.yaml'}

function die() {
    echo $@ 1>&2
    exit 1
}

which which > /dev/null || die "Please install which command to continue"
which git > /dev/null   || die "Please install git to continue"
which mvn > /dev/null   || die "Please install maven to continue"
which java > /dev/null  || die "Please install java to continue"
which find > /dev/null  || die "Please install find utility to continue"


if [ ! -d 'swagger-codegen' ]; then
    git clone https://github.com/swagger-api/swagger-codegen
    pushd swagger-codegen
    mvn clean package
    popd
fi


rm -rf swagger-codegen-output/
java -jar swagger-codegen/modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate \
    -i "${AMUN_SWAGGER_YAML}" \
    -l python \
    -o swagger-codegen-output/ \
    -c swagger-codegen.json

rm -rf amun/swagger_client Documentation
cp -r swagger-codegen-output/amun/swagger_client/ amun/swagger_client
# There is a bug in swagger-codegen - it does not respect sub-package for some files, this is a simple workaround.
find swagger-codegen-output/amun.swagger_client/ -iname '*.py' -exec sed -i '/from amun.swagger_client/! s/^from amun\.\(.*\)/from amun.swagger_client.amun.\1/' {} \+
cp -r swagger-codegen-output/amun.swagger_client/* amun/swagger_client
cp -r swagger-codegen-output/docs Documentation

# Nullable values are not recognized by swagger-codegen.sh.
sed -i '/.*if container is None:/,+1 d' "amun/swagger_client/models/inspection_status_response_build.py"
sed -i '/.*if exit_code is None:/,+1 d' "amun/swagger_client/models/inspection_status_response_build.py"
sed -i '/.*if finished_at is None:/,+1 d' "amun/swagger_client/models/inspection_status_response_build.py"
sed -i '/.*if reason is None:/,+1 d' "amun/swagger_client/models/inspection_status_response_build.py"
sed -i '/.*if started_at is None:/,+1 d' "amun/swagger_client/models/inspection_status_response_build.py"

sed -i '/.*if container is None:/,+1 d' "amun/swagger_client/models/inspection_status_response_job.py"
sed -i '/.*if exit_code is None:/,+1 d' "amun/swagger_client/models/inspection_status_response_job.py"
sed -i '/.*if finished_at is None:/,+1 d' "amun/swagger_client/models/inspection_status_response_job.py"
sed -i '/.*if reason is None:/,+1 d' "amun/swagger_client/models/inspection_status_response_job.py"
sed -i '/.*if started_at is None:/,+1 d' "amun/swagger_client/models/inspection_status_response_job.py"

