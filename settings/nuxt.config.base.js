import base from '/baserow/web-frontend/config/nuxt.config.base.js'

const baseConfig = base('/baserow/web-frontend')
baseConfig.modules.push('../plugins/graph_visualization/web-frontend/module.js')

export default baseConfig
