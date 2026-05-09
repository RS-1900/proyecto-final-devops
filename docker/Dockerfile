FROM python:3.9-slim as builder
WORKDIR /app
COPY requirements.txt .
#instala  dependencias en una carpeta local
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.9-slim
WORKDIR /app
# Copiamo solo las dependencias instaladas de la etapa anterior
COPY --from=builder /root/.local /root/.local
COPY app.py .

# checa q que las dependencias esten en el PATH
ENV PATH=/root/.local/bin:$PATH

EXPOSE 5000
CMD ["python", "app.py"]
