# main.py
import os
import sys
import argparse
from dxf_creator import create_dxf_document, setup_layers
from osm_processor import process_osm_file
from config import LAYER_MAPPING

def main():
    """Main function to run the conversion process."""
    parser = argparse.ArgumentParser(description="Convert OSM data to DXF format.")
    parser.add_argument("input_file", help="Path to the input .osm or .pbf file.")
    parser.add_argument("output_file", help="Path for the output .dxf file.")
    args = parser.parse_args()

    input_path = args.input_file
    output_path = args.output_file

    if not os.path.exists(input_path):
        print(f"Error: Input file not found at '{input_path}'")
        sys.exit(1)

    print("1. Creating DXF document...")
    doc = create_dxf_document()
    msp = doc.modelspace()

    print("2. Setting up layers...")
    setup_layers(doc, LAYER_MAPPING)

    print(f"3. Processing OSM file: '{input_path}'...")
    try:
        process_osm_file(input_path, msp)
    except Exception as e:
        print(f"An error occurred during OSM processing: {e}")
        sys.exit(1)


    print(f"4. Saving DXF file to: '{output_path}'...")
    try:
        doc.saveas(output_path)
        print("Conversion successful!")
    except IOError:
        print(f"Error: Could not save DXF file to '{output_path}'.")
        sys.exit(1)

if __name__ == "__main__":
    main()