<?php

$mes = 'Enero';
$verdadero = true;

// if ($verdadero) {
//   echo "verdadero";
// }
// else {
//   echo "falso";
// }

if ($mes == 'Diciembre') {
  echo "Feliz Navidad";
}
elseif ($mes=='Enero') {
  echo "Feliz año nuevo";
}
elseif ($mes=='Julio') {
  echo "Feliz Julio";
}
else {
  echo "Ese mes no esta en en celebracion";
}

?>
