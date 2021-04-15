import { PluginNamePlugin } from '@graph-visualization/plugins'
import { GraphViewType } from '@graph-visualization/viewTypes'

export default ({ store, app }) => {
  app.$registry.register('plugin', new PluginNamePlugin())
  app.$registry.register('view', new GraphViewType())
}