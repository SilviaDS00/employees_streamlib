import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Data employees') # title

# Add url and column name
DATA_URL = ("../data/employees.csv") # url

# Load data
@st.cache_data # cache data
def load_data(nrows): # nrows: number of rows
    data = pd.read_csv(DATA_URL, nrows=nrows) # read data
    lowercase = lambda x: str(x).lower() # convert to lowercase
    data.rename(lowercase, axis='columns', inplace=True) # rename columns
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...') # text element
# Load 10,000 rows of data into the dataframe.
data = load_data(20) # load data
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache_data)") # text element

# Add checkbox for plot data on a table
if st.checkbox('Show employees'): # add checkbox
    st.write(data) # write data

# Plot data on a histogram
st.subheader('Salary') # subheader

# Filter data
col1, col2, col3 = st.columns(3)
# En la primera columna, muestra el selector de color
color = col1.color_picker('Choose a color', '#B07ECA')
# En la segunda columna, muestra el interruptor 'Show names'
show_names = col2.toggle('Show names', True)
# En la tercera columna, muestra el interruptor 'Show salaries'
show_salaries = col3.toggle('Show salaries', False)

# Crea un control deslizante para seleccionar un rango de salario
salary_range = st.slider('Salary range', int(data['salary'].min()), int(data['salary'].max()), (int(data['salary'].min()), int(data['salary'].max())))

# Filtra los datos por el rango de salario seleccionado
filtered_data = data[(data['salary'] >= salary_range[0]) & (data['salary'] <= salary_range[1])]

# Crea un gráfico de barras con los nombres de los empleados en el eje y y los salarios en el eje x
plt.figure(figsize=(8, 7)) # tamaño del gráfico
if show_names:
    plt.barh(filtered_data['full name'], filtered_data['salary'], color=color)
    plt.ylabel('Employee')
    plt.xlim(0, 4500)
else:
    plt.yticks([]) 
    plt.barh(range(len(filtered_data)), filtered_data['salary'], color=color)
    plt.xlim(0, 4500)

if show_salaries:
    for i, v in enumerate(filtered_data['salary']): # i: índice, v: valor
        plt.text(v + 6, i - 0.15, str(v) + "€") # añade el texto al gráfico


plt.xlabel('Salary')
plt.title('Salaries of Employees')

# Muestra el gráfico en Streamlit
st.pyplot(plt.gcf())  # gcf() significa 'get current figure'
