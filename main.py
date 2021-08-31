import streamlit as st
from datetime import date
import yfinance as yf
#from fbprophet import Prophet
#from fbprophet.plot import plot_plotly
from plotly import graph_objs as go
start = "2015-01-01"
end = date.today().strftime("%Y-%m-%d")
st.title("Stock Prediction model")
stocks =("AAPL","GOOG","MSFT","GME")
selected_stock = st.selectbox("Select Dataset for prediction", stocks)
n_years = st.slider("Year of prediction",1,4)
period = n_years*365
@st.cache
def load_data(ticker):
    data = yf.download(ticker,start,end)
    data.reset_index(inplace = True)
    return data
data_load_state = st.text("Load Data...")
data = load_data(selected_stock)
data_load_state.text("Loading data...done")
st.subheader("raw data")
st.write(data.tail())
def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x = data['Date'], y = data['Open'], name ='Stock open'))
    fig.add_trace(go.Scatter(x = data['Date'], y = data['Close'], name ='Stock Close'))
    fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)
plot_raw_data()   
