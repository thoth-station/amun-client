#!/usr/bin/env bash
# Generate OpenAPI client from Amun's swagger specification.
# Fridolin Pokorny <fridolin.pokorny@gmail.com>
#
# This file automates generation of the openapi client and makes it reproducible. Run this
# file to automatically generate Python openapi client for interacting with Amun.

set -ex

AMUN_SWAGGER_YAML=${1:-'http://amun.test.thoth-station.ninja/api/v1/openapi.json'}

function die() {
    echo $@ 1>&2
    exit 1
}

which which > /dev/null || die "Please install which command to continue"
which wget > /dev/null  || die "Please install wget to continue"
which find > /dev/null  || die "Please install find utility to continue"


[[ -f 'openapi-generator-cli.jar' ]] || {
    wget -O openapi-generator-cli.jar \
    http://central.maven.org/maven2/org/openapitools/openapi-generator-cli/4.2.2/openapi-generator-cli-4.2.2.jar
}


rm -rf swagger-codegen-output/
java -jar openapi-generator-cli.jar generate \
     -i "${AMUN_SWAGGER_YAML}" \
     -g python \
     -o swagger-codegen-output \
     -c swagger-codegen.json

rm -rf amun/swagger_client Documentation
find swagger-codegen-output/amun/swagger_client/ -iname '*.py' -exec sed -i '/from amun.swagger_client/! s/^from amun\.\(.*\)/from amun.swagger_client.amun.\1/' {} \+
cp -r swagger-codegen-output/amun/swagger_client/ amun/swagger_client
cp -r swagger-codegen-output/docs Documentation
