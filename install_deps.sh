#!/bin/bash
set -e

echo "🚀 Настройка Rust и Python для Render"

export CARGO_HOME=$HOME/.cargo
export RUSTUP_HOME=$HOME/.rustup
mkdir -p $CARGO_HOME $RUSTUP_HOME

pip install --upgrade pip wheel setuptools maturin

pip install --only-binary :all: pydantic-core

pip install -r requirements.txt --prefer-binary

echo "✅ Установка завершена успешно!"
