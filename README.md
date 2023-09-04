# ProyectoFinal
TRABAJO FINAL  - modulo3
---------------------       Diplomante: Simeon Rodrigo Carita Aspi    -------------------------------
---------------------                      C.I.: 6773235              .-------------------------------
-------------------------------------------------------------------------------------------------------
Crear una base de datos con el nombre 
db_proyecto
-------------------------------------------------------------------------------------------------------
Crear la Tabla usuario
-------------------------------------------------------------------------------------------------------
Insertar Iniciamente los siguientes Datos
INSERT INTO usuario(id, ci, nombre, primer_ap, segundo_ap, fecha_nac) VALUES ('3b920204-63aa', '6773235', 'Rodry', 'Carita', 'Aspi', '1995-10-08')
-------------------------------------------------------------------------------------------------------
Obtener Datos
http://127.0.0.1:5000/api/usuarios/
-------------------------------------------------------------------------------------------------------
Agregar usuario
http://127.0.0.1:5000/api/usuarios/add

{
	"ci": "587925",
	"nombre": "Jorge",
	"primer_ap": "Nina",
	"segundo_ap": "Souza",
	"fecha_nac": "1900-09-15"
}
-------------------------------------------------------------------------------------------------------
Eliminar usuario
http://127.0.0.1:5000/api/usuarios/delete/ESCRIBIR_EL_ID_A_ELIMINAR
-------------------------------------------------------------------------------------------------------
Actualizar Datos del Usuario
http://127.0.0.1:5000/api/usuarios/update/ESCRIBIR_EL_ID_A_ACTUALIZAR
{
	"ci": "2222222",
	"nombre": "Juanjo",
	"primer_ap": "Nina",
	"segundo_ap": "Souza",
	"fecha_nac": "1900-09-15"
}



