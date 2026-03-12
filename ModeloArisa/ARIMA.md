Aqui ideas del modelo sariMa

Modelo ARIMA se usa cuando los datos no son estacionarios

modelo A LOS DATOS ORIGINALES se  transforman y se generan nuevos valores que lo vuelven estacionaria

se aplica a datos transformados y se agrega un modelo arma o autorregresivo

se aplica el valor de las diferencias de los valores originales 

primera diferencia diferencia valores real 

segunda diferencia diferencia entre los valores de la primera diferencia 

|t|x|1ra diff|2da diff|
|-|-|-|-|
|1|29|||
|2|46|17||
|3|71|25|8|
|4|104|33|8|
|5|145|41|8|
|6|194|49|8|
|7|251|57|8|
|8|316|65|8|
|9|389|73|8|
|10|470|81|8|
|11|559|89|8|
|12|656|97|8|



Arima consiste apliacar orden de las difernecias y con esas diferencias se aplica un modelo arma se ajustan al valor de las diferencias que son valores estacionarios 

Hollwinters se adecua bien con pocos datos



Modelo ARIMA tecnica utilizada para estadistic, para analizar y predecir series de tiempo (Datos ordenados en el tiempo) 

ARIMA = Autoregresive(AR) - Integrated(I) - Miving Average(MA)



AR->Se usa para valores pasados de la serie para predecir el valor actual 
-Ventas de hoy a partir de ayer, 2 dias ,3 dias etc

Formula:

-Yt= c+o1yt-1+oyt-2+....+et

--yt= valor actual

--yt-1 = valor anterior

--o= coeficentes que aprende el modelo

--e = error



I-> Esta se usa para hacer estacionaria la serie de tiempo esto significa que la medida no cambia en el tiempo, la varianza es estable y no hay tendencias fuertes

muchos datos reales no son estacionarios como en ventas que puede haber una tenencia creciente 

Y't = yt-yt-1
esto elimina las tendencias

el numero de veces que se aplica las diferencias es d



MA-> la parte MA usa errores pasados del modelo para mejorar la predicción, por ejemplo si el modelo de ayer se equivoco mucho el modelo usa ese error para ajustar la predicción de hoy
Formula simplificada 

-yt=c+et+01et-1+0et-2



MODELO ARIMA

Se escribe como 

-ARIMA(p,d,q)

p-numero de terminus autorregresivos

d-numero de diferenciaciones

q-numero de terminos de media movil



Para que se usa 

Muchísimo en empresas para:



-Finanzas

--predicción de precios

--predicción de ingresos



-Retail

--predicción de demanda

--inventario



-Telecom

--tráfico de red

--volumen de mensajes



-Logística

--volumen de pedidos

--demanda futura



Arima no maneja estacionalidad bien como ventas mayores en dicembre o mayor trafico en ciertos dias del mes o de la semana 



SARIMAX es mas recomendado siq ueremos agregar ferias y fiestas eventos de pueblos etc



&nbsp; 

