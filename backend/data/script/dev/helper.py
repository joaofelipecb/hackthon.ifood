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
