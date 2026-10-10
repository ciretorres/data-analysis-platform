<script setup lang="ts">
import { ref, watch } from 'vue'

interface Dataset {
  id: number
  name: string
  description: string | null
  file_name: string
  created_at: string
}

const props = defineProps<{
  modo: 'crear' | 'editar'
  dataset?: Dataset
}>()

const emit = defineEmits<{
  guardar: [datos: { name: string; description: string | null; file_name: string }]
  cancelar: []
}>()

const name = ref('')
const description = ref('')
const file_name = ref('')
const errores = ref<{ name?: string; file_name?: string; general?: string }>({})
const enviando = ref(false)

watch(() => props.dataset, (nuevo) => {
  if (nuevo && props.modo === 'editar') {
    name.value = nuevo.name
    description.value = nuevo.description ?? ''
    file_name.value = nuevo.file_name
  }
}, { immediate: true })

function validar(): boolean {
  errores.value = {}

  if (!name.value.trim()) {
    errores.value.name = 'El nombre es obligatorio.'
  } else if (name.value.length > 100) {
    errores.value.name = 'El nombre no puede tener más de 100 caracteres.'
  }

  if (!file_name.value.trim()) {
    errores.value.file_name = 'El nombre de archivo es obligatorio.'
  } else if (file_name.value.length > 255) {
    errores.value.file_name = 'El nombre de archivo no puede tener más de 255 caracteres.'
  }

  return Object.keys(errores.value).length === 0
}

async function enviar() {
  if (!validar()) return

  enviando.value = true

  try {
    emit('guardar', {
      name: name.value.trim(),
      description: description.value.trim() || null,
      file_name: file_name.value.trim(),
    })
  } finally {
    enviando.value = false
  }
}
</script>

<template>
  <form @submit.prevent="enviar">
    <div>
      <label for="name">Nombre *</label>
      <input id="name" v-model="name" type="text" maxlength="100" />
      <p v-if="errores.name" class="error">{{ errores.name }}</p>
    </div>

    <div>
      <label for="description">Descripción</label>
      <textarea id="description" v-model="description"></textarea>
    </div>

    <div>
      <label for="file_name">Nombre de archivo *</label>
      <input id="file_name" v-model="file_name" type="text" maxlength="255" />
      <p v-if="errores.file_name" class="error">{{ errores.file_name }}</p>
    </div>

    <p v-if="errores.general" class="error">{{ errores.general }}</p>
    
    <div>
      <button type="submit" :disabled="enviando">
        {{ modo === 'crear' ? 'Crear dataset' : 'Guardar cambios' }}
      </button>
      <button type="button" @click="emit('cancelar')">Cancelar</button>
    </div>
  </form>
</template>

<style scoped>
form {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.error {
  color: #f87171;
  font-size: 0.875rem;
  margin: 0.25rem 0 0;
}

button {
  margin-right: 0.5rem;
}
</style>
