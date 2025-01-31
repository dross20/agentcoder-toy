from util import run_llm, extract_code, load_prompt

FUNCTION_PROMPT_FN = "generate_function_prompt.txt"
REFINE_FUNCTION_PROMPT_FN = "generate_refined_function_prompt.txt"
TEST_PROMPT_FN = "generate_test_prompt.txt"

function_context = load_prompt(FUNCTION_PROMPT_FN)
refine_function_context = load_prompt(REFINE_FUNCTION_PROMPT_FN)
test_context = load_prompt(TEST_PROMPT_FN)

def _generate_code(context: str, input: str, model: str = None) -> str:
    """Generate LLM response and extract Python code."""
    raw_response = run_llm(context, input, model)
    code = extract_code(raw_response)
    return code

def generate_function(input: str, model: str = None) -> str:
    """Generate LLM response from function generation prompt."""
    return _generate_code(function_context, input, model)

def generate_refined_function(input: str, old_completion: str, exception: str, model: str = None) -> str:
    """Generate LLM response from refined function generation prompt and a past generation attempt."""
    input_final = f"Previous attempt:\n{old_completion}\nException thrown:\n{exception}\nInput:\n{input}"
    return _generate_code(refine_function_context, input_final, model)

def generate_test(input: str, model: str = None) -> str:
    """Generate LLM response from unit test prompt."""
    return _generate_code(test_context, input, model)