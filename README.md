# 🚀 AI-POWERED CI/CD CONTENT PIPELINE

## ✨ End-to-End Automation with Gemini & Kestra

| Status | AI Core | Orchestration | Deployment |
| :--- | :--- | :--- | :--- |
| **✅ Complete & Operational** | **Gemini 2.5 Flash** | **Kestra (Declarative Flows)** | **Vercel** |

## 💡 Project Overview: The Content Automation Solution

This project solves the critical issue of content deployment latency by establishing a sophisticated, two-repository CI/CD workflow. It transforms raw, unstructured text into production-ready JSON and deploys it live, orchestrated entirely by a declarative automation platform.

**Achievement:** Demonstrating the seamless integration of LLM intelligence (Gemini) with enterprise-grade orchestration (Kestra) and modern front-end delivery (Vercel). 

---

## 🏗️ Architecture & Core Technologies

This architecture is built on a **Two-Repository System** to ensure clean separation of concerns, high security, and maximum scalability.

### 1. AI Core: Gemini 2.5 Flash
* **Role:** Intelligence and Structuring.
* **Function:** Uses the `google-genai` SDK to process input, generating professional summaries. It is strictly constrained to output a **validated JSON object** for machine consumption.

### 2. Automation Layer: Kestra
* **Role:** Declarative Orchestration and Security.
* **Function:** Manages the entire pipeline logic via **Kestra YAML Flows**, handling execution, Git commits, and the final deployment trigger. This choice showcases mastery of scalable, event-driven orchestration.

### 3. Deployment: Vercel
* **Role:** Frontend Publishing.
* **Function:** Triggered via a dedicated **HTTP Request task** within the Kestra Flow using the secure `VERCEL_DEPLOY_HOOK` secret, ensuring instant publishing.

---

## ⚙️ Full Pipeline Process Flow (Kestra Orchestration)

The entire automated process is initiated via the **Command Line Interface (CLI)** and executed by Kestra in a seamless 6-step sequence:

1.  **Repository Checkout:** Kestra clones the repository.
2.  **Dependency Setup:** Kestra installs required Python dependencies (including the `google-genai` SDK).
3.  **AI Content Generation:** The Python script executes, calls **Gemini 2.5 Flash**, and saves the **validated JSON** to `content_output.json`.
4.  **Content Commit:** Kestra commits the newly generated `content_output.json` back to the repository.
5.  **Vercel Deployment Trigger:** Kestra sends a secure POST request to the **Vercel Deploy Hook**.
6.  **Live Verification:** Vercel builds and deploys the new content, resulting in an instant update on the live website.

| Tool / Concept | Project Use | Learn More |
| :--- | :--- | :--- |
| **Gemini 2.5 Flash API** | **Intelligent Content Generation** and **JSON Structuring** | [Gemini API Quickstart: JSON Mode](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/JSON_mode.ipynb) |
| **Kestra** | **Declarative Workflow Management** (YAML Flows) | [Kestra: CI/CD Pipeline Documentation](https://kestra.io/docs/version-control-cicd/cicd) |
| **Vercel** | **Frontend Hosting** and **Instant Publishing** | [Vercel: Deploy Hooks Documentation](https://vercel.com/docs/deployments) |

---

## 🎯 Core Technical Achievements & Architectural Insights

The final solution required overcoming complex, high-level architectural and security challenges:

* **Orchestration Mastery:** Implementing the entire CI/CD logic using **Kestra's declarative YAML Flows**, showcasing expertise in enterprise-grade workflow management.
* **Security & Secrets Management:** Successfully securing the **Gemini API Key** and **Vercel Deploy Hook** using **Kestra's native secret manager**, ensuring no sensitive data is exposed.
* **Resilience Fixes:** Overcoming critical debugging points, including ensuring the correct execution environment for the Python script and successfully configuring the deployment webhook to resolve persistent errors.
* **Initiation Versatility:** The pipeline can be initiated from the **Command Line Interface (CLI)**, webhooks, or the Kestra UI, demonstrating high flexibility in deployment triggers.

---

## 📁 Key Files & Their Role in the Flow

| File | Purpose | Orchestration Tool |
| :--- | :--- | :--- |
| **`ai-content-generator.yml`** | **Kestra Flow Definition** | Defines the sequential tasks (Clone, Install, Run, Commit, Deploy) that run the entire pipeline. |
| **`process_ai.py`** | **AI Execution Logic** | Python script that interacts with the Gemini API to generate and validate the JSON output. |
| **`input.txt`** | **Content Source** | The raw, unstructured text that serves as the prompt for the AI. |
| **`content_output.json`** | **Final Output** | The machine-readable, AI-generated JSON file that is committed and consumed by the frontend. |

---

## 🧠 Skills & Tools Learned from this Project

This project provides invaluable hands-on experience in high-demand, full-stack automation areas:

| Skill Category | Tool / Concept | Key Learning Gained |
| :--- | :--- | :--- |
| **AI Integration** | **Gemini 2.5 Flash API** | Practical application of **Structured Prompting** for reliable JSON output. |
| **Advanced Orchestration**| **Kestra** | Writing complex, modular, and **declarative YAML Flows** for scalability. |
| **DevOps & CI/CD** | **Vercel Deploy Hooks** | Securing continuous deployment via HTTP request triggers and managing environments. |
| **Foundational** | **Python, CLI, Git** | API interaction, command line mastery, and version control best practices. |

---
