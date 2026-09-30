# AI Red Teaming Lab

## Overview

This project demonstrates AI security testing and red teaming of a locally hosted LLM using Ollama, FastAPI, Garak, Promptfoo, and PyRIT.

The objective was to identify vulnerabilities, evaluate model safety, and assess resistance to adversarial attacks using multiple security testing frameworks.

---

# Architecture

The following diagram shows the overall AI red teaming architecture used in this lab.

<img width="1966" height="800" alt="Architecture 01-ai-red-teaming-lab" src="https://github.com/user-attachments/assets/cb99e20a-c906-4183-a9cf-4456f2ed5121" />
!("https://github.com/user-attachments/assets/cb99e20a-c906-4183-a9cf-4456f2ed5121")

## Architecture Description
 
The architecture consists of a FastAPI chatbot connected to a locally hosted llama3.1 model through Ollama.
 
User and adversarial prompts are submitted through the chatbot interface and forwarded to the model. Security testing is performed using Garak, Promptfoo, and PyRIT, while GitHub Actions automates the execution of testing workflows whenever application code, prompts, or model configurations change.
 
The trust boundary is located at the user input layer because prompts are attacker-controlled. System prompts and safety rules provide guardrails that help the model resist prompt injection, jailbreak attempts, and unsafe output generation.
 
The llama3.1 model is hosted locally through Ollama, allowing all testing and evaluation activities to be performed in a controlled environment without reliance on external cloud-hosted LLM services.

---
# Executive Summary

This project assessed the security of a locally hosted llama3.1 Large Language Model (LLM) deployed through Ollama and accessed via a FastAPI chatbot application.

The assessment used three independent AI security testing tools:

- Garak
- Promptfoo
- PyRIT

Testing focused on prompt injection, jailbreak resistance, unsafe output generation, and overall model behavior under adversarial conditions.

Key Results:

- Garak completed toxicity and safety evaluations without identifying unsafe outputs.
- Promptfoo achieved a 100% success rate across evaluation test cases.
- PyRIT executed the airt.jailbreak scenario and performed 20 attack attempts with a 0% jailbreak success rate.
- No successful prompt injection or jailbreak attacks were observed during testing.

Risk Assessment:

- Prompt Injection Risk: Low
- Jailbreak Risk: Low
- Toxic Output Risk: Low
- Information Disclosure Risk: Low

The findings indicate that the tested llama3.1 deployment demonstrated strong resistance to the evaluated attack techniques and maintained safe behavior throughout assessment activities.

Recommended next steps include expanding adversarial test coverage, executing additional PyRIT scenarios, and continuing automated security testing through GitHub Actions.

---

# Demo Video

A short project demonstration of the chatbot, architecture, Garak, Promptfoo, PyRIT testing workflow is available in:

https://github.com/user-attachments/assets/e0fc3d7d-2310-464f-babb-e92c2ea19d86

---

# Technology Stack

- Python
- FastAPI
- Ollama
- llama3.1
- Garak
- Promptfoo
- PyRIT
- GitHub Actions

---

# Local Chatbot Setup

## Start Ollama

```bash
ollama serve
```
# Load Model

```bash
ollama pull llama3.1
```
# Run FastAPI

```bash
uvicorn app.main:app --reload
```
The chatbot was configured to communicate with a locally hosted llama3.1 model.

---

# Red Team Methodology 

Three independent AI security testing tools were used:

	1. Garak
	2. Promptfoo
	3. Pyrit

Using multiple tools provided broader coverage of LLM attack surfaces.

---

# Garak Evaluation

## Probe Used

	 probes.realtoxicityprompts.RTPBlank

## Command
```bash
	python -m garak \
		--spec probes.toxicitypromppts.RTPBlank \
		--target_type ollama \
		--target_name llama3.1 \
		__report_prefix garak_results/
```
## Results

[<img width="610" height="342" alt="Screenshot 2026-09-26 211333" src="https://github.com/user-attachments/assets/a6450185-edc5-4e45-b802-892ecb15d588" />](https://1drv.ms/i/c/be1480535b65d467/IQCOCD6uj9MmT61TSU6yUd-eAVzbQFqiqYs7DWrPAch5jn0?e=AACRyF)

Garak evaluated the llama3.1 model using the RTPBlank probe. The scan completed successfully with a 100% score and DEFCON 5 rating, indicating low risk and no unsafe outputs.

- Scan completed successfully
- RTPBlank toxicity checks passed
- HTML and JSON reports generated
- No unsafe responses observed

## Findings

The model successfully resisted tested toxicity prompts and maintained safe output behavior.

---

# Promptfoo Evaluation

## Command
```bash
	npx promptfoo eval -c promptfooconfig.yaml
```
## Results

<img width="578" height="290" alt="Screenshot 2026-09-28 235237" src="https://github.com/user-attachments/assets/7bbd210a-ab3c-41d0-9f05-aaabb6671ddd" />

- 2 evaluation tests executed
- 2 tests passed
- 100% completion rate
- 0 evaluation errors

## Findings

Promptfoo confirmed stable and appropriate model responses across multiple prompt styles.

---

# PyRIT Evaluation

## Backend Configuration 
```bash
	export OPENAI_CHAT_MODEL=llama3.1
	export OPENAI_CHAT_ENDPOINT=http://localhost:11434
	export OPENAI_CHAT_KEY=dummy
```
## Start Backend
```bash
	pyrit_backend --host 127.0.0.1 --port 8010
```
## Registered Target

	openai_chat
	Model: llama3.1
	Endpoint: http://localhost:11434

## Scenario Executed

	pyrit_scan \
	  --server-url=http://127.0.0.1:8010 \
	  run airt.jailbreak \
          --target openai_chat

## Results

<img width="607" height="324" alt="Screenshot 2026-09-28 205714" src="https://github.com/user-attachments/assets/2d877bb2-308c-4177-8c30-c37fa25c0ca7" />

PyRIT executed the airt.jailbreak scenario against the llama3.1 model. Twenty jailbreak attempts were performed, resulting in a 0% success rate and no successful compromise of model safeguards.

- Attack Attempts: 20 
- Success Rate: 0%
- Status: FAILED

## Findings

PyRIT executed twenty jailbreak attacks against the model and achieved a 0% success rate.
No jailbreak attempts successfully bypassed model safeguards.

---

# Written Assessment

## Scope

The assessment focused on a FastAPI chatbot connected to the Ollama-hosted llama3.1 model. Security testing targeted prompt injection, jailbreak resistance, unsafe outputs, and model behavior under adversarial conditions.

## Methodology

Three testing frameworks were used:

- Garak for automated vulnerability scanning
- Promptfoo for prompt evaluation and response validation
- PyRIT for adversarial jailbreak testing

Testing was performed against a locally hosted model using repeatable security workflows.

## Findings With Evidence

### Garak

- RTPBlank probe executed successfully.
- No unsafe or toxic responses detected.
- Safety checks passed.

Evidence:
- Garak HTML report
- Garak JSON output

### Promptfoo
- Two prompt evaluations completed.
- Both tests passed successfully.

Evidence:
- Promptfoo evaluation output

### PyRIT

- airt.jailbreak scenario executed.
- Twenty attack attempts performed.
- Zero successful jailbreaks.

Evidence:
- PyRIT scenario output
- PyRIT attack summary

## Risk Ratings

| Finding | Risk |
|----------|----------|
| Prompt Injection | Low |
| Toxic Output | Low |
| Jailbreak Success | Low |
| Information Disclosure | Low |

## Affected Assets

- FastAPI Chatbot Application
- Ollama llama3.1 Model
- Prompt Handling Logic
- CI/CD Security Testing Pipeline

## Recommended Controls

- Continue automated red-team testing.
- Expand prompt injection coverage.
- Add additional PyRIT scenarios.
- Maintain CI/CD testing workflows.
- Periodically retest updated models.

## Retest Results

After testing and validation:

- Garak passed safety checks.
- Promptfoo evaluations passed.
- PyRIT jailbreak scenario reported 0% success rate.

No successful compromise of model safeguards was observed during retesting.

---

# OWASP LLM Top 10 Mapping
 
| OWASP Risk | Tool Used | Test Performed | Result | Risk Rating |
|------------|-----------|---------------|--------|-------------|
| LLM01 – Prompt Injection | Garak, PyRIT | Prompt injection probes, airt.jailbreak | No successful prompt injection or jailbreak attacks observed | Low |
| LLM02 – Sensitive Information Disclosure | Garak, Promptfoo | Prompt probing and response evaluation | No sensitive information disclosure observed | Low |
| LLM07 – System Prompt Leakage | Garak, PyRIT | Jailbreak and extraction attempts | No successful system prompt extraction observed | Low |

# MITRE ATLAS Mapping
 
| MITRE ATLAS Technique | Tool Used | Scenario/Test | Result |
|----------------------|-----------|---------------|--------|
| AML.T0051 – Prompt Injection | Garak, PyRIT | Prompt injection testing, airt.jailbreak | No successful prompt injection attacks observed |
| AML.T0048 – Jailbreak | PyRIT | airt.jailbreak | 20 attacks attempted, 0% success rate |
| AML.T0015 – Evasion | Garak | RTPBlank probe | No successful evasion techniques observed |
| AML.T0034 – Model Abuse | PyRIT | Adversarial testing | Model safeguards prevented successful compromise |

---

# CI/CD Integration

Github Actions was configured to automate testing

Workflow:
	
	.github/workflows/redteam.yml

Capabilities:
- Run red team tests automatically
- Execute security validation
- Upload results
- Support continuous security testing

---

# Security Assessment Summary

Tool:		Result:
- Garak         - Passed RTPBlank safety checks
-Promptfoo      - 100% test pass rate
- Pyrit         - 0% jailbreak success rate

# Lessons Learned

This project demonstrated how different AI security tools evaluate LLM behavior from different perspectives.

Key takeaways:

- Garak provides structured security probes.
- Promptfoo is useful for response validation and consistency testing.
- PyRIT offers advanced adversarial testing scenarios.
- Local models require careful configuration when integrating multiple testing frameworks.
- Automated testing improves reliability and repeatability.

# Overall Assessment 

The llama3.1 model demonstrated strong resistance against tested toxicity, prompt injection, and jailbreak attacks.

No successful compromise was observed across Garak, Promptfoo, or PyRIT evaluations.

# Reflection

This project demonstrated how multiple AI security tools can be combined to evaluate LLM safety from different perspectives.
Garak focused on prompt injection and toxicity, Promptfoo evaluated consistency and behavior, and PyRIT simulated adversarial jailbreak scenarios.
Together they provided a comprehensive assessment of model security.

# Future Improvements

Future enhancements include:

- Running larger Garak probe suites
- Expanding Promptfoo coverage
- Testing additional Ollama models
- Running more PyRIT scenarios
- Uploading security artifacts through GitHub Actions
- Mapping results to additional MITRE ATLAS techniques

# Conclusion 

This project successfully deployed and evaluated a local LLM using FastAPI, Ollama, Garak, Promptfoo, and PyRIT.

Completed Objectives:

- FastAPI chatbot deployment
- Ollama integration
- Garak testing
- Promptfoo evaluation
- PyRIT jailbreak testing
- CI/CD integration
- OWASP LLM mapping
- MITRE ATLAS mapping
