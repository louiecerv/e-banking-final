#Input the relevant libraries
import numpy as np
import pandas as pd
import streamlit as st
from scipy.stats import spearmanr
import scipy.stats as stats

# Define the Streamlit app
def app():

    st.subheader('Statistical Analysis on the Relationship of E-banking Usage and Infleunce on Spending Habits')
    text = """This part of the data app sought to answer this research question:
    Is there a significant relationship between e-banking usage and the influence on spending habits
    among College of Business and Management students?"""
    with st.expander("About the research question. CLick to expand."):
        st.write(text)

    df = pd.read_csv('correlation.csv', header=0)


    st.subheader("Spearman's rank correlation coefficient")
    text = """Spearman's rank correlation coefficient, denoted by the Greek letter rho (ρ), is a statistical 
    test used to measure the strength and direction of a monotonic relationship between two sets of data. 
    Unlike Pearson's correlation coefficient, which assumes a linear relationship, 
    Spearman's rank only cares about the order or rank of the data points.
    Monotonic Relationship: It assesses how well the relationship between two variables can be 
    described by a trend that consistently increases or decreases (either always going 
    up or always going down).
    Strength: The coefficient produces a value between 1 and -1. A value of 1 indicates a 
    perfect positive monotonic relationship (as one variable increases, the other always increases). 
    A value of -1 indicates a perfect negative monotonic relationship (as one variable increases, 
    the other always decreases). A value of 0 means no monotonic relationship.
    \nDirection: The positive or negative value reflects the direction of the monotonic trend."""
    st.write(text)

    st.subheader('Spearman Rank Order Correlation Coefficient of E-Banking Usage and Influence on Spending Habits')

    # Assuming your dataframe is called 'df'
    usage = df['Usage']
    influence = df['Influence']

    # Calculate Spearman's rank correlation coefficient
    spearman_coeff, p_value = spearmanr(usage, influence)

    # Print the results
    st.write("Spearman Rank Correlation Coefficient: {:.2f}".format(spearman_coeff))
    st.write("p-value: {:.4f}".format(p_value))
    
    text = """The Spearman rank correlation coefficient of 0.32 indicates a positive correlation 
    between e-banking usage and influence on spending habits. The Spearman correlation coefficient 
    ranges from -1 to 1. A value of 1 indicates a perfect positive monotonic relationship, 
    meaning that as one variable increases, the other variable also increases in a 
    consistent manner. A value of -1 indicates a perfect negative monotonic relationship, 
    where as one variable increases, the other variable decreases consistently. A value of 0 
    indicates no monotonic relationship between the variables.
    \nIn this case, a Spearman rank correlation coefficient of 0.32 suggests a 
    moderate positive monotonic relationship between e-banking usage and influence on 
    spending habits. It indicates that as e-banking usage increases, there is a tendency for 
    spending habits to also increase, but not necessarily in a linear manner.
    \nThe p-value of 0.0000 indicates that the observed correlation coefficient is statistically 
    significant at conventional levels of significance (e.g., α = 0.05). This means that we can 
    reject the null hypothesis that there is no correlation between e-banking usage and influence 
    on spending habits in favor of the alternative hypothesis that there is a correlation.
    \nTherefore, based on this interpretation, there is evidence to suggest that there is a 
    statistically significant, moderate positive correlation between e-banking usage and influence 
    on spending habits among the respondents of the questionnaire. However, it's important 
    to note that correlation does not imply causation, and other factors may also influence 
    spending habits aside from e-banking usage."""
    st.write(text)

#run the app
if __name__ == "__main__":
    app()
