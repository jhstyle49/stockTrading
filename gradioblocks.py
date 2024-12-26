import yfinance as yf 
import pandas as pd
import numpy as np

import gradio as gr

ticker_usd = ['^GSPC', '^SP500TR']
result=yf.download(ticker_usd, start='1900-01-01')
result.columns = ['_'.join(c) for c in result.columns]
result = result.reset_index()
result['Date'] = result['Date'].dt.strftime('%Y-%m-%d')
result['Date'] = pd.to_datetime(result['Date'])

remain_cols = []
for t in ticker_usd:
    remain_cols.append(f"Close_{t}")
    
result = result[['Date']+remain_cols]
result = result.dropna()
result_mon = result.copy()
result_year = result.copy()

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

# iface = gr.Interface(fn=greet, inputs="text", outputs="text")
# iface.launch(share=True)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)

demo.launch()

