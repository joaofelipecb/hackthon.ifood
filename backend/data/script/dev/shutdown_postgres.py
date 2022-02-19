import kubernetes as k8s
import helper


def main():
    k8s.config.load_kube_config()
    with k8s.client.ApiClient() as k8s_client:
        k8s_apps_v1 = k8s.client.AppsV1Api(k8s_client)
        k8s_core_v1 = k8s.client.CoreV1Api(k8s_client)

        helper.delete_service(k8s_core_v1, 'postgres')
        helper.delete_deployment(k8s_apps_v1, 'postgres-deployment')
        helper.delete_secret(k8s_core_v1, 'postgres-secret')


if __name__ == '__main__':
    main()
