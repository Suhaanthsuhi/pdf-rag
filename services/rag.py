class RagService:
    def __init__(self, vector_store, prompt, llm):
        self.vector_store = vector_store
        self.prompt = prompt
        self.llm = llm

    def answer(self, question: str):
        # fetch the similarity search btw query & docs
        chunks = self.vector_store.similarity_search(question)
        
        context = "\n\n".join(
            chunk.content
            for chunk in chunks
        )

        prompt = self.prompt.invoke(
            {
                "context": context,
                "question": question,
            }
        )

        return self.llm.invoke(prompt)

