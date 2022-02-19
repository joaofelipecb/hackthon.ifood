import kubernetes as k8s
import helper


def apply_kubernetes_pgadmin(k8s_client):
    resource_files = [
            'backend/data/kubernetes/dev/pgadmin-secrets.yaml',
            'backend/data/kubernetes/dev/pgadmin-deployment.yaml',
            'backend/data/kubernetes/dev/pgadmin-service.yaml',
            'backend/data/kubernetes/dev/pgadmin-ingress.yaml',
                 ]
    for resource_file in resource_files:
        helper.apply_kubernetes_or_handle_error(k8s_client, resource_file)


def main():
    k8s.config.load_kube_config()
    with k8s.client.ApiClient() as k8s_client:
        k8s_watch = k8s.watch.Watch()
        k8s_core_v1 = k8s.client.CoreV1Api(k8s_client)

        apply_kubernetes_pgadmin(k8s_client)


if __name__ == '__main__':
    main()
