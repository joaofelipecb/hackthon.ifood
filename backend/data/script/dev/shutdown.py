import kubernetes as k8s

def delete_ingress(k8s_core_v1, object_name):
    try:
        k8s_core_v1.delete_namespaced_ingress(
                object_name,
                namespace = 'default'
                )
        print(f'Ingress {object_name} deleted')
    except k8s.client.exceptions.ApiException as e:
        if e.reason == 'Not Found':
            print((
                   f'Ingress {object_name} not deleted '
                   'because it was not found'
                  ))
        else:
            raise e


def delete_deployment(k8s_apps_v1, object_name):
    try:
        k8s_apps_v1.delete_namespaced_deployment(
                object_name,
                namespace = 'default'
                )
        print(f'Deployment {object_name} deleted')
    except k8s.client.exceptions.ApiException as e:
        if e.reason == 'Not Found':
            print((
                   f'Deployment {object_name} not deleted '
                   'because it was not found'
                  ))
        else:
            raise e


def delete_service(k8s_core_v1, object_name):
    try:
        k8s_core_v1.delete_namespaced_service(
                object_name,
                namespace = 'default'
                )
        print(f'Service {object_name} deleted')
    except k8s.client.exceptions.ApiException as e:
        if e.reason == 'Not Found':
            print((
                   f'Service {object_name} not deleted '
                   'because it was not found'
                  ))
        else:
            raise e


def delete_persistent_volume_claim(k8s_core_v1, object_name):
    try:
        k8s_core_v1.delete_namespaced_persistent_volume_claim(
                object_name,
                namespace = 'default'
                )
        print(f'Persistent Volume Claim {object_name} deleted')
    except k8s.client.exceptions.ApiException as e:
        if e.reason == 'Not Found':
            print((
                   f'Persistent Volume Claim {object_name} not deleted '
                   'because it was not found'
                  ))
        else:
            raise e


def delete_persistent_volume(k8s_core_v1, object_name):
    try:
        k8s_core_v1.delete_persistent_volume(
                object_name
                )
        print(f'Persistent Volume {object_name} deleted')
    except k8s.client.exceptions.ApiException as e:
        if e.reason == 'Not Found':
            print((
                   f'Persistent Volume {object_name} not deleted '
                   'because it was not found'
                  ))
        else:
            raise e


def main():
    k8s.config.load_kube_config()
    with k8s.client.ApiClient() as k8s_client:
        k8s_apps_v1 = k8s.client.AppsV1Api(k8s_client)
        k8s_core_v1 = k8s.client.CoreV1Api(k8s_client)
        k8s_networking_v1 = k8s.client.NetworkingV1Api(k8s_client)

        delete_ingress(k8s_networking_v1, 'jenkins-ingress')
        delete_service(k8s_core_v1, 'jenkins')
        delete_deployment(k8s_apps_v1, 'jenkins-deployment')
        #delete_persistent_volume_claim(k8s_core_v1, 'jenkins-pv-claim')
        #delete_persistent_volume(k8s_core_v1, 'jenkins-pv-volume')

if __name__ == '__main__':
    main()
