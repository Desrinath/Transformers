import ollama

def ask_llm(context, question):

    prompt = f"""
    Answer ONLY from the provided context.

    Context:
    {context}

    Question:
    {question}
    """

    response = ollama.chat(
        model='mistral',
        messages=[
            {
                'role':'user',
                'content':prompt
            }
        ]
    )

    return response['message']['content']