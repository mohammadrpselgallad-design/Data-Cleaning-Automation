import os
import tkinter as tk
from tkinter import filedialog

def clean_data(text):
    return text.strip().lower()

# 1. Create a hidden window for the file picker
root = tk.Tk()
root.withdraw()

print("🎯 Please select 'clients_raw_data.txt' from the window...")
input_file = filedialog.askopenfilename(title="Select Customer Data File", filetypes=[("Text files", "*.txt")])

if input_file:
    output_dir = os.path.dirname(input_file)
    output_file = os.path.join(output_dir, "cleaned_50_report.txt")
    
    print("🚀 Extracting and cleaning all 50 customers...")
    
    # Read the ENTIRE file content at once
    with open(input_file, "r", encoding="utf-8") as source:
        full_content = source.read()
    
    # THE PILLAR: Split the text block into individual lines automatically
    all_lines = full_content.splitlines()
    
    # Open destination file to write the clean organized list
    with open(output_file, "w", encoding="utf-8") as destination:
        destination.write("=== CLEANED CUSTOMER DATABASE (50 CLIENTS) ===\n\n")
        
        customer_count = 0
        for line in all_lines:
            if not line.strip() or "," not in line:
                continue
                
            parts = line.split(",")
            if len(parts) == 2:
                clean_name = clean_data(parts[0])
                clean_email = clean_data(parts[1])
                
                customer_count += 1
                destination.write(f"#{customer_count} | Client Name:  {clean_name}\n")
                destination.write(f"     | Client Email: {clean_email}\n")
                destination.write("-" * 45 + "\n")
                
    print(f"✨ Done! Successfully organized {customer_count} customers inside: '{output_file}'")
else:
    print("❌ Cancelled: You didn't select any file.")
