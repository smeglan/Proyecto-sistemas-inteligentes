<h1>Proyecto final sistemas inteligentes 2(readme en contrucción)</h1>

<h2>Primera parte</h2>
<p>1. El <b>API</b> que recibe procesa los datos del ROI se encuentra en /app/server/api.py, puede dar click aqui para visualizar el archivo <a href='./app/server/api.py'>link</a></p>
<br/>
<p>2. El <b>visor del ROI</b> se encuentra en /app/client/visor.py, puede dar click aqui para visualizar el archivo <a href='./app/client/visor.py'>link</a></p>
<br/>
<h3>Comandos del teclado</h3>
<table>
  <tr>
    <th>Tecla</th>
    <th>Función</th>
  </tr>
  <tr>
    <td>ESC</td>
    <td>Cerrar aplicación</td>
  </tr>
  <tr>
    <td>C</td>
    <td>Almacenar una foto para enviarla </td>
  </tr>
  <tr>
    <td>A</td>
    <td>Permite visualizar la ultima foto añadida</td>
  </tr>
  <tr>
    <td>E</td>
    <td>Enviar todo el conjunto de imagenes al servidor</td>
  </tr>
  <tr>
    <td>T</td>
    <td>Se usa para añadir imagenes al raw (es necesario modificar la clase por codigo antes de usarlo)</td>
  </tr>
</table>
<br/>
<h2>Segunda parte</h2>
<p>
  1. Para la construcción del dataset se utilizo un script que genera las clases y aplica varios filtros, generando tambien una carpeta con los datos de entrenamientos dividos por clase, dicho script se encuentra en la carpeta app/server/trainer.py <a href='./app/server/trainer.py'>link</a>
</p>
<p>
  2. La implementación de las 3 redes neuronales se encuentra en el archivo  <a href='./app/server/CNNBuilder.py'>CNNBuilder.py</a> con sus respectivas entradas y clases.
</p>
<p>
  3. El proceso de entrenamiento se encuentra en el archivo <a href='./app/server/CNNBuilder.py'>CNNBuilder.py</a>, todo con un 10 KFold.
</p>
<p>
  4. 
</p>
<h3>Matriz de confusión</h3>
<h4>Model 1</h4>
<table>
  <tr>
    <td>45</td>
    <td>0</td>
    <td>1</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>0</td>
    <td>104</td>
    <td>2</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>0</td>
    <td>0</td>
    <td>45</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>0</td>
    <td>0</td>
    <td>35</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>0</td>
    <td>6</td>
    <td>0</td>
    <td>0</td>
    <td>40</td>
  </tr>
</table>

<h4>Model 2</h4>
 <table>
  <tr>
    <td>56</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>0</td>
    <td>94</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>0</td>
    <td>4</td>
    <td>52</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>28</td>
    <td>0</td>
  </tr>
  <tr>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>46</td>
  </tr>
</table>

<h4>Model 3</h4>
 <table>
  <tr>
    <td>49</td>
    <td>5</td>
    <td>3</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>0</td>
    <td>91</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>0</td>
    <td>0</td>
    <td>56</td>
    <td>0</td>
    <td>2</td>
  </tr>
  <tr>
    <td>0</td>
    <td>1</td>
    <td>0</td>
    <td>33</td>
    <td>0</td>
  </tr>
  <tr>
    <td>1</td>
    <td>1</td>
    <td>0</td>
    <td>0</td>
    <td>38</td>
  </tr>
</table>
<h3>Tabla de Resultados</h3>
<table>
  <tr>
    <th>N° Nombre</th>
    <th>Modelo</th>
    <th>Accuracy</th>
    <th>Precision</th>
    <th>Recall</th>
    <th>F1</th>
    <th>Loss</th>
    <th>Epocas</th>
    <th>Tiempos</th>
  </tr>
  <tr>
    <td>1</td>
    <td>Model 1</td>
    <td>1</td>
    <td>0.95</td>
    <td>0.98</td>
    <td>0.97</td>
    <td>0.1185</td>
    <td>22</td>
    <td></td>
  </tr>
  <tr>
    <td>2</td>
    <td>Model 2</td>
    <td>0.9857</td>
    <td>0.98</td>
    <td>1</td>
    <td>0.99</td>
    <td>0.0843</td>
    <td>22</td>
    <td></td>
  </tr>
  <tr>
    <td>3</td>
    <td>Model 3</td>
    <td>0.9571</td>
    <td>0.96</td>
    <td>0.93</td>0.96 
    <td>0.94</td>
    <td>0.0848</td>
    <td>22</td>
    <td></td>
  </tr>
</table>
<br/>
