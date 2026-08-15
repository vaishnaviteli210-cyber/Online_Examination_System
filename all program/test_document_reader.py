from document_reader import extract_text


file_path = input("Enter complete document path: ")

text = extract_text(file_path)

if text:
    print("\nDocument read successfully.")
    print("-----------------------------")
    print(text[:100000])
else:
    print("Could not read the document.")