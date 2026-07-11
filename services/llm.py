from langchain.chat_models import init_chat_model

class LLM:
    def __init__(
        self,
        model_name: str = "qwen/qwen3-32b",
        model_provider: str = "groq",
        temperature: float = 0.7,
    ):
        self.model_name = model_name
        self.model_provider = model_provider
        self.temperature = temperature

    def __repr__(self):
        return (
            f"LLM(model={self.model_name}, "
            f"provider={self.model_provider}, "
            f"temperature={self.temperature})"
        )

    def model(self):
        return init_chat_model(
            model=self.model_name,
            model_provider=self.model_provider,
            temperature=self.temperature,
        )