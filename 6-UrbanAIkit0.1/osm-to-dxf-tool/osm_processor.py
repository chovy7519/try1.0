# osm_processor.py
import osmium
import sys
from config import LAYER_MAPPING, DEFAULT_LAYER
from dxf_creator import add_line, add_polygon

class OSMHandler(osmium.SimpleHandler):
    def __init__(self, msp):
        super(OSMHandler, self).__init__()
        self.msp = msp
        # Using a dictionary to store node coordinates (lon, lat)
        self.nodes = {}

    def get_layer_for_tags(self, tags):
        """Determines the DXF layer based on OSM tags."""
        for key, value in tags:
            # Check for specific key-value pairs first
            if (key, value) in LAYER_MAPPING:
                return LAYER_MAPPING[(key, value)][0]
        # Check for key-only matches
        for key, value in tags:
            if key in LAYER_MAPPING:
                return LAYER_MAPPING[key][0]
        return DEFAULT_LAYER[0]

    def node(self, n):
        """Stores node coordinates."""
        # For simplicity, we'll treat lon/lat as x/y.
        # For real-world applications, a projection would be needed.
        self.nodes[n.id] = (n.location.lon, n.location.lat)

    def way(self, w):
        """Processes OSM ways (lines and areas)."""
        try:
            layer_name = self.get_layer_for_tags(w.tags)
            points = [self.nodes[node.ref] for node in w.nodes]

            if w.is_closed() and ('area' in w.tags and w.tags['area'] != 'no'):
                # It's an area (polygon)
                add_polygon(self.msp, points, layer_name)
            elif not w.is_closed():
                 # It's a line
                add_line(self.msp, points, layer_name)
            # Some closed ways are not areas (e.g., roundabouts), treat them as lines
            elif w.is_closed():
                add_line(self.msp, points, layer_name)

        except KeyError as e:
            # This can happen if a way references a node that is outside the
            # processed OSM extract. We just ignore it.
            print(f"Warning: Node {e} not found for way {w.id}. Skipping.", file=sys.stderr)


def process_osm_file(filepath, msp):
    """Applies the OSM handler to the given file."""
    handler = OSMHandler(msp)
    # Use 'location_handler' to store node locations efficiently
    handler.apply_file(filepath, locations=True)