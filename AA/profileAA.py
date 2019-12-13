# aree di attesa 

# aggiunge tag source=RAFVG
add_source = False
source = 'PCIV'

# do not add unique reference IDs to OSM?

# aggiunge tag ref:<dataset_id>=<id del Mpaaf>
# True -> relying only on geometric matching every time
no_dataset_id = True
# anagrafe regionale delle strutture turistico-ricettive
dataset_id = 'pciv'

# Overpass query to use when searching OSM for data
#overpass_timeout = 120 default
overpass_timeout = 300
#query = [('amenity', 'fuel'),('waterway', 'fuel')] both conditions
#query = [('amenity', 'fuel')],[('waterway', 'fuel')]  or condition
#query = [('amenity', 'fuel'),('disused:amenity','fuel')]  namespace disused and abandoned are implicit
#query = [('amenity', 'fuel'),('ref:mise','.*')] 
query = [('emergency', 'assembly_point')]

# parameter --osm will use indipendently generated queries, ie:
# http://overpass-turbo.eu/s/BZq
# http://overpass-turbo.eu/s/BZM (amenity=fuel and fuel:cng or fuel:lpg not "yes" 
# use wget -O manual-query.osm <http_addr obtained exporting compact query>

# attenzione, coord errate possono rendere enorme il bbox
# use openrefine for lat lon ranges
# vantaggio: fa richieste multiple ad overpass
bbox = True

# italia
#bbox = [35.28,6.62,47.1,18.79]

# tags to replace on matched OSM objects
master_tags = ('name')

delete_unmatched = False
tag_unmatched = { 'fixme':'area di attesa non elecata da Protezione Civile: verificare' }


# max distance to search for a match in meters
#max_distance = 30 matched 0
#max_distance = 130 matched 15 (error suggesting merge different POIs)
max_distance = 100

