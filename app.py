import streamlit as st
import pandas as pd
import hashlib
from pathlib import Path

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Spare Part Authenticity Verification",
    layout="centered"
)

st.title("Spare Part Authenticity Verification Portal")
st.write(
    "Enter the Product ID to check whether the product is genuine, high risk, or counterfeit."
)

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    data_path = Path(__file__).parent / "data" / "product_quality_data.csv"
    return pd.read_csv(data_path)

df = load_data()

# -----------------------------
# PRODUCT CLASSIFICATION LOGIC
# -----------------------------
def classify_product(row):
    # HARD FAIL → COUNTERFEIT
    if (
        row["Packaging_Integrity"] == "No"
        or row["Serialization_Status"] == "No"
    ):
        return "Counterfeit"

    # SOFT FAIL → HIGH RISK
    elif row["Inspection_Score"] < 75:
        return "Genuine - High Risk"

    # PASS → LOW RISK
    else:
        return "Genuine - Low Risk"


# -----------------------------
# BLOCKCHAIN HASH (SIMULATED)
# -----------------------------
def generate_blockchain_hash(row, authenticity_status):
    record = (
        row["Product_ID"]
        + row["Batch_ID"]
        + row["Component_Type"]
        + row["Supplier_ID"]
        + str(row["Inspection_Score"])
        + row["Packaging_Integrity"]
        + row["Serialization_Status"]
        + authenticity_status
    )
    return hashlib.sha256(record.encode()).hexdigest()


# -----------------------------
# USER INPUT
# -----------------------------
product_id = st.text_input(
    "Enter Product ID (e.g., P301-01)"
).strip()

# -----------------------------
# VERIFY BUTTON
# -----------------------------
if st.button("Verify Product"):

    result = df[df["Product_ID"] == product_id]

    if result.empty:
        st.error("❌ Product ID not found in the system.")

    else:
        row = result.iloc[0]
        status = classify_product(row)

        if status == "Counterfeit":
            st.error("❌ Product is COUNTERFEIT")
        elif status == "Genuine - High Risk":
            st.warning("⚠️ Product is GENUINE but HIGH RISK")
        else:
            st.success("✅ Product is GENUINE and LOW RISK")

        st.subheader("Product Details")
        st.write("**Product ID:**", row["Product_ID"])
        st.write("**Batch ID:**", row["Batch_ID"])
        st.write("**Component Type:**", row["Component_Type"])
        st.write("**Supplier ID:**", row["Supplier_ID"])
        st.write("**Inspection Score:**", row["Inspection_Score"])
        st.write("**Packaging Integrity:**", row["Packaging_Integrity"])
        st.write("**Serialization Status:**", row["Serialization_Status"])
        st.write("**Risk Classification:**", status)

        st.subheader("Blockchain Verification Proof")
        blockchain_hash = generate_blockchain_hash(row, status)
        st.code(blockchain_hash)
