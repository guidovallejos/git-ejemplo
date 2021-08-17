import pandas as pd
import openpyxl as oxl
import zipfile, os, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import uniform


#Crea diccionario para almacenar datos
df=pd.DataFrame()
resultados={}
col=["precio USD","superficie m2","costo USD/m2","barrio","titulo","link"]
resultados[col[0]]=[]
resultados[col[1]]=[]
resultados[col[2]]=[]    
resultados[col[3]]=[]    
resultados[col[4]]=[]
resultados[col[5]]=[]


#Abrir navegador chromedriver.exe y la pagina web
driver = webdriver.Chrome('C:\Python38\chromedriver.exe')
#D:\Programas\Anaconda3/chromedriver.exe
time.sleep(uniform(5, 7))


driver.get('https://www.infocasas.com.bo/venta/lotes-o-terrenos/cochabamba')
paginas=3

#https://www.remax.bo/PublicListingList.aspx?SelectedCountryID=120#mode=gallery&tt=261&cr=2&mpts=19426&pt=19426&cur=USD&sb=PriceIncreasing&page=1&sc=120&rl=2803&pm=50540,50541,50546&cll=8081580,8081581,8081600,8081602&lsgeo=2803,50540,8081580,0&sid=e1083e16-9f2d-4c67-bab4-45bdb9ec1b0a
#https://www.ultracasas.com/buscar/terreno-en-venta--en--cochabamba---cochabamba?page=1
time.sleep(uniform(15, 20))
#Primer ciclo para cambiar de pagina www.infocasas.com
pagina=1
for pag in range(0,paginas):  
    #Toma todas las publicaciones de la hoja actual
    elms=driver.find_elements_by_class_name('propiedades-slider ') 
    #Ciclo para recorrer las publicaciones y extraer informacion
    for elm in elms:
        precio=elm.find_element_by_class_name('precio').text
        precio=precio.replace('.','').replace(',','.')
        precio=float(precio.replace('U$S ','')) 
        superficie=elm.find_element_by_xpath('.//div[@class="contentIcons"]/div[@class="iconos last"]/span[@class="descri-numero"]').text
        superficie=superficie.replace('.','')
        superficie=float(superficie.replace(',','.'))
        costo_m2=precio/superficie
        barrio=elm.find_element_by_class_name('barrio').text
        titulo=elm.find_element_by_xpath('.//a[@class="checkMob"]/p[@class="titulo "]').text
        enlace=elm.find_element_by_xpath('.//a[@class="checkMob"]').get_attribute('href')
        
        #descripcion=elm.find_element_by_xpath('.//div[@class="descriptionProp"]/div[@class="inDescription"]/p').text    
        #print(descripcion)
        #print(precio,superficie,barrio,titulo,enlace)
        
        #Guarda informacion en el diccionario
        resultados[col[0]].append(precio)
        resultados[col[1]].append(superficie)
        resultados[col[2]].append(costo_m2)
        resultados[col[3]].append(barrio)
        resultados[col[4]].append(titulo)
        resultados[col[5]].append(enlace)
    #Cambia de pagina 
    pagina+=1
    try:
        driver.get(driver.find_element_by_xpath('//*[@id="paginado"]/a[@class="next "]').get_attribute('href'))
    except:
        print('pagina ',pagina-1)    
    time.sleep(uniform(10, 15))

    

driver.get('https://www.ultracasas.com/buscar/terreno-en-venta--en--cochabamba---cochabamba?page=1')
paginas=4
time.sleep(uniform(15, 20))    
#Primer ciclo para cambiar de pagina www.ultracasas.com
pagina=1
for pag in range(0,paginas):  
    #Toma todas las publicaciones de la hoja actual
    elms=driver.find_elements_by_xpath('//div[@itemtype="http://schema.org/SingleFamilyResidence"]')
    #('inmuebles-content') 
    #Ciclo para recorrer las publicaciones y extraer informacion
    for elm in elms:
        precio=elm.find_element_by_class_name('inmuebles-item-precio')
        precio=precio.find_element_by_xpath('h4').text
        precio=precio.replace('$us. ','')
        precio=precio.replace('$us ','')
        precio=precio.replace(',','')
        precio=float(precio) 
        superficie=elm.find_element_by_xpath('.//div[@class="inmuebles-item-caption pos-relative"]/div[@class="inmuebles-item-precio"]/ul[@class="list-inline "]/li[@class="icon-default-color"]').text
        superficie=superficie.replace(',','')
        superficie=float(superficie.replace(' m2',''))
        costo_m2=precio/superficie
        barrio=elm.find_element_by_xpath('.//h3[@class="text-ellipsis"]').text
        enlace=elm.find_element_by_xpath('.//a[@class="cursor-pointer"]').get_attribute('href')
        titulo=elm.find_element_by_xpath('.//h2[@class="text-ellipsis line-height-30px"]').text
                
        #descripcion=elm.find_element_by_xpath('.//div[@class="descriptionProp"]/div[@class="inDescription"]/p').text    
        #print(descripcion)
        #print(precio,superficie,barrio,titulo,enlace)
        
        #Guarda informacion en el diccionario
        resultados[col[0]].append(precio)
        resultados[col[1]].append(superficie)
        resultados[col[2]].append(costo_m2)
        resultados[col[3]].append(barrio)
        resultados[col[4]].append(titulo)
        resultados[col[5]].append(enlace)
    #Cambia de pagina
    #x=driver.find_element_by_xpath('.//a[@id="linkNext"]').get_attribute('href')
    pagina+=1
    try:
        driver.get(driver.find_element_by_xpath('//*[@id="linkNext"]').get_attribute('href'))
    except:
        print('pagina ',pagina-1)
    time.sleep(uniform(10, 15))
    


driver.get('https://www.remax.bo/PublicListingList.aspx?SelectedCountryID=120#mode=gallery&tt=261&cr=2&mpts=19426&pt=19426&cur=USD&sb=PriceIncreasing&page=1&sc=120&rl=2803&pm=50540,50541,50546&cll=8081580,8081581,8081600,8081602&lsgeo=2803,50540,8081580,0&sid=e1083e16-9f2d-4c67-bab4-45bdb9ec1b0a')
paginas=4
time.sleep(uniform(15, 20))    
#Primer ciclo para cambiar de pagina www.ultracasas.com
pagina=1
for pag in range(0,paginas):  
    #Toma todas las publicaciones de la hoja actual
    elms=driver.find_elements_by_class_name('gallery-item-container')
    print(len(elms))
    #Ciclo para recorrer las publicaciones y extraer informacion
    for elm in elms:       
        #print(elm.text)
        #precio=elm.find_element_by_xpath('.//div[@class="gallery-item"]/div[@class="gallery-price"]/span[@class="gallery-price-main"]').text
        precio=elm.find_element_by_class_name('gallery-price-main').text
        precio=precio.replace(' USD','')
        precio=precio.replace(',','')
        precio=float(precio) 
        print(precio)
        #superficie=elm.find_element_by_xpath('.//div[@class="gallery-item"]/div[@class="gallery-icons"]/span').text
        superficie=elm.find_element_by_class_name('gallery-attr-item-value').text
        #print(superficie)
        superficie=superficie.replace(',','')
        superficie=float(superficie)
        costo_m2=precio/superficie
        barrio=elm.find_element_by_xpath('.//div[@class="gallery-title"]/a').text
        barrio=barrio[barrio.find(" - ")+3:]       
        enlace=elm.find_element_by_xpath('.//div[@class="gallery-title"]/a').get_attribute('href')
        titulo=elm.find_element_by_xpath('.//div[@class="gallery-title"]/a').text        
        
        #print(precio,superficie,barrio,titulo,enlace)
        #Guarda informacion en el diccionario
        resultados[col[0]].append(precio)
        resultados[col[1]].append(superficie)
        resultados[col[2]].append(costo_m2)
        resultados[col[3]].append(barrio)
        resultados[col[4]].append(titulo)
        resultados[col[5]].append(enlace)
    #Cambia de pagina
    pagina+=1
    try:
        driver.find_element_by_class_name('page-next').click()
    except:
        print('pagina ',pagina-1)
    time.sleep(uniform(10, 15))



#convierte diccionario en dataframe
df = pd.DataFrame(resultados)
print(df)

#exporta a excel, el excel se encuentra en el path de trabajo
df.to_excel('example.xlsx', sheet_name='example')

#cierra el chromedriver
driver.quit()