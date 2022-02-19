import kubernetes as k8s
import helper

def apply_kubernetes_postgres(k8s_client):
    resource_files = [
            'data/kubernetes/dev/postgres-secrets.yaml',
            'data/kubernetes/dev/postgres-pv-volume.yaml',
            'data/kubernetes/dev/postgres-pv-claim.yaml',
            'data/kubernetes/dev/postgres-deployment.yaml',
            'data/kubernetes/dev/postgres-service.yaml'
                     ]
    for resource_file in resource_files:
        helper.apply_kubernetes_or_handle_error(k8s_client, resource_file)


def main():
    k8s.config.load_kube_config()
    with k8s.client.ApiClient() as k8s_client:
        apply_kubernetes_postgres(k8s_client)

if __name__ == '__main__':
    main()
