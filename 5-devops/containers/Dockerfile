FROM python:3.11-slim

WORKDIR /workspace
ENV PIP_NO_CACHE_DIR=1

COPY . /workspace

RUN apt-get update         && apt-get install -y --no-install-recommends git         && rm -rf /var/lib/apt/lists/*         && python -m pip install --upgrade pip         && pip install nbformat nbconvert nbval mkdocs mkdocs-material

CMD ["bash"]
