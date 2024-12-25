import gradio as gr

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