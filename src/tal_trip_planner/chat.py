import streamlit as st
#from llm import send_request 
import pandas as pd
from tal_trip_planner.main import run
from flask import jsonify
import json

def main():
    st.set_page_config(page_title="Travel Planner", layout="wide")
    st.markdown(
    """
    <style>
    /* Background */
    .stApp {
        background: linear-gradient(135deg, #f8f9fa, #ffffff);
        color: #333;
        font-family: 'Poppins', sans-serif;
    }

    /* Logo */
    header .stAppViewContainer {
        background-color: #16a085; /* Talentica Green */
        padding: 10px;
    }

    /* Titles and headings */
    h1, h2, h3 {
        color: #16a085; /* Talentica Green */
        text-align: center;
        font-weight: bold;
    }

    /* Input box */
    .stTextInput>div>div>input {
        background-color: white;
        color: black;
        border-radius: 8px;
        border: 2px solid #16a085;
        padding: 10px;
    }

    /* Buttons */
    .stButton>button {
        background-color: #16a085; /* Talentica Green */
        color: white;
        border-radius: 8px;
        padding: 10px;
        font-size: 16px;
        border: none;
        transition: 0.3s;
        font-weight: bold;
    }

    .stButton>button:hover {
        background-color: #12876f;
        transform: scale(1.05);
    }

    /* Response success box */
    .stAlert {
        background-color: #e0f2f1;
        color: #000000 !important;
        border-radius: 8px;
        padding: 10px;
    }

    /* Table styling */
    table {
        width: 100%;
        border-collapse: collapse;
        border-radius: 10px;
        overflow: hidden;
    }

    th {
        background-color: #16a085; /* Talentica Green */
        color: white;
        font-size: 16px;
        padding: 12px;
        text-align: center;
    }

    tr:nth-child(even) {
        background-color: #f1f8e9; /* Soft Green */
    }

    tr:nth-child(odd) {
        background-color: #ffffff;
    }

    td {
        padding: 10px;
        border-bottom: 1px solid #ddd;
        text-align: center;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #16a085; /* Talentica Green */
        color: white;
    }
</style>

<div style="display: flex; align-items: center;">
        <img src="https://www.talentica.com/wp-content/uploads/2021/09/Talentica-Logo.svg" 
             width="180" style="margin-right: 10px;">
        <h1 style="color: #16a085;">Travel Planner ✈️</h1>
    </div>
    """,
    unsafe_allow_html=True
)
    # st.title("✨ Travel Planner ✈️")

    # Input field for user message
    st.markdown("""
    Enter your travel details in the following format:
    ```
    name, source, destination, travel_date (YYYY-MM-DD), preferred_method
    ```
    Example: Ramesh, Bangalore, Puner, 2025-02-28, flight
    
    Note: travel_date and preferred_method are optional
    """)
    user_message = st.text_input("Enter your travel details:")

    if st.button("Submit"):
        if user_message.strip():
            try:
                # Parse the comma-separated input
                params = [param.strip() for param in user_message.split(',')]

                
                # Validate input
                if len(params) < 2:
                    st.error("Please enter at least source and destination separated by comma.")
                    return
                
                name = params[0]
                source = params[1]
                destination = params[2]
                travel_date = params[3] if len(params) > 2 else None
                preferred_method = params[4] if len(params) > 3 else 'flight'

                with st.spinner("Sending request..."):
                    raw_response = run(name,source, destination, travel_date, preferred_method)

                    st.success("Response received!")
                    data = f"{raw_response}"
                    flattened_data = []
                    for entry in raw_response:
                        recommendation = entry.get("recommendation")
                        for traveler in entry["travelers"]:
                            for route in traveler["routes"]:
                                flattened_data.append(
                                    {
                                        "Traveler": name,
                                        "Route No": route["route_no"],
                                        "Travel Date": route["travel_date"],
                                        "Origin": route["origin"],
                                        "Transport Modes": route["transport_modes"],
                                        "Stops": route["stops"],
                                        "Operators": route["operators"],
                                        "Departure - Arrival": route["departure_arrival"],
                                        "Total Time": route["total_time"],
                                        "Total Cost": route["total_cost"],
                                    }
                                )

                # Convert list of dictionaries to DataFrame
                df = pd.DataFrame(flattened_data)

                # Streamlit app
                st.markdown('<h1 class="title">Travel Routes Overview</h1>', unsafe_allow_html=True)

                st.dataframe(df.style.set_properties(**{
                    "background-color": "white",
                    "border-radius": "5px",
                    "color": "#212529",
                    "border": "1px solid #ddd"
                }))
                st.markdown('<h3 class="title">Recommendation</h3>', unsafe_allow_html=True)
                st.markdown(recommendation)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please enter a message before submitting.")


if __name__ == "__main__":
    main()