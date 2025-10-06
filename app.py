import gradio as gr
from prompts import build_prompt
from llm_groq import groq_generate

def chat_fn(history, user_input):
    # Format previous turns for context
    history_str = ""
    for user, bot in history:
        history_str += f"User: {user}\nBot: {bot}\n"
    history_str += f"User: {user_input}\nBot:"

    prompt = build_prompt(history_str)
    response = groq_generate(prompt)
    history = history + [[user_input, response]]
    return history, history, ""

with gr.Blocks() as demo:
    gr.Markdown("# Persona Voice Bot\nAsk questions to Danish Akhtar's AI persona.")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Your question", placeholder="Type your question and press Enter")
    clear = gr.Button("Clear chat")

    def reset():
        return [], [], ""

    # Note: Pass and return history for both chatbot and state
    msg.submit(chat_fn, [chatbot, msg], [chatbot, chatbot, msg], queue=False)
    clear.click(reset, [], [chatbot, chatbot, msg], queue=False)

demo.launch()