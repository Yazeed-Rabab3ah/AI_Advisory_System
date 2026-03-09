# Agentic Market Expansion Advisor

## Overview

This project implements an **Agentic AI advisory system** that helps a Jordanian restaurant expand into the **UAE market**, specifically **Dubai and Abu Dhabi**.

The system answers business questions and provides structured recommendations for key aspects of restaurant expansion, including location selection, pricing strategy, menu adaptation, marketing, operations, and financial planning.

The system is built using a **multi-agent architecture**, where each agent specializes in a specific domain of expertise. A **Master Advisor Agent** coordinates the specialized agents and produces a final structured response for the user.

---

# System Architecture

The system follows a **multi-agent architecture**.

A **Master Agent** receives the user request and decides which specialized agents should be used to generate the final response.

### Workflow
User Question
# ↓
Master Advisor Agent
# ↓
Relevant Specialized Agents
# ↓
Combined Structured Recommendation
# ↓
User Response

# Agents

| Agent | Responsibility |
|------|------|
| Location Agent | Suggests best districts in Dubai and Abu Dhabi |
| Competitor Analysis Agent | Identifies competitors and market positioning |
| Menu Strategy Agent | Suggests menu adaptations for UAE customers |
| Pricing Strategy Agent | Recommends price ranges and positioning |
| Marketing Strategy Agent | Designs launch marketing strategies |
| Delivery Platform Agent | Advises on Talabat, Deliveroo, and Careem strategies |
| Operations & Staffing Agent | Recommends staffing structure and operational setup |
| Licensing & Regulatory Agent | Explains required permits and approvals |
| Supplier Strategy Agent | Recommends sourcing and supplier strategies |
| Risk Analysis Agent | Identifies business risks and mitigation strategies |
| Financial Analysis Agent | Estimates startup costs, revenue potential, and break-even |

---

# Technologies Used

- **Python**
- **Agno Agent Framework**
- **OpenAI GPT-4.1 (Master Agent)**
- **OpenAI GPT-4.1-mini (Specialized Agents)**
- **Google Maps API**
- **RAG Knowledge Base (company data)**
- **SQLite & ChromaDB**
- **uv package manager**

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Yazeed-Rabab3ah/AI_Advisory_System.git
cd AI_Advisory_System
```
Install dependencies using uv:

```bash 
uv sync
```
Run app:
```bash 
uv run main.py
```

Note: Demo video link in documentation

