import ollama

def run_llm(context: str, input: str, model: str ='deepseek-r1:1.5b') -> str:
    '''Calls LLM using local Ollama instance'''
    model = model or 'deepseek-r1:1.5b'
    ollama.pull(model)
    response = ollama.generate(model, f"{context}\n\n{input}")
    return response['response']

def extract_code(input: str) -> str:
    '''Extracts Python code from LLM response'''
    return input.split('```python')[-1].split('```')[0].strip()

def load_prompt(prompt_name: str) -> str:
    '''Load prompt from text file'''
    prompt_file = open(f'./prompts/{prompt_name}')
    prompt = prompt_file.read()
    prompt_file.close()
    return prompt

def load_input(input_name: str) -> str:
    input_file = open(f'./test_cases/{input_name}')
    input = input_file.read()
    input_file.close()
    return input

def print_step(text: str) -> None:
    '''Print step name with formatting'''
    message = text.center(50, "=")
    print(message)