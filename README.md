<h1>Proyecto final sistemas inteligentes 2</h1>

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
<p>>
  2. La implementación de las 3 redes neuronales se encuentra en el archivo  <a href='./app/server/CNNBuilder.py'>CNNBuilder.py</a> con sus respectivas entradas y clases.
</p>
<p>
  3. El proceso de entrenamiento se encuentra en el archivo <a href='./app/server/CNNBuilder.py'>CNNBuilder.py</a>, todo con un 10 KFold.
</p>
<p>
  4. 
</p>
<h3>Tabla de Resultados</h3>
<table>
  <tr>
    <th>N° Nombre</th>
    <th>Modelo</th>
    <th>Accuracy</th>
    <th>Precision</th>
    <th>Recall</th>
    <th>F1</th>
    <th>Score</th>
    <th>Loss</th>
    <th>Epocas</th>
    <th>Tiempos</th>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>
<br/>
<br/>
<h2>Video de youtube</h2>
<a href="https://www.youtube.com/watch?v=EtUNMJWU9LQ">
  <img src="https://www.uncommunitymanager.es/wp-content/uploads/seo_google_youtube.jpg"/>
 </a>
<p>Disponible en <a href="https://www.youtube.com/watch?v=EtUNMJWU9LQ">Video</a></p>
