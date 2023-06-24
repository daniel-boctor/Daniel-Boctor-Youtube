#!/bin/bash

domain="example.com"
api_key='api_key'
hosts=("" "www." "demo.")

local_ip=$(curl -s http://checkip.amazonaws.com)

echo "Local IP: $local_ip"

authoritative_nameservers=$(dig +short $domain NS | head -n1)

echo "Authoritative nameserver for $domain: $authoritative_nameservers"

for host in "${hosts[@]}"; do

        echo

        resolved_ip=$(dig +short @$authoritative_nameservers $host$domain)

        echo "Resolved IP for $host$domain: $resolved_ip"

        if [ "$resolved_ip" = "$local_ip" ]; then
                echo "$host$domain records are up to date!"
        else
                echo "$host$domain records are OUTDATED!"
                response=$(curl -s "https://dynamicdns.park-your-domain.com/update?host=${host//./}&domain=$domain&password=$api_key")

                err_count=$(echo $response | grep -oP "<ErrCount>\K.*(?=</ErrCount>)")
                err=$(echo $response | grep -oP "<Err1>\K.*(?=</Err1>)")

                if [ "$err_count" = "0" ]; then
                        echo "API call successful! DNS propagation may take a few minutes..."
                else
                        echo "API call failed! Reason: $err"
                fi
        fi
done