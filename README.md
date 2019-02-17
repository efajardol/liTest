lfTEST
======

Este proyecto contiene una prueba de desarrollo de un sitio web mediante el uso de django RESTful conectado con una base de datos PostgreSQL que permite administrar vehículos y propietarios mediante el uso de la siguiente información:

**Propietario:**

* Nombre
* Número de cédula
* imagen de la cédula (archivo pdf, jpg o png)
* dirección de correo electrónico

**Vehículo:**

* número de placa
* tipo
* marca

La aplicación permite agregar y eliminar conductores; se pueden realizar búsquedas para obtener una lista de todos los vehículos registrados (también como un archivo en formato cvs) o de un vehículo coincidente con una placa; búsquedas de conductores por nombre, número de cédula y placa de su vehículo; finalmente se puede obtener como información resumida de los vehículos el total de vehículos registrados y un histograma por marca.

la siguiente lista detalla la funcionalidad de la aplicación que responde a una estructura RESTful:

|**Endpoint**  |**HTTP method**|**Resultado** |
|--------------|---------------|--------------|
|drivers       |GET            |listar conductores|
|drivers       |POST           |crear conductor|
|drivers/name  |GET            |buscar condutor por nombre|
|drivers/name  |PUT            |actualizar conductor|
|drivers/name  |DEL            |borrar conductor|
|drivers/id/   |GET            |buscar condutor por cédula|
|drivers/plate/|GET            |buscar condutor por placa de su vehículo|
|vehicles      |GET            |listar vehículos registrados|
|vehicles/cvs  |GET            |listar vehículos registrados mediante CVS|
|vehicles/count|GET            |listar número de vehículos registrados|
|vehicles/hist |GET            |listar histograma de vehículos por marca|
