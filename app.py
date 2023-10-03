import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
# main dataset
gap=px.data.gapminder()
gap=pd.DataFrame(gap)
st.set_page_config(page_title="countries")
st.title("EXPLORATORY DATA ANALYSIS ON COUNTRIES DATASET")
st.markdown("<hr>", unsafe_allow_html=True)
st.write("TEAM MEMBERS")
st.markdown("- RUPAK 22BCE10127")
st.markdown("- Akshat Agrawal 22BCE10745")
st.markdown("- Prince Choudhary 22BCE10837.")
st.markdown("- MOHAK GOPALE 22BCG10079")
st.markdown("<hr>", unsafe_allow_html=True)
btn_1=st.button("click here to compare different countries")
btn_2=st.button("click here for EDA")
if btn_2:
    st.markdown("<hr>", unsafe_allow_html=True)
    st.write("_based on UN on data from 1952 TO 2007._")
    st.header("GDP Per Capita Income VS Life Expectancy")
    # plot animation of the above curve on the basic of year
    gdp_vs_pci=px.scatter(gap, x='lifeExp', y='gdpPercap',
            color='continent',size='pop',
            size_max=100, hover_name='country',
            range_x=[30,95],
            animation_frame='year',animation_group='country',color_continuous_scale='Magma')
    st.plotly_chart(gdp_vs_pci)
    st.subheader("Discription of the Graph")
    st.write("""


The graph illustrates the relationship between life expectancy (x-axis) and GDP per capita (y-axis) for countries around the world. Each data point represents a country, and the points are color-coded by continent. The size of each point corresponds to the population of the respective country, with larger points indicating larger populations. Additionally, the animation in the graph displays changes over time, with each frame representing a different year.

""")
    
    st.markdown("<hr>", unsafe_allow_html=True)
    # richest over the years 
    st.header("Richest countries over the years")
    df_sorted = gap.sort_values(by=['year', 'gdpPercap'], ascending=[True, False])
    top_10_by_year = df_sorted.groupby('year').head(10)
    top_eco=px.bar(top_10_by_year,x='country',y='gdpPercap',animation_frame='year')
    st.plotly_chart(top_eco)
    st.subheader("Discription of the graph")
    st.write("the above graph displays how the top 10 richest countries and their GDP per capita changes over the years")
    st.markdown("<hr>", unsafe_allow_html=True)
    # poorest over the years 
    st.header("Poorest countries over the years")
    df_sorted_2 = gap.sort_values(by=['year', 'gdpPercap'], ascending=[True, True])
    least_10_by_year = df_sorted_2.groupby('year').head(10)
    least_eco=px.bar(least_10_by_year,x='country',y='gdpPercap',animation_frame='year')
    st.plotly_chart(least_eco)
    st.subheader("Discription of the graph")
    st.write("the above graph displays how the top 10 poorest countries and their GDP per capita changes over the years")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.header("POPULATION TRENDS")
    conti_opt=gap['continent'].unique()
    year_opt=gap['year'].unique()
    selected_conti=st.selectbox('Choose a continent',conti_opt)
    selected_year=st.selectbox('Choose an year',year_opt)
    #  the pie chart of pop 

    temp_df = gap[(gap['year'] == selected_year) & (gap['continent'] == selected_conti)]
    pie_=px.pie(temp_df, values='pop', names='country')
    # btn_3=st.button("click here to display")
    # if btn_3:
    st.plotly_chart(pie_)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("SUNBURST CHART FOR POPULATION AND LIFE EXPECTANCY")
    temp_df = gap[gap['year'] == 2007]
    sun=px.sunburst(temp_df, path=['continent','country'],values='pop',color='lifeExp')
    st.plotly_chart(sun)
    st.subheader("discription of graph")
    st.write("""
The sunburst chart visually represents data related to the population and life expectancy of countries in the year 2007, organized by continent and country.

Key Observations:

Continent Hierarchy: The chart is structured as a hierarchical diagram starting with continents at the outermost level. Each continent is represented by a colored segment, and the size of the segment corresponds to the total population of all the countries within that continent.

Country Breakdown: As you move inward from the continents, the segments break down further into individual countries within each continent. Each country is color-coded based on its life expectancy, with warmer colors indicating higher life expectancy and cooler colors representing lower life expectancy.

Population and Life Expectancy: The chart's segments provide a visual representation of both population and life expectancy. The size of each segment (outer to inner) reflects population, with larger segments indicating higher population. Additionally, the color intensity within each country segment represents its life expectancy, allowing for a quick assessment of which countries have higher or lower life expectancies.""")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.header("life expectancy trends(heatmap)")
    temp_df = gap.pivot_table(index='year',columns='continent',values='lifeExp',aggfunc='mean')
    heat=px.imshow(temp_df)
    st.plotly_chart(heat)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.header(" 3d scatter plot of all country data for 2007")
    # 3d scatterplot
    # plot a 3d scatter plot of all country data for 2007
    temp_df_2 = gap[gap['year'] == 2007]
    scat_3d=px.scatter_3d(temp_df_2, x='lifeExp',y='pop',z='gdpPercap',log_y=True,color='continent',hover_name='country')
    st.plotly_chart(scat_3d)
# sidebar
st.sidebar.title("compare 2 countries")
country_opt=gap['country'].unique()
country1=st.sidebar.selectbox("first country ",country_opt)
country2=st.sidebar.selectbox("second country ",country_opt)
btn_3=st.sidebar.button("click to compare")
if btn_3:
    # LIFE EXP OVER THE YEARS
    st.markdown("<hr>", unsafe_allow_html=True)
    temp_df_exp = gap[gap['country'].isin([country1,country2])].pivot(index='year',columns='country',values='lifeExp')
    st.plotly_chart(px.line(temp_df_exp, x=temp_df_exp.index, y=temp_df_exp.columns,title="LIFE EXPECTANCY OVER THE YEARS"))
    st.markdown("<hr>", unsafe_allow_html=True)
    # population
    temp_df_pop = gap[gap['country'].isin([country1,country2])].pivot(index='year',columns='country',values='pop')
    st.plotly_chart(px.line(temp_df_pop, x=temp_df_pop.index, y=temp_df_pop.columns,title="POPULATION GROWTH OVER THE YEARS"))
    # gdp
    st.markdown("<hr>", unsafe_allow_html=True)
    temp_df_gdp = gap[gap['country'].isin([country1,country2])].pivot(index='year',columns='country',values='gdpPercap')
    st.plotly_chart(px.line(temp_df_gdp, x=temp_df_gdp.index, y=temp_df_gdp.columns,title="GDP PER CAPITA OVER THE YEARS"))
    st.markdown("<hr>", unsafe_allow_html=True)
if btn_1:
    st.write("customise your seleted countries from sidebar")
    
