import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

# Initialize the Translator
translator = Translator()

# Function to perform translation
def translate_text():
    try:
        input_text = In_text.get(1.0, tk.END)
        source_lang = src_lang.get()
        target_lang = dest_lang.get()

        if not input_text.strip():
            messagebox.showwarning("Input Error", "Please enter some text to translate.")
            return
        
        # Get the language code corresponding to the selected source language
        source_lang_code = [code for code, name in LANGUAGES.items() if name == source_lang]
        source_lang = source_lang_code[0] if source_lang_code else None

        # Get the language code for the target language
        target_lang_code = [code for code, name in LANGUAGES.items() if name == target_lang]
        target_lang = target_lang_code[0] if target_lang_code else None

        if source_lang is None or target_lang is None:
            messagebox.showwarning("Language Selection Error", "Please select valid source and target languages.")
            return

        # Perform the translation
        translation = translator.translate(input_text, src=source_lang, dest=target_lang)
        ou_text.delete(1.0, tk.END)
        ou_text.insert(tk.END, translation.text)
    except Exception as e:
        messagebox.showerror("Translation Error", f"An error occurred: {str(e)}")

# Function to filter languages based on user input
def filter_languages(event, combobox):
    typed_char = event.char.lower()
    if typed_char.isalpha():  # Ensure it's a letter
        filtered_languages = [name for name in LANGUAGES.values() if name.lower().startswith(typed_char)]
        combobox['values'] = filtered_languages
        if filtered_languages:
            combobox.set(filtered_languages[0])  # Set the first match as the current value

# Function to clear input and output
def clear_text():
    In_text.delete(1.0, tk.END)
    ou_text.delete(1.0, tk.END)
    src_lang.set(LANGUAGES['english'])  # Reset to English
    dest_lang.set(LANGUAGES['greek'])    # Reset to Greek

root = tk.Tk()
root.title("Multi-Language Translator")

# Set window size and center it on the screen
window_width = 1000
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate position to center the window
x_position = int((screen_width / 2) - (window_width / 2))
y_position = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Configure the root window layout for dynamic resizing
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Main frame that holds all widgets
main_frame = tk.Frame(root, bg="teal")
main_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

# Configure grid layout for the main frame
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_rowconfigure(1, weight=1)
main_frame.grid_rowconfigure(2, weight=1)
main_frame.grid_rowconfigure(3, weight=1)
main_frame.grid_rowconfigure(4, weight=1)
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)

# Header message
message = tk.Label(main_frame, text="Welcome to Multi-Language Translator!", font='Arial 20 bold', fg="white", bg="teal")
message.grid(row=0, column=0, columnspan=2, pady=25)

# Source language dropdown
label_src = tk.Label(main_frame, text="Source Language:", bg="skyblue", font=("Helvetica", 12))
label_src.grid(row=1, column=0, sticky="e", padx=10)
src_lang = ttk.Combobox(main_frame, values=list(LANGUAGES.values()), state="readonly", font=("Helvetica", 11))
src_lang.set("english")  # Default to English
src_lang.grid(row=1, column=1, sticky="w", padx=10)
src_lang.bind('<KeyRelease>', lambda event: filter_languages(event, src_lang))

# Target language dropdown
label_dest = tk.Label(main_frame, text="Translation Language:", bg="skyblue", font=("Helvetica", 12))
label_dest.grid(row=2, column=0, sticky="e", padx=10)
dest_lang = ttk.Combobox(main_frame, values=list(LANGUAGES.values()), state="readonly", font=("Helvetica", 11))
dest_lang.set("greek")  # Default to Greek
dest_lang.grid(row=2, column=1, sticky="w", padx=10)
dest_lang.bind('<KeyRelease>', lambda event: filter_languages(event, dest_lang))

# Input text box
input_label = tk.Label(main_frame, text="Enter your text to translate:", font='Arial 15 bold', fg="white", bg="teal")
input_label.grid(row=3, column=0, sticky="ne", padx=10)
In_text = tk.Text(main_frame, height=8, width=40, font="bold", padx=5, pady=5)
In_text.grid(row=3, column=1, sticky="nw", padx=10)

# Output text box
output_label = tk.Label(main_frame, text="The translated text is:", font='Arial 15 bold', fg="white", bg="teal")
output_label.grid(row=4, column=0, sticky="ne", padx=10)
ou_text = tk.Text(main_frame, height=8, width=40, font="bold", padx=5, pady=7)
ou_text.grid(row=4, column=1, sticky="nw", padx=10)

# Translate button
translate_button = tk.Button(main_frame, text="Translate", command=translate_text, bg="blue", fg="white", font=("Helvetica", 12))
translate_button.grid(row=5, column=0, columnspan=2, pady=20)

# Clear button
clear_button = tk.Button(main_frame, text="Clear", command=clear_text, bg="red", fg="white", font=("Helvetica", 12))
clear_button.grid(row=6, column=0, columnspan=2, pady=8)

root.mainloop()
