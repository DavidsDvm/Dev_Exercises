<?php

$meses= array(
    'Enero', 'Febrero', 'Marzo', 'Abril',
    'Mayo', 'Junio', 'Julio', 'Agosto',
    'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
);

$numeros = array(1, 22, 23, 10, 9, 5, 70, 100, 28);

rsort($numeros);
?>

<!DOCTYPE html>
<html lang="es" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Meses del año</title>
  </head>
  <body>
    <h1>Meses del año</h1>
    <ul>
      <?php

      foreach ($numeros as $mes) {
        echo "<li>" . $mes . "</li>";
      }

      ?>
    </ul>
  </body>
</html>
