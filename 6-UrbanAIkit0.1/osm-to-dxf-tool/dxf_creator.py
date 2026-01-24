# dxf_creator.py
import ezdxf
from ezdxf.document import Drawing

def create_dxf_document():
    """Creates a new DXF document."""
    return ezdxf.new()

def setup_layers(doc: Drawing, layer_mapping: dict):
    """Creates layers in the DXF document based on the mapping."""
    for key, (layer_name, color) in layer_mapping.items():
        if layer_name not in doc.layers:
            doc.layers.new(name=layer_name, dxfattribs={'color': color})
    # Also create the default layer
    default_layer, default_color = ("DEFAULT", 7)
    if default_layer not in doc.layers:
        doc.layers.new(name=default_layer, dxfattribs={'color': default_color})


def add_line(msp, points, layer_name):
    """Adds a LWPOLYLINE to the modelspace."""
    msp.add_lwpolyline(points, dxfattribs={'layer': layer_name})

def add_polygon(msp, points, layer_name):
    """Adds a closed LWPOLYLINE (polygon) to the modelspace."""
    msp.add_lwpolyline(points, close=True, dxfattribs={'layer': layer_name})