import sys
# pathnameto_eppy = 'c:/eppy'
pathnameto_eppy = '../'
sys.path.append(pathnameto_eppy)

from eppy.modeleditor import IDF


def getU(idf, const):

	RT = 0
	materials = idf.idfobjects['MATERIAL']
	constructions = idf.idfobjects['CONSTRUCTION']

	for construction in constructions:
		if construction.Name == const:
			for material in materials:
				for fieldname in construction.fieldnames:
					#print (material.Name, construction[fieldname])
					if material.Name == construction[fieldname]:

						rt_layer = material.Thickness/material.Conductivity
						RT += rt_layer
						r_layer = 0

	if(const == "Exterior Wall" or const == 'Interior Wall'):
		RT = RT #+ 0.04 + 0.13
	elif(const == "Exterior Roof" or const == 'Interior Roof'):
		RT = RT #+ 0.04 + 0.17
	elif(const == "Exterior Floor" or const == 'Interior Floor'):	
		RT = RT #+ 0.04 + 0.10

	U = 1/RT					
	return (U,"W/(m2.K)")


def getCT(idf, const):

	CT = 0
	materials = idf.idfobjects['MATERIAL']
	constructions = idf.idfobjects['CONSTRUCTION']

	for construction in constructions:
		if construction.Name == const:
			for material in materials:
				for fieldname in construction.fieldnames:
					#print (material.Name, construction[fieldname])
					if material.Name == construction[fieldname]:
						ct_layer = material.Thickness * (material.Specific_Heat/1000) * material.Density
						print (material.Name, ct_layer)
						CT += ct_layer
						ct_layer = 0

	return (int(CT),"kJ/(m2.K)")





				
				

