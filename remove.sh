#!/bin/sh

set -e

APP_NAME="speedtestweb"

echo "======================================"
echo "🧹 Removendo $APP_NAME"
echo "======================================"

# Para e remove containers, redes e volumes do compose
echo "🛑 Parando e removendo containers..."
docker compose down --remove-orphans

echo "✅ $APP_NAME removido com sucesso!"

echo "ℹ️ Imagens NÃO foram apagadas."
echo "   Para remover a imagem manualmente:"
echo "   docker image rm tonanuvem/speedtestweb:latest"
