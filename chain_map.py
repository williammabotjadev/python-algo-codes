# A Demo for a ChainMap collection

from collections import ChainMap

defaults = {
    'theme': 'Default',
    'language': 'en',
    'showIndex': True,
    'showFooter': True 
}

cm = ChainMap(defaults)

print(cm)

cm_one = cm.new_child({
    'theme': 'blue_sky'
})

print(cm_one['theme'])

cm_one.pop('theme')

print(cm_one['theme'])

cm_one.maps[0] = {
    'theme': 'dessert',
    'showIndex': False
}

print(cm_one['showIndex'])