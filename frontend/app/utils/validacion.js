// Funciones puras de validación y formato para la carga de archivos (RF-04).
// No usan la red ni el estado de la aplicación: solo reciben datos y devuelven
// un resultado. Por eso se pueden probar de forma independiente.

/** Lista cerrada de formatos admitidos en el nivel 1 (RF-04). */
export const EXTENSIONES_PERMITIDAS = ['csv', 'json', 'pdf']

/**
 * Devuelve true si el nombre termina en una extensión admitida, sin
 * distinguir mayúsculas de minúsculas (CL-11).
 *
 * validarExtension('datos.csv')      -> true
 * validarExtension('informes.JSON')  -> true
 * validarExtension('acta.PDF')       -> true
 * validarExtension('datos.csv.txt')  -> false (CL-10)
 * validarExtension('notas.txt')      -> false (CL-01)
 */
export function validarExtension(nombre) {
  const texto = typeof nombre === 'string' ? nombre : ''
  const punto = texto.lastIndexOf('.')
  if (punto <= 0) return false // sin extensión o solo ".csv"
  const extension = texto.slice(punto + 1).toLowerCase()
  return EXTENSIONES_PERMITIDAS.includes(extension)
}

/**
 * Convierte bytes a KB o MB con formato español (coma decimal).
 * Un archivo vacío (0 bytes) devuelve '0 KB'.
 *
 * formatearTamano(2048)    -> '2 KB'
 * formatearTamano(1536)    -> '1,5 KB'
 * formatearTamano(5242880) -> '5 MB'
 */
export function formatearTamano(bytes) {
  const total = Number(bytes)
  if (!Number.isFinite(total) || total <= 0) return '0 KB'

  if (total >= 1024 * 1024) {
    const mb = total / (1024 * 1024)
    return `${mb.toLocaleString('es-ES', { maximumFractionDigits: 2 })} MB`
  }

  const kb = total / 1024
  return `${kb.toLocaleString('es-ES', { maximumFractionDigits: 1 })} KB`
}

/**
 * Trunca nombres largos con puntos suspensivos (CL-08).
 * Si el nombre cabe en `max` caracteres, se devuelve tal cual.
 *
 * truncarNombre('a'.repeat(120)) -> 'aaaa…' (60 caracteres)
 */
export function truncarNombre(nombre, max = 60) {
  const texto = typeof nombre === 'string' ? nombre : ''
  if (texto.length <= max) return texto
  return `${texto.slice(0, max - 1)}…`
}
