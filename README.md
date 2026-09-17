# AIOps Community — AI-Driven Incident Response & Telemetry Agent

> **Open-source AIOps framework and autonomous incident response toolkit powered by LLMs, LangChain, Prometheus, and OpenTelemetry.**

[![Community](https://img.shields.io/badge/Community-aiops.community-blue.svg)](https://aiops.community)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB.svg)](https://python.org)
[![LangChain](https://img.shields.io/badge/Framework-LangChain-00A67E.svg)](https://langchain.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

##  Features

- **Root Cause Analysis (RCA) Agent**: Automatically correlates anomalous Kubernetes pods, high memory spikes, and error logs into human-readable triage reports.
- **Metric Stream Anomaly Detection**: Unsupervised time-series anomaly detection on Prometheus telemetry data.
- **Auto-Remediation Playbooks**: Safe, policy-governed automated restarts, horizontal pod autoscaler adjustments, and traffic rerouting via Istio.
- **Slack & PagerDuty Integration**: Real-time AI summaries sent directly to operational war rooms.

---

##  Architecture

```
                       ┌──────────────────────┐
                       │  OpenTelemetry /     │
                       │  Prometheus Metrics  │
                       └──────────┬───────────┘
                                  │
                                  ▼
                       ┌──────────────────────┐
                       │  Anomaly Detection   │
                       │  Engine (Z-Score/ML) │
                       └──────────┬───────────┘
                                  │ (Anomaly Trigger)
                                  ▼
                       ┌──────────────────────┐
                       │  LangChain / LLM     │
                       │  Incident Copilot    │
                       └──────────┬───────────┘
                                  │
                   ┌──────────────┴──────────────┐
                   ▼                             ▼
        ┌─────────────────────┐       ┌─────────────────────┐
        │ Auto-Remediation    │       │ Slack / Teams       │
        │ Execution Engine    │       │ War Room Alerts     │
        └─────────────────────┘       └─────────────────────┘
```

---

##  Quickstart

```bash
# Clone the repository
git clone https://github.com/rennanfsimoes/aiops-community.git
cd aiops-community

# Install dependencies
pip install -r requirements.txt

# Start the AIOps Telemetry Agent
python src/agent/anomaly_detector.py --prometheus-url http://localhost:9090
```

---

##  License
MIT License - Copyright (c) 2025-2026 Rennan Simões.
