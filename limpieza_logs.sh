#!/bin/bash

TARGET_DIR="$HOME/environment"

# busca archivos que terminen en .log y los vacia sin eliminarlos
find $TARGET_DIR -name "*.log" -exec truncate -s 0 {} +


echo "Limpieza de logs completada el: $(date)" >> $TARGET_DIR/mantenimiento.log


