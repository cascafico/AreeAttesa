# addressed update 

# aggiunge tag source=pippo
add_source = False
source = 'PCFVG'

# do not add unique reference IDs to OSM?

# aggiunge tag ref:<dataset_id>=<id del Comune di Milano (IDMASTER)>
# True -> relying only on geometric matching every time
no_dataset_id = True
dataset_id = 'civici'

# Overpass query to use when searching OSM for data
overpass_timeout = 300
query = [('addr:housenumber','.*')] 
#query = [('addr:housenumber','~.*')]  e se lettera e interno non hanno stesso case?
#query = [('addr:street','~.*')] 

# parameter --osm will use indipendently generated queries, ie:
# http://overpass-turbo.eu/s/14UI
# consider exluding amenities, shops etc if delete_unmatched=True

# use wget -O manual-query.osm <http_addr obtained exporting compact query>

bbox = True


# tags to replace on matched OSM objects
master_tags = ('survey:date', 'addr:housenumber', 'addr:street')

# delete_unmatched = True cancellerebbe anche i POI con indirizzo
delete_unmatched = True
tag_unmatched = { 'fixme':'this addr is missing from source dataset: please check' }


# max distance to search for a match in meters
max_distance = 3

#sembra non funzioni
duplicate_distance = 0.5

