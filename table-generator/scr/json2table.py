import json
import click
from tabulate import tabulate

@click.command()
@click.argument('input_file', type=click.File('r'))
@click.argument('output_file', type=click.File('w'))
def json_to_markdown_table(input_file, output_file):
	"""convert input json file into markdown table for cheat sheet,
		and save it to output file.

	Args:
		input_file (json): path to json file
		output_file (txt): path to output text file
	"""
    data = json.load(input_file)

    # Convert JSON data to a list of lists
    table_data = [[key, f"`{value}`", f"${value}$"] for key, value in data.items()]

    # Convert the list of lists to a markdown table
    table = tabulate(table_data, headers=["snippet", "", ""], tablefmt="pipe")

    # Write the markdown table to the output file
    output_file.write(table)
    click.echo("Markdown table successfully created!")
    
if __name__ == '__main__':
	json_to_markdown_table()