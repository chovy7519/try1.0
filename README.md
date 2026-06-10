# UrbanAI-Kit

UrbanAI-Kit is an AI-assisted tool suite for urban planning and design workflows. It is built for colleagues in design institutes who often need to collect spatial data, convert planning formats, generate visual references, and search professional knowledge under tight project timelines.

This repository is used as a public-facing case study and partial project archive. The internal deployment, sensitive data, and organization-specific implementation details are not included.

## One-Sentence Summary

UrbanAI-Kit turns repeated urban planning tasks into AI-assisted tools: data acquisition, format conversion, AIGC visual generation, and RAG-based professional Q&A.

## Background

In urban planning and design projects, many daily tasks are repetitive but still require domain judgment:

- Finding and downloading usable spatial data
- Converting between planning formats and drawing formats
- Collecting POI, road network, and base-map information
- Producing visual references and urban design mood images
- Reviewing planning text against domain knowledge and project requirements
- Explaining professional standards and workflows to team members

UrbanAI-Kit was created to make these workflows lighter, faster, and easier to reuse inside a professional design environment.

## Target Users

Primary users:

- Urban planners
- Urban designers
- Architects and landscape designers
- Design institute colleagues who need lightweight data and AI support

Typical use cases:

- Early-stage site research
- Urban renewal and planning analysis
- Design concept exploration
- Planning document review
- Internal AI workflow training

## My Role

Project lead / AI product and prototype builder.

Main responsibilities:

- Identified repeated pain points in urban planning workflows
- Defined the product scope and module structure
- Used AI coding to build scripts, prototypes, and lightweight tools
- Configured APIs and tool workflows for data access and processing
- Built RAG-based professional knowledge workflows for planning Q&A and text review
- Supported internal communication, training, and adoption

## Current Status

UrbanAI-Kit has been deployed on the group's internal developer platform.

The public repository is intentionally limited to non-sensitive project framing and reusable product logic. Internal code, data, account information, API keys, and deployment details are excluded.

## Core Modules

### 1. AI Vision And Spatial Recognition

Explores computer vision and multimodal workflows for planning-related image and map interpretation.

Representative directions:

- Satellite image / road feature recognition
- Planning image understanding
- Drawing and visual material interpretation
- Image-to-workflow assistance for designers

### 2. Data Processing Tools

Supports common data preparation tasks in planning and design work.

Representative directions:

- OSM data processing
- POI data collection and download workflows
- Road network analysis
- Lightweight conversion between planning data and CAD/GIS-oriented workflows
- DXF / drawing-related format handling

### 3. AIGC For Urban Design

Explores how AIGC can support urban design ideation and visual communication.

Representative directions:

- Urban concept image generation
- Design intention image generation
- Visual reference production
- Scenario-based prompt workflows for city design

### 4. RAG-Based Professional Knowledge

Builds a domain-specific knowledge workflow for planning-related Q&A and document assistance.

Representative directions:

- Planning knowledge retrieval
- Professional Q&A
- Planning text review
- Internal knowledge reuse
- Reducing repeated explanation and manual lookup

### 5. Economic / Scenario Models

Explores lightweight planning-related analysis models, such as industrial park economic estimation and scenario comparison.

## Product Principles

- Start from real repeated work, not abstract AI capability.
- Keep every AI output reviewable and editable by professionals.
- Prefer small tools that can be inserted into existing workflows.
- Separate public demo logic from internal data and deployment details.
- Use AI coding to accelerate prototyping, but keep product judgment at the center.

## Technical Approach

UrbanAI-Kit combines several kinds of implementation work:

```text
AI coding -> scripts and lightweight tools
API configuration -> data access and external service integration
RAG workflow -> professional knowledge retrieval and Q&A
AIGC workflow -> image generation and design reference production
Product design -> user scenarios, module planning, and workflow integration
```

Commonly used AI and development tools include Codex, Claude Code, Gemini, RunningHub, and related AI coding / AIGC workflows.

## What This Project Demonstrates

UrbanAI-Kit is not only a technical experiment. It demonstrates a product-building pattern:

1. Observe repeated professional work.
2. Translate pain points into product modules.
3. Use AI coding to quickly build usable tools.
4. Connect APIs, data workflows, and RAG knowledge bases.
5. Deploy internally and collect feedback from real colleagues.
6. Turn the internal project into a safe, public case study.

## Privacy And Boundary

This public README does not include:

- Internal deployment addresses
- Organization-specific code or credentials
- Sensitive project data
- Internal documents or client information
- Private RAG corpus content

The goal of this repository is to explain the product thinking, workflow structure, and AI application logic behind UrbanAI-Kit without exposing confidential materials.

## Next Steps

- Rename this repository from `try1.0` to a clearer public name, such as `urban-ai-kit` or `urban-ai-kit-case-study`.
- Add anonymized screenshots or diagrams of the product structure.
- Add a module architecture diagram.
- Add selected non-sensitive demo scripts or pseudocode.
- Add a short product case study in Chinese for recruiters and interviewers.
