FROM python:3.11

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY knowledgeboxai_mcp_server.py ./

CMD ["python", "knowledgeboxai_mcp_server.py"]
