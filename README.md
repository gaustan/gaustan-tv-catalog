# Catálogo de Gaustan TV

Edita `catalogo.json` en GitHub y aumenta `revision` con cada cambio. En la app abre **Listas → Actualizar catálogo de GitHub**.

## Mantener favoritos

No cambies los campos `id` de las fuentes ni de las entradas existentes, incluso si corriges nombre o URL. Para una entrada nueva crea un ID único permanente. `schemaVersion` debe seguir siendo 1. El cliente combina actualizaciones sin borrar entradas, ediciones ni favoritos; las eliminaciones se realizan localmente. El botón permite agregar fuentes faltantes de forma explícita.

## Tipos

`stream`: URL HTTP/HTTPS directa. `web`: referencia HTML, nunca se importa como vídeo. `references` contiene enlaces de contexto, incluido Years and Years, sin reproducción comprobada. `language` y `provenance` son informativos. Los subtítulos personales siguen gestionándose en la app.

## Publicación

Solo enlaces públicos del catálogo distribuido; no se publican biblioteca privada del usuario, claves de firma, APK, usuarios, contraseñas, tokens ni vídeos. Las fuentes pueden cambiar y publicar un enlace no certifica derechos o disponibilidad.

`catalogo.m3u` es una exportación para reproductores externos. Tras editar JSON ejecuta `python exportar.py` para regenerarla. Gaustan TV lee JSON; no requiere actualizar esta exportación para sincronizar.

## Formato

Cada fuente tiene id, name, origin y entries. Cada entrada tiene id, name, group, url, type, tvgId (opcional), logo (opcional), language y provenance. HTTPS es preferible. No introduzcas credenciales.
