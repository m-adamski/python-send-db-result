#!/usr/bin/env bash

REGISTRY="ghcr.io/m-adamski/python-send-db-result"

if [ ! -f Dockerfile ]; then
    echo "Run this script from the root directory of the docker configuration"
    exit 1
fi

# Read tag
read -p "$(echo -e "Enter tag name (latest): ")" tag
tag=${tag:-latest}

# Build Docker image
if docker build --no-cache --platform linux/amd64 -t $REGISTRY:"$tag" . ; then

    # Push Docker image with specified tag
    read -p "$(echo -e "\nWould you like to push image to the registry? [y/N]: ")" push
    push=${push:-n}

    case ${push:0:1} in
    y | Y)
        docker push $REGISTRY:"$tag"
        ;;
    esac
fi
