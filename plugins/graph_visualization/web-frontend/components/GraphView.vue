<template>
  <div>
    <link
      href="http://0.0.0.0:3003/static/css/2.9171e6ae.chunk.css"
      rel="stylesheet"
    />
    <link
      href="http://0.0.0.0:3003/static/css/main.cb82c3c8.chunk.css"
      rel="stylesheet"
    />
    <div id="root"></div>
    <script src="http://0.0.0.0:3003/static/js/run.js"></script>
    <script src="http://0.0.0.0:3003/static/js/2.37d52e8a.chunk.js"></script>
    <script src="http://0.0.0.0:3003/static/js/main.1a645d7c.chunk.js"></script>
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
