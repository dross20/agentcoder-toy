from agent import generate_function, generate_refined_function, generate_test
from util import print_step, load_input
import argparse

parser = argparse.ArgumentParser(
    prog="Toy AgentCoder",
    description="Toy implementation of AgentCoder framework for multi-agent code generation"
)

parser.add_argument('-f', '--filename')

def run_agentcoder():
    args = parser.parse_args()
    input = load_input(args.filename or "1.txt")

    print_step("GENERATING CODE COMPLETION")
    function_completion = generate_function(input)
    print(function_completion)

    print_step("GENERATING UNIT TESTS")
    tests = generate_test(input)
    print(tests)

    while True:
        print_step("RUNNING UNIT TESTS")
        code = function_completion + "\n\n" + tests
        try:
            exec(code)
        except Exception as e:
            print_step("TESTS FAILED")
            print(e)

            print_step("GENERATING NEW CODE COMPLETION")
            function_completion = generate_refined_function(input, function_completion, e)
        else:
            print_step("TESTS SUCCEEDED")
            break

if __name__ == "__main__":
    run_agentcoder()