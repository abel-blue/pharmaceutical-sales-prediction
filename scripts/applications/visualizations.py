import streamlit as st
import pandas as pd
import sys
import pickle


def app():

    st.title("Rosmann Pharmaceutical Sales Prediction")

    st.header("Distribution and Visualization of the pharmaceutical Data")

    st.subheader("Correlation Analysis")
    st.image('images/correlation_analysis.png')

    st.subheader("Open Stores On Week Days")
    st.image('images/openStores_onWeekDays.png')

    st.subheader("Customer Behaviour On Store Open and Close Time")
    st.image('images/customer_behaviour_onStoreOpenCloseTime.png')

    st.subheader("Assortment Effect On Sales")
    st.image('images/assortment_effect.png')

    st.subheader("Competitor Distance Effect On Sales")
    st.image('images/compettor_distance_effect.png')

    st.subheader("Promotion Distribution On Train and Test Data")
    st.image('images/promotion_distribution_OntrainData.png')

    st.subheader("Open Stores on WeekDays")
    st.image('images/openStores_onWeekDays.png')

    st.subheader("promotion and month relation")
    st.image('images/promo_month_relation.png')

    st.subheader("promotion and customer relation")
    st.image('images/promotion_customer_relation.png')

    st.subheader("promotion distribution On trainData")
    st.image('images/promotion_distribution_OntrainData.png')

    st.subheader("promotion and sales relation")
    st.image('images/promotion_sales_relation.png')

    st.subheader("sales and cusotmer relation on DaysOfWeek")
    st.image('images/sales_cusotmer_onDaysOfWeek.png')

    st.subheader("sales and customer on Holidays")
    st.image('images/sales_customer_onHoliday.png')

    st.subheader("sales and customer relation on Specific Holidays")
    st.image('images/sales_customer_onSpecificHolidays.png')

    st.subheader("sales and customers relations on Store Type")
    st.image('images/sales_customers_onStoreType.png')

    st.subheader("sales on weekDays")
    st.image('images/sales_onweekDays.png')

    st.subheader("storeType open Count within WeekDays")
    st.image('images/storeType_openCountwithInWeekDays.png')

    st.header("Model Analysis")

    st.subheader("test and val loss plot")
    st.image('images/test_val_plot.png')

    st.subheader("Feature Importance on model")
    st.image('images/featureImportanceOfAmodel.png')

    st.subheader("Prediciton image - Time Series")
    st.image('images/Prediciton image.png')
