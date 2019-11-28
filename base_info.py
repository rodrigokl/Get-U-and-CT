import sys
# pathnameto_eppy = 'c:/eppy'
pathnameto_eppy = '../'
sys.path.append(pathnameto_eppy)

from eppy.modeleditor import IDF
from get_u_ct import *

iddfile = "/usr/local/EnergyPlus-8-9-0/Energy+.idd"
IDF.setiddname(iddfile)

idfname = "/home/labcee/Documentos/MODELO BASE/Alvenaria sem isolamento/VH/ZB2_VH_ALV_SEM_ISOLAMENTO.idf"

idf = IDF(idfname)



print (getU(idf, "Exterior Wall"))
print (getU(idf, "Exterior Roof"))
print (getU(idf, "Exterior Floor"))



