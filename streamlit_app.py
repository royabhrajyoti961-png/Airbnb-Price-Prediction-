import streamlit as st
import pandas as pd
from src.Airbnb.pipelines.Prediction_Pipeline import CustomData, PredictPipeline

# Set page config for a professional terminal/glassmorphism vibe
st.set_page_config(page_title="Airbnb Price Predictor", layout="centered")

st.title("📊 Airbnb Price Prediction Terminal")
st.markdown("---")

st.subheader("Property Characteristics")
# Create layout columns for the input fields
col1, col2 = st.columns(2)

with col1:
    property_type = st.selectbox("Property Type", ["Apartment", "House", "Condo", "Loft"])
    room_type = st.selectbox("Room Type", ["Entire home/apt", "Private room", "Shared room"])
    accommodates = st.number_input("Accommodates", min_value=1, max_value=16, value=2)
    bathrooms = st.number_input("Bathrooms", min_value=0.0, max_value=10.0, value=1.0, step=0.5)
    bedrooms = st.number_input("Bedrooms", min_value=0, max_value=10, value=1)
    beds = st.number_input("Beds", min_value=1, max_value=20, value=1)

with col2:
    city = st.selectbox("City", ["NYC", "LA", "SF", "DC", "Chicago", "Boston"])
    bed_type = st.selectbox("Bed Type", ["Real Bed", "Futon", "Pull-out Sofa", "Airbed"])
    cancellation_policy = st.selectbox("Cancellation Policy", ["strict", "flexible", "moderate"])
    cleaning_fee = st.selectbox("Cleaning Fee Included?", ["True", "False"])
    amenities = st.text_input("Amenities (e.g., TV, Wireless Internet)", "TV")

st.subheader("Host & Geolocation Metrics")
col3, col4 = st.columns(2)

with col3:
    host_has_profile_pic = st.selectbox("Host Has Profile Pic?", ["True", "False"])
    host_identity_verified = st.selectbox("Host Identity Verified?", ["True", "False"])
    host_response_rate = st.number_input("Host Response Rate (%)", min_value=0, max_value=100, value=100)
    instant_bookable = st.selectbox("Instant Bookable", ["True", "False"])

with col4:
    latitude = st.number_input("Latitude", value=40.7128, format="%.4f")
    longitude = st.number_input("Longitude", value=-74.0060, format="%.4f")
    number_of_reviews = st.number_input("Number of Reviews", min_value=0, value=10)
    review_scores_rating = st.number_input("Overall Review Rating", min_value=0, max_value=100, value=95)

st.markdown("---")

if st.button("🔮 Predict Rental Price", use_container_width=True):
    try:
        # Map inputs to your existing CustomData schema
        data = CustomData(
            property_type=property_type,
            room_type=room_type,
            amenities=amenities,
            accommodates=str(accommodates),
            bathrooms=str(bathrooms),
            bed_type=bed_type,
            cancellation_policy=cancellation_policy,
            cleaning_fee=cleaning_fee,
            city=city,
            host_has_profile_pic=host_has_profile_pic,
            host_identity_verified=host_identity_verified,
            host_response_rate=str(host_response_rate),
            instant_bookable=instant_bookable,
            latitude=str(latitude),
            longitude=str(longitude),
            number_of_reviews=str(number_of_reviews),
            review_scores_rating=str(review_scores_rating),
            bedrooms=str(bedrooms),
            beds=str(beds)
        )

        final_data = data.get_data_as_dataframe()

        # Run pipeline prediction
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_data)
        result = round(pred[0], 2)

        st.success(f"### Estimated Price: ${result} / night")

    except Exception as e:
        st.error(f"Error during execution: {e}")
