from vllm import LLM, SamplingParams

# Sample prompts.
prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]

messages = [
    {"role": "user", "prompt": "Can you provide ways to eat combinations of bananas and dragonfruits?"},
    {"role": "assistant", "prompt": "Sure! Here are some ways to eat bananas and dragonfruits together: 1. Banana and dragonfruit smoothie: Blend bananas and dragonfruits together with some milk and honey. 2. Banana and dragonfruit salad: Mix sliced bananas and dragonfruits together with some lemon juice and honey."},
    {"role": "user", "prompt": "What about solving an 2x + 3 = 7 equation?"},
]
# Create a sampling params object.
sampling_params = SamplingParams(temperature=0.0, max_tokens=500)

# Create an LLM.
llm = LLM(model="microsoft/Phi-3-medium-4k-instruct", tensor_parallel_size=2)
# Generate texts from the prompts. The output is a list of RequestOutput objects
# that contain the prompt, generated text, and other information.
outputs = llm.generate(messages, sampling_params)

print(outputs)