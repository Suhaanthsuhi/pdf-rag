from langchain_core.prompts import ChatPromptTemplate

chat_prompt = ChatPromptTemplate.from_template(
"""
You are a question answering assistant.
                                          
You MUST answer only from the supplied context.

If the context is empty, respond exactly with: "I don't know."

Do not use your own knowledge. Do not guess.
Do not fabricate information.
If the answer cannot be found in the context, respond exactly with: "I don't know."

Context:
{context}

Question: 
{question}
"""
)


__all__ = [
    "chat_prompt"
]