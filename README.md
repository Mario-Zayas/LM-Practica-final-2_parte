Práctica final (2ª parte)

El alumno decide que es lo que va a hacer la aplicación web, decide cuantas páginas va a tener,…, pero las características mínimas de la aplicación web que debes hacer serán las siguientes:

    La aplicación web debe tener una vista tipo lista, donde se vea una lista de recursos de la API.
    Debe tener también una vista detalle, donde se vea información concreta de algún recurso de la API.
    Debe tener al menos un formulario para filtrar la información que se muestra.
    La aplicación web debe tener hoja de estilo.
    La aplicación web debe estar desplegada en una plataforma como servicio (PaaS).

Posibles mejoras

    Utilizar más de una API. Combinar en vuestra aplicación información de varias APIS. O utilizar una API y más información que tengáis en algún fichero JSON.
    Añadir más elementos de los que se indican en el punto anterior: añadir más páginas, añadir más formularios, mostrar la información de alguna otra manera,…
    Utilizar alguna petición POST que permita cambiar el estado de la aplicación web y modifique su información. (Esta mejora se podrá realizar si la API escogida no lo permite, normalmente con API restful con key no suelen tener opción a modificar con peticiones del tipo POST).

¿Qué hay que entregar?

    ¿Qué mejoras crees que has añadido a tu aplicación?
    La URL del repositorio git
    La URL de la página desplegada en una plataforma como servicio 

En este proyecto es la versión aplicación del programa de Clash Royale. Tratará de lo siguiente:

    Tendrá 8 páginas más el base.html.
    En la página inicio tendrá 1 imagen la cual te redireccionará a otra pagina con 3 imagenes y titulos distintos.
    Tendrá 2 peticiones distintas entre sí.
    Una hará una petición a un buscador que filtra por código de jugador y nos muestra todos los detalles del jugador     solicitado. No es necesario el uso de "#".
    La otra hará una petición a un buscador de clanes por el nombre y mostrará cada detalle del clan, asi como donde       se originó. Tenga en cuenta que hay muchos clanes con el mismo nombre, por lo que resultará dificil encontrar el       que usted quiere.
    La ultima pagina lo que hará será buscar y listar de manera automatica todos los torneos.
    Ademas tendrá 3 paginas web en las cuales se mostrarán los TOP 1000 de Jugadores y Clanes asi como el TOP de           torneos.

Es necesario que sepa que debe ingresar el token que se encuentra en esta página: https://developer.clashroyale.com/#/.

Debes registrarte o iniciar sesión para poder acceder a la creación de claves, una vez creada lo unico que debes hacer es cambiar el token ("key") de "app.py" por el tuyo.
