import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("matplotlib and seaborn visulization in streamlit")

##load the data
df = pd.read_csv("./tips.csv")

st.dataframe(df.head())

# st.markdown("---")
# with st.container():
#     st.write('1.Find number of male and female distribution (pie and bar)')
#     value_counts = df["sex"].value_counts()
#     #st.write(value_counts.index)
#     col1, col2 = st.columns(2)
#     with col1:
#         st.subheader('Line Chart')
#         ##draw pie count
#         # fig,ax = plt.subplots()
#         # ax.pie(value_counts, autopct = "%0.2f%%", labels = ['Male','Female'])
#         # st.pyplot(fig)
#         fig, ax = plt.subplots()
#         ax.plot(value_counts.index, value_counts.values, marker='o', linestyle='-', color='b')
#         ax.set_xlabel('Sex')
#         ax.set_ylabel('Count')
#         ax.set_title('Distribution of Male and Female')
#         # Annotate points
#         for i, txt in enumerate(value_counts.values):
#             ax.annotate(txt, (value_counts.index[i], value_counts.values[i]), textcoords="offset points", xytext=(0,10), ha='center')

#         st.pyplot(fig)

#     # ##draw pie count
#     # fig,ax = plt.subplots()
#     # ax.pie(value_counts, autopct = "%0.2f%%", labels = ['Male','Female'])
#     # st.pyplot(fig)
#     with col2:
#         st.subheader("Bar Chart")
#         #draw bar plot
#         fig,ax = plt.subplots()
#         ax.bar(value_counts.index,value_counts)
#         st.pyplot(fig)
#    # #draw bar plot
#     # fig,ax = plt.subplots()
#     # ax.bar(value_counts.index,value_counts)
#     # st.pyplot(fig)
#    ##put this is expander
#     with st.expander("Click here to display value counts"):
#         st.dataframe(value_counts)

# data_types = df.dtypes
# cat_cols = tuple(data_types[data_types == "object"].index)


# st.markdown("---")
# with st.container():
#     feature = st.selectbox("Select the Feature you want to display bar and pie chart", 
#                            cat_cols
#                            )
#     # st.write('1.Find number of male and female distribution (pie and bar)')
#     value_counts = df[feature].value_counts()
#     #st.write(value_counts.index)
#     col1, col2 = st.columns(2)
#     with col1:
#         st.subheader('Pie Chart')
#         ##draw pie count
#         fig,ax = plt.subplots()
#         ax.pie(value_counts,autopct="%0.2f%%", labels = value_counts.index)
#         st.pyplot(fig)

#     with col2:
#         st.subheader("Bar Chart")
#         #draw bar plot
#         fig,ax = plt.subplots()
#         ax.bar(value_counts.index,value_counts)
#         st.pyplot(fig)


#     ##put this is expander
#     with st.expander("Click here to display value counts"):
#         st.dataframe(value_counts)



##2 question : Find ditribution of Male and Female spent
st.markdown("----")
with st.container():
    st.write('2.Find ditribution of Male and Female spent')
    chart = ("box", "violin","kdeplot")
    chart_selection = st.selectbox("Select the chart type",chart)
    fig, ax = plt.subplots()
    if chart_selection == "box":
        sns.boxplot(x ='sex', y="total_bill",data = df, ax=ax)
    elif chart_selection == 'violin':
        sns.violinplot(x='sex',y ="total_bill",data=df, ax=ax)
    elif chart_selection == "kdeplot":
        sns.kdeplot(x =df['total_bill'], hue=df['sex'],ax=ax)
    # else:
    #     sns.histplot(x='total',hue = 'sex', data = df,ax=ax)
    #sns.boxplot(x="sex", y = "total_bill", data= df, ax=ax)

    st.pyplot(fig)

