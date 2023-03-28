def split_text_file(input_file, output_prefix, max_chars=2048):
    with open(input_file, "r") as infile:
        content = infile.read()

    num_parts = (len(content) // max_chars) + 1

    for i in range(num_parts):
        start_index = i * max_chars
        end_index = min((i + 1) * max_chars, len(content))
        part_content = content[start_index:end_index]

        output_file = f"{output_prefix}_part_{i + 1}.txt"
        with open(output_file, "w") as outfile:
            outfile.write(part_content)


if __name__ == "__main__":
    input_file = "input.txt"  # Replace with your input file path
    output_prefix = "output"  # Replace with your desired output file prefix

    split_text_file(input_file, output_prefix)
