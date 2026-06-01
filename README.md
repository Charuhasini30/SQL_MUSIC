##🤖 LLM-Powered SQL Query Agent (FastAPI + Groq + SQLite)
##🧠 Introduction

The LLM-Powered SQL Query Agent is an AI-driven system that enables users to query structured databases using natural language. Instead of manually writing SQL queries, users can ask questions in plain English, and the system automatically converts them into optimized SQL statements using a Large Language Model (LLaMA 3 via Groq API).

This project demonstrates the integration of:

Generative AI (LLMs)
Backend API development (FastAPI)
Secure SQL query validation
Database management (SQLite)

The system ensures that only safe and read-only queries are executed, preventing data corruption and SQL injection attacks.

##Problem Statement

Traditional database querying requires:

Knowledge of SQL syntax
Understanding of table relationships
Ability to write joins, filters, and aggregations

This creates a barrier for non-technical users.

This system solves that by:
Translating natural language → SQL
Ensuring secure query execution
Returning structured and readable results

##🎯 Objectives
Convert natural language into SQL queries
Automatically extract database schema
Validate SQL queries for security
Execute safe queries on SQLite database
Return structured JSON responses
Prevent SQL injection and destructive operations

##🏗️ System Architecture
User
 ↓
FastAPI (API Layer)
 ↓
Agent Pipeline
 ↓
Groq LLM (LLaMA 3.3-70B)
 ↓
SQL Validator
 ↓
SQLite Database
 ↓
JSON Response

##⚙️ Technology Stack
Backend: FastAPI
LLM: LLaMA 3.3-70B (Groq API)
Database: SQLite (Chinook Dataset)
Language: Python 3.10+
Environment: python-dotenv
Server: Uvicorn

##🔄 Working Methodology
1. Schema Extraction

The system extracts database structure using:

Table names
Column names
Schema formatting for LLM context

👉 Ensures the model understands database structure before generating SQL.

2. SQL Generation (LLM)

Function: generate_sql(question, schema)

User question + schema sent to LLM
Model: llama-3.3-70b-versatile (Groq)
Output: optimized SQL query
3. SQL Validation (Security Layer)

Function: validate_sql(query)

Security checks:

✔ Allows only SELECT queries
❌ Blocks:

DROP
DELETE
INSERT
UPDATE
ALTER
TRUNCATE

👉 Prevents SQL injection and destructive operations.

4. SQL Execution

Function: execute_sql(query)

Executes query on SQLite database
Fetches results
Converts output to JSON format
🌐 API Documentation
🔹 Endpoint
GET /ask
🔹 Example Request
http://127.0.0.1:8000/ask?question=How many tracks are in the Rock genre?
🔹 Example Response
{
  "response": {
    "question": "How many tracks are in the Rock genre?",
    "sql_query": "SELECT COUNT(*) FROM Track t JOIN Genre g ON t.GenreId = g.GenreId WHERE g.Name = 'Rock';",
    "answer": "COUNT(*): 1297"
  }
}

##🚀 Key Highlights
Natural Language → SQL conversion using LLM
Secure SQL validation layer
Read-only database enforcement
Real-time query execution
API-based architecture using FastAPI

##🔐 Security Features
Only SELECT queries allowed
Blocks destructive SQL operations
Prevents SQL injection attacks
Validates queries before execution

##📈 Future Improvements
Support for multiple databases (MySQL/PostgreSQL)
Advanced query optimization
Role-based access control (RBAC)
Web-based UI dashboard
Multi-table reasoning improvements

##🏆 Project Impact
This project demonstrates:
Real-world application of Generative AI
Secure backend system design
Database interaction using LLMs
Production-style API architecture
It highlights skills in AI + Backend + Security + System Design, making it highly relevant for research and abroad scholarship applications.

##👩‍💻 Author

Charuhasini
AI & Data Science Student
GitHub: https://github.com/Charuhasini30
