from csvwlib import CSVWConverter
from rdflib import Graph, URIRef

url = "http://localhost/tcc/"
csvPath = url + "data.csv"

schemaNCPath = url + "QualisTabular_metadata_csv.json"
schemaPath = url + "QualisTabular_metadata.json"
schemaNormalizedPath = url + "QualisTabular_metadata_normalized.json"

def changeUrls(graph, urlFrom, urlTo):
  for s, p, o in graph.triples((None, None, None)):
    if urlFrom in s:
      graph.remove((s, p, o))
      s = URIRef(s.replace(urlFrom, urlTo))
      graph.add((s, p, o))
    if urlFrom in p:
      graph.remove((s, p, o))
      p = URIRef(p.replace(urlFrom, urlTo))
      graph.add((s, p, o))
    if urlFrom in o:
      graph.remove((s, p, o))
      o = URIRef(o.replace(urlFrom, urlTo))
      graph.add((s, p, o))

def convertToRDF(schemaPath, mode='minimal', base="http://lod.unicentro.br/QualisBrasil/"):
  converted = CSVWConverter.to_rdf(metadata_url=schemaPath, mode=mode)
  changeUrls(converted, url, base)
  return converted

def serialize(converted, output='output.txt', format='nt'):
  converted.serialize(destination=output, format=format)

print("Converting csv nochanges path.")
converted = convertToRDF(schemaNCPath,  mode="minimal", base="http://lod.unicentro.br/QualisBrasil/TabularCsv/")
serialize(converted, format='nt', output="noChanges/minimal.nt")
serialize(converted, format='ttl', output="noChanges/output_minimal.ttl")

converted = convertToRDF(schemaNCPath,  mode="standard", base="http://lod.unicentro.br/QualisBrasil/TabularCsv/")
serialize(converted, format='nt', output="noChanges/standard.nt")
serialize(converted, format='ttl', output="noChanges/output_standard.ttl")

print("Converting csv path.")
converted = convertToRDF(schemaPath,  mode="minimal", base="http://lod.unicentro.br/QualisBrasil/Tabular/")
serialize(converted, format='nt', output="normal/minimal.nt")
serialize(converted, format='ttl', output="normal/output_minimal.ttl")

converted = convertToRDF(schemaPath,  mode="standard", base="http://lod.unicentro.br/QualisBrasil/Tabular/")
serialize(converted, format='nt', output="normal/standard.nt")
serialize(converted, format='ttl', output="normal/output_standard.ttl")

print("Converting csv normalized path.")
converted = convertToRDF(schemaPath,  mode="minimal", base="http://lod.unicentro.br/QualisBrasil/TabularNormalized/")
serialize(converted, format='nt', output="normalized/minimal.nt")
serialize(converted, format='ttl', output="normalized/output_minimal.ttl")

converted = convertToRDF(schemaPath,  mode="standard", base="http://lod.unicentro.br/QualisBrasil/TabularNormalized/")
serialize(converted, format='nt', output="normalized/standard.nt")
serialize(converted, format='ttl', output="normalized/output_standard.ttl")