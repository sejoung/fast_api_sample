#!/bin/bash

while true; do
    count=$(netstat -na | grep ESTABLISHED | grep 3306 | wc -l)
    echo "Active MySQL Connections: $count"
    sleep 1  # 1초마다 실행 (원하는 간격으로 변경 가능)
done
