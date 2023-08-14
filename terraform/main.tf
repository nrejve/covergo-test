provider "kind" {
  version = "0.3.2"
}

resource "kind_cluster" "example" {
  name = "new"

  worker_nodes = 2

  control_plane_config {
    kubernetes_version = "latest"
  }

  worker_node_config {
    kubernetes_version = "latest"
  }
}

