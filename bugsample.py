import ast
import tkinter as tk
from tkinter import scrolledtext

def check_syntax(code):
    """Check the syntax of the code and return error type and message if any."""
    try:
        ast.parse(code)  # Parse the code to check syntax
        return None  # No syntax errors
    except SyntaxError as e:
        return {
            "error_type": "SyntaxError",
            "message": e.msg,
            "line": e.lineno,
            "suggestion": "Check the syntax at the specified line. Common issues include missing colons, parentheses, or incorrect indentation."
        }

def execute_code(code):
    """Execute the code and return any runtime errors encountered."""
    try:
        exec(code, {})  # Execute the code in an isolated environment
        return None  # No runtime errors
    except Exception as e:
        return {
            "error_type": type(e).__name__,
            "message": str(e),
            "suggestion": "Check the traceback for more details. Ensure variables are properly defined and used correctly."
        }

def analyze_code(code):
    """Analyze the code for errors and provide feedback."""
    syntax_error = check_syntax(code)
    if syntax_error:
        return syntax_error

    runtime_error = execute_code(code)
    if runtime_error:
        return runtime_error

    return {"status": "No errors found. The code executed successfully."}

def analyze_button_click():
    """Handle button click event to analyze the code."""
    code = code_input.get("1.0", "end-1c")
    result = analyze_code(code)
    
    # Clear the output box
    result_output.delete(1.0, "end")

    if "status" in result:
        result_output.insert(tk.END, result["status"])
    else:
        result_output.insert(tk.END, f"Error Type: {result['error_type']}\n")
        result_output.insert(tk.END, f"Message: {result['message']}\n")
        result_output.insert(tk.END, f"Line: {result.get('line', 'N/A')}\n")
        result_output.insert(tk.END, f"Suggestion: {result['suggestion']}\n")



# Create the main window
root = tk.Tk()
root.title("Python Code Analyzer")



# Create a frame for buttons
button_frame = tk.Frame(root, bg='lightblue')
button_frame.pack(fill=tk.X, side=tk.TOP)



# Create a label for instruction
instruction_label = tk.Label(root, text="Enter your Python code below (type 'END' to finish):", font=("Helvetica", 14))
instruction_label.pack(pady=20)

# Create a scrollable text widget for code input
code_input = scrolledtext.ScrolledText(root, width=80, height=15, font=("Courier New", 12), wrap=tk.WORD)
code_input.pack(pady=10)

# Create a button to trigger code analysis
analyze_button = tk.Button(root, text="Analyze Code", command=analyze_button_click, font=("Helvetica", 14), bg="lightgreen", relief="raised")
analyze_button.pack(pady=20)

# Create a scrolled text widget for displaying results
result_output = scrolledtext.ScrolledText(root, width=80, height=10, font=("Courier New", 12), wrap=tk.WORD)
result_output.pack(pady=10)

# Run the GUI loop
root.mainloop()
