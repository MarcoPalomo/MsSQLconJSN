#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, csv, pymssql
import zipfile, re, fnmatch

class MsSql:
    ''' Paramètres MsSql '''
    server = '10.0.3.35'
    user = 'sa'
    password = '713tbq42'

 

for fic in os.listdir('.'):
        if fnmatch.fnmatch(fic, '*.zip'):
                ficIn = fic

 

#cheminZip =''

 

ficCsv = ''
ficZip = zipfile.ZipFile(ficIn, 'r')
#ficZip = zipfile.ZipFile('IDFIDT.zip')

for fich in ficZip.namelist():
    if 'csv' in fich:
        ficCsv = fich
        break

 

#ficCsv = cheminZip+'/'+fich
ficZip.extract(ficCsv, './')
ficZip.close()

 

def requete():
    cnx = pymssql.connect(MsSql().server, MsSql().user, MsSql().password, '', as_dict=True)

    cur = cnx.cursor()
    cur.execute('SET DATEFORMAT dmy')

    cnx.commit()
    sqlrequest = ("bulk insert [0051-Piece-PROD].[dbo].[T_PurgeMaileva] from '"+ficCsv+ r"' with (FIRSTROW = 2, FORMATFILE = '\\prod1\no_std\Maileva\dossier-PurgeMaileva.fmt' ,MAXERRORS=0)")

    cur.execute(sqlrequest)
    cnx.commit()
    cnx.close()

requete()
