import kubernetes as k8s
import json


def apply_kubernetes_or_handle_error(k8s_client, resource_file):
    try:
        k8s.utils.create_from_yaml(k8s_client, resource_file)
        print(f'Resource {resource_file} created')
    except k8s.utils.FailToCreateError as e:
        for api_exception in e.api_exceptions:
            data = json.loads(api_exception.body)
            if data.get('reason') == 'AlreadyExists':
                print((
                       f'Resource {resource_file} not created '
                       'because it already exists'
                      ))
            else:
                raise e


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


