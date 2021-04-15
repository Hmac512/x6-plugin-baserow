import { ViewType } from '@baserow/modules/database/viewTypes'
import GraphView from '@graph-visualization/components/GraphView'

export class GraphViewType extends ViewType {
  static getType() {
    return 'graph'
  }

  getIconClass() {
    return 'graph'
  }

  getName() {
    return 'Graph'
  }

  getComponent() {
    return GraphView
  }
}
