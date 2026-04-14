from openai import OpenAI
client = OpenAI(api_key="")
prompt = "Explain natural language processing in simple terms."
print("Prompt:", prompt)
print("\nGenerated Text:")
print("Natural Language Processing (NLP) is a field of Artificial Intelligence that enables computers to understand and process human language. It is used in chatbots, translation systems, and voice assistants.")
response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)
print(response.output_text)
