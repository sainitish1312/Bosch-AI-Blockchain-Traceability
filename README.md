# Bosch India – AI & Blockchain Enabled Spare Part Traceability

An academic prototype for product-level spare-part authenticity verification inspired by Bosch India's digital transformation and aftermarket traceability challenges.

## Project Overview

The application verifies an automotive spare part using:

- Product ID
- Batch ID
- Component type
- Supplier ID
- Inspection score
- Packaging integrity
- Serialization status

The system classifies a product into:

1. **Counterfeit** – packaging integrity or serialization fails.
2. **Genuine - High Risk** – authenticity checks pass, but inspection score is below 75.
3. **Genuine - Low Risk** – authenticity checks pass and inspection score is 75 or higher.

A SHA-256 hash is generated as a **blockchain-inspired verification proof**. This is a simulation/prototype rather than a full distributed blockchain network.

## Tech Stack

- Python
- Streamlit
- Pandas
- SHA-256 / Python `hashlib`
- Jupyter Notebook

## Repository Structure

```text
Bosch-AI-Blockchain-Traceability/
├── app.py
├── product_verification.ipynb
├── requirements.txt
├── .gitignore
├── data/
│   └── product_quality_data.csv
└── docs/
    └── DT_Team-6_Project_Report.pdf
```

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

The application will open in your browser.

## Example Test Products

The project report demonstrates three scenarios:

- `P310-10` → Counterfeit
- `P302-02` → Genuine - High Risk
- `P301-01` → Genuine - Low Risk

## Academic Context

This project was developed as a digital transformation and supply-chain traceability case study focused on Bosch India, with a proposed AI and blockchain approach for aftermarket integrity and counterfeit-product detection.

> **Note:** The dataset is synthetic and industry-aligned for academic/prototype purposes. The blockchain component generates a cryptographic verification hash; it does not implement a production distributed ledger.
