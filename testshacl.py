import requests
import pyshacl
from rdflib import Graph

# Define the URLs of the shapes
url_karnataka = "https://raw.githubusercontent.com/MonobikashDas/shacladdressvalidator/main/shape_karnataka.ttl"
url_india = "https://raw.githubusercontent.com/MonobikashDas/shacladdressvalidator/main/shape_india.ttl"

# Fetch shapes from URLs
shapes_karnataka = requests.get(url_karnataka).text
shapes_india = requests.get(url_india).text

# Create a new graph for combined shapes
shacl_combined = Graph()

# Parse shapes into the combined graph
shacl_combined.parse(data=shapes_karnataka, format="turtle")
shacl_combined.parse(data=shapes_india, format="turtle")

# Load data graph
#data_graph_file = "data_graph.ttl"
data_graph_file = "actual_data.jsonld"
data_graph = Graph()
data_graph.parse(data_graph_file, format="json-ld")

# Validate data against the combined shapes
conforms, results_graph, results_text = pyshacl.validate(
    data_graph,
    shacl_graph=shacl_combined,
    inference="rdfs",
    serialize_report_graph="turtle",
    debug=True,
)

# Print validation results
print(f"Conforms: {conforms}")
print(f"Validation Report:\n{results_text}")
