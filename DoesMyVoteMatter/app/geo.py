import geopandas as gpd
import fiona
import pyogrio

relative_path = "../shapefiles/shp"
gpd.read_file(relative_path)

# layers = fiona.listlayers(relative_path)

layers = gpd.list_layers(relative_path)
print(layers)

for index, row in layers.iterrows():
    print(f"District {index + 1}:")
    print(f"Name: {row['Rucho_Lewis_Congress_3']}")
    print(f"Geometry Type: {row['geometry'].geom_type}")
    print(f"Coordinates: {row['geometry']}")
    print()

"""
proads.zip
│── roads.shp       # Geometry data
│── roads.shx       # Index file
│── roads.dbf       # Attribute data
│── roads.prj       # Projection information
│── roads.cpg       # Character encoding information (optional)
│── roads.qix       # Spatial index (optional)
│── roads.xml       # Metadata (optional)
"""