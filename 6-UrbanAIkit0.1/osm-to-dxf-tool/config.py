# config.py

# This dictionary maps OSM tags to DXF layer names and colors.
# The key is a tuple (tag_key, tag_value) or just a tag_key.
# The value is a tuple (layer_name, color_index).
# See ACI (AutoCAD Color Index) for color numbers: https://gohtx.com/acadcolors.php

LAYER_MAPPING = {
    # Roads
    "highway": ("ROADS", 1),  # Red

    # Buildings
    "building": ("BUILDINGS", 5),  # Blue

    # Green Spaces
    ("leisure", "park"): ("GREEN_SPACES", 3),  # Green
    ("leisure", "garden"): ("GREEN_SPACES", 3),
    ("landuse", "forest"): ("GREEN_SPACES", 3),
    ("landuse", "grass"): ("GREEN_SPACES", 3),

    # Water
    ("natural", "water"): ("WATER", 4),  # Cyan

    # Railways
    "railway": ("RAILWAYS", 2),  # Yellow
}

# Default layer for features that don't match any rule
DEFAULT_LAYER = ("DEFAULT", 7) # White/Black