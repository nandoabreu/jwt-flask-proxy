#! /usr/bin/env bash
#set -x

container_up=$(docker ps | grep proxy | grep Up)
if [ -z "$container_up" ]; then
    echo "No container up. Run first:"
    echo "   $ make up #or"
    echo "   $ HTTP_PORT=8081 make up"
    exit 1
fi

contenttype='Content-Type: application/json'

function test {
    url="http://127.0.0.1:${1}/auth"
    echo -e "\n=== Testing $url =========="

    method=POST
    data='{"user":"nandoabreu@github"}'
    res=$(curl -s -i $method -H "$contenttype" $url -d "$data")
    echo -n "POST with data / status test: "
    [[ "$res" =~ "200 OK" ]] && echo "Test OK" || echo "ERR"
    echo -n "POST with data / token test: "
    [[ "$res" =~ "token" ]] && echo "Test OK" || echo "ERR"

    method=POST
    data=''
    res=$(curl -s -i $method -H "$contenttype" $url -d "$data")
    echo -n "POST with EMPTY data / status test: "
    [[ "$res" =~ "200 OK" ]] && echo "ERR" || echo "Test OK"
    echo -n "POST with EMPTY data / no token: "
    [[ "$res" =~ "token" ]] && echo "ERR" || echo "Test OK"

    method=POST
    data=
    res=$(curl -s -i $method -H "$contenttype" $url)
    echo -n "POST with NO data / status test: "
    [[ "$res" =~ "200 OK" ]] && echo "ERR" || echo "Test OK"
    echo -n "POST with NO data / no token: "
    [[ "$res" =~ "token" ]] && echo "ERR" || echo "Test OK"

    method=
    data=''
    res=$(curl -s -i $method -H "$contenttype" $url -d "$data")
    echo -n "GET with EMPTY data / status test: "
    [[ "$res" =~ "200 OK" ]] && echo "ERR" || echo "Test OK"
    echo -n "GET with EMPTY data / no token: "
    [[ "$res" =~ "token" ]] && echo "ERR" || echo "Test OK"

    method=
    data=
    res=$(curl -s -i $method -H "$contenttype" $url)
    echo -n "GET with NO data / status test: "
    [[ "$res" =~ "200 OK" ]] && echo "ERR" || echo "Test OK"
    echo -n "GET with NO data / no token: "
    [[ "$res" =~ "token" ]] && echo "ERR" || echo "Test OK"
}

IFS=$'\n'
for line in $container_up; do
    port=$(echo $line | sed 's/.*:\([0-9]\+\)-.*/\1/')
    test $port
done

