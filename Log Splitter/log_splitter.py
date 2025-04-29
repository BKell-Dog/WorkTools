import tkinter as tk
from tkinter import filedialog, messagebox

def extract_segment_between_delimiters(input_file, start_delimiter, end_delimiter, output_file):
    with open(input_file, 'r') as file:
        content = file.read()

    # Find the first occurrence of the start delimiter
    start_index = content.find(start_delimiter)
    if start_index == -1:
        print(f"Start delimiter '{start_delimiter}' not found in the file.")
        return

    if end_delimiter:
        # Find the first occurrence of the end delimiter after the start delimiter
        end_index = content.find(end_delimiter, start_index)
        if end_index == -1:
            print(f"End delimiter '{end_delimiter}' not found in the file.")
            return
        # Extract the segment between the delimiters
        segment = content[start_index:end_index + len(end_delimiter)]
    else:
        # Extract the segment from the start delimiter to the end of the file
        segment = content[start_index:]

    # Write the segment to the new file
    with open(output_file, 'w') as file:
        file.write(segment)

    print(f"Segment has been extracted and saved as '{output_file}'.")

def select_input_file():
    file_path = filedialog.askopenfilename(title="Select the input file")
    input_file_entry.delete(0, tk.END)
    input_file_entry.insert(0, file_path)

def save_output_file():
    file_path = filedialog.asksaveasfilename(title="Save the output file as", defaultextension=".txt")
    output_file_entry.delete(0, tk.END)
    output_file_entry.insert(0, file_path)

def run_extraction():
    input_file = input_file_entry.get()
    start_delimiter = start_delimiter_entry.get()
    end_delimiter = end_delimiter_entry.get()
    output_file = output_file_entry.get()

    if not input_file:
        messagebox.showerror("Error", "No input file selected.")
        return
    if not start_delimiter:
        messagebox.showerror("Error", "No start delimiter entered.")
        return
    if not output_file:
        messagebox.showerror("Error", "No output file selected.")
        return

    extract_segment_between_delimiters(input_file, start_delimiter, end_delimiter, output_file)
    messagebox.showinfo("Success", f"Segment has been extracted and saved as '{output_file}'.")

# Create the main window
root = tk.Tk()
root.title("Log Splitter.py")

# Title and subtitle
tk.Label(root, text="Log Splitter.py", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=3, padx=10, pady=10)
subtitle = ("Split any log or text file based on delimiters to help you parse data faster. "
            "This script will either split a file at the first instance of the start delimiter and save the second half, "
            "or extract a segment of the file between a start and end delimiter.")
tk.Label(root, text=subtitle, font=("Helvetica", 10), wraplength=400, justify="center").grid(row=1, column=0, columnspan=3, padx=10, pady=5)

# Input file selection
tk.Label(root, text="Input Log File:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
input_file_entry = tk.Entry(root, width=50)
input_file_entry.grid(row=2, column=1, padx=10, pady=5)
tk.Button(root, text="Browse...", command=select_input_file).grid(row=2, column=2, padx=10, pady=5)

# Start delimiter entry
tk.Label(root, text="Start Delimiter:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
start_delimiter_entry = tk.Entry(root, width=50)
start_delimiter_entry.grid(row=3, column=1, padx=10, pady=5)

# End delimiter entry
tk.Label(root, text="End Delimiter (leave blank to go to the end of the file):").grid(row=4, column=0, padx=10, pady=5, sticky="e")
end_delimiter_entry = tk.Entry(root, width=50)
end_delimiter_entry.grid(row=4, column=1, padx=10, pady=5)

# Output file selection
tk.Label(root, text="Output File:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
output_file_entry = tk.Entry(root, width=50)
output_file_entry.grid(row=5, column=1, padx=10, pady=5)
tk.Button(root, text="Browse...", command=save_output_file).grid(row=5, column=2, padx=10, pady=5)

# Run button
tk.Button(root, text="Run", command=run_extraction).grid(row=6, column=1, padx=10, pady=20)

# Start the GUI event loop
root.mainloop()
