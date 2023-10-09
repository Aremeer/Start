def text_to_svg(input_file, output_file):
    # Read text content from the input file
    with open(input_file, 'r') as file:
        text_content = file.read()

    # SVG template
    svg_template = """<svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
        <text x="10" y="40" font-family="Arial" font-size="14">{}</text>
    </svg>""".format(text_content)

    # Write SVG content to the output file
    with open(output_file, 'w') as svg_file:
        svg_file.write(svg_template)

# Example usage
text_to_svg('input.txt', 'output.svg')
