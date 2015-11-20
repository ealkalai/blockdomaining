#!/bin/bash

curl -X POST http://localhost:8090/__admin/shutdown
java -jar wiremock.jar --port 8090 > /dev/null 2>&1 &
