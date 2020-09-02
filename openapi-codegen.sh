#!/usr/bin/env bash
# Generate OpenAPI client from Amun's swagger specification.
# Fridolin Pokorny <fridolin.pokorny@gmail.com>
#
# This file automates generation of the openapi client and makes it reproducible. Run this
# file to automatically generate Python openapi client for interacting with Amun.

set -ex

AMUN_SWAGGER_YAML=${1:-'http://amun-api-thoth-test-core.apps.ocp.prod.psi.redhat.com/api/v1/openapi.json'}
OPENAPI_GENERATOR_CLI_VERSION="4.2.2"

function die() {
    echo $@ 1>&2
    exit 1
}

which which > /dev/null || die "Please install which command to continue"
which wget > /dev/null  || die "Please install wget to continue"
which find > /dev/null  || die "Please install find utility to continue"


[[ -f 'openapi-generator-cli.jar' ]] || {
    wget -O openapi-generator-cli.jar \
    "https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/${OPENAPI_GENERATOR_CLI_VERSION}/openapi-generator-cli-${OPENAPI_GENERATOR_CLI_VERSION}.jar"
}


rm -rf swagger-codegen-output/
java -jar openapi-generator-cli.jar generate \
     -i "${AMUN_SWAGGER_YAML}" \
     -g python \
     -o swagger-codegen-output \
     -c swagger-codegen.json

rm -rf amun/swagger_client Documentation
find swagger-codegen-output/amun/swagger_client/ -iname '*.py' -exec sed -i '/from amun.swagger_client/! s/^from amun\.\(.*\)/from amun.swagger_client.amun.\1/' {} \+
find swagger-codegen-output/amun/swagger_client -iname '*.py' -exec sed -i 's/from amun.debug_api import DebugApi/from amun.swagger_client.amun.debug_api import DebugApi/' {} \+
find swagger-codegen-output/amun/swagger_client -iname '*.py' -exec sed -i 's/from amun.inspection_api import InspectionApi/from amun.swagger_client.amun.inspection_api import InspectionApi/' {} \+
find swagger-codegen-output/docs -iname '*.md' -exec sed -i 's|All URIs are relative to .*|All URIs are relative to https://amun.test.thoth-station.ninja/api/v1|' {} \+
cp -r swagger-codegen-output/amun/swagger_client/ amun/swagger_client
cp -r swagger-codegen-output/docs Documentation
cp -r swagger-codegen-output/amun/swagger_client/* amun/swagger_client
sed -i '/__version__ = "0.0.1"/d' 'amun/swagger_client/__init__.py'
