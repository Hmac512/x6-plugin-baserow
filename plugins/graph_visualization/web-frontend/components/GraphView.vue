<template>
  <div>
    <link href="http://localhost:3003/css/app.91d11c53.css" as="style" />
    <link href="http://localhost:3003/js/app.8826a26e.js" as="script" />
    <link
      href="http://localhost:3003/js/chunk-vendors.e883f397.js"
      as="script"
    />
    <link href="http://localhost:3003/css/app.91d11c53.css" rel="stylesheet" />
    <div id="app"></div>
    <script src="http://localhost:3003/js/chunk-vendors.e883f397.js"></script>
    <script src="http://localhost:3003/js/app.8826a26e.js"></script>
  </div>
</template>

<script>
export default {
  name: 'GraphView',
  props: {
    primary: {
      type: Object,
      required: true,
    },
    fields: {
      type: Array,
      required: true,
    },
    view: {
      type: Object,
      required: true,
    },
    table: {
      type: Object,
      required: true,
    },
    database: {
      type: Object,
      required: true,
    },
  },
}
</script>
