
import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Display Title and Description
st.title("Report Lost Item Form")
st.sidebar.success("Select a page above.")
st.markdown("Enter the details of the lost item below.")

# Establishing a Google Sheets connection
conn = st.connection("gsheets", type=GSheetsConnection)

# Fetch existing lost entry data
existing_data = conn.read(worksheet="Lost_Entry", usecols=list(range(14)), ttl=5)
existing_data = existing_data.dropna(how="all")

st.dataframe(existing_data)

#=======Form

with st.form(key="lost_entry_form"):
    full_name = st.text_input(label="Full Name*")
    address = st.text_input("Address*")
    phone_num = st.text_input("Phone Number*")
    email = st.text_input("Email Address*")
    item_type = st.text_input(label="Item Type*")
    brand = st.text_input(label="Brand")
    color = st.text_input(label="Color")
    features = st.text_input(label="Features")
    date_lost = st.date_input(label="Date of Loss")
    time_lost= st.time_input(label="Time of Loss")
    date_last = st.date_input(label="Date Last Seen")
    time_last = st.time_input(label="Time last seen")
    location = st.text_input(label="Location where item was lost.")
    add_details = st.text_input(label="Additional Details")

    # Mark mandatory fields
    st.markdown("**required*")

    submit_button = st.form_submit_button(label="Submit Vendor Details")

    # If the submit button is pressed
    if submit_button:
        # Check if all mandatory fields are filled
        if not full_name or not address or not phone_num or not email:
            st.warning("Ensure all mandatory fields are filled.")
            st.stop()

        else:
            # Create a new row of vendor data
            vendor_data = pd.DataFrame(
                [
                    {
                        "Full Name": full_name,
                        "Address": address,
                        "Phone Number": phone_num,
                        "Email Adress": email,
                        "Type of Item": item_type,
                        "Brand": brand,
                        "Color": color,
                        "Features": features,
                        "Date of Loss": date_lost,
                        "Time of Loss": time_lost,
                        "Date Last Seen": date_last,
                        "Time Last Seen": time_last,
                        "Location Lost": location,
                        "Additional Details": add_details,
                    }
                ]
            )

            # Add the new vendor data to the existing data
            updated_df = pd.concat([existing_data, vendor_data], ignore_index=True)

            # Update Google Sheets with the new vendor data
            conn.update(worksheet="Lost_Entry", data=updated_df)

            st.success("Lost Item details successfully submitted!")