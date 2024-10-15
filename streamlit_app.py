import streamlit as st
import pandas as pd

st.title('GitHub Repository Analysis App')

# File uploader
upload_file = st.file_uploader("Upload your CSV file")

if upload_file is not None:
    df = pd.read_csv(upload_file)

    # Display the DataFrame
    st.write(df)

    # Sidebar filters
    st.sidebar.title("Filters")
    topic = st.sidebar.selectbox("Select Topic", df['Programming_Language'].unique())
    min_stars = st.sidebar.slider("Minimum Stars", 0, int(df['Number_of_Stars'].max()), 100)
    min_forks = st.sidebar.slider("Minimum Forks", 0, int(df['Number_of_Forks'].max()), 10)
    license_type = st.sidebar.selectbox("Select License Type", df['License_Type'].unique())

    # Display filters
    st.write(f"Topic: {topic}")
    st.write(f"Minimum Stars: {min_stars}")
    st.write(f"Minimum Forks: {min_forks}")
    st.write(f"License Type: {license_type}")

    # Filter data
    filtered_df = df[(df['Programming_Language'] == topic) &
                     (df['Number_of_Stars'] >= min_stars) &
                     (df['Number_of_Forks'] >= min_forks)&
                     (df['License_Type'] == license_type)&
                     (df['Number_of_Stars'] >= min_stars) &
                     (df['Number_of_Forks'] >= min_forks)]


    # Display filtered data
    st.write(f"Repositories with {min_stars}+ stars and {min_forks}+ forks in {topic}")
    st.dataframe(filtered_df)

    # Visualization
    st.bar_chart(filtered_df[['Repository_Name', 'Number_of_Stars']].set_index('Repository_Name'))
else:
    st.write("Please upload a CSV file.")
