# pharmacies update 

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
query = [('amenity', 'school')],[('amenity', 'kindergarten')]

# parameter --osm will use queried data istead, for instance:
# http://overpass-turbo.eu/s/BZq
# http://overpass-turbo.eu/s/BZM (amenity=fuel and fuel:cng or fuel:lpg not "yes" 
# use wget -O manual-query.osm <http_addr obtained exporting compact query>

# attenzione, coord errate possono rendere enorme il bbox
# use openrefine for lat lon ranges
# vantaggio: fa richieste multiple ad overpass
bbox = True

# tags to replace on matched OSM objects
master_tags = ('isced:level')

delete_unmatched = False
#tag_unmatched = { 'fixme':'questo albero può essere abbattuto/declassificato' }


# max distance to search for a match in meters
max_distance = 80

