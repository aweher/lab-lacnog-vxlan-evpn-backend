#!/bin/bash
echo "Desplegando backend..."
docker compose pull && docker compose up -d