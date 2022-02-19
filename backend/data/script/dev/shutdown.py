import kubernetes as k8s
import helper


def main():
    k8s.config.load_kube_config()
    with k8s.client.ApiClient() as k8s_client:
        k8s_apps_v1 = k8s.client.AppsV1Api(k8s_client)
        k8s_core_v1 = k8s.client.CoreV1Api(k8s_client)
        k8s_networking_v1 = k8s.client.NetworkingV1Api(k8s_client)

        helper.delete_ingress(k8s_networking_v1, 'jenkins-ingress')
        helper.delete_service(k8s_core_v1, 'jenkins')
        helper.delete_deployment(k8s_apps_v1, 'jenkins-deployment')


if __name__ == '__main__':
    main()
