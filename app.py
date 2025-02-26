import streamlit as st
from PIL import Image
from core import extract_text, extract_invoice_details, save_to_airtable, calculate_automatic_tax

def ocr_mode():
    st.subheader("Upload an Image")
    uploaded_file = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        text = extract_text(image)
        st.subheader("Extracted Text:")
        st.text_area("", text, height=200)

        details = extract_invoice_details(text)
        st.subheader("Extracted Invoice Details:")
        st.json(details)

        if st.button("Save to Airtable"):
            save_to_airtable(details)
            st.success("Data saved to Airtable successfully!")

def indian_tax_calculator():
    st.subheader("Indian GST Tax Calculator")
    input_method = st.radio("Select Input Method", ["Automatic Calculation", "Manual Entry"])

    if input_method == "Automatic Calculation":
        base_amount = st.number_input("Enter Base Amount (in INR)", min_value=0.0, value=0.0, step=0.01, key='auto_base')
        gst_rate = st.selectbox("Select GST Rate (%)", options=[5, 12, 18, 28], key='auto_rate')
        sale_type = st.selectbox("Select Sale Type", options=["Intra-State", "Inter-State"], key='auto_sale')

        if st.button("Calculate Tax"):
            tax_results = calculate_automatic_tax(base_amount, gst_rate, sale_type)
            st.write("**Base Amount:** INR", base_amount)
            if sale_type == "Intra-State":
                st.write("**CGST ({}%):** INR".format(gst_rate/2), tax_results.get("CGST"))
                st.write("**SGST ({}%):** INR".format(gst_rate/2), tax_results.get("SGST"))
            else:
                st.write("**IGST ({}%):** INR".format(gst_rate), tax_results.get("IGST"))
            st.write("**Total Amount:** INR", tax_results.get("Total Amount"))
            
            calculated_data = {
                "Input Method": "Automatic",
                "Base Amount": base_amount,
                "GST Rate": gst_rate,
                "Sale Type": sale_type
            }
            calculated_data.update(tax_results)
            
            if st.button("Save Calculated Data to Airtable"):
                save_to_airtable(calculated_data)
                st.success("Data saved to Airtable successfully!")
    else:
        st.subheader("Manual Data Entry")
        invoice_number = st.text_input("Invoice Number", "")
        date = st.text_input("Date (DD/MM/YYYY)", "")
        base_amount_manual = st.number_input("Enter Base Amount (in INR)", min_value=0.0, value=0.0, step=0.01, key='manual_base')
        gst_rate_manual = st.selectbox("Select GST Rate (%)", options=[5, 12, 18, 28], key='manual_rate')
        sale_type_manual = st.selectbox("Select Sale Type", options=["Intra-State", "Inter-State"], key='manual_sale')

        computed_tax = st.checkbox("Compute Tax Automatically from Base Amount?")
        if computed_tax:
            tax_results = calculate_automatic_tax(base_amount_manual, gst_rate_manual, sale_type_manual)
            if sale_type_manual == "Intra-State":
                st.write("Calculated CGST: INR", tax_results.get("CGST"))
                st.write("Calculated SGST: INR", tax_results.get("SGST"))
            else:
                st.write("Calculated IGST: INR", tax_results.get("IGST"))
            tax_data = {
                "Input Method": "Manual (Computed)",
                "Invoice Number": invoice_number,
                "Date": date,
                "Base Amount": base_amount_manual,
                "GST Rate": gst_rate_manual,
                "Sale Type": sale_type_manual
            }
            tax_data.update(tax_results)
        else:
            cgst_manual = st.number_input("Enter CGST (if applicable)", min_value=0.0, value=0.0, step=0.01, key='manual_cgst')
            sgst_manual = st.number_input("Enter SGST (if applicable)", min_value=0.0, value=0.0, step=0.01, key='manual_sgst')
            igst_manual = st.number_input("Enter IGST (if applicable)", min_value=0.0, value=0.0, step=0.01, key='manual_igst')
            total_manual = st.number_input("Enter Total Amount (in INR)", min_value=0.0, value=0.0, step=0.01, key='manual_total')
            tax_data = {
                "Input Method": "Manual",
                "Invoice Number": invoice_number,
                "Date": date,
                "Base Amount": base_amount_manual,
                "GST Rate": gst_rate_manual,
                "Sale Type": sale_type_manual,
                "CGST": cgst_manual,
                "SGST": sgst_manual,
                "IGST": igst_manual,
                "Total Amount": total_manual
            }
        if st.button("Save Manual Data to Airtable"):
            save_to_airtable(tax_data)
            st.success("Data saved to Airtable successfully!")

def main():
    st.sidebar.title("Navigation")
    mode = st.sidebar.radio("Select Mode", ("OCR", "Tax Calculator"))

    if mode == "OCR":
        st.title("OCR for Receipts and Tax Invoices")
        ocr_mode()
    elif mode == "Tax Calculator":
        st.title("Indian GST Tax Calculator")
        indian_tax_calculator()

if __name__ == "__main__":
    main()
