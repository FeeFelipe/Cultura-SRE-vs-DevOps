[![CI](https://github.com/FeeFelipe/Cultura-SRE-vs-DevOps/actions/workflows/ci.yml/badge.svg)](https://github.com/FeeFelipe/Cultura-SRE-vs-DevOps/actions)

> Lab do módulo **Princípios de Confiabilidade**  
📄 [Ver arquivo do workflow](.github/workflows/ci.yml)

---
# 🧪 Reliability Lab (Python)

[![CI](https://github.com/FeeFelipe/Cultura-SRE-vs-DevOps/actions/workflows/ci.yml/badge.svg)](https://github.com/FeeFelipe/Cultura-SRE-vs-DevOps/actions)

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


## 🚀 Executando localmente (recomendado: Docker)

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/FeeFelipe/Cultura-SRE-vs-DevOps.git
cd Cultura-SRE-vs-DevOps
```

### 2️⃣ Subir o serviço com Docker Compose

```bash
docker compose up --build -d
curl -i http://localhost:8080/health
```

O serviço estará disponível em http://localhost:8080/health

---

## ⚙️ Execução opcional sem Docker

Se preferir rodar fora de container (apenas para fins de estudo):

```bash
cd health
pip install -r requirements.txt
python main.py
curl -i http://localhost:8080/health
```
O serviço estará disponível em http://localhost:8080/health

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

**Com Docker Compose:**
```bash
docker compose down
HEALTH_FAIL=true docker compose up --build -d
curl -i http://localhost:8080/health
```

**Sem Docker (execução direta):**
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
cd health
docker build -t reliability-lab-py:1.0.0 .
docker run --rm -p 8080:8080 reliability-lab-py:1.0.0
```

---

## ⚙️ Executando via Docker Compose


O serviço é definido em `docker-compose.yml` na raiz do projeto:

```yaml
version: "3.9"

services:
  reliability-lab:
    build: ./health
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
docker compose up --build
```

**Testar o health-check:**  
```bash
curl -i http://localhost:8080/health
```

**Simular falha:**  

```bash
docker compose down
HEALTH_FAIL=true docker compose up
```

**Parar:**  

```bash
docker compose down
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


