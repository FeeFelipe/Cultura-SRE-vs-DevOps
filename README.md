# 🧪 Reliability Lab (Python)

[![CI](https://github.com/fiap-sre-labs/reliability-lab-py/actions/workflows/ci.yml/badge.svg)](https://github.com/fiap-sre-labs/reliability-lab-py/actions)

> Lab do módulo **Princípios de Confiabilidade**  
> Demonstra como aplicar métricas de SRE em um pipeline CI/CD com health-check e rollback automático.

---

## 🎯 Objetivo

Implementar uma aplicação simples em **Python + Flask** com um endpoint `/health`  
e um pipeline **GitHub Actions** que:

- Executa **testes automatizados**  
- Realiza **health-check pós-deploy**  
- Bloqueia o deploy e **simula rollback** em caso de falha  
- Mede latência e compara com **SLO configurado**

---

## ⚙️ Tecnologias

- Python 3.11  
- Flask 3.0  
- Pytest  
- GitHub Actions  
- Docker e Docker Compose

---

## 🚀 Executando localmente

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/fiap-sre-labs/reliability-lab-py.git
cd reliability-lab-py
```

### 2️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 3️⃣ Executar a aplicação

```bash
python main.py
```

### 4️⃣ Testar o endpoint `/health`

```bash
curl -i http://localhost:8080/health
```

**Resposta esperada:**

```json
{
  "status": "UP",
  "service": "reliability-lab-py",
  "version": "1.0.0",
  "timestamp": "2025-10-20T18:00:00Z"
}
```

---

## 💥 Simular falha

Para testar o comportamento de erro (retorno HTTP 500):

```bash
HEALTH_FAIL=true python main.py
curl -i http://localhost:8080/health
```

**Resposta esperada:**

```json
{
  "status": "DOWN",
  "service": "reliability-lab-py",
  "version": "1.0.0",
  "timestamp": "2025-10-20T18:00:00Z"
}
```

---

## 🧩 Testes automatizados

Execute os testes com **pytest**:

```bash
pytest -v
```

---

## 🧰 Pipeline CI/CD

O workflow `.github/workflows/ci.yml` realiza:

1. Instalação e execução dos testes  
2. Health-check (retorno 200)  
3. Medição de latência (SLO ≤ 200ms)  
4. Simulação de falha (`HEALTH_FAIL=true`)  
5. Rollback automático (interrompe pipeline)

📄 [Ver arquivo do workflow](.github/workflows/ci.yml)

---

## 🐳 Executando via Docker

```bash
docker build -t reliability-lab-py:1.0.0 .
docker run --rm -p 8080:8080 reliability-lab-py:1.0.0
```

---

## ⚙️ Executando via Docker Compose

Arquivo `docker-compose.yml`:

```yaml
version: "3.9"

services:
  reliability-lab:
    build: .
    container_name: reliability-lab
    ports:
      - "8080:8080"
    environment:
      SERVICE_NAME: reliability-lab-py
      VERSION: 1.0.0
      PORT: 8080
      # Para simular falha no health-check, mude para "true"
      HEALTH_FAIL: "false"
```

### Comandos úteis

**Subir o serviço:**  
```bash
docker-compose up --build
```

**Testar o health-check:**  
```bash
curl -i http://localhost:8080/health
```

**Simular falha:**  
```bash
docker-compose down
HEALTH_FAIL=true docker-compose up
```

**Parar:**  
```bash
docker-compose down
```

---

## 🧠 Para refletir

- Seu pipeline atual valida a saúde da aplicação antes de liberar deploys?  
- Como você definiria um **SLO de latência** real para seu serviço?  
- O que seria necessário para automatizar rollback em produção?

---

## 📚 Próximo passo

> Integrar este lab ao conteúdo da aula **Princípios de Confiabilidade**,  
> demonstrando o equilíbrio entre **velocidade de entrega** e **estabilidade operacional**.


