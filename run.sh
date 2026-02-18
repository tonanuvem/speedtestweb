#!/bin/sh

set -e

APP_NAME="speedtestweb"

echo "======================================"
echo "🚀 Subindo $APP_NAME com Docker Compose"
echo "======================================"

# Garante que a imagem mais recente seja baixada
echo "📥 Atualizando imagem..."
docker compose pull

# Sobe (ou recria) os containers
echo "🐳 Iniciando containers..."
docker compose up -d

echo "✅ $APP_NAME está rodando!"
echo "🌐 Acesse em: http://localhost:5000"
